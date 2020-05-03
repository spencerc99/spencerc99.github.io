import re
import toml
from typing import (Set,List, IO, AnyStr)

INTERNAL_ARTICLE_REGEX = re.compile('\(\/[^)]+')
LINKED_ARTICLES_FIELDNAME = 'related'
ARTICLE_METADATA_DELIMETER = '---'

def parse_linked_articles(lines: List[AnyStr]) -> Set[str]:
    articles = set()
    for line in lines:
        matches = re.findall(INTERNAL_ARTICLE_REGEX, line)
        for match in matches:
            linked_post = match[1:]
            articles.add(linked_post)

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
            linked_field_line = lines[linked_field_idx].trim()
            existing_articles = set(list(linked_field_line[linked_field_line.index(':')+1:]))
            all_articles = existing_articles.union(linked_articles)
            if len(all_articles) == len(linked_articles):
                # don't write if not needed
                return
            print(f'changing to "{LINKED_ARTICLES_FIELDNAME}: {str(list(all_articles))}" at {linked_field_idx}')
            lines[linked_field_idx] = f'{LINKED_ARTICLES_FIELDNAME}: {str(list(all_articles))}\n'
        else:
            print(f'inserting "{LINKED_ARTICLES_FIELDNAME}: {str(list(linked_articles))}" at {end_of_metadata_idx}')
            lines.insert(end_of_metadata_idx, f'{LINKED_ARTICLES_FIELDNAME}: {str(list(linked_articles))}\n')
        f.seek(0)
        f.writelines(lines)

