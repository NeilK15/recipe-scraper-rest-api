import sys

sys.path.append("/Users/neilkapur/Local/recipe-scraper/src")

from lib.recipe_scrapper import RecipeScrapper

RecipeScrapper.initialize()
RecipeScrapper.create_recipe("https://downshiftology.com/recipes/breakfast-potatoes/")
