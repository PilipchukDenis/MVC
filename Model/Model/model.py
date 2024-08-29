class Shoes:
    def __init__(self, gender, shoe_type, colour, price, manufacturer, size):
        self.gender = gender
        self.shoe_type = shoe_type
        self.colour = colour
        self.price = price
        self.manufacturer = manufacturer
        self.size = size

    def __str__(self):
        return (f"Тип: {self.gender}, Вид: {self.shoe_type}, Цвет: {self.colour}, "
                f"Цена: {self.price}, Производитель: {self.manufacturer}, Размер: {self.size}")


