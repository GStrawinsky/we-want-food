from collections import defaultdict
from recipe import Recipe


class GroceryList:
    def __init__(self, data, meal_indices) -> None:
        self.meal_indices: list[str] = meal_indices
        self.data = data
        
    def get(self) -> str:
        grocery_dict = self.merge_produce_lists()
        return self.parse_grocery_list(grocery_dict)

    def merge_produce_lists(self) -> dict :
        
        recipes = [Recipe(i, self.data[i]["name"], self.data[i]["groceries"]) for i in self.meal_indices]

        grocery_list = defaultdict(list)

        for d in recipes:
            groceries = d.groceries
            for g in groceries.keys():
                if g in grocery_list:
                    grocery_list[g].append(groceries[g])
                else:
                    grocery_list[g] = [groceries[g]]

        return grocery_list
    
    def parse_grocery_list(self, grocery_dict: dict) -> str:
        parsed_groceries = ""
        for ingredient, quantity in grocery_dict.items():
            parsed_groceries = parsed_groceries + "\n" + "--{}: {}".format(ingredient, quantity)
        return parsed_groceries

    def __repr__(self) -> str:
        return f"GroceryList(meal_indices={repr(self.meal_indices)})"

