from selenium.webdriver.common.by import By


class Loginpage:
    def __init__(self,driver):
         self.driver=driver

         self.username_textbox_name="user_name"
         self.password_textBox_name='user_password'
         self.login_Button_id='submitButton'

    def loginProcess(self,username,password):
        self.driver.find_element(By.NAME,self.username_textbox_name).send_keys(username)
        self.driver.find_element(By.NAME,self.password_textBox_name).send_keys(password)
        self.driver.find_element(By.ID,self.login_Button_id).click()
