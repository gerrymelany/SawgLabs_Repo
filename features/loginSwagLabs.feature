Feature: Swag Labs Application LogIn

  @critical_login
  Scenario: Successful login
    Given I go to the login page
    When I input correct username and password
    And I click the login button
    Then I should see the inventory page

  Scenario: Login with incorrect username and password
    Given I go to the login page
    When I input wrong username and password
    And I click the login button
    Then I should see the error message "Epic sadface: Username and password do not match any user in this service"

  Scenario: Login with incorrect username and correct password
    Given I go to the login page
    When I input wrong username and correct password
    And I click the login button
    Then I should see the error message "Epic sadface: Username and password do not match any user in this service"

  Scenario: Login with correct username and incorrect password
    Given I go to the login page
    When I input correct username and incorrect password
    And I click the login button
    Then I should see the error message "Epic sadface: Username and password do not match any user in this service"

