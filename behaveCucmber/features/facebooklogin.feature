Feature: Facebook Login

    Scenario: Login to facebook with invalid parameters
        Given I Lanuch chrome browser
        When I open facebook login Homepage
        And Enter username "admin" and password "admin123"
        And Click on login button
        Then User must not successfully login 