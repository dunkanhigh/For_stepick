from selenium.webdriver.common.by import By


def test_button_add_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    browser.get(link)
    button = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert len(button) != 0, "Button didn't find"
