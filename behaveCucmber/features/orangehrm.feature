Feature: OrangeHRM Login

    Scenario: Login to OrangeHRM with valid parameters
        Given I open chrome browser
        When I open OrangeHRM login Homepage
        And Enter the username "admin" and password "admin123"
        And Click on the login button
        Then User must successfully login to Dashboard page