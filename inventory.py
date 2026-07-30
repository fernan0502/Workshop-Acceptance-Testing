from datetime import datetime


class Product:
    def _init_(self, name, quantity=0, category="General"):
        self.name = name
        self.quantity = quantity
        self.category = category
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def _repr_(self):
        return (
            f"Product(name={self.name!r}, "
            f"quantity={self.quantity!r}, "
            f"category={self.category!r})"
        )

class Inventory:

    def __init__(self):
        self.products = []

    # Feature 1
    def add_product(self, name, quantity=0, category="General"):
        if not name or not name.strip():
            raise ValueError("Product name cannot be empty.")

        product = Product(name.strip(), quantity, category)
        self.products.append(product)
        return product

    # Feature 2
    def list_products(self):
        return list(self.products)

    # Feature 3
    def update_quantity(self, name, quantity):
        for product in self.products:
            if product.name == name:
                product.quantity = quantity
                return True
        return False