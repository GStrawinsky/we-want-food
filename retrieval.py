import json
import random


def give_meals(data_json, n):
    with open(data_json) as f:
        data = json.load(f)

    meal = random.choices(list(data.keys()), k = n)

    return(meal)
