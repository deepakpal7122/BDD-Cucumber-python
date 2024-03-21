from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('D Lanuch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path="D:\\Sofware\\Software_file\\chromedriver_win32\\chromedriver.exe")
    context.driver.implicitly_wait(10)

@when('D open OrangeHRM login homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

@when('D Enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element(By.XPATH, '//input[@name="username"]').send_keys(user)
    context.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(pwd)


@when('D Click on login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//button[@type="submit"]').click()


@then('User must successfully login to the Dashboard page')
def step_impl(context):
    try:
        text = context.driver.find_element(By.XPATH, '//*[@class="oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module"]')
        if text == "Dashboard":
            context.driver.close()
            assert True, "Test Passed"  
    except:
        context.driver.close()
        assert False, "Test Failed"
    
    
'''
@then ('User must successfully login to the Dashboard page')
def step_impl(context):
    try:
        text = context.driver.find_element(By.XPATH, "(//*[text()='Dashboard'])[2]").text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "Dashboard":
        context.driver.close()
        assert True, "Test Passed"
'''
