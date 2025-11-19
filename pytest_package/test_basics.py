'''
Pytest  :   Pytest is a unit testing framework.
            Testing the small portion of the entire program, we call it as unit testing.
            To perform unit testing in selenium, we go for pytest

            To install pytest
            Go to command prompt    -->     pip install pytest

            RULES
            *   filename should always start with test_ or end with _test
                Eg  :   test_filename.py        OR          filename_test.py
            *   function names/method names should start with test_
                Eg  :   def test_func_name():
                            pass
            *   Classname also should start with Test
                Eg  :   class TestClassName:
                            pass

            When we follow the rules, pytest will automatically recognize the functions, files, classes which are
            following the rules.
            So we can execute the functions without calling them and we can execute the classes without creating the object

            To execute the test_files
            Right click anywhere on the test file --> open in --> terminal --> pytest test_filename.py -vs
                -v  --> Verbosity.  This gives the detailed explanation of the code
                -s  --> Scripting.  This prints all the prints statements



'''
import time

# def login():
#     print("login executing")
#
# def logout():
#     print("logout executing")
#
# login()
# logout()
#
# ## To execute a function, function call is mandatory
#
# #######################################################################################
#
# class Sample:
#
#     def login(self):
#         print("login executing")
#
#     def logout(self):
#         print("logout executing")
#
# s_obj = Sample()
# s_obj.login()
# s_obj.logout()
#
# ## To execute the class, we should create the object and call the attributes

#######################################################################################

# def test_login():
#     print("login executing")
#
# def test_logout():
#     print("logout executing")
#
# ## collected 2 items
# ## test_basics.py::test_login      login executing         PASSED
# ## test_basics.py::test_logout     logout executing        PASSED

#######################################################################################

# def test_login():
#     print("login executing")
#
# def signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")
#
# ## collected 2 items
# ## test_basics.py::test_login      login executing         PASSED
# ## test_basics.py::test_logout     logout executing        PASSED

'''
signup function is not executed because it is not following the pytest rules.
Pytest can only recognize the functions which are following the rules.
'''

#######################################################################################

# def test_login():
#     print("login executing")
#     def test_signup():
#         print("signup executing")
#
# ## collected 1 item
# ## test_basics.py::test_login      login executing          PASSED

'''
Incase of nested test_functions, pytest cannot recognize the inner function, it can recognize only the outer test_function 
'''

#######################################################################################

# def test_login():
#     pri("login executing")
#
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")
#
# ## collected 3 items
# ## test_basics.py::test_login                              FAILED
# ## test_basics.py::test_signup     signup executing        PASSED
# ## test_basics.py::test_logout     logout executing        PASSED

'''
Failure of one testcase doesnot affect the execution of the other testcases 
'''

#######################################################################################

# def test_login():
#     print("login executing")
#
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")
#
# test_login()
# test_signup()
# test_logout()
#
# ## collecting ... login executing
# ## signup executing
# ## logout executing
# ## collected 3 items
# ## test_basics.py::test_login      login executing             PASSED
# ## test_basics.py::test_signup     signup executing            PASSED
# ## test_basics.py::test_logout     logout executing            PASSED

'''
When we call the test functions, the execution will happen twice.
First it will execute the function call and then the pytest execution
'''

#######################################################################################

# def test_add(a, b):
#     print(a + b)
#
# ## collected 1 item
# ## test_basics.py::test_add        ERROR

'''
NOTE    :   test_functions do not take any parameters
'''

#######################################################################################

# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 3 items
# ## test_basics.py::TestSample::test_login      login executing         PASSED
# ## test_basics.py::TestSample::test_signup     signup executing        PASSED
# ## test_basics.py::TestSample::test_logout     logout executing        PASSED


#######################################################################################

# class Sample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 0 items
#
# ## classname is not following the pytest rules

#######################################################################################

# class TestSample:
#
#     def login(self):
#         print("login executing")
#
#     def signup(self):
#         print("signup executing")
#
#     def logout(self):
#         print("logout executing")
#
# ## collected 0 items
#
# ## attributes are not following the rules


#######################################################################################

# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# s_obj = TestSample()
# s_obj.test_login()
# s_obj.test_signup()
# s_obj.test_logout()
#
# ## collecting ... login executing
# ## signup executing
# ## logout executing
# ## collected 3 items
# ## test_basics.py::TestSample::test_login      login executing         PASSED
# ## test_basics.py::TestSample::test_signup     signup executing        PASSED
# ## test_basics.py::TestSample::test_logout     logout executing        PASSED

#############################################################################################
#
# class TestSample:
#
#     def test_login(self, name):
#         print("login executing")
#
# ## collected 1 item
# ## test_basics.py::TestSample::test_login          ERROR

#######################################################################################

# class TestSample:
#
#     def __init__(self):
#         pass
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
# #
# # ## collected 0 items
# # ## PytestCollectionWarning: cannot collect test class 'TestSample' because it has a __init__ constructor


#######################################################################################

import unittest
from selenium import webdriver

class TestRegister(unittest.TestCase):

    @classmethod
    def setup(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://demowebshop.tricentis.com/')
        time.sleep(2)

    def test_reg_link(self):
        self.driver.find_element('xpath', '//a[text()="Register"]').click()
        time.sleep(2)

    def test_gender_btn(self):
        self.driver.find_element('id', 'gender-male').click()

    def test_fname(self):
        self.driver.find_element('id', 'FirstName').send_keys('Ram')

    def test_lname(self):
        self.driver.find_element('id', 'LastName').send_keys('Kumar')

    def test_reg_email(self):
        self.driver.find_element('id', 'Email').send_keys('ram@gmail.com')

    def test_reg_pwd(self):
        self.driver.find_element('id', 'Password').send_keys('ram@12345')

    def test_confirm_pwd(self):
        self.driver.find_element('id', 'ConfirmPassword').send_keys('ram@12345')

if __name__ == "__main__":
    unittest.main()

# class TestLogin:
#
#     def test_login_link(self):
#         driver.find_element('xpath', '//a[text()="Log in"]').click()
#         time.sleep(2)
#
#     def test_login_email(self):
#         driver.find_element('id', 'Email').send_keys('ram@gmail.com')
#
#     def test_login_pwd(self):
#         driver.find_element('id', 'Password').send_keys('ram@12345')

#######################################################################################










































































