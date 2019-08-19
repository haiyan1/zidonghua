from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
import unittest


class Service(unittest.TestCase):

    def setUp(self):
        self.client = webdriver.Chrome()
        self.client.set_window_size(1200, 1020)
        time.sleep(2)
        self.url = "http://10.8.40.233:8080/api/index.html#/login"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_chanpgunali(self):
        client = self.client
        url = "http://10.8.40.233:8080/api/index.html#/login"
        client.get(url)
        time.sleep(2)

        # 输入用户名和密码
        yonghuming = client.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div/form/div[1]/input').send_keys(
            "admin")
        mima = client.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div/form/div[2]/input').send_keys(
            "123456")

        # 点击登录按钮
        client.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div/form/button').click()
        time.sleep(2)

        # 切换到系统主菜单
        client.switch_to.window(client.window_handles[-1])

        # 切换到产品一级菜单
        client.find_element_by_xpath('//*[@id="app"]/div/div/ul/li[4]/a/span').click()
        time.sleep(1)

        # 点击新增产品按钮
        client.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div/div[2]/div[2]/div/button').click()
        time.sleep(1)

        # 选择待上传的文件
        client.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div/div/div/div[1]/div/div[2]/form/div/div[2]/div[2]/div/input').send_keys(
            'C:/Users/Administrator/Desktop/sg.json')

        # 点击弹窗的确定按钮
        client.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div/div/div/div[1]/div/div[3]/span/button[2]/span').click()
        time.sleep(3)

        try:
            yanz1 = client.find_element_by_xpath('/html/body/div[2]/div').text
            if yanz1 == "产品导入成功":
                print("产品管理用例执行成功，测试结果为通过")
        except:
            print("产品管理用例执行失败，测试结果为不通过")

    def tearDown(self):
        self.client.quit()
        self.assertEqual([],self.verificationErrors)




