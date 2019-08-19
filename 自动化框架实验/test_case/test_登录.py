
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchAttributeException
from selenium.webdriver.support.ui import WebDriverWait
import HTMLTestRunner
import unittest, re


class Denglu(unittest.TestCase):
    def setUp(self):
        self.client = webdriver.Chrome()
        time.sleep(2)
        self.url="http://10.8.40.233:8080/api/index.html#/login"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_denglu(self):
        client = self.client
        client.get(self.url)
        time.sleep(2)

        # 获取用户名输入框
        e = client.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div/form/div[1]/input')

        # 获取密码输入框
        t = client.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div/form/div[2]/input')
        # 分别输入用户名和密码
        e.send_keys("admi")
        t.send_keys("123456")
        # element=WebDriverWait(client,10).until(lambda client:client.find_element_by_css_selector(".btn"))
        # 点击登录按钮
        client.find_element_by_css_selector(".btn").click()
        time.sleep(2)

        try:
            # 登录成功后跳转页面
            client.switch_to.window(client.window_handles[-1])
            # 在跳转页面上获取“监控业务”菜单，能获取到则登录成功，获取失败则登录失败
            element = client.find_element_by_xpath('//*[@id="app"]/div/div/ul/li[2]/ul/li[1]/a')
            print("")
            print("登录成功")
        except:
            print("")
            print("登录失败")


    def tearDown(self):
        self.client.quit()
        self.assertEqual([],self.verificationErrors)


if __name__ == "__main__":
    unittest.main()




