from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('I Lanuch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path="D:\\Sofware\\Software_file\\chromedriver_win32\\chromedriver.exe")


@when('I open facebook login Homepage')
def step_impl(context):
    context.driver.get("https://www.facebook.com/")

@when('Enter username "{admin}" and password "{admin123}"')
def step_impl(context, admin, admin123):
    context.driver.find_element(By.ID, "email").send_keys(admin)
    context.driver.find_element(By.ID, "pass").send_keys(admin123)


@when('Click on login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@type='submit']").click()


@then('User must not successfully login')
def step_impl(context):
    context.driver.close()
    
