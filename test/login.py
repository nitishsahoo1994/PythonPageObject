from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import unittest
from PageObjectModule.pages.LoginPage import Loginpage
from PageObjectModule.genericLib.FileLib import FileLib

fil = FileLib()

class BaseClass:

    @classmethod
    def setUpClass(cls) -> None:

        cls.driver=webdriver.Chrome(executable_path='C:\Selenium\chromedriver_win32\chromedriver.exe')
        cls.driver.get(fil.getPropertyFile('url'))
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def setUp(self) -> None:
        driver = self.driver
        login=Loginpage(driver)
        login.loginProcess(fil.getPropertyFile('username'),fil.getPropertyFile('password'))

    def tearDown(self) -> None:
        driver = self.driver
        action=ActionChains(driver)
        action.move_to_element(By.XPATH,"//span[text()=' Administrator']/../following-sibling::td[1]/img").perform()
        driver.find_element(By.XPATH,"//a[text()='Sign Out']").click()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()




