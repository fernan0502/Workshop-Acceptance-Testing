# language: en

Feature: Remove a product from the inventory
  As a user
  I want to remove products from the inventory
  So that unavailable products no longer appear

  Scenario: Attempt to remove a product that does not exist
    Given the inventory contains products:
      | Product |
      | Coffee  |
      | Sugar   |
    When the user removes the product "Coffee"
    Then the inventory should not contain "Coffee"