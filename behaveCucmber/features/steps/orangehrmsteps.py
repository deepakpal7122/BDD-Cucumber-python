from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given('I open chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path="D:\\Sofware\\Software_file\\chromedriver_win32\\chromedriver.exe")
    context.driver.implicitly_wait(10)

@when('I open OrangeHRM login Homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@when('Enter the username "{admin}" and password "{admin123}"')
def step_impl(context, admin,  admin123):
    context.driver.find_element(By.XPATH, '//input[@placeholder="Username"]').send_keys(admin)
    context.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(admin123)


@when('Click on the login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()


@then('User must successfully login to Dashboard page')
def step_impl(context):
    dasboard_ele = context.driver.find_element(By.XPATH, "//h6[text()='Dashboard']").text
    assert dasboard_ele == "Dashboard"
    time.sleep(3)
    context.driver.close()

