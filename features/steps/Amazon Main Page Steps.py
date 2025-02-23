from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then, step


SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
HAM_MENU_BTN = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, 'td.navFooterDescItem a')
SIGN_IN_BTN = (By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-inner")
SEARCH_RESULT = (By.CSS_SELECTOR,  )


@given('Open Amazon page')
def search_amazon(context, search_word):
    context.driver.find_element(*SEARCH_BTN).click()


@when('Click on button from SignIn popup')
def click_sign_in_btn(context):
    sign_in_btn = context.driver.wait.until(
        EC.element_to_be_clickable(SIGN_IN_BTN), 'Sign in btn not clickable'
    )
    sign_in_btn.click()


@then('Verify hamburger menu btn present')
def verify_ham_menu(context):
    context.driver.find_element(*HAM_MENU_BTN)

@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    all_products = context.driver.find_elements(+SEARCH_RESULTS)
    for product in all_products:
        assert product.find_element(*PRODUCT_TITLE).text != '', 'Error' 'Title should not be blank'
        print(title)

