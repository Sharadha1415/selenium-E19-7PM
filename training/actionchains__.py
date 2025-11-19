'''
The operations which involve mouse(Right click, double click, moue hovering, drag and drop, scrolling)/keyboard,
we call them as "low-level" operations.
To perform low-level operations in selenium, we go for ActionChains

'''
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

ac_obj = ActionChains(driver)

####################################################################################################

# ## mouse hovering operation
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# women = driver.find_element('xpath', '(//a[text()="Women"])[1]')
# ac_obj.move_to_element(women).perform()
# time.sleep(2)
#
# home = driver.find_element('xpath', '(//a[text()="Home"])[1]')
# ac_obj.move_to_element(home).perform()
# time.sleep(2)
#
# genz = driver.find_element('xpath', '(//a[text()="Genz"])[1]')
# ac_obj.move_to_element(genz).perform()


####################################################################################################

'''
Double click
'''

## Eg1
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# ele1 = driver.find_element('xpath', '//button[text()="Copy Text"]')
# ac_obj.double_click(ele1).perform()

##--------------------------------------------------------------------------------------------------------
# ## Eg2
# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(2)
#
# ele = driver.find_element('xpath', '//div[text()="Create a new account"]')
# ac_obj.double_click(ele).perform()

####################################################################################################

'''
Right click
'''
#
# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(2)
#
# # ac_obj.context_click().perform()        ## It will right click at the start of the application
#
# ## To right click on a specific element
# ele = driver.find_element('xpath', '//div[text()="Create a new account"]')
# ac_obj.context_click(ele).perform()

####################################################################################################

'''
Scrolling operations
'''

# driver.get('https://www.swarovski.com/')
# time.sleep(2)

# ## page-down operation
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
#
# ac_obj.send_keys(Keys.PAGE_UP).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_UP).perform()


# ## Scroll down to the end of the application
# ac_obj.send_keys(Keys.END).perform()
# time.sleep(3)
# ac_obj.send_keys(Keys.HOME).perform()


##-----------------------------------------------------------------------
# ## to scroll to a particular web-element
#
# driver.get('https://www.swarovski.com/')
# time.sleep(2)
#
# ele = driver.find_element('xpath', '//h3[text()="Maximum brilliance"]')
# ac_obj.scroll_to_element(ele).perform()

####################################################################################################

'''
Drag and drop
'''

# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# ele = driver.find_element('xpath', '//h2[text()="SVG Elements"]')
# ac_obj.scroll_to_element(ele).perform()
#
# draggable_ele = driver.find_element('xpath', '//div[@id="draggable"]')
# droppable_ele = driver.find_element('xpath', '//div[@id="droppable"]')
#
# ac_obj.drag_and_drop(draggable_ele, droppable_ele).perform()

####################################################################################################

# ## TAB key
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@id="name"]').send_keys('susmita')
# time.sleep(2)
#
# ac_obj.send_keys(Keys.TAB).perform()            ## It will go to email textbox
# time.sleep(1)
#
# ac_obj.send_keys('susmita@gmail.com').perform()
#

####################################################################################################
# ## BACKSPACE
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@id="name"]').send_keys('susmita')
# time.sleep(2)
#
# ac_obj.send_keys(Keys.BACKSPACE).perform()
# time.sleep(1)
# ac_obj.send_keys(Keys.BACKSPACE).perform()

####################################################################################################

## ctrl+a
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# ac_obj.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).perform()

####################################################################################################

# ## ctrl + backspace
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@id="name"]').send_keys('susmita')
# time.sleep(2)
#
# ac_obj.key_down(Keys.CONTROL).send_keys(Keys.BACKSPACE).key_up(Keys.CONTROL).perform()

####################################################################################################

driver.get('https://www.facebook.com/r.php?entry_point=login')
time.sleep(2)

fname = driver.find_element('xpath', '//input[@name="firstname"]')
lname = driver.find_element('xpath', '//input[@name="lastname"]')

fname.send_keys('Harry')
time.sleep(2)

fname.send_keys(Keys.CONTROL + 'a')         ## select the data
fname.send_keys(Keys.CONTROL + 'c')         ## copy the data

ac_obj.send_keys(Keys.TAB).perform()        ## switching the control to last name
lname.send_keys(Keys.CONTROL + 'v')         ## paste the data












