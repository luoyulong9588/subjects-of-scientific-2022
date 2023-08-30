# -*- coding: utf-8 -*-
import json

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fast_study import *

global url
from rich import print
import selenium

class AutoStudy:
    def __init__(self, username='18523117701', password='lyl61285946', _page="1"):
        # super(AutoStudy, self).__init__()
        self.username = username if username else '18523117701'
        self.password = password if password else 'lyl61285946'
        self.page = int(_page) if _page else 1
        self.q = 0
        self.p = 0
        self.driver = None
        self.openChrome()

    def openChrome(self):
        chrome_pitons = Options()
        chrome_pitons.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
        chrome_pitons.add_argument('--headless')
        if not self.driver:
            self.driver = webdriver.Chrome(options=chrome_pitons)  # 创建实例
        self.driver.implicitly_wait(5)
        # self.driver.minimize_window()
        self.driver.get('https://uat1.cqrspx.cn/portal/login?noticeStyle=2')
        # heartrate.trace(browser=True)
        time.sleep(2)
        # 切换到登陆页面
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div/div[2]/div[2]/div[1]/a[1]').click()
        time.sleep(1)
        self.login()

    def test_header(self):
        headers = self.driver.execute_script(
            "var req = new XMLHttpRequest();req.open('GET', document.location, false);req.send(null);return req.getAllResponseHeaders()")
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
        time.sleep(5)
        self.step_into_2022()
        # self.step_into_2020()

    def step_into_2022(self):
        element_2022 = '//*[@id="grid1"]//div[1]/div[2]/div[3]/div/div[1]/div/div/div'
        self.driver.find_element(by=By.XPATH, value=element_2022).click()
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        entry_2022 = '//*[@id="searchBar"]/section/div/div[2]/section/div[2]/section[1]/div'
        self.driver.find_element(by=By.XPATH, value=entry_2022).click()
        time.sleep(2)
        self.driver.minimize_window()
        self.save_cookies()
        self.start_fast_study()

    def step_into_2023(self):
        element_2022 = '//*[@id="grid1"]//div[1]/div[2]/div[3]/div/div[1]/div/div/div'
        self.driver.find_element(by=By.XPATH, value=element_2022).click()
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        entry_2022 = '//*[@id="searchBar"]/section/div/div[2]/section/div[2]/section[1]/div'
        self.driver.find_element(by=By.XPATH, value=entry_2022).click()
        time.sleep(2)
        self.driver.minimize_window()
        self.save_cookies()
        self.start_fast_study()

    def step_into_2020(self):
        element_2020 = '//*[@id="image-style-1-16604195151991890836740"]/div[2]/div[3]/div/div[3]/h3'
        self.driver.find_element(by=By.XPATH, value=element_2020).click()
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        entry_2020 = '//*[@id="searchBar"]/section/div/div[2]/section/div[2]/section[3]/section/div[1]/div/button[1]'
        self.driver.find_element(by=By.XPATH, value=entry_2020).click()
        time.sleep(2)
        self.driver.minimize_window()
        self.save_cookies()
        self.start_fast_study()

    def save_cookies(self):
        with open(f'{self.username}.txt', 'w') as f:
            # 将cookies保存为json格式
            f.write(json.dumps(self.driver.get_cookies()))
        console.print(f"cookies 成功保存至 {self.username}.txt！")

    def start_fast_study(self):
        i = self.page
        app = FastStudy(self.username)
        while True:
            console.rule(f"STUDYING PAGE {i} PROGRESS", align='center')
            app.start(i)
            select = input(f"第 {i} 页已学习完成,要继续下一页的学习吗?[Y/n]")
            if select != "Y":
                break
            i += 1

        console.rule(f"STUDY PROCESS PAGE 1 - {i} FINISHED!", align='center')
        console.rule("SLEEPING 2 SECONDS", align='center')
        time.sleep(2)
        console.print(Panel('[blue]任务完成! \n你现在只需要手动点开每一个课程即可获取相应学分。[/]'))
        input("")

    def username_client(self):
        time.sleep(1)
        loginID = self.driver.find_element(by=By.ID, value='phoneName')
        loginID.click()
        loginID.clear()
        loginID.send_keys(self.username)

    def passwd_client(self):
        passwdID = self.driver.find_element(by=By.ID, value='phonepassword')
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
    # pass_list = ["15922538007", "19923399226", "13110209945", "13629707889", "13629783219", "18523117701"]
    console.print(Panel('[yellow]INPUT YOUR PHONE NUMBER AND PRESS ENTER.[/]'))
    phone = input("PHONE:")
    console.print(Panel('[yellow]INPUT YOUR PASSWORD AND PRESS ENTER.[/]'))
    passwd = input("PASSWD:")
    console.print(Panel('[yellow]INPUT THE START PAGE(1 - N).[/]'))
    page = input("PAGE_NUMBER:")
    console.print(Panel(f'[yellow]YOUR INPUT ACCOUNT INFO\nPHONE NUMBER:{phone}\nPASSWORD:{passwd}[/]'))
    console.print("CONFIRE YOUR ACCOUNT INFO, PROCESS WILL START IN 10 SECOND. PRESS [CTRL + C] TO END PROCESS.")
    for step in track(range(100), description="Waitting..."):
        time.sleep(0.1)
        # do_step(step)
    console.print("稍作等待,程序需要一些时间来获取cookies")
    # if phone not in pass_list:
    #     passwd = passwd + "    "
    AutoStudy(phone, passwd, page)

    # AutoStudy()
