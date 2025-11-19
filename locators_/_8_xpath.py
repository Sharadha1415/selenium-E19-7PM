'''
xpath   :   It is a locator to locate any element on the application uniquely.
            Using xpath, we can locate the web elements using attributes, using text, can do indexing, can locate
            dynamically changing elements.
            We can locate any element on the application using xpath

            There are 2 types of xpath
            *   Absolute xpath  :   Starts from the root of html
                                    We use / to write the absolute xpath
                                    / represents immediate child

                                    DRAWBACKS
                                    *   Depends on the full path from the root
                                    *   Difficult to maintain
                                    *   Not reusable
                                    *   Not readable
                                    *   Very lengthy and time consuming

            *   Relative xpath  :   Doesnot start from the root of html
                                    We use // to write relative xpath
                                    // represents any child

'''
import time

# ## Eg1
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-E19-7PM-Aug28-2025\files\css_selector_dup.html')
# time.sleep(2)
#
# driver.find_element('xpath', 'html/body/input[1]').send_keys('susmitha')
# time.sleep(1)
# driver.find_element('xpath', 'html/body/input[2]').send_keys('susmitha@12345')

# ###########################################################################################################
#
# ## Eg2
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
# driver.find_element('xpath', 'html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('xpath', 'html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input').send_keys('secret_sauce')
# time.sleep(1)
# driver.find_element('xpath', 'html/body/div/div/div[2]/div[1]/div/div/form/input').click()

###########################################################################################################

'''
attribute name and value    :   //tagname[@attr_name="attr_value"]
                                @ represents attribute
'''

# ## Eg1
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.instagram.com/accounts/emailsignup/')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@aria-label="Mobile Number or Email"]').send_keys('harry@gmail.com')
# time.sleep(1)
# driver.find_element('xpath', '//input[@type="password"]').send_keys('harry@12345')
# time.sleep(1)
# driver.find_element('xpath', '//input[@name="fullName"]').send_keys('harry_potter')
# time.sleep(1)
# driver.find_element('xpath', '//input[@name="username"]').send_keys('harry_12345678')

###########################################################################################################

# ## Eg2
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//a[@data-group="women"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[@data-group="home"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[@data-group="genz"]').click()

###########################################################################################################

# ## Eg3
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.youtube.com')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@name="search_query"]').send_keys('vj siddhu vlogs')
# time.sleep(2)
# driver.find_element('xpath', '//button[@title="Search"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[@id="video-title"]').click()

###########################################################################################################
## Eg4

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@id="user-name"]').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('xpath', '//input[@placeholder="Password"]').send_keys('secret_sauce')
# time.sleep(1)
# driver.find_element('xpath', '//input[@value="Login"]').click()
# time.sleep(3)
# driver.find_element('xpath', '//button[@id="react-burger-menu-btn"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[@id="logout_sidebar_link"]').click()

###########################################################################################################

## Eg5

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://www.hotstar.com/')
# time.sleep(3)
# driver.find_element('xpath', '//button[@data-testid="modal-close-button"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[@aria-label="Search"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//input[@id="searchBar"]').send_keys('RRR')

###########################################################################################################

## Eg6

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://www.ajio.com/')
# time.sleep(2)
# driver.find_element('xpath', '//a[@title="WOMEN"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[@title="KIDS"]').click()

###########################################################################################################
'''
text    :   //tagname[text()="text"]
'''

# ## Eg1
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.flipkart.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//span[text()="Mobiles & Tablets"]').click()
# time.sleep(2)
#
# driver.find_element('xpath', '//span[text()="Become a Seller"]').click()
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Start Selling"]').click()
#
# ###########################################################################################################
#
# ## Eg2
#
# from selenium import webdriver
#
# driver = webdriver.Firefox()
#
# driver.get('https://www2.hm.com/en_in/index.html')
# time.sleep(4)
#
# driver.find_element('xpath', '//a[text()="Ladies"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Kids"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Home"]').click()

###########################################################################################################

# ## Eg3
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Women"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Beauty"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Genz"]').click()

###########################################################################################################

'''
Group indexing  :   (any_xpath)[index_num]
If we dont give any index number, by default it will always consider the first occurance

'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-E19-7PM-Aug28-2025\files\css_selector.html')
# time.sleep(2)
#
# driver.find_element('xpath', '(//input[@name="fname"])[1]').send_keys('Joey')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@name="fname"])[2]').send_keys('Chandler')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@name="fname"])[3]').send_keys('Ross')

###########################################################################################################

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '(//a[@class="desktop-main"])[2]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[@class="desktop-main"])[4]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[@class="desktop-main"])[6]').click()

###########################################################################################################

# ## Eg3
#
# from selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.python.org/')
# time.sleep(2)
#
# driver.find_element('xpath', '(//a[text()="Downloads"])[2]').click()

###########################################################################################################
'''
contains    :   To locate the partial portion of the complete text of any tagname
                SYNTAX  :   //tagname[contains(text(), "partial_text")]
                
'''

# ## Eg1
# from selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.giva.co/')
# time.sleep(2)
# driver.find_element('xpath', '//span[contains(text(), "Gold with Lab Diamonds")]').click()
# time.sleep(2)
# driver.find_element('xpath', '//span[contains(text(), "GIVA Gift Card")]').click()

###########################################################################################################

# ## Eg2
# from selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
# driver.find_element('xpath', '(//a[contains(text(), "Books")])[3]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[contains(text(), "Computers")])[3]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[contains(text(), "Electronics")])[3]').click()

###########################################################################################################

'''
Dependent-Independent xpath
    *   Identify the dependent and independent elements
    *   Write the xpath of the independent element
    *   Traverse back until we get the common match for dependent-independent element
    *   Continue the xpath for the dependent element
    

'''

'''
Eg1. wap to click on the checkbox of Ruby in demo.html
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-E19-7PM-Aug28-2025\files\demo.html')
# time.sleep(2)
#
# driver.find_element('xpath', '//td[text()="Ruby"]/..//input[@name="download"]').click()

#########################################################################################################
'''
Eg2.    wap to click on the download link of windows in demo.html
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-E19-7PM-Aug28-2025\files\demo.html')
# time.sleep(2)
#
# driver.find_element('xpath', '//td[text()="Windows"]/..//a[text()="Download"]').click()


#########################################################################################################

'''
Eg3.    wap to click on the release notes of python 3.13.4 in https://www.python.org/
'''

# from selenium import webdriver
#
# driver = webdriver.Firefox()
#
# driver.get('https://www.python.org/')
# time.sleep(2)
#
# driver.find_element('xpath', '(//a[text()="Downloads"])[1]').click()
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Python 3.13.4"]/../..//a[text()="Release Notes"]').click()

#########################################################################################################

'''
Eg4.    wap to print the sellprice and buyprice of bitcoin in https://www.iforex.in/tools/live-rates   
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.iforex.in/tools/live-rates')
# time.sleep(4)
#
# gold_sellprice = driver.find_element('xpath', '(//div[text()="Gold"]/../..//span)[2]')
# print(f'The sell price of gold is {gold_sellprice.text}')
#
# gold_buyprice = driver.find_element('xpath', '(//div[text()="Gold"]/../..//span)[3]')
# print(f'The buy price of gold is {gold_buyprice.text}')

#########################################################################################################
'''
Eg5.
Wap to print the price of mrf in https://in.tradingview.com
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://in.tradingview.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//span[text()="Search"]').click()
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@name="query"]').send_keys('mrf')
# time.sleep(1)
#
# driver.find_element('xpath', '(//span[@class="icon-KLRTYDjH"])[1]').click()
# time.sleep(2)
#
# mrf_price = driver.find_element('xpath', '//span[text()="MRF"]/../../..//span[@class="priceWrapper-qWcO4bp9"]')
# print(mrf_price.text)

#########################################################################################################

































