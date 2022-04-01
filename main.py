# from alarm_clock import Alarm_Clock

# clock_one = Alarm_Clock(1600, True, 900)

# clock_one.turn_alarm_off()

# print(clock_one.alarm_clock_alarm)

from customer import Customer
from shopping_cart import Shopping_Cart
from product import Product

customer_one = Customer("Fred")

product_one = Product("milk", 3.50, "Grocery")

product_two = Product("boots", 90 , "Clothing")

product_three = Product ("Rubber Chicken", 10, "Pets")

customer_one.add_product()
customer_one.add_product()
customer_one.add_product()
customer_one.view_shopping_cart()
customer_cart = Shopping_Cart
customer_cart.add_amount()
print(customer_one.customer_name)