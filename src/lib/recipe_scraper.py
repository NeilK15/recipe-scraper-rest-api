# Other modules
import requests  # TEMPORARY (PLACE IN UTIL METHODS)
from bs4 import BeautifulSoup, Tag
import sys
import os
import uuid

# Local modules
from src.utils import *
from src.constant import keywords
from src.extraction import *


class RecipeScraper:
    def __init__(self, dataPath: str = None, url: str = None):
        """
        This method initializes a Recipe Scrapper and creates the necessary files
        and directories needed for processing recipes gathered via html. If no dataPath
        is specified, the files will be placed under <currentWorkingDirectory>/data. A
        URL is required

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
        if url == None:
            raise SyntaxError("Enter valid URL")

        if dataPath == None:
            id = uuid.uuid1()
            print(id)
            cwd = os.getcwd()
            dataPath = "/".join([cwd, f"data-{id}"])
            make_directory(dataPath)

        # Setting the variables
        self.__url = url
        self.__soup = make_request(url)

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

        self.initialized = True

    # Properties
    @property
    def soup(self) -> BeautifulSoup:
        return self.__soup

    # Logic methods
    def create_recipe(self):
        if self.url == None:
            return

        self.soup.find_all()

        insts = self.extract_instructions()
        for inst in insts:
            print(inst.text)

        # recipe = Recipe()
        # recipe.prep_time = Time()

    def extract_instructions(self):
        return self.soup.find_all(has_instructions)

    def extract_info(self):
        return TimeExtracting.extract_prep_time(self.soup)
