from selenium import webdriver
import time
import unittest
from selenium.webdriver.support.ui import WebDriverWait


class Store(unittest.TestCase):
    def setUp(self):
        self.client = webdriver.Chrome()
        self.client.set_window_size(1300, 1020)
        time.sleep(2)
        self.url = "http://10.8.40.233:8080/api/index.html#/login"
        self.verificationErrors = []
        self.accept_next_alert = True
    def test_shouquan(self):
        self.username = "admin"
        self.password = "123456"
        client = self.client
        client.get(self.url)
        time.sleep(2)

        # 获取用户名输入框并输入用户名
        client.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div/form/div[1]/input').send_keys(self.username)

        # 获取密码输入框并输入密码
        t = client.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div/form/div[2]/input').send_keys(self.password)

        # 点击登录按钮
        client.find_element_by_css_selector(".btn").click()
        time.sleep(2)

        # 跳转到系统主菜单
        client.switch_to.window(client.window_handles[-1])

        # 点击授权管理一级菜单
        client.find_element_by_xpath('//*[@id="app"]/div/div/ul/li[7]/a/span').click()
        time.sleep(1)

        # 点击【用户授权管理】子菜单
        client.find_element_by_xpath('//*[@id="app"]/div/div/ul/li[7]/ul/li[2]/a').click()
        time.sleep(1)

        # 选择一个用户点击“加授权”按钮
        client.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div/div/div/div[3]/div[3]/table/tbody/tr[1]/td[5]/div/button[1]').click()
        time.sleep(2)

        # 选择第一个产品包
        client.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div/div/div/div[1]/div/div[2]/form/div[3]/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span').click()
        time.sleep(1)

        # 点击确定按钮
        client.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div/div[1]/div/div[3]/span/button[2]/span').click()
        time.sleep(3)

        try:
            yanz = client.find_element_by_xpath('/html/body/div[2]/div').text
            if yanz == "操作成功":
                print("用户授权成功")
            else:
                print("用户授权失败")
        except:
            print("用户授权失败")

    def tearDown(self):
        self.client.quit()
        self.assertEqual([],self.verificationErrors)


