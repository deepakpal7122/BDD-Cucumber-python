from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('Lanuch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(executable_path="D:\\Sofware\\Software_file\\chromedriver_win32\\chromedriver.exe")

@when('open facebook homepage')
def openHomepage(context):
    context.driver.get("https://www.facebook.com/")
    
@then('verify that the logo present on page')
def verifyLogo(context):
    status = context.driver.find_element(By.XPATH, '//*[@class="fb_logo _8ilh img"]').is_displayed()
    assert status is True

@then('close browser')
def closeBrowser(context):
    context.driver.close()