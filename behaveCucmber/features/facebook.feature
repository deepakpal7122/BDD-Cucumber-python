Feature: Facebook Logo
    Scenario:  Logo present on Facebook home page
    Given Lanuch chrome browser
    When open facebook homepage 
    Then verify that the logo present on page
    And close browser