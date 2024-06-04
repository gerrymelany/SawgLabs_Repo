from behave import given, when, then
from selenium.webdriver.common.by import By
from features.pages.globalFunctions import BaseFunctions
from features.pages.loginSwagLabsPage import LoginPage

tie = 0

@given(u'I go to the login page')
def step_impl(context):
    context.driver.get(context.base_url)
    bf = BaseFunctions(context.driver)
    login_inputs = bf.select_element(By.XPATH, "//div[@class='login_logo'][contains(.,'Swag Labs')]", tie)
    assert "Swag Labs" in login_inputs.text, f"Expected title 'Swag Labs' does not match the real one '{login_inputs}'"

@when(u'I input correct username and password')
def step_impl(context):
    lp = LoginPage(context.driver)
    lp.enter_username("standard_user", tie)
    lp.enter_password("secret_sauce", tie)

@when(u'I click the login button')
def step_impl(context):
    lp = LoginPage(context.driver)
    lp.click_login_button(tie)

@then(u'I should see the inventory page')
def step_impl(context):
    bf = BaseFunctions(context.driver)
    products_page = bf.select_element(By.XPATH, "//span[@class='title'][contains(.,'Products')]", tie)
    assert "Products" in products_page.text, f"Expected caption 'Products' does not match the real one '{products_page}'"

@when(u'I input wrong username and password')
def step_impl(context):
    lp = LoginPage(context.driver)
    lp.enter_username("papa", tie)
    lp.enter_password("papa123", tie)


@then(u'I should see the error message "Epic sadface: Username and password do not match any user in this service"')
def step_impl(context):
    bf = BaseFunctions(context.driver)
    login_error = bf.select_element(By.XPATH, "//h3[@data-test='error'][contains(.,'Epic sadface: Username and password do not match any user in this service')]", tie)
    assert "Epic sadface: Username and password do not match any user in this service" in login_error.text, f"Expected logIn error does not match the real one '{login_error}'"


@when(u'I input wrong username and correct password')
def step_impl(context):
    lp = LoginPage(context.driver)
    lp.enter_username("blabla", tie)
    lp.enter_password("secret_sauce", tie)


@when(u'I input correct username and incorrect password')
def step_impl(context):
    lp = LoginPage(context.driver)
    lp.enter_username("standard_user", tie)
    lp.enter_password("papa123", tie)
