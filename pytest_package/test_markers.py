'''
Markers :   To group the testcases, we go for makers
    There are 2 types of markers
    *   custom marker
    *   inbuilt marker  :   There are 4 types
                            *   skip
                            *   skipif
                            *   parametrize
                            *   xfail

'''
import time

import pytest

# def test_login():
#     print("login executing")
#
# @pytest.mark.sanity
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.sanity
# def test_reg():
#     print("reg executing")
#
# def test_logout():
#     print("logout executing")
#
# ## In terminal
# ## pytest test_markers.py -vs -m="sanity"
# ## collected 4 items / 2 deselected / 2 selected
# ## test_markers.py::test_signup    signup executing       PASSED
# ## test_markers.py::test_reg       reg executing           PASSED

###################################################################################

# @pytest.mark.sanity
# def test_login():
#     print("login executing")
#
# @pytest.mark.smoke
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.regression
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.sanity
# def test_logout():
#     print("logout executing")
#
# ## In terminal
# ## pytest test_markers.py -vs -m="sanity"               --> test_login and test_logout will execute
# ## pytest test_markers.py -vs -m="smoke"                --> test_signup will execute
# ## pytest test_markers.py -vs -m="regression"           --> test_reg will execute
# ## pytest test_markers.py -vs -m="sanity and smoke"     --> 0 executed
# ## pytest test_markers.py -vs -m="sanity and regression"--> 0 executed
# ## pytest test_markers.py -vs -m="smoke and regression" --> 0 executed
# ## pytest test_markers.py -vs -m="sanity or regression" --> test_login, test_reg and test_logout will execute
# ## pytest test_markers.py -vs -m="smoke or regression"  --> test_signup and test_reg will execute
# ## pytest test_markers.py -vs -m="sanity and smoke"     --> test_login, test_signup and test_logout will execute


###################################################################################

# @pytest.mark.smoke
# @pytest.mark.sanity
# def test_login():
#     print("login executing")
#
# @pytest.mark.smoke
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.sanity
# @pytest.mark.regression
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.smoke
# @pytest.mark.regression
# def test_logout():
#     print("logout executing")
#
# ## In terminal
# ## pytest test_markers.py -vs -m="sanity"                   --> test_login and test_teg will execute
# ## pytest test_markers.py -vs -m="smoke"                    --> test_login, test_signup and test_logout
# ## pytest test_markers.py -vs -m="regression"               --> test_reg and test_logout
# ## pytest test_markers.py -vs -m="smoke and sanity"         --> test_login will exceute
# ## pytest test_markers.py -vs -m="smoke and regression"     --> test_logout will execute
# ## pytest test_markers.py -vs -m="sanity and regression"    --> test_reg will execute
# ## pytest test_markers.py -vs -m="smoke or sanity"          --> all 4 will execute
# ## pytest test_markers.py -vs -m="smoke or regression"      --> all 4 will execute
# ## pytest test_markers.py -vs -m="sanity or regression"     --> test_login, test_signup and test_logout will execute
#
# ###################################################################################
#
# @pytest.mark.sanity
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_reg(self):
#         print("reg executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## All the attributes of the TestSample class belongs to sanity
#
# ###################################################################################

# class TestSample:
#
#     @pytest.mark.sanity
#     def test_login(self):
#         print("login executing")
#
#     def test_reg(self):
#         print("reg executing")
#
#     @pytest.mark.smoke
#     def test_signup(self):
#         print("signup executing")
#
#     @pytest.mark.sanity
#     def test_logout(self):
#         print("logout executing")


###################################################################################
'''
skip    :   To skip the execution of the testcases, we use skip marker.
            This is an unconditional skip.
            Means, to skip the execution of the testcase, we dont have to pass any condition or reason.
            It will just skip the execution of the testcases which are decorated with @pytest.mark.skip
            
            SYNTAX  :   @pytest.mark.skip([reason])
                        def test_case():
                            pass   
'''

# def test_login():
#     print("login executing")
#
# @pytest.mark.skip
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.skip
# def test_reg():
#     print("reg executing")
#
# def test_logout():
#     print("logout executing")
#
# ## collected 4 items
# ## test_markers.py::test_login     login executing         PASSED
# ## test_markers.py::test_signup                            SKIPPED (unconditional skip)
# ## test_markers.py::test_reg                               SKIPPED (unconditional skip)
# ## test_markers.py::test_logout    logout executing        PASSED

####################################################################################

# def test_login():
#     print("login executing")
#
# @pytest.mark.skip(reason="signup already done")
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.skip(reason="reg already done")
# def test_reg():
#     print("reg executing")
#
# def test_logout():
#     print("logout executing")
#
# ## collected 4 items
# ## test_markers.py::test_login     login executing     PASSED
# ## test_markers.py::test_signup                        SKIPPED (signup already done)
# ## test_markers.py::test_reg                           SKIPPED (reg already done)
# ## test_markers.py::test_logout    logout executing    PASSED


####################################################################################

# @pytest.mark.skip
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_reg(self):
#         print("reg executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 4 items
# ## test_markers.py::TestSample::test_login     SKIPPED (unconditional skip)
# ## test_markers.py::TestSample::test_signup    SKIPPED (unconditional skip)
# ## test_markers.py::TestSample::test_reg       SKIPPED (unconditional skip)
# ## test_markers.py::TestSample::test_logout    SKIPPED (unconditional skip)

####################################################################################

'''
skipif  :   This is also used to skip the execution of the testcases, but the skip is based on a condition
            skipif takes 2 parameters, condition and reason
            
            SYNTAX  :   @pytest.mark.skipif(condition, reason)
                        def test_case():
                            pass       
                        
                        If the condition is True, it will skip the execution of the testcase
                        If the condition is False, then it will execute the testcase
                        
                        If we skip the condition, by default the condition will be considered as True.
                        If we skip the reason, it will give error.
'''

# @pytest.mark.skipif(True, reason='login is completed')
# def test_login():
#     print("login executing")
#
# ## collected 1 item
# ## test_markers.py::test_login     SKIPPED (login is completed)

######################################################################################
#
# @pytest.mark.skipif(False, reason='login is completed')
# def test_login():
#     print("login executing")
#
# ## collected 1 item
# ## test_markers.py::test_login     login executing         PASSED


######################################################################################

# @pytest.mark.skipif(False)
# def test_login():
#     print("login executing")
#
# ## collected 1 item
# ## test_markers.py::test_login ERROR
#
# ## Because we did not give the reason
# ## reason is the mandatory parameter


######################################################################################

# @pytest.mark.skipif(reason='login done')
# def test_login():
#     print("login executing")
#
# ## collected 1 item
# ## test_markers.py::test_login SKIPPED         (login done)
#
# ## By default, condition is True.
# ## So if we skip the condition, the test case execution will be skipped

######################################################################################

'''
xfail   :   This is an expected failure

            SYNTAX  :   @pytest.mark.xfail
                        def test_func():
                            pass  
                        
                        We are expecting the test_func to fail.
                        If the testcase is failed, then the output will be XFAIL
                        If the testcase is passed, then the output will be XPASS
'''

# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# wait_obj = WebDriverWait(driver, 5)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# @pytest.mark.xfail
# def test_login():
#     driver.find_element('id', 'user-name').send_keys('standard_user')
#     driver.find_element('id', 'password').send_keys('secret_sauceeeeee')
#     driver.find_element('id', 'login-button').click()
#     time.sleep(2)
#     wait_obj.until(expected_conditions.visibility_of_element_located(('xpath', '//span[text()="Products"]')))

#######################################################################################################

# def test_case1():
#     print("tc1 executing")
#
# @pytest.mark.xfail
# def test_case2():
#     raise Exception("Expecting failure from this testcase")
#
# def test_case3():
#     pr("tc3 executing")
#
# def test_case4():
#     pt("tc4 executing")
#
# ## collected 4 items
# ## test_markers.py::test_case1     tc1 executing       PASSED
# ## test_markers.py::test_case2                         XFAIL
# ## test_markers.py::test_case3                         FAILED
# ## test_markers.py::test_case4                         FAILED

#######################################################################################################

# @pytest.mark.xfail
# def test_case1():
#     print("tc1 executing")

# @pytest.mark.xfail
# def test_case2():
#     raise Exception("Expecting failure from this testcase")
#
# ## collected 2 items
# ## test_markers.py::test_case1     tc1 executing       XPASS
# ## test_markers.py::test_case2                         XFAIL


#######################################################################################################

'''
parametrize
'''

@pytest.mark.parametrize("a, b", [(10, 20)])
def test_login(a, b):
    print(a + b)

## collected 1 item
## test_markers.py::test_login[10-20]      30      PASSED

##################################################################################

@pytest.mark.parametrize("a, b", [(10, 20), (10, -10), (90, 100), (99, 99), (2, 3), (1, 1)])
def test_login(a, b):
    print(a + b)

## collected 6 items
## test_markers.py::test_login[10-20]      30      PASSED
## test_markers.py::test_login[10--10]     0       PASSED
## test_markers.py::test_login[90-100]     190     PASSED
## test_markers.py::test_login[99-99]      198     PASSED
## test_markers.py::test_login[2-3]        5       PASSED
## test_markers.py::test_login[1-1]        2       PASSED

###################################################################################

# @pytest.mark.parametrize("a, b", [(10, 20, 30)])
# def test_login(a, b):
#     print(a + b)
#
# ## collected 0 items / 1 error
# ## The number of formal args and actual arsg doesnt match

###################################################################################

@pytest.mark.parametrize("a, b, c", [(10, 20, 30)])
def test_login(a, b):
    print(a + b)

## collected 0 items / 1 error


































