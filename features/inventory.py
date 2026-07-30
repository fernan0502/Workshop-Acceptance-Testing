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