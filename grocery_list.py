# I give the list of dict keys, 
# I get out a complete list of groceries
# get all keys

import json
from operator import gt
import typing

def merge_produce_lists(meals: list[str]) -> dict[str, str]:
    with open("meals.json") as f:
        data = json.load(f)

    grocieries: list[dict[str, str]] = [data[i] for i in meals]

    grocery_list = {}

    # d is a dict
    for d in grocieries:
        # k is a key value pair
        produces = d.keys()
        for p in produces:
            if p in grocery_list:
                grocery_list[p] = [grocery_list[p], d[p]]
            else:
                grocery_list[p] = d[p]


    return grocery_list

