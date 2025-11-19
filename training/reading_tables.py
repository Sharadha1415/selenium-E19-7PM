import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(2)

table_data = driver.find_elements('xpath', '//table[@name="BookTable"]//td')
# print(table_data)       ## list of web-elements         ## [wb1, wb2, wb3, wb4,..]

for r in range(2, 8):
    for c in range(1, 5):
        data = driver.find_element('xpath', f'//table[@name="BookTable"]//tr[{r}]/td[{c}]')
        print(data.text, end='\t\t')
    print()





























