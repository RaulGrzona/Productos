from app.product import Product

class TestProduct:
    def test__init__(self):
        p1 = Product(name="Mouse", price=30, stock=3)
        assert p1.name == "Mouse"
        assert p1.price == 30
        assert p1.stock == 3
        assert p1.brand == "Coke"
        assert Product.brand == "Coke"
        
    def test__get_product_with_higher_price__false(self):
        p1 = Product(name="Mouse", price=30, stock=3)
        p2 = Product(name="Cable USB", price=330, stock=3)
        assert p1.get_product_with_higher_price(p2) == p2

    def test__get_product_with_higher_price__true(self):
        p1 = Product(name="Mouse", price=30, stock=3)
        p2 = Product(name="Cable USB", price=3, stock=3)
        assert p1.get_product_with_higher_price(p2) == p1

    def test__get_highest_price__2_products(self):
        p1 = Product(name="Mouse", price=30, stock=3)
        p2 = Product(name="Cable USB", price=330, stock=3)
        products = [p1, p2]
        assert Product.get_highest_price(products) == 330

    def test__get_highest_price__empty(self):
        products = []
        assert Product.get_highest_price(products) == -1

    def test__get_highest_price__wrong_data(self):
        products = [1, 2, 3]
        assert Product.get_highest_price(products) == -1

    def test__get_highest_price__wrong_data_2(self):
        p1 = Product(name="Mouse", price=30, stock=3)
        products = [1, p1, 3]
        assert Product.get_highest_price(products) == 30

