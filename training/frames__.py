'''
iframe  :   It is an inline-frame
            The web-application inside another application is an iframe.

            The tagname of an iframe is always "iframe"

            To handle the iframes
            *   Locate the frame
            *   Switch the driver to the frame
                SYNTAX  :   driver.switch_to.frame(frame)
            *   Perform the operations inside the frame
            *   Once after performing the oprations inside the frame, switch back to the parent frame
                SYNTAX  :   driver.switch_to.parent_frame()

'''

import time

## Eg1
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
ac_obj = ActionChains(driver)

driver.get('https://www.linkedin.com')
time.sleep(2)

## locate the iframe
google_frame = driver.find_element('xpath', '//iframe[@title="Sign in with Google Button"]')

## switch the driver to the frame
driver.switch_to.frame(google_frame)

## perform the operations inside the frame
driver.find_element('xpath', '//span[text()="Continue with Google"]').click()
time.sleep(2)

## switch back to the parent frame
driver.switch_to.parent_frame()
time.sleep(2)

## scroll down until youtube frame is visible
ele = driver.find_element('xpath', '//h2[contains(text(), "Join your colleagues")]')
ac_obj.scroll_to_element(ele).perform()
time.sleep(2)

## locate the youtube frame
youtube_frame = driver.find_element('xpath', '//iframe[@title="Gayatri Iyer: In it to chase my dream | #InItTogether"]')

## switch the driver to the youtube frame
driver.switch_to.frame(youtube_frame)
time.sleep(2)

## perform the operations in the youtube frame
driver.find_element('xpath', '//button[@title="Play"]').click()
#
# ####################################################################################################
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-E19-7PM-Aug28-2025\files\iframe.html')
# time.sleep(2)
#
# ## locate the frame1
# frame1 = driver.find_element('xpath', '//iframe[@id="FR1"]')
#
# ## switch the driver to the frame1
# driver.switch_to.frame(frame1)
#
# ## perform the operations inside the frame1
# driver.find_element('xpath', '//input[@id="small-searchterms"]').send_keys('Books')
#
# ## switch back to parent frame
# driver.switch_to.parent_frame()
# time.sleep(2)
#
# ## locate the frame2
# frame2 = driver.find_element('xpath', '//iframe[@id="FR2"]')
#
# ## switch the driver to the frame2
# driver.switch_to.frame(frame2)
#
# ## perform the operations inside the frame2
# driver.find_element('xpath', '//input[@id="search_form"]').send_keys('vehicle insurance')
# time.sleep(2)
#
# ## switch back to parent frame
# driver.switch_to.parent_frame()

##################################################################################################

# ## Eg1
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# ac_obj = ActionChains(driver)
#
# driver.get('https://www.linkedin.com')
# time.sleep(2)
#
# f2 = driver.find_element('xpath', '//iframe[@name="microsoft_signin_iframe_1"]')
# driver.switch_to.frame(f2)












