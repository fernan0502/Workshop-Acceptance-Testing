# language: en

Feature: Clear the inventory
  As a user
  I want to clear the inventory
  So that I can start over with an empty inventory

  Scenario: Clear the inventory
    Given the inventory contains products:
      | Product |
      | Coffee  |
      | Sugar   |
    When the user clears the inventory
    Then the inventory should be empty