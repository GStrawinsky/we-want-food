from dataclasses import dataclass


@dataclass
class Recipe:
    def __init__(self, index, name, groceries) -> None:
        self.name: str = name
        self.groceries: dict[str, str] = groceries
        self.index: str = index
        
    def __repr__(self) -> str:
        return f"Recipe(index={repr(self.index)}, name={repr(self.name)}, groceries={repr(self.groceries)})"



