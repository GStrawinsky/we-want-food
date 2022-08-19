from collections import defaultdict
import json
from domain import Recipe

## TODO: could be in a class with all rolled recipes cached
def merge_produce_lists(data, meal_indices: list[str]) -> dict :

    recipes = [Recipe(i, data[i]["name"], data[i]["groceries"]) for i in meal_indices]

    grocery_list = defaultdict(list)

    for d in recipes:
        groceries = d.groceries
        for g in groceries.keys():
            if g in grocery_list:
                grocery_list[g].append(groceries[g])
            else:
                grocery_list[g] = [groceries[g]]


    return grocery_list

