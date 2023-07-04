import sys

sys.path.append("/Users/neilkapur/Local/recipe-scraper/src")

from lib.recipe_scraper import RecipeScraper

scraper = RecipeScraper(
    dataPath="/Users/neilkapur/Local/recipe-scraper/data-d59b8d88-192e-11ee-9718-7eccf7be6701",
    url="https://downshiftology.com/recipes/breakfast-potatoes/",
)

scraper.stage_recipe()
