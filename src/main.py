import sys
import os

# print(str(sys.argv))


def main():
    sys.path.append(f"{os.getcwd()}/src")

    from src.lib.recipe_scraper import RecipeScraper

    if len(sys.argv) != 2:
        print("Please supply the correct amount of arguments")
        return

    scraper = RecipeScraper(
        dataPath="/Users/nkapur/Local/kapur-home-stuff/recipe-scraper-rest-api/data",
        url=str(sys.argv[1]),
    )

    print(scraper.stage_recipe().to_json())


if __name__ == "__main__":
    main()
