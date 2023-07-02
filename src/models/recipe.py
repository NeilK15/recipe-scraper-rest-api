from typing import List
from src.models import *


class Recipe:
    def __init__(self):
        self.__id: int

        # Times
        self.__prep_time: Time
        self.__cook_time: Time
        self.__total_time: Time

        self.__course: str
        self.__cuisine: str
        self.__keywords: List[str]
        self.__servings: int
        self.__author: str
        self.__url: str
        self.__imageUrl: str
        self.__description: str

        # Ingredients
        self.__ingredients: List[Ingredient]

        self.__instructions: List[Instruction]
        self.__tips: dict

        self.__nutrition: Nutrition

    # Properties

    @property
    def id(self) -> int:
        return self.__id

    @property
    def prep_time(self) -> Time:
        return self.__prep_time

    @property
    def cook_time(self) -> Time:
        return self.__cook_time

    @property
    def total_time(self) -> Time:
        return self.__total_time

    @property
    def course(self) -> str:
        return self.__course

    @property
    def cuisine(self) -> str:
        return self.__cuisine

    @property
    def keywords(self) -> List[str]:
        return self.__keywords

    @property
    def servings(self) -> int:
        return self.__servings

    @property
    def author(self) -> str:
        return self.__author

    @property
    def url(self) -> str:
        return self.__url

    @property
    def imageUrl(self) -> str:
        return self.__imageUrl

    @property
    def description(self) -> str:
        return self.__description

    @property
    def ingredients(self) -> List[Ingredient]:
        return self.__ingredients

    @property
    def instructions(self) -> List[Instruction]:
        return self.__instructions

    @property
    def tips(self) -> List[Tip]:
        return self.__tips

    @property
    def nutrition(self) -> Nutrition:
        return self.__nutrition
