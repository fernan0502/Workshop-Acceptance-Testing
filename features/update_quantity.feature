# language: en

Feature: Update product quantity
  As a user
  I want to update the quantity of a product
  So that the inventory stock is correct

  Scenario: Update the quantity of a product
    Given the inventory contains products:
      | Product | Quantity |
      | Coffee  | 10       |
    When the user updates product "Coffee" to quantity "25"
    Then the inventory should show product "Coffee" with quantity "25"