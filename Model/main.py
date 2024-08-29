from typing import List
from View import ShoesView

if __name__ == "__main__":
    shoes = Shoes("men", "skeachers", "black", 4999.99, "Nike", 42)
    view = ShoesView()
    controller = ShoesController(shoes, view)

