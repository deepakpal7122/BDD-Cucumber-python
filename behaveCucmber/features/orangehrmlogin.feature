Feature: OrangeHRM Login

    Scenario: Login to  OrangeHRM with valid parameters
        Given D Lanuch chrome browser
        When D open OrangeHRM login Homepage
        And D Enter username "admin" and password "admin123"
        And D Click on login button
        Then User must successfully login to the Dashboard page

    Scenario Outline: Login to OrangeHRM with multiple parameters
        Given D Lanuch chrome browser
        When D open OrangeHRM login Homepage
        And D Enter username "<username>" and password "<password>"
        And D Click on login button
        Then User must successfully login to the Dashboard page

        Examples:
            |   username    |   password    |
            |   admin123    |   admin       |
            |   admin       |   admin123    |
            # |   adminxyz    |   admin123    |
            # |   admin       |   adminxyz    |