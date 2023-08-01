Feature: User Login and Logout
    As a user
    I want to log in and out of the application
    So that I can access my account and ensure security
    Only if my account and credentials are valid

Scenario: Login and Logout
    Given the user is on the login page
    When the user enters valid credentials and clicks the login button
    Then the user should be on the main homepage
    When the user logs out
    Then the user should be on the login page

Scenario: User cannot login with a locked account
    Given the user is on the login page
    When the user enters valid credentials for a locked account and clicks the login button
    Then the user should see an error message indicating the account is locked

Scenario: User cannot login with invalid credentials
    Given the user is on the login page
    When the user leaves both username and password fields empty and clicks the login button
    Then the user should see an error message indicating the username is required
    When the user enters only a username, and clicks the login button
    Then the user should see an error message indicating the password is required
    When the user enters an invalid username and an incorrect password, and clicks the login button
    Then the user should see an error message indicating the password is incorrect
