# if 11%2==0:
#     print("even")
# else:
#     print("odd")



# assert 10%2==0
# print("hello world")

# assert 11%2==0
# print("hello world")

assert False


# import time
# import pytest
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# wait_obj = WebDriverWait(driver, 5)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
#
# @pytest.mark.dependency()               ## Independent testcase
# def test_login():
#     driver.find_element('id', 'user-name').send_keys('standard_user')
#     driver.find_element('id', 'password').send_keys('secret_sauceeeee')
#     driver.find_element('id', 'login-button').click()
#     time.sleep(2)
#     wait_obj.until(expected_conditions.visibility_of_element_located(('xpath', '//span[text()="Products"]')))

#
# @pytest.mark.dependency(depends=['test_login'])
# def test_logout():
#     driver.find_element('xpath', '//button[@id="react-burger-menu-btn"]').click()
#     time.sleep(2)
#     driver.find_element('xpath', '//a[@id="logout_sidebar_link"]').click()
#
#


















