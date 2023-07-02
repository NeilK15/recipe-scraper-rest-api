from bs4 import BeautifulSoup, Tag
from src.constant import keywords
from typing import List


def has_instructions(tag: Tag):
    if "instructions" in tag.text.lower():
        return tag
