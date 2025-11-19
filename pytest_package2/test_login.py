import time
import allure

class TestLogin:

    def test_login_link(self, setup):
        setup.find_element('xpath', '//a[text()="Log in"]').click()
        time.sleep(2)

    def test_login_email(self, setup):
        setup.find_element('id', 'Email').send_keys('ram@gmail.com')

    def test_login_pwd(self, setup):
        setup.find_element('id', 'Password').send_keys('ram@12345')

        allure.attach(
            setup.get_screenshot_as_png(),
            name="demo_loginpage",
            attachment_type=allure.attachment_type.PNG
        )
































