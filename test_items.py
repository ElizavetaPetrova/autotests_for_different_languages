import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_quest_should_see_cart_link(browser):
    browser.get(link)
    time.sleep(5)
    item = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert item, 'no item'