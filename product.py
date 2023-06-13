class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    def get_product_with_higher_price(self, other_product):
        if self.price > other_product.price:
            return self
        else:
            return other_product

    def get_highest_price(products) :
        max_price = float('-inf')
        for product in products:
            if product.price > max_price:
                max_price = product.price
        return max_price
