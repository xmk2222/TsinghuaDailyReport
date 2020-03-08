# -*- coding:utf-8 -*-
# @Time : 2020/3/8 15:35
# @Author : naihai
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class Report(object):
    def __init__(self, user_name, user_pass):
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.url = "https://thos.tsinghua.edu.cn/fp/view?m=fp#from=hall&" \
                   "serveID=d42b05be-1ad8-4d96-8c1e-14be2bb24e26&" \
                   "act=fp/serveapply"
        self.user_name = user_name
        self.user_pass = user_pass

    def run(self):
        self.__get_report_page()
        self.__submit_report()

    def __get_report_page(self):
        self.driver.get(self.url)
        # 登录
        if self.driver.find_element_by_xpath("//*[@id='theform']") is not None:
            print("尚未登录，登录中")
            self.driver.find_element_by_xpath('//*[@id="i_user"]').send_keys(self.user_name)
            self.driver.find_element_by_xpath('//*[@id="i_pass"]').send_keys(self.user_pass)
            # 点击 登录 按钮
            self.driver.find_element_by_xpath('//*[@id="theform"]/div[4]/a').click()
            time.sleep(3)
            try:
                self.driver.find_element_by_xpath('//*[@id="msg_note"]')
                print("您的用户名或密码不正确")
                raise RuntimeError("Login Failed")
            except NoSuchElementException:
                print("登录成功")
        else:
            print("已经处于登录状态")

    def __submit_report(self):
        self.driver.get(self.url)
        time.sleep(10)
        self.driver.find_element_by_xpath('//*[@id="commit"]').click()
        try:
            self.driver.find_element_by_xpath('//*[@id="page-content"]/div[2]/div[1]/div/h2/text()')
            print("提交失败")
            raise RuntimeError("Submit Failed")
        except NoSuchElementException:
            print("提交成功")


if __name__ == '__main__':
    Report("xxx", "xxx").run()
