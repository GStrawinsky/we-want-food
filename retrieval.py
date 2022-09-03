import random
from recipe import Recipe


def give_meals(data, n) -> list[Recipe]:

    meal_indices = random.sample(list(data.keys()), k=n)

    recipes = [Recipe(i, data[i]["name"], data[i]["groceries"]) for i in meal_indices]

    return recipes
