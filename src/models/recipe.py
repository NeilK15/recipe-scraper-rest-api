from typing import List
import uuid
import time
from datetime import date

from src.models.recipe_parts import Time, Ingredient, Nutrition, Instruction, Tip


class Recipe:
    def __init__(
        self,
        prep_time=None,
        cook_time=None,
        total_time=None,
        course=None,
        cuisine=None,
        keywords=None,
        servings=None,
        author=None,
        url=None,
        image_url=None,
        description=None,
        ingredients=None,
        instructions=None,
        tips=None,
        nutrition=None,
    ):
        self.__id: int = uuid.uuid1().int

        # Times
        self.__prep_time: Time = prep_time
        self.__cook_time: Time = cook_time
        self.__total_time: Time = total_time

        self.__course: str = course
        self.__cuisine: str = cuisine
        self.__keywords: List[str] = keywords
        self.__servings: int = servings
        self.__author: str = author
        self.__url: str = url
        self.__image_url: str = image_url
        self.__description: str = description

        # Ingredients
        self.__ingredients: List[Ingredient] = ingredients

        self.__instructions: List[Instruction] = instructions
        self.__tips: List[Tip] = tips

        self.__nutrition: Nutrition = nutrition

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
        return self.__image_url

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

    # Viewing and exporting methods
    def to_json(self) -> dict:
        to_json = {
            "id": self.__id,
            "prepTime": self.__prep_time.value,
            "prepTimeUnit": self.__prep_time.unit,
            "cookTime": self.__cook_time.value,
            "cookTimeUnit": self.__cook_time.unit,
            "totalTime": self.__total_time.value,
            "totalTimeUnit": self.__total_time.unit,
            "course": self.__course,
            "cuisine": self.__cuisine,
            "keywords": self.__keywords,
            "servings": self.__servings,
            "author": self.__author,
            "url": self.__url,
            "imageUrl": self.__image_url,
            "description": self.__description,
            "ingredients": self.__ingredients,
            "instructions": self.__instructions,
            "tips": self.__tips,
            "nutrition": self.__nutrition,
            "metadata": {
                "dateCreated": date.isoformat(date.today()),
                "dateTimeExtracted": "2023-07-02 15:00:00.000",
                "extractionMethod": "web-scrapping",
            },
        }

        return to_json
