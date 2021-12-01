import re
import toml
import os
import ast
from sys import stderr
from typing import (Set,List, IO, AnyStr)

INTERNAL_ARTICLE_REGEX = re.compile('\\[[^)]+\\]\\((\\/[^)]+)')
ABSOLUTE_URL_REGEX = re.compile(
    '(\\[[^\\])]*\\]\\([^)]*(?:(?:spencerchang\\.me)|(?:localhost:1313))(\\/[^)]+)\\))')
LINKED_ARTICLES_FIELDNAME = 'related'
ARTICLE_METADATA_DELIMETER = '---'
CONTENT_PATHS = ['content/posts/', 'content/experiments/100posts/']

def clean_internal_link(link):
    if link[-1] == '/':
        link = link[:-1]
    return link

def is_directory_path(path): 
    for content_dir in CONTENT_PATHS:
        if path in content_dir:
            return True
    return False

def parse_linked_articles(lines: List[AnyStr]) -> Set[str]:
    articles = set()
    for line in lines:
        absolute_matches = re.findall(ABSOLUTE_URL_REGEX, line)
        for full_match, relative_match in absolute_matches:
            # skip the directory matches because they don't point to articles.
            if is_directory_path(relative_match):
                continue
            print(f'Absolute link found {full_match}, convert to relative link {relative_match}', file=stderr)
            articles.add(clean_internal_link(relative_match))
            
        relative_matches = re.findall(INTERNAL_ARTICLE_REGEX, line)
        for match in relative_matches:
            # skip the directory matches because they don't point to articles.
            if is_directory_path(match):
                continue
            articles.add(clean_internal_link(match))

    return articles    
        

def upsert_related_articles(filename: str):
    try: 
        with open(filename, 'r+') as f:
            lines = f.readlines()
            linked_articles = parse_linked_articles(lines)
            linked_field_idx = None
            end_of_metadata_idx = None

            for idx, line in enumerate(lines[1:]):
                if line.startswith(ARTICLE_METADATA_DELIMETER):
                    end_of_metadata_idx = idx + 1
                    break
                if line.startswith(LINKED_ARTICLES_FIELDNAME + ':'):
                    linked_field_idx = idx + 1

            if linked_field_idx:
                linked_field_line = lines[linked_field_idx].strip()
                existing_articles = set(ast.literal_eval(linked_field_line[linked_field_line.index(':')+2:]))
                all_articles = existing_articles.union(linked_articles)
                if len(existing_articles) == len(linked_articles):
                    # don't write if not needed
                    return
                print(f'changing to "{LINKED_ARTICLES_FIELDNAME}: {str(list(all_articles))}" at {linked_field_idx}')
                lines[linked_field_idx] = f'{LINKED_ARTICLES_FIELDNAME}: {str(list(all_articles))}\n'
            else:
                print(f'inserting "{LINKED_ARTICLES_FIELDNAME}: {str(list(linked_articles))}" at {end_of_metadata_idx}')
                lines.insert(end_of_metadata_idx, f'{LINKED_ARTICLES_FIELDNAME}: {str(list(linked_articles))}\n')
            f.seek(0)
            f.writelines(lines)
    except:
        print(f'Failed to update {filename}', file=stderr)

if __name__ == "__main__":
    for content_dir in CONTENT_PATHS: 
        for filename in os.listdir(content_dir):
            if '.DS_Store' in filename:
                continue
            if os.path.isdir(f'{content_dir}{filename}'):
                filename = f'{filename}/index.md'
            print(f'Upserting related content for {content_dir}{filename}')
            upsert_related_articles(f'{content_dir}{filename}')
