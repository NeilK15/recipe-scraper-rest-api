import sys

sys.path.append("/Users/neilkapur/Local/recipe-scraper/src")

from lib.recipe_scraper import RecipeScraper

scraper = RecipeScraper(url="https://downshiftology.com/recipes/breakfast-potatoes/")

info = scraper.extract_info()

print(info)
