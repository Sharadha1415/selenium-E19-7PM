import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

## launch the application
driver.get('https://www.myntra.com/')
time.sleep(2)

## maximize browser
driver.maximize_window()
time.sleep(2)

# ## minimize window
# driver.minimize_window()

## To go back
driver.back()
time.sleep(2)

## To go forward
driver.forward()
time.sleep(2)

## To refresh
driver.refresh()
time.sleep(2)

## fullscreen_window
driver.fullscreen_window()
time.sleep(2)

## properties
print(driver.current_url)
print(driver.title)
print(driver.name)


#########################################################################

# Take screenshot

driver.save_screenshot('myntra_ss.png')
# By default the screenshot will be saved in the same location as our python file.

## To save the screenshot in a different location
driver.save_screenshot(r'C:\Users\Ramya\PycharmProjects\Sel-E19-7PM-Aug28-2025\screenshots_\myn_ss.png')

## close the browser
driver.close()












































