class Product:
    brand = "Coke"  # class attribute

    def __init__(self, name, price, stock):  # INSTANCIA
        self.name = name
        self.price = price
        self.stock = stock  # object attribute

    def get_product_with_higher_price(self, other_product):  # method instance
        return self if self.price > other_product.price else other_product

    @staticmethod
    def get_highest_price(products):  # static method

        return max((p.price for p in products if isinstance(p, Product)), default=-1)

    @classmethod
    def get_brand(cls):
        return cls.brand

    @classmethod
    def set_brand(cls, new_brand):
        cls.brand = new_brand

