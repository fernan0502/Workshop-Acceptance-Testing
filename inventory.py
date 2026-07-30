from datetime import datetime


class Product:
    def __init__(self, name, quantity=0, category="General"):
        self.name = name
        self.quantity = quantity
        self.category = category
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __repr__(self):
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

    #Feature 4
    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                return True
        return False

    # Feature 5 (added)
    def clear_inventory(self):
        self.products = []

    def is_empty(self):
        return len(self.products) == 0

    def find_product(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None


def print_products(inventory):
    if inventory.is_empty():
        print("The inventory is empty.")
        return

    print("Products:")
    for product in inventory.list_products():
        print(
            f"- {product.name} "
            f"(Quantity: {product.quantity}) "
            f"[Category: {product.category}]"
        )


def main():
    inventory = Inventory()

    menu = """
==== Inventory Manager ====
1. Add a product
2. List products
3. Update product quantity
4. Remove a product
5. Clear inventory
6. Exit
Select an option: """

    while True:
        choice = input(menu).strip()

        if choice == "1":
            name = input("Product name: ").strip()
            quantity = int(input("Quantity: "))
            category = input("Category [General]: ").strip() or "General"

            try:
                inventory.add_product(name, quantity, category)
                print(f'Product "{name}" added.')
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            print_products(inventory)

        elif choice == "3":
            name = input("Product name: ").strip()
            quantity = int(input("New quantity: "))

            if inventory.update_quantity(name, quantity):
                print(f'Quantity of "{name}" updated.')
            else:
                print(f'Product "{name}" not found.')

        elif choice == "4":
            name = input("Product name to remove: ").strip()

            if inventory.remove_product(name):
                print(f'Product "{name}" removed.')
            else:
                print(f'Product "{name}" not found.')

        elif choice == "5":
            inventory.clear_inventory()
            print("The inventory has been cleared.")

        elif choice == "6":
            print("Closing the Inventory Manager....")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()