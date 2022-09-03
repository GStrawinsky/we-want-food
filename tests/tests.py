import unittest
from grocery_list import GroceryList

from retrieval import give_meals
import json

class Test(unittest.TestCase):

    def __init__(self,  *args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)
        self.data = self.load_data()

    def load_data(self):
        data = '{"1": {"name": "Test1", "groceries": {"bread": "1", "salmon": "100g"}}, "2": {"name": "Test2", "groceries": {"bread": "2", "salmon": "200g"}}}'
        return json.loads(data)

    def test_1(self):

        answer = give_meals(self.data, 2)

        indices = [r.index for r in answer]
        names = [r.name for r in answer]
        groceries = [r.groceries for r in answer]

        self.assertListEqual(indices, ["1", "2"])
        self.assertListEqual(names, ["Test1", "Test2"])
        self.assertListEqual(groceries, [{"bread": "1", "salmon": "100g"}, {"bread": "2", "salmon": "200g"}])

    def test_2(self):
    
        grocery_obj = GroceryList(self.data, ["1", "2"])
        answer = grocery_obj.merge_produce_lists()

        expected = {"bread": ["1", "2"], "salmon": ["100g", "200g"]}

        self.assertDictEqual(answer, expected)



if __name__ == "__main__":
    unittest.main(verbosity=2)