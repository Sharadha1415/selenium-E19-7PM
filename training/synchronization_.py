'''
SYNCHRONIZATION :   Matching the speed of the webdriver to the speed of the web-application

There are 2 types
*   unconditional synchronization   :   No conditions are passed
            We achieve unconditional synchronization by passing time.sleep()
            Unnecessary wait is too much in unconditional synchronization.

*   conditional synchronization     :   Conditions are passed
        There are 2 types
        *   implicit_wait   :   Here the conditions are internally given.
                                SYNTAX  :   driver.implicitly_wait(n_seconds)
                                Whenever there is a delay, implicit_wait will automatically make the driver wait for n seconds.
                                It will wait until the element is available,
                                As soon as the element is available, it will start performing the operations right away.
                                There is no unnecessary wait.
                                One implicit_wait is sufficient for the whole program
                                It will be applied globally.

        *   explicit_wait   :   Here the conditions are passed externally
                                Here the wait happens  based on a condition

                                We should import WebDriverWait and expected_conditions

                                from selenium.webdriver.support.ui import WebDriverWait
                                from selenium.webdriver.support import expected_conditions
                                    WebDriverWait       --> class
                                    expected_conditions --> module

                                wait_obj = WebDriverWait(driver, timeouttime)

        WebDriverWait   :   It allows the driver to wait for a certain condition to check before we continue the operation.
                            Instead of waiting for a fixed amount of time, it waits until a condition is True or maximum time is reached.

        expected_conditions :   The conditions to be applied on the web-elements are already pre-defined and they are defined in expected_conditions.py
                            To make use of the pre-defined conditions we import expected_conditions

        until()         :   It is a method of WebDriverWait
                            It checks whether the given condition is satisfied or not
                            If the condition is True, it will continue the operations.
                            If the condition is False, it will always gives TimeOutException


'''

import time

# ## time.sleep()
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-E19-7PM-Aug28-2025\files\loading.html')
# time.sleep(20)
#
# driver.find_element('xpath', '//input[@name="fname"]').send_keys('Mounika')
# time.sleep(1)
# driver.find_element('xpath', '//input[@name="lname"]').send_keys('KM')
#
# #################################################################################################
#
# ## implicit_wait
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-E19-7PM-Aug28-2025\files\loading.html')
# driver.implicitly_wait(30)
#
# driver.find_element('xpath', '//input[@name="fname"]').send_keys('Mounika')
# driver.find_element('xpath', '//input[@name="lname"]').send_keys('KM')
#
# # #################################################################################################
#
# ## explicit_wait
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
# wait_obj = WebDriverWait(driver, 30)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-E19-7PM-Aug28-2025\files\loading.html')
#
# wait_obj.until(expected_conditions.visibility_of_element_located(('xpath', '//div[contains(text(), "FirstName")]')))
#
# driver.find_element('xpath', '//input[@name="fname"]').send_keys('Mounika')
# time.sleep(1)
# driver.find_element('xpath', '//input[@name="lname"]').send_keys('KM')
#
#
# #################################################################################################
#
# ## explicit_wait
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
# wait_obj = WebDriverWait(driver, 10)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
# driver.find_element('xpath', '//input[@id="user-name"]').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('xpath', '//input[@id="password"]').send_keys('secret_sauceeeeeeeee')
# time.sleep(1)
# driver.find_element('xpath', '//input[@id="login-button"]').click()
# time.sleep(2)
#
# try:
#     wait_obj.until(expected_conditions.visibility_of_element_located(('xpath', '//span[text()="Products"]')))
#     print("successfull login")
# except:
#     print("unsuccesfull login")

#################################################################################################

# ## unconditional synchronization
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-E19-7PM-Aug28-2025\files\progressbar.html')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Click Me"]').click()
# time.sleep(40)
# driver.find_element('xpath', '//button[text()="Click Me"]').click()

#################################################################################################

## conditional synchronization

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

wait_obj = WebDriverWait(driver, 45)
driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-E19-7PM-Aug28-2025\files\progressbar.html')
time.sleep(2)

driver.find_element('xpath', '//button[text()="Click Me"]').click()

wait_obj.until(expected_conditions.visibility_of_element_located(('xpath', '//div[text()="100%"]')))
time.sleep(1)

driver.find_element('xpath', '//button[text()="Click Me"]').click()


























































