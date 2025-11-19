'''
name    :   name is an attribute which is also a locator
            If we have "name" attribute, then we can go for "name" locator

            DRAWBACKS
            *   name is not unique
                Incase of multiple occurances, name locator will always consider the first occurance

'''


import time


# ## Eg1
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.instagram.com/')
# time.sleep(2)
#
# driver.find_element('name', 'username').send_keys('Ruchitha')
# time.sleep(1)
# driver.find_element('name', 'password').send_keys('ruchitha@12345')
# time.sleep(1)


###########################################################################################

# ## Eg2
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(2)
#
# driver.find_element('name', 'firstname').send_keys('Harry')
# time.sleep(1)
# driver.find_element('name', 'lastname').send_keys('Potter')
# time.sleep(1)
# driver.find_element('name', 'reg_email__').send_keys('harry@gmail.com')
# time.sleep(1)
# driver.find_element('name', 'reg_passwd__').send_keys('harry@12345')

###########################################################################################

## Eg3

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-E19-7PM-Aug28-2025\files\css_selector.html')
time.sleep(2)

driver.find_element('name', 'fname').send_keys('Mounika')
time.sleep(1)
driver.find_element('name', 'fname').send_keys('Swarnalatha')

## Both the values will be filled in the same textbox

































