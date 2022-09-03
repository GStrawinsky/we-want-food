import argparse
import sys
import retrieval
import grocery_list
import json
import telegram_bot

def run(args):
    
    meals = retrieval.give_meals(DATA, args.meals)
    for meal in meals:
        print(f"{meal.index}: {meal.name}")
        if args.ingredients:
            for ingredient, quantity in meal.groceries.items():
                print("\t--{}: {}".format(ingredient, quantity))


def run_grocery_list(indices):
    grocery_object = grocery_list.GroceryList(DATA, indices)
    groceries_parsed = grocery_object.get()
    telegram_bot.send_grocery_list(groceries_parsed)
    print(groceries_parsed) 


def validate(args):
    if args.meals is not None and 0 > args.meals:
        print("Meals must be a non-negative number", file=sys.stderr)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Program for automating the generation of meal \
                     plans and their associated ingredients")
    parser.add_argument("-m", "--meals", type=int, default=3,
                        help="The number of meals to generate")
    parser.add_argument("-i", "--interactive", default=False, type=bool,
                        metavar="I", help="Should prompt be interactive")
    parser.add_argument("-f", "--file", type=str, default="meals.json",
                        help="Path to the meals file")
    parser.add_argument("-g", "--ingredients", action="store_true",
                        help="Show ingredients")
    parser.add_argument("-gl", "--grocerylist", nargs="+", type=str,
                        help="Make a grocery list")

    args = parser.parse_args()
    validate(args)

    with open(args.file) as f:
        DATA = json.load(f)

    if args.grocerylist:
        run_grocery_list(args.grocerylist)
    else:
        run(args)
