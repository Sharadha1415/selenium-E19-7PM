''''
partial link text   :   Same as link text, here also the tagname should be anchor tag
                        Instead of locating the complete text, we can locate the web-element using the partial portion of the text.
                        So to locate partial text we use "partial link text" locator
'''


import time

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# driver.find_element('partial link text', 'Books').click()
# time.sleep(2)
# driver.find_element('partial link text', 'Computers').click()
# time.sleep(2)
# driver.find_element('partial link text', 'Apparel & ').click()

################################################################################

## Eg2

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.kushals.com/')
time.sleep(2)

driver.find_element('partial link text', 'Bangles').click()
time.sleep(2)
driver.find_element('partial link text', 'Wedding Store').click()
time.sleep(2)
driver.find_element('partial link text', 'Happy Customers').click()
time.sleep(2)
driver.find_element('partial link text', 'Careers').click()
