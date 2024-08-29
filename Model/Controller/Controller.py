class ShoesController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def update_gender(self):
        gender = self.view.get_gender()
        self.model.gender = gender

    def update_shoe_type(self):
        shoe_type = self.view.get_shoe_type()
        self.model.shoe_type = shoe_type

    def update_colour(self):
        colour = self.view.get_colour()
        self.model.colour = colour

    def update_price(self):
        price = self.view.get_price()
        self.model.price = price

    def update_manufacturer(self):
        manufacturer = self.view.get_manufacturer()
        self.model.manufacturer = manufacturer

    def update_size(self):
        size = self.view.get_size()
        self.model.size = size

    def display_shoes(self):
        self.view.display_shoes_info(self.model)

