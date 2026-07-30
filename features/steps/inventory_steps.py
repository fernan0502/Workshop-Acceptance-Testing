from behave import given, when, then
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from inventory import Inventory

# Feature: Add a product to the inventory

# Step 1: given the inventory is empty
@given("the inventory is empty")
def step_impl(context):
    context.inventory = Inventory()


# Step 2: when the user adds a product "{product}"
@when('the user adds a product "{product}"')
def step_impl(context, product):
    context.inventory.add_product(product, 0)


# Step 3: then the inventory should contain "{product}"
@then('the inventory should contain "{product}"')
def step_impl(context, product):
    names = [p.name for p in context.inventory.list_products()]
    assert product in names, f'Product "{product}" not found in inventory'


# Feature: List all products in the inventory

# Step 1: given the inventory contains products
@given("the inventory contains products:")
def step_impl(context):
    context.inventory = Inventory()

    for row in context.table:
        quantity = int(row["Quantity"]) if "Quantity" in row.headings else 0
        context.inventory.add_product(row["Product"], quantity)


# Step 2: when the user lists all products
@when("the user lists all products")
def step_impl(context):
    context.products = context.inventory.list_products()


# Step 3: then the output should contain
@then("the output should contain:")
def step_impl(context):
    names = [p.name for p in context.products]

    for row in context.table:
        assert row["Product"] in names, (
            f'Product "{row["Product"]}" not found'
        )


# Feature: Update product quantity

# Step 1: when the user updates product "{product}" to quantity "{quantity}"
@when('the user updates product "{product}" to quantity "{quantity}"')
def step_impl(context, product, quantity):
    context.update_result = context.inventory.update_quantity(
        product,
        int(quantity),
    )


# Step 2: then the inventory should show product "{product}" with quantity "{quantity}"
@then('the inventory should show product "{product}" with quantity "{quantity}"')
def step_impl(context, product, quantity):
    found = context.inventory.find_product(product)

    assert found is not None, f'Product "{product}" not found'
    assert found.quantity == int(quantity), (
        f'Expected quantity {quantity} but got {found.quantity}'
    )


# Feature: Remove a product from the inventory

# Step 1: when the user removes the product "{product}"
@when('the user removes the product "{product}"')
def step_impl(context, product):
    context.remove_result = context.inventory.remove_product(product)

    if not context.remove_result:
        context.error_message = f'Product "{product}" not found'
    else:
        context.error_message = None


# Step 2: then the inventory should not contain "{product}"
@then('the inventory should not contain "{product}"')
def step_impl(context, product):
    names = [p.name for p in context.inventory.list_products()]
    assert product not in names, (
        f'Product "{product}" should have been removed'
    )


# Step 3: the system should show the message "{message}"
@then('the system should show the message "{message}"')
def step_impl(context, message):
    assert context.error_message == message, (
        f'Expected "{message}" but got "{context.error_message}"'
    )


# Feature: Clear the inventory

# Step 1: when the user clears the inventory
@when("the user clears the inventory")
def step_impl(context):
    context.inventory.clear_inventory()


# THEN: the inventory should be empty
@then("the inventory should be empty")
def step_impl(context):
    assert len(context.inventory.list_products()) == 0, "The inventory is not empty"
