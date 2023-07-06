import sys

# print(str(sys.argv))

sys.path.append("/Users/neilkapur/Local/recipe-scraper/src")

from lib.recipe_scraper import RecipeScraper


scraper = RecipeScraper(
    dataPath="/Users/neilkapur/Local/recipe-scraper/data",
    url=str(sys.argv[1]),
)

print(scraper.stage_recipe().to_json())
