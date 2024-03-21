Feature: Sceanariobg home

    Background: common stpes
    Given New I Lanuch chrome browser
    When New I open OrangeHRM login Homepage
    And New Enter valid username and password 
    And New Click on login button

    Scenario: Login to  OrangeHRM Application
        Then User must login to the Dashboard page

    Scenario: Search user
        When New navigate to search page
        Then search page should display

    Scenario: Advance search user
        When navigate to advance search page
        Then advance search page should display