import time
import pytest

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

@pytest.fixture(scope='class')
def setup():
    driver = webdriver.Chrome(opts)
    driver.get("https://demowebshop.tricentis.com/")
    time.sleep(2)
    yield driver
    driver.close()














