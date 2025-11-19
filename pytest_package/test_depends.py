import time
import pytest

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
#
# @pytest.mark.dependency(depends=['test_login'])
# def test_logout():
#     driver.find_element('xpath', '//button[@id="react-burger-menu-btn"]').click()
#     time.sleep(2)
#     driver.find_element('xpath', '//a[@id="logout_sidebar_link"]').click()

################################################################################################################

# @pytest.mark.dependency()
# def test_login():
#     print("login executing")
#
#
# @pytest.mark.dependency(depends=['test_login'])         ## test_logout is dependent on test_login
# def test_logout():
#     print("logout executing")
#
# ## collected 2 items
# ## test_depends.py::test_login     login executing         PASSED
# ## test_depends.py::test_logout    logout executing        PASSED

################################################################################################################

# @pytest.mark.dependency()
# def test_login():
#     raise Exception
#
# @pytest.mark.dependency(depends=['test_login'])         ## test_logout is dependent on test_login
# def test_logout():
#     print("logout executing")
#
# ## collected 2 items
# ## test_depends.py::test_login         FAILED
# ## test_depends.py::test_logout        SKIPPED (test_logout depends on test_login)

################################################################################################################

# @pytest.mark.dependency()
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.dependency()
# def test_login():
#     print("login executing")
#
# @pytest.mark.dependency(depends=['test_reg', 'test_login'])         ## test_logout is dependent on test_login
# def test_logout():
#     print("logout executing")
#
# ## collected 3 items
# ## test_depends.py::test_login     login executing     PASSED
# ## test_depends.py::test_reg       reg executing       PASSED
# ## test_depends.py::test_logout    logout executing    PASSED

################################################################################################################

# @pytest.mark.dependency()
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.dependency()
# def test_login():
#     pt("login executing")
#
# @pytest.mark.dependency(depends=['test_reg', 'test_login'])         ## test_logout is dependent on test_login and test_reg
# def test_logout():
#     print("logout executing")
#
# ## collected 3 items
# ## test_depends.py::test_reg       reg executing       PASSED
# ## test_depends.py::test_login                         FAILED
# ## test_depends.py::test_logout                        SKIPPED (test_logout depends on test_login)

################################################################################################################

# class TestSample:
#
#     @pytest.mark.dependency()
#     def test_login(self):
#         print("login executing")
#
#     @pytest.mark.dependency(depends=['test_login'])
#     def test_logout(self):
#         print("logout executing")
#
#
# ## collected 2 items
# ## test_depends.py::TestSample::test_login     login executing     PASSED
# ## test_depends.py::TestSample::test_logout                        SKIPPED (test_logout depends on test_login)


################################################################################################################

# class TestSample:
#
#     @pytest.mark.dependency()
#     def test_login(self):
#         print("login executing")
#
#     @pytest.mark.dependency(depends=['TestSample::test_login'])
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 2 items
# ## test_depends.py::TestSample::test_login     login executing     PASSED
# ## test_depends.py::TestSample::test_logout    logout executing    PASSED

################################################################################################################

# class TestSample:
#
#     @pytest.mark.dependency()
#     def test_login(self):
#         prt("login executing")
#
#     @pytest.mark.dependency(depends=['TestSample::test_login'])
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 2 items
# ## test_depends.py::TestSample::test_login     FAILED
# ## test_depends.py::TestSample::test_logout    SKIPPED (test_logout depends on TestSample::test_login)


################################################################################################################

import time
import pytest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

wait_obj = WebDriverWait(driver, 5)

driver.get('https://www.saucedemo.com/')
time.sleep(2)


@pytest.mark.dependency()               ## Independent testcase
def test_login():
    driver.find_element('id', 'user-name').send_keys('standard_user')
    driver.find_element('id', 'password').send_keys('secret_sauceeeee')
    driver.find_element('id', 'login-button').click()
    time.sleep(2)
    wait_obj.until(expected_conditions.visibility_of_element_located(('xpath', '//span[text()="Products"]')))
    # assert driver.find_element('xpath','//span[text()="Products"]')












