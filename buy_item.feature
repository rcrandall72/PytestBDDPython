Feature: User Buys Item
    As a user
    I want to be able to add an item to my cart
    So that I can buy it

Scenario: Buy Item
    Given the user is logged in
    When the user adds an item to the cart
    Then the cart total should increase by 1
    When the user opens the cart
    Then the item name added should appear
    When the user enters their information
    When the user finalizes their order
    Then the confirmation prompt should appear
