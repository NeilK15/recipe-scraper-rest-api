from bs4 import BeautifulSoup, Tag
from src.constant import keywords
from typing import List


class TimeExtracting:
    def extract_prep_time(soup: BeautifulSoup) -> List[str]:
        possible_prep_times = []
        for keyword in keywords.get_prep_time_keywords():
            prep_times = TimeExtracting.get_text_from_keyword(soup, keyword)
            for prep_time in prep_times:
                possible_prep_times.append(prep_time)

        return possible_prep_times

    def get_text_from_keyword(soup: BeautifulSoup, keyword: str) -> str:
        return soup.find_all(
            True, string=lambda text: TimeExtracting.filter_words(text, keyword)
        )

    def filter_words(text, keyword):
        if text:
            return keyword in text.lower()
