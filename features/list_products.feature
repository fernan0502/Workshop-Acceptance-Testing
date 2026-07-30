# language: en

Feature: List all products in the inventory
  As a user
  I want to list all products
  So that I can see everything available

  Scenario: List all products in the inventory
    Given the inventory contains products:
      | Product |
      | Coffee  |
      | Sugar   |
    When the user lists all products
    Then the output should contain:
      | Product |
      | Coffee  |
      | Sugar   |