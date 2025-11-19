'''


'''


import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-E19-7PM-Aug28-2025\files\css_selector.html')
time.sleep(2)

driver.find_element('tag name', 'input').send_keys('Prashant')
time.sleep(1)
driver.find_element('tag name', 'input').send_keys('Naveen')























