# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AssignmentSeleniumPython(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://saucelabs.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_assignment_selenium_python(self):
        driver = self.driver
        driver.get(self.base_url )

# DID NOT WORK:        driver.find_element_by_link_text("Navigation").click()

        driver.find_element_by_class_name("hamburger").click()
        driver.find_element_by_xpath("//a[@title='Resources']").click()
          
        try: self.assertEqual("Resources", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()

        driver.find_element_by_class_name("hamburger").click()

        driver.find_element_by_css_selector("li.page.pull-left > a[title=\"Pricing\"]").click()
        try: self.assertEqual("Sauce Labs: Pricing", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()

        driver.find_element_by_class_name("hamburger").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Features')])[3]").click()
        try: self.assertEqual("Sauce Labs: Features", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
        
        driver.find_element_by_class_name("hamburger").click()

        driver.find_element_by_css_selector("li.page.pull-left > a[title=\"Docs\"]").click()
        try: self.assertEqual("Sauce Labs Docs", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
        
        driver.find_element_by_class_name("hamburger").click()
        driver.find_element_by_xpath("//a[@title='Sign up']").click()


        try: self.assertEqual("Sauce Labs: Sign Up for a Free Trial", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()

        driver.find_element_by_class_name("hamburger").click()

        driver.find_element_by_xpath("(//a[contains(text(),'Company')])[2]").click()
        try: self.assertEqual("Sauce Labs: Values", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
        
        driver.find_element_by_class_name("hamburger").click()
        driver.find_element_by_css_selector("li.page.pull-left > a[title=\"Enterprise\"]").click()
        try: self.assertEqual("Sauce Labs: Enterprise-grade testing on Sauce", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
        
        driver.find_element_by_class_name("hamburger").click()

        driver.find_element_by_xpath("//a[@title='Log in']").click()
        
        try: self.assertEqual("Sauce Labs: Login", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
        
        driver.find_element_by_class_name("hamburger").click()

        driver.find_element_by_xpath("//a[@title='Community']").click()
        try: self.assertEqual("Open Sauce", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
        
        driver.find_element_by_class_name("hamburger").click()

        driver.find_element_by_xpath("//a[@title='Solutions']").click()
        try: self.assertEqual("Selenium Testing by Sauce Labs", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
