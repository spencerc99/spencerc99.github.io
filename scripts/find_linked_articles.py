import re
import toml
import os
import ast
from sys import stderr
from typing import (Set,List, IO, AnyStr)

INTERNAL_ARTICLE_REGEX = re.compile('\\(\\/[^)]+')
LINKED_ARTICLES_FIELDNAME = 'related'
ARTICLE_METADATA_DELIMETER = '---'
CONTENT_PATH = 'content/posts/'

def clean_internal_link(link):
    if link[-1] == '/':
        link = link[:-1]
    return link

def parse_linked_articles(lines: List[AnyStr]) -> Set[str]:
    articles = set()
    for line in lines:
        if 'spencerchang.me' in line:
            print('Absolute link found, convert to relative link', file=stderr)
        matches = re.findall(INTERNAL_ARTICLE_REGEX, line)
        for match in matches:
            linked_post = match[1:]
            if linked_post == '/posts':
                continue
            cleaned_linked_post = clean_internal_link(linked_post)
            articles.add(cleaned_linked_post)

    return articles    
        

def upsert_related_articles(filename: str):
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

if __name__ == "__main__":
    for filename in os.listdir(CONTENT_PATH):
        if '.DS_Store' in filename:
            continue
        if os.path.isdir(f'{CONTENT_PATH}{filename}'):
            filename = f'{filename}/index.md'
        print(f'Upserting related content for {CONTENT_PATH}{filename}')
        upsert_related_articles(f'{CONTENT_PATH}{filename}')
