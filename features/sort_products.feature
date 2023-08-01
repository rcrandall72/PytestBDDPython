Feature: Sort Products
  As a user
  I want to sort items on the products page
  So that I can view items in different orders

  Scenario Outline: Sort Products A to Z
    Given the user is logged in
    When the user sorts the items A to Z
    Then the items should be displayed in alphabetical order

  Scenario Outline: Sort Products Z to A
    Given the user is logged in
    When the user sorts the items Z to A
    Then the items should be displayed in reverse alphabetical order

  Scenario Outline: Sort Products Low to High
    Given the user is logged in
    When the user sorts the items low to high
    Then the items should be displayed in ascending order

  Scenario Outline: Sort Products High to Low
    Given the user is logged in
    When the user sorts the items high to low
    Then the items should be displayed in descending order
