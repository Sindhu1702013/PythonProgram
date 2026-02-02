class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_item(self, item, price):
        self.cart[item] = price
        return f"{item} added to cart"

    def view_cart(self):
        if not self.cart:
            return "Cart is empty"
        return self.cart

    def get_total(self):
        return sum(self.cart.values())

# ---- Testing ----
cart = ShoppingCart()

print(cart.add_item("Laptop", 50000))
print(cart.add_item("Mouse", 800))
print("Cart:", cart.view_cart())
print("Total Price:", cart.get_total())
