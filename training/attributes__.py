import time


'''
text    :   It is a property of a web-element.
            It will give the text of the web-element
            SYNTAX  :   web_element.text
              
'''

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.myntra.com/')
time.sleep(2)

ele = driver.find_element('xpath', '//a[@data-group="home"]')
print(ele.text)


##################################################################################

'''
get_attribute   :   This is an attribute of a web-element.
                    It will give the attribute values.
                    
                    SYNTAX  :   web_element.get_attribute("attr_name")  
'''
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.myntra.com/')
time.sleep(2)

home = driver.find_element('xpath', '(//a[text()="Home"])[1]')
print(home.get_attribute('href'))
print(home.get_attribute('style'))
print(home.get_attribute('class'))
print(home.get_attribute('data-group'))















































