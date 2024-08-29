class ShoesView:
    def display_shoes_info(self, shoes):
        print("Информация об обуви:")
        print(shoes)

    def get_gender(self):
        return input("Введите тип обуви (men/women): ")

    def get_shoe_type(self):
        return input("Введите вид обуви (sneakers, boots, sandals, shoes и т.д.): ")

    def get_colour(self):
        return input("Введите цвет обуви: ")

    def get_price(self):
        return float(input("Введите цену обуви: "))

    def get_manufacturer(self):
        return input("Введите производителя обуви: ")

    def get_size(self):
        return int(input("Введите размер обуви: "))


