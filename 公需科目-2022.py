# coding:gbk
import json

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fast_study import *

global url
from rich import print


class AutoStudy:
    def __init__(self, username='18523117701', password='lyl61285946'):
        # super(AutoStudy, self).__init__()
        self.username = username if username else '18523117701'
        self.password = password if password else 'lyl61285946'
        self.q = 0
        self.p = 0
        self.driver = None
        self.openChrome()

    def openChrome(self):
        chrome_pitons = Options()
        if not self.driver:
            self.driver = webdriver.Chrome(chrome_options=chrome_pitons)  # 创建实例
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get('https://uat1.cqrspx.cn/portal/login?noticeStyle=2')
        # heartrate.trace(browser=True)
        time.sleep(2)
        # 切换到登陆页面
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div/div[2]/div[2]/div[1]/a[1]').click()
        time.sleep(1)
        self.login()

    def test_header(self):
        headers = self.driver.execute_script("var req = new XMLHttpRequest();req.open('GET', document.location, false);req.send(null);return req.getAllResponseHeaders()")
        headers = headers.splitlines()
        print(headers)
        time.sleep(9)

    def login(self):

        self.test_header()
        self.username_client()
        time.sleep(1)
        self.passwd_client()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value='//*[@id="phoneloginForm"]/div[3]/button').click()
        # 登陆
        time.sleep(10)
        self.step_into_2022()

    def step_into_2022(self):
        element_2022 = '//*[@id="grid1"]//div[1]/div[2]/div[3]/div/div[1]/div/div/div'
        self.driver.find_element(by=By.XPATH, value=element_2022).click()
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        entry_2022 = '//*[@id="searchBar"]/section/div/div[2]/section/div[2]/section[1]/div'
        self.driver.find_element(by=By.XPATH, value=entry_2022).click()
        time.sleep(2)
        self.save_cookies()
        self.start_fast_study()

    def save_cookies(self):
        with open('cookies.txt', 'w') as f:
            # 将cookies保存为json格式
            f.write(json.dumps(self.driver.get_cookies()))
        console.print("cookies 成功保存至 cookies.txt！")

    def start_fast_study(self):
        console.rule("STUDYING PAGE 1", align='center')
        self.study_page_1()
        console.rule("SUCCESS PAGE 1", align='center')
        console.rule("STUDYING PAGE 2", align='center')
        self.study_page_2()
        console.rule("STUDYING PAGE 2", align='center')
        console.rule("SLEEPING 2 SECONDS", align='center')
        time.sleep(2)
        console.print(Panel('[blue]PROJECT FINISHED OF SCIENTIFIC 2022. \nYOU NEED CLICK EACH SESSION FOR ONCE TO CONFIRM SCORE INCREASED.[/]'))
        input("")

    def study_page_1(self):
        FastStudy().main(1)

    def study_page_2(self):
        FastStudy().main(2)

    def username_client(self):
        time.sleep(1)
        loginID = self.driver.find_element_by_id('phoneName')
        loginID.click()
        loginID.clear()
        loginID.send_keys(self.username)

    def passwd_client(self):
        passwdID = self.driver.find_element_by_id('phonepassword')
        passwdID.click()
        passwdID.clear()
        passwdID.send_keys(self.password)

    def check_element(self, element):
        source = self.driver.page_source
        if element in source:
            return True
        else:
            return False


if __name__ == '__main__':
    console.print(Panel('[yellow]INPUT YOUR PHONE NUMBER AND PRESS ENTER.[/]'))
    phone = input(":")
    console.print(Panel('[yellow]INPUT YOUR PASSWORD AND PRESS ENTER.[/]'))
    passwd = input(":")
    console.print(Panel(f'[yellow]YOUR INPUT ACCOUNT INFO\nPHONE NUMBER:{phone}\nPASSWORD:{passwd}[/]'))
    console.print("确认你的输入信息没有错误，按任意键继续..")
    input("")
    AutoStudy(phone, passwd)

    # AutoStudy()
