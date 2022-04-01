from shopping_cart import Shopping_Cart

class Customer:
    def __init__(self, name):
        self.customer_name= name
        self.shopping_cart_object = Shopping_Cart
        self.cart_products = []
    def add_product(self):
        add_to_cart = Shopping_Cart
        add_to_cart.add_new_product(self)

    def view_shopping_cart(self):
        print(self.cart_products)