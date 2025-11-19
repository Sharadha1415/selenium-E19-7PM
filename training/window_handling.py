import time

# ## Eg1
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# ac_obj = ActionChains(driver)
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# handles1 = driver.window_handles
# print(handles1)         ## [parent_handle]
#
# ## scroll down till the end of the application
# ac_obj.send_keys(Keys.END).perform()
# time.sleep(2)
#
# ## click on google+
# driver.find_element('xpath', '//a[text()="Google+"]').click()       ## opens in a new tab
# time.sleep(2)
#
# ## Initializing window_handles
# handles2 = driver.window_handles
# print(handles2)         ## [parent_handle, child_handle]
#
# ## handles2[0] -->  parent_handle
# ## handles2[1] -->  child handle
#
# ## switch the driver to the child_handle
# driver.switch_to.window(handles2[1])
# time.sleep(2)
#
# ## entering the data to the search box
# driver.find_element('xpath', '//input[@placeholder="Search blog"]').send_keys('Google pixel 9 pro')
# time.sleep(2)
#
# ## switch back to the parent tab
# driver.switch_to.window(handles2[0])
# time.sleep(2)
#
# ## clicking on youtube
# driver.find_element('xpath', '//a[text()="YouTube"]').click()       ## opens in a new tab
# time.sleep(2)
#
# ## Initializing window_handles
# handles3 = driver.window_handles
# print(handles3)         ## [parent_handle, child1, child2]
#
# ## switch to child2
# driver.switch_to.window(handles3[2])
# time.sleep(2)
#
# ##
# driver.find_element('xpath', '//input[@name="search_query"]').send_keys('Selenium Python')

# #########################################################################################################
#
#
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# opts.add_argument("--disable-notifications")
#
# driver = webdriver.Chrome(opts)
# ac_obj = ActionChains(driver)
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# ## hovering to the home element
# home = driver.find_element('xpath', '(//a[text()="Home"])[1]')
# ac_obj.move_to_element(home).perform()
# time.sleep(2)
#
# ## clicking on Pooja essentials
# driver.find_element('xpath', '//a[text()="Pooja Essentials"]').click()
# time.sleep(2)
#
# ## click on product
# driver.find_element('xpath', '//h4[@class="product-product"]').click()          ## It opens in a new tab
# time.sleep(2)
#
# ## initialize window handles
# handles = driver.window_handles
# print(handles)          ## [parent_handle, child_handle]
#
# ## switch the driver to the child_handle
# driver.switch_to.window(handles[1])
# time.sleep(2)
#
# ## click on add to bag
# driver.find_element('xpath', '//div[text()="ADD TO BAG"]').click()
# time.sleep(2)
#
# ## switch back to the parent tab
# driver.switch_to.window(handles[0])
# time.sleep(2)
#
# ## click on product
# driver.find_element('xpath', '(//h4[@class="product-product"])[2]').click()         ## opens in new tab
# time.sleep(2)
#
# ## initialize window_handles
# handles2 = driver.window_handles
# print(handles2)         ## [parent, child1, child2]
#
# ## switch the driver to child2
# driver.switch_to.window(handles2[2])
# time.sleep(2)
#
# ## click on add to bag
# driver.find_element('xpath', '//div[text()="ADD TO BAG"]').click()
# time.sleep(2)


#########################################################################################################


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
opts.add_argument("--disable-notifications")

driver = webdriver.Chrome(opts)
ac_obj = ActionChains(driver)

driver.get('https://www.myntra.com/')
time.sleep(2)

home = driver.find_element('xpath', '(//a[text()="Home"])[1]')
ac_obj.move_to_element(home).perform()
time.sleep(2)

driver.find_element('xpath', '//a[text()="Pooja Essentials"]').click()
time.sleep(2)

driver.find_element('xpath', '//h4[@class="product-product"]').click()          ## It opens in a new tab
time.sleep(2)

driver.find_element('xpath', '(//h4[@class="product-product"])[2]').click()         ## opens in new tab
time.sleep(2)

driver.find_element('xpath', '(//h4[@class="product-product"])[3]').click()         ## opens in new tab
time.sleep(2)


def handling_windows():
    return driver.window_handles

handles_list = handling_windows()

for handle in handles_list:
    driver.switch_to.window(handle)

    if 'VEDANUM' in driver.title:
        driver.find_element('xpath', '//div[text()="ADD TO BAG"]').click()
        break

