'''
Alerts  :   Alerts are not inspectable.
            Suppose if we are able to inspect, then it is not an alert.

            To handle the alerts, we will switch the driver to the alert
            SYNTAX  :   alert_obj = driver.switch_to.alert
                        alert_obj has two attributes to handle the alert
                        *   accept()    :   To accept the alert, we use alert_obj.accept()
                        *   dismiss()   :   To dismiss the alert, we use alert_obj.dismiss()

            There are different types alerts
            *   simple alert    :   If the alert is having only one option, then it is a simple alert.
                                    To handle the simple alert, first switch the driver to the alert
                                    Now we can either use accept or dismiss.
                                    alert_obj.accept()  or      alert_obj.dismiss()

            *   confirmation alert  :   If the alert is having two options, then it is a confirmation alert.
                                    To handle the confirmation alert, first switch the driver to the alert
                                    To click on OK/YES/AGREE,.. we give alert_obj.accept()
                                    To click on CANCEL/NO/DISAGREE,.. we give alert_obj.dismiss()

            *   Prompt alert    :   Here the alert will take the data from the user.
                                    To handle the prompt alert, first switch the driver to the alert
                                    alert_obj.send_keys("data")
                                    alert_obj.accept()



'''

import time
#
# ## Confirmation alert
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Confirmation Alert"]').click()
# time.sleep(2)
#
# ## switch the driver to the alert
# alert_obj = driver.switch_to.alert
#
# ## To click on OK/YES/AGREE,..
# alert_obj.accept()
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Confirmation Alert"]').click()
# time.sleep(2)
#
# ## To click on CANCEL/NO/DISAGREE,..
# alert_obj.dismiss()
#
# ######################################################################################
#
# ## Simple alert
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Simple Alert"]').click()
# time.sleep(2)
#
# alert_obj = driver.switch_to.alert
#
# alert_obj.accept()
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Simple Alert"]').click()
# time.sleep(2)
# alert_obj.dismiss()
#
# ######################################################################################
#
# ## prompt alert
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Prompt Alert"]').click()
# time.sleep(2)
#
# alert_obj = driver.switch_to.alert
#
# alert_obj.send_keys('Maria')
# alert_obj.accept()
#
#
# ######################################################################################
#
# ## Authentication pop-ups
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://the-internet.herokuapp.com/basic_auth')
#
# ## The above url will give a pop-up which will ask for the username and password to launch the application.
# ## It is not inspectable
#
# ##--------------------
#
# ## To handle such pop-ups, we will give the username and password in the url while launching the application
# ## SYNTAX   :   https://username:password@url
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')

######################################################################################

# ## file-upload pop-up
#
# ## single-file upload
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# choose_file = driver.find_element('xpath', '//input[@id="singleFileInput"]')
# file_path = r'C:\Users\Ramya\PycharmProjects\Sel-E19-7PM-Aug28-2025\files\ramya_resume.doc'
#
# choose_file.send_keys(file_path)
#
# ##--------------------------------------------------------------------------------------
#
# ## multiple-file upload
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# multiple_files = driver.find_element('xpath', '//input[@id="multipleFilesInput"]')
#
# f1 = r'C:\Users\Ramya\PycharmProjects\Sel-E19-7PM-Aug28-2025\files\css_selector.html'
# f2 = r'C:\Users\Ramya\PycharmProjects\Sel-E19-7PM-Aug28-2025\files\css_selector_dup.html'
# f3 = r'C:\Users\Ramya\PycharmProjects\Sel-E19-7PM-Aug28-2025\files\demo.html'
# f4 = r'C:\Users\Ramya\PycharmProjects\Sel-E19-7PM-Aug28-2025\files\ramya_resume.doc'
#
# multiple_files.send_keys(f'{f1}\n{f2}\n{f3}\n{f4}')
#
# ######################################################################################
#
# ## push notifications
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# opts.add_argument('--disable-notifications')
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.irctc.co.in/nget/train-search')


###################################################################



## Confirmation alert
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(2)

driver.find_element('xpath', '//button[text()="Confirmation Alert"]').click()
time.sleep(2)

def handle_alert():
    return driver.switch_to.alert

alert = handle_alert()
alert.accept()
time.sleep(2)

driver.find_element('xpath', '//button[text()="Confirmation Alert"]').click()
time.sleep(2)

## To click on CANCEL/NO/DISAGREE,..
alert.dismiss()


































