class Product:
    brand = "Coke"  # class attribute

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock  # object attribute

    def get_product_with_higher_price(self, other_product):  # method instance
        if self.price > other_product.price:
            return self
        else:
            return other_product

    @staticmethod
    def get_highest_price(products):  # static method
        max_price = float(-1)
        for product in products:
            if isinstance(product, Product) and product.price > max_price:
                max_price = product.price
        return max_price
