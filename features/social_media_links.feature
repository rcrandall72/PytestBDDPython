Feature: Social Media Links
  As a user
  I want to click on social media links
  So that I can open their respective pages

  Scenario Outline: Open Social Media Links
    Given the user is logged in
    When the user opens the <social_media> link
    Then the <social_media> page should be opened

    Examples:
      | social_media  |
      | Twitter       |
      | Facebook      |
      | LinkedIn      |
