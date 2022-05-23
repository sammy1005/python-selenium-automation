from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import when, given, then
from time import sleep


ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
PRODUCT_NAME = (By.ID, 'productTitle')
#COLOR_OPTIONS = (By.CSS_SELECTOR, "#inline-twister-expander-content-color_name li[class*='desktop']")
COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name ul li")
#COLOR_NAME = (By.ID, 'inline-twister-expanded-dimension-text-color_name')
COLOR_NAME = (By.CSS_SELECTOR, "#variation_color_name span.selection")



@given('Open amazon {product_id} product')
def open_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')


@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    context.driver.wait.until(EC.invisibility_of_element_located(ADD_TO_CART_BTN))


@when('User can click through color')
def get_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Current product: {context.product_name}')


@then('Verify user can click through color')
def verify_clicking_colors(context):
    expected_colors = ['Blue Gingham - Long Sleeve', 'Burgundy - Long Sleeve', 'Navy - Long Sleeve', 'Navy Blue - Long Sleeve', 'Charcoal - Long Sleeve', 'Black - Long Sleeve', 'Black Plaid - Long Sleeve', 'Blue - Long Sleeve', 'Blue Gingham - Short Sleeve', 'Brick', 'Charcoal Gray - Long Sleeve', 'Green - Long Sleeve', 'Heather Gray - Long Sleeve', 'Light Blue - Long Sleeve', 'Light Blue Stripe - Long Sleeve', 'Navy Geometric - Long Sleeve', 'Navy Geometric - Short Sleeve', 'Navy Stripe - Short Sleeve', 'Skull Print - Long Sleeve', 'Slate Blue - Long Sleeve']
    actual_colors = []

    color_options = context.driver.find_elements(*COLOR_OPTIONS)
    for option in color_options:
        option.click()
        sleep(1)
        color_name = context.driver.find_element(*COLOR_NAME).text
        actual_colors += [color_name]

    assert actual_colors == expected_colors, f'Error! Expected {expected_colors}, but got {actual_colors}'