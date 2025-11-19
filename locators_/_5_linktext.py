'''
link text   :   The text present between the anchor tag, we call it as a link text.
                To locate the link text, we go for "link text" locator

'''
import time

## Eg1
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://demowebshop.tricentis.com/')
time.sleep(2)

driver.find_element('link text', 'Register').click()
time.sleep(2)
driver.find_element('link text', 'Log in').click()


###############################################################################

## Eg2

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.myntra.com/')
time.sleep(2)

driver.find_element('link text', 'Women').click()
time.sleep(2)
driver.find_element('link text', 'Home').click()
time.sleep(2)
driver.find_element('link text', 'Genz').click()








































