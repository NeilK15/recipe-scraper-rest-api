# Other modules
import requests  # TEMPORARY (PLACE IN UTIL METHODS)
from bs4 import BeautifulSoup, Tag
import sys
import os

# Local modules
# from src.models import *
from src.utils import *


class RecipeScrapper:
    initialized = False

    @staticmethod
    def initialize(dataPath: str = None):
        """
        This method initializes the Recipe Scrapper and creates the necessary files
        and directories needed for processing recipes gathered via html. If no dataPath
        is specified, the files will be placed under <currentWorkingDirectory>/data.

        The data path will be structured as follows:

        data (dataPath)
          finalized
            final.json
          raw
            info_raw.txt
            ingredients_raw.txt
            instructions_raw.txt
            metadata_raw.txt
            nutrition_raw.txt
            tips_raw.txt
          staged
            review.json

        """

        if dataPath == None:
            cwd = os.getcwd()
            # Implement later
            dataPath = "/".join([cwd, "data"])
            make_directory(dataPath)

        # Creating the path strings and then creating the folders
        raw_path = "/".join([dataPath, "raw"])
        staged_path = "/".join([dataPath, "staged"])
        finalized_path = "/".join([dataPath, "finalized"])

        make_directory(raw_path)
        make_directory(staged_path)
        make_directory(finalized_path)

        # Lists of file to be created
        raw_files = [
            "info_raw.txt",
            "ingredients_raw.txt",
            "instructions_raw.txt",
            "tips_raw.txt",
            "nutrition_raw.txt",
            "metadata_raw.txt",
        ]
        staged_files = ["review.json"]
        finalized_files = ["final.json"]

        # Making all the files
        for file in raw_files:
            make_file(raw_path, file)

        for file in staged_files:
            make_file(staged_path, file)

        for file in finalized_files:
            make_file(finalized_path, file)

        RecipeScrapper.initialized = True

    @staticmethod
    def create_recipe(url: str):
        if not RecipeScrapper.initialized:
            raise RuntimeError("RecipeScrapper has not been initialized")

        if url == None:
            return

        soup = make_request(url)
        text = soup.get_text()
        soup.find_all()

        insts = RecipeScrapper.extract_instructions(soup)
        for inst in insts:
            print(inst.text)

        # recipe = Recipe()
        # recipe.prep_time = Time()

    def extract_instructions(soup: BeautifulSoup):
        return soup.find_all(has_instructions)
