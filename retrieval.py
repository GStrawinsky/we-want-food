import json
import random


def give_meals(data_json, n):
    with open(data_json) as f:
        data = json.load(f)

    meal = random.sample(list(data.keys()), k=n)

    return meal


def give_ingredients(data_json, meal):
    with open(data_json) as f:
        data = json.load(f)

    return data[meal]
