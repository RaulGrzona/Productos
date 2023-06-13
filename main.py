from product import Product

product1 = Product("Mouse USB", 500, 10)
product2 = Product("Cable VGA", 350, 10)
product3 = Product("Monitor LG 29", 500, 10)
product4 = Product("Mother PC LG355", 2350, 3)

print(" 1 : Highest price of products")
print(" 2 : Product list ")

input_number = int(input("Input Number: "))
if input_number == 1:
    products = [product1, product2, product3, product4]
    # Get highest price
    highest_price = Product.get_highest_price(products)
    print("The highest price is :", highest_price)
else:
    products = [product1, product2, product3, product4]
    for product in products:
        print(f"{product.name}\t{product.price}\t{product.stock}")