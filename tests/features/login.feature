Feature: Login / Logout

    @valid_user
    Scenario: Login with valid credentials
        When I login with "standard_user" and "secret_sauce"
        Then I should see the inventory page

    @invalid_user
    Scenario Outline: Login with invalid credentials
        When I login with "<username>" and "<password>"
        Then I should see the error "<error>"

        Examples:
            | username      | password     | error                                                                     |
            | invalid_user  | secret_sauce | Epic sadface: Username and password do not match any user in this service |
            | standard_user | invalid_pass | Epic sadface: Username and password do not match any user in this service |
            | standard_user |              | Epic sadface: Password is required                                        |
            |               | secret_sauce | Epic sadface: Username is required                                        |
            |               |              | Epic sadface: Username is required                                        |

    @locked_user
    Scenario Outline: Login with locked user
        When I login with "locked_out_user" and "secret_sauce"
        Then I should see the error "Epic sadface: Sorry, this user has been locked out."

    @logout
    Scenario: Logout from session
        When I login with "standard_user" and "secret_sauce"
        Then I should see the inventory page
        When I logout
        Then I should see the login page
        When I go to the Inventory page
        Then I should see the error "Epic sadface: You can only access '/inventory.html' when you are logged in."