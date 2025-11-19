import time

# ## Solution1
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.makemytrip.com/')       ## login form appears
# driver.maximize_window()
# time.sleep(2)
#
# ## close the login form
# driver.find_element('xpath', '//span[@class="commonModal__close"]').click()
# time.sleep(2)
#
# ## click on departure
# driver.find_element('xpath', '//span[text()="Departure"]').click()
# time.sleep(2)
#
# def select_date(month, date):
#     while True:
#         try:
#             driver.find_element('xpath', f'//div[text()="{month}"]/../..//p[text()="{date}"]').click()
#             break
#         except:
#             driver.find_element('xpath', '//span[@aria-label="Next Month"]').click()
#
# select_date('July 2026', 15)
#
# ###############################################################################################################
#
# ## Solution2
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.makemytrip.com/')           ## login form will appear
# driver.maximize_window()
# time.sleep(2)
#
# ## closing the login form
# driver.find_element('xpath', '//span[@class="commonModal__close"]').click()
# time.sleep(2)
#
# ## click on departure
# driver.find_element('xpath', '//span[text()="Departure"]').click()
# time.sleep(2)
#
# while True:
#     month = driver.find_element('xpath', '(//div[@class="DayPicker-Caption"])[1]')
#     print(month.text)
#
#     if month.text == 'February 2026':
#         driver.find_element('xpath', '(//p[text()="20"])[1]').click()
#         break
#     else:
#         driver.find_element('xpath', '//span[@aria-label="Next Month"]').click()


###############################################################################################################

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
opts.add_argument("--disable-notifications")

driver = webdriver.Chrome(opts)

driver.get('https://www.goibibo.com/')
time.sleep(2)

driver.find_element('xpath', '//span[@class="logSprite icClose"]').click()
time.sleep(2)

driver.find_element('xpath', '//span[text()="Departure"]').click()
time.sleep(2)

while True:
    try:
        driver.find_element('xpath', '//div[text()="June 2026"]/../..//p[text()="20"]').click()
        break
    except:
        driver.find_element('xpath', '//span[@class="DayPicker-NavButton DayPicker-NavButton--next"]').click()






























