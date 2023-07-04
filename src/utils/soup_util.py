from bs4 import BeautifulSoup, Tag
from src.constant import keywords
from typing import List, Iterable


def has_instructions(tag: Tag):
    if "instructions" in tag.text.lower():
        return tag


def get_tags_from_keyword(soup: BeautifulSoup, keyword: str = None):
    if keyword == None:
        return soup.find_all(True)

    return soup.find_all(True, string=lambda text: filter_words(text, keyword))


def get_siblings(element: BeautifulSoup, keyword: str = None) -> Iterable[Tag]:
    return get_tags_from_keyword(element.parent, keyword)


def get_text_from_class_name(soup: BeautifulSoup, class_name: str) -> str:
    return soup.find(True, class_=class_name).text


def get_texts_from_class_name(soup: BeautifulSoup, class_name: str) -> Iterable[Tag]:
    return soup.find_all(True, class_=class_name)


def get_tags_from_class_names(
    soup: BeautifulSoup, class_names: Iterable[str]
) -> Iterable[Tag]:
    tags = []
    for class_name in class_names:
        specifc_tags = soup.find_all(True, class_=class_name)
        for tag in specifc_tags:
            tags.append(tag.text)

    return tags


def filter_words(text, keyword):
    if text:
        return keyword in text.lower()
