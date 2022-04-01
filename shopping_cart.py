from product import Product
class Shopping_Cart:
    def __init__(self):
        self.cart_products = []
        self.product_price = ()
        
    def add_amount(self):
        price_list = Product
        self.calculate_total= sum(price_list)
        return self.calculate_total

    def add_new_product(self):
        new_item = input("What would you like to add to shopping cart?")
        self.cart_products.append(new_item)
    def empty_cart(self):
        del self.cart_products