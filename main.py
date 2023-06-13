from product import Product

product1 = Product("Mouse USB", 500, 10)
product2 = Product("Cable VGA", 350, 10)
product3 = Product("Monitor LG 29", 500, 10)
product4 = Product("Mother PC LG355", 2350, 3)

products = [product1, product2, product3, product4]
# Obtener el precio más alto
highest_price = Product.get_highest_price(products)
print("El precio más alto es:", highest_price)
