from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
import unittest


class Product(unittest.TestCase):
    def setUp(self):
        self.client = webdriver.Chrome()
        self.client.set_window_size(1200, 1020)
        time.sleep(2)
        self.url="http://10.8.40.233:8080/api/index.html#/login"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_add(self):
        client = self.client
        client.get(self.url)
        time.sleep(2)
        self.product_tag = "12344"
        self.product_name = "新建产品包5"

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

        # 点击【产品包管理】菜单
        client.find_element_by_xpath('//*[@id="app"]/div/div/ul/li[4]/ul/li[2]/a').click()
        time.sleep(1)
        # 点击“添加产品包”按钮
        client.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div/div[1]/div[2]/div/button/span').click()

        # 输入产品包tag
        client.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div/div/div/div[1]/div/div[2]/form/div[1]/div/div[1]/input').send_keys(
            self.product_tag)
        # 输入产品包名称
        client.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div/div/div/div[1]/div/div[2]/form/div[2]/div/div[1]/input').send_keys(
            self.product_name)
        time.sleep(1)
        client.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div/div/div/div[1]/div/div[2]/form/div[3]/div/div/div[1]/input').click()
        time.sleep(1)
        # 产品包类型选择“实时音频业务”
        client.find_element_by_xpath('/html/body/div[3]/div/div[1]/ul/li[2]/span').click()

        # 点击产品列表
        time.sleep(1)
        client.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div/div/div/div[1]/div/div[2]/form/div[4]/div/div/div[2]/input').click()
        # 选择第一个产品
        time.sleep(1)
        client.find_element_by_xpath('/html/body/div[4]/div/div[1]/ul/li[1]/span').click()
        client.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div/div[1]/div/div[2]').click()
        # 点击确定按钮，提交表单信息
        time.sleep(1)
        client.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div/div/div/div[1]/div/div[3]/span/button[2]/span').click()
        time.sleep(2)

        try:
            # 获取弹窗的内容作为验证点
            yanz = client.find_element_by_xpath('/html/body/div[2]/div').text
            if yanz == ("添加产品包 " + self.product_name + " 成功"):
                print("产品包管理用例执行成功，测试结果通过")
            else:
                print("产品包管理用例执行失败，测试结果不通过")
        except:
            print("产品包管理用例执行失败，测试结果不通过")


    def tearDown(self):
        self.client.quit()
        self.assertEqual([],self.verificationErrors)
