from typing import List, Iterable

from bs4 import BeautifulSoup, Tag

from src.utils import *
from src.constant import *
from src.models.recipe_parts import Time
from .time_type import TimeType


class Extraction:
    # Extraction methods
    def extract_time(soup: BeautifulSoup, time_type: TimeType) -> Time:
        match time_type:
            case TimeType.TIME_PREP:
                names = class_names.PREP_TIME_VALUE, class_names.PREP_TIME_UNIT
            case TimeType.TIME_COOK:
                names = class_names.COOK_TIME_VALUE, class_names.COOK_TIME_UNIT
            case TimeType.TIME_TOTAL:
                names = class_names.TOTAL_TIME_VALUE, class_names.TOTAL_TIME_UNIT
            case _:
                raise SyntaxError("Invalid time_type")

        time_value = get_int_from_str(get_text_from_class_name(soup, names[0]))
        # print("|", time_value, "|")
        time_unit = get_text_from_class_name(soup, names[1])

        return Time(time_value, time_unit)

    def extract_name(soup) -> str:
        return str(get_text_from_class_name(soup, class_names.NAME))

    def extract_course(soup) -> str:
        return str(get_text_from_class_name(soup, class_names.COURSE))

    def extract_cuisine(soup) -> str:
        return str(get_text_from_class_name(soup, class_names.CUISINE))

    def extract_keywords(soup) -> List[str]:
        return None

    def extract_servings(soup) -> int:
        return get_int_from_str(get_text_from_class_name(soup, class_names.SERVINGS))

    def extract_author(soup) -> str:
        return str(get_text_from_class_name(soup, class_names.AUTHOR))

    def extract_url(soup) -> str:
        return None

    def extract_image_url(soup) -> str:
        return str(get_text_from_class_name(soup, class_names.IMAGE_URL))

    def extract_description(soup) -> str:
        return str(get_text_from_class_name(soup, class_names.DESCRIPTION))

    def _attempt_class_name_extraction(self) -> Iterable[Tag]:
        return get_text_from_class_name(self._soup, self._class_names)
