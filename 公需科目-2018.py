from selenium import webdriver
import time
from bs4 import BeautifulSoup
from PIL import Image, ImageEnhance
from aip import AipOcr
from os import path
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

global url


# 通过给定的locator定位到相应的标签
def find_element(locator, driver, timeout=10):
    element = WebDriverWait(driver, timeout, 1).until(lambda x: x.find_element(*locator))
    return element


def reaadimg(path):
    img = Image.open(path)
    w, h = img.size
    for x in range(w):
        for y in range(h):
            r, g, b = img.getpixel((x, y))
            if 190 <= r <= 255 and 170 <= g <= 255 and 0 <= b <= 140:
                img.putpixel((x, y), (0, 0, 0))
            if 0 <= r <= 90 and 210 <= g <= 255 and 0 <= b <= 90:
                img.putpixel((x, y), (0, 0, 0))
    img = img.convert('L').point([0] * 150 + [1] * (256 - 150), '1')
    return img


# username = "18523117701"  # 请替换成你的用户名
# password = "000000"  # 请替换成你的密码

class autostudy():
    def __init__(self):
        super(autostudy, self).__init__()
        self.username = "18523117701"
        self.password = "lyl61285946"
        self.q = 0
        self.p = 0
        self.openChrome()

    def openChrome(self):
        chromeOpitons = Options()
        prefs = {
            "profile.managed_default_content_settings.images": 1,
            "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
            "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,
            "PluginsAllowedForUrls": ["https://cqrl.21tb.com", "http://cqrl.21tb.com"]
        }
        chromeOpitons.add_experimental_option('prefs', prefs)

        self.driver = webdriver.Chrome(chrome_options=chromeOpitons)  # 创建实例
        self.driver.implicitly_wait(5)
        # self.driver.maximize_window()
        self.driver.get('https://uat1.cqrspx.cn/portal/login?noticeStyle=2')
        # heartrate.trace(browser=True)
        self.login()

    def login(self):
        self.username_client()
        time.sleep(1)
        self.passwd_client()
        time.sleep(1)
        self.securityCode_and_clientButton()

    def selentpage(self):
        time.sleep(1)
        windows = self.driver.find_elements_by_class_name('tbc-shortcut-icon')
        time.sleep(1)
        windows[0].click()
        time.sleep(5)
        self.driver.switch_to_frame('tbc_window_iframe_15')
        time.sleep(3)
        classID = self.check_element('重庆市2018年专技人员继续教育公需科目培训')
        # print(classID)
        self.driver.find_element_by_xpath(".//a[contains(text(),'重庆市2018年专技人员继续教育公需科目培训')]").click()
        time.sleep(5)
        self.findClassID()

    def get_studyProject(self):
        # print("get_project````")
        time.sleep(2)
        windows = self.driver.window_handles
        print(len(windows))
        self.driver.switch_to_window(windows[1])
        print(f"当前网页标题: {self.driver.title}")
        self.driver.find_element_by_xpath('//*[@id="searchBar"]/section/div/div[2]/section/div[2]/section[1]/div/section[2]/div/div[1]').click()
        time.sleep(3)
        class_title = self.driver.find_element_by_xpath('//*[@id="searchBar"]/section/div/div[2]/div/div[1]')
        class_percent = self.driver.find_element_by_xpath('//*[@id="searchBar"]/section/div/div[2]/div/div[5]/span')
        print(f"准备学习课程：{class_title.text}")
        print(f"课程完成度：{class_percent.text}")
        self.start_study()




    def findClassID(self):
        self.lessonID = self.driver.find_elements_by_xpath(
            ".//*[@class='track-dialog-inner-list track-dialog-course-list']")
        time.sleep(1)
        # print('self.lessonID len:',len(self.lessonID))
        self.get_lessonID()

    def get_lessonID(self):
        pass

        '''
        bxlessons = self.lessonID[0]
        xxlessons = self.lessonID[1]
        bxlessonID = bxlessons.get_attribute('innerHTML')
        bxlessonID = BeautifulSoup(bxlessonID, 'lxml')
        xxlessonID = xxlessons.get_attribute('innerHTML')
        xxlessonID = BeautifulSoup(xxlessonID, 'lxml')
        bx = bxlessonID.findAll('li')
        xx = xxlessonID.findAll('li')
        titles = bxlessonID.select('li a')
        titlesxx = xxlessonID.select('li a')

        self.driver.switch_to.default_content()
        self.bxClass = []
        # self.bxClass.append('bd291bd585fe4dacb4d08fa3d56cad72')   #ceshiyong ,yao shancu
        self.xxClass = []
        bxed_title = []
        xxed_title = []
        bx_title = []
        xx_title = []
        k = 0
        for i in bx:
            pan = 'track-course-right' in str(i)
            title = titles[k].get('title')
            if pan:
                bxed_title.append(title)
                pass
            else:
                u = i.a.attrs['id']
                bx_title.append(title)
                # print(u)
                # print('\n')
                self.bxClass.append(u)
            k += 1
        for i in range(len(bxed_title)):
            print('[必修：已完成]', bxed_title[i])
        for i in range(len(bx_title)):
            print('[必修：未完成]', bx_title[i])

        m = 0
        for j in xx:
            pan = 'track-course-right' in str(j)
            title = titlesxx[m].get('title')
            if pan:
                xxed_title.append(title)
                pass
            else:
                u = j.a.attrs['id']
                xx_title.append(title)
                self.xxClass.append(u)
            m += 1
        for i in range(len(xxed_title)):
            print('[选修：已完成]', xxed_title[i])
        for i in range(len(xx_title)):
            print('[选修：未完成]', xx_title[i])

        # print('self.bxClass:\n',self.bxClass)
        # print('\n')
        self.clickClassbx()
        '''

    def clickClassbx(self):
        handles = self.driver.window_handles
        time.sleep(4)
        i = self.xxClass[self.q]
        if self.q >= len(self.xxClass):
            self.endbx()
        else:
            try:
                self.driver.switch_to_window(handles[0])
                self.driver.switch_to_frame('tbc_window_iframe_15')
                self.driver.find_element_by_id(i).click()
                print('开始学习课程；ID %s' % i)
            except:
                # self.driver.find_element_by_id(i).click()
                print('未能进入课程；ID %s' % i)
            handles = self.driver.window_handles
            self.driver.switch_to_window(handles[1])
            print('切换到window1')
            self.checkPages()

    def clickClassxx(self):
        handles = self.driver.window_handles
        time.sleep(4)
        i = self.xxClass[self.p]
        if self.p >= len(self.bxClass):
            self.endbx()
        else:
            try:
                self.driver.switch_to_window(handles[0])
                self.driver.switch_to_frame('tbc_window_iframe_15')
                self.driver.find_element_by_id(i).click()
                print('clickClass: try点击了一次')
            except:
                print('clickClass: except运行了一次')
            handles = self.driver.window_handles
            self.driver.switch_to_window(handles[1])
            print('切换到window1')
            self.checkPages()

        # for i in self.bxClass:
        #     try:
        #         time.sleep(4)
        #         self.driver.switch_to_window(handles[0])
        #         self.driver.switch_to_frame('tbc_window_iframe_15')
        #         self.driver.find_element_by_id(i).click()
        #         self.driver.switch_to_default_content()
        #         print('clickClass: try点击了一次')
        #     except:
        #         print('clickClass: except运行了一次')
        #     time.sleep(8)
        #     handles = self.driver.window_handles
        #     self.driver.switch_to_window(handles[1])
        #     print('切换到window1')
        #     self.checkPages()

    def endbx(self):
        print('必修学习完成')
        time.sleep(5)
        self.clickClassxx()
        time.sleep(10000)

    def checkPages(self):
        time.sleep(3)
        handles = self.driver.window_handles
        self.driver.switch_to_window(handles[1])
        check = self.check_element('cl-catalog-item-sub')
        if check is True:
            print('检查正确，调用学习模块')
            self.start_study()
        else:
            print('检查错误')

    """
    def start_studybx(self):
        j=0
        # print('开始进入学习')
        while True:
            page_source = self.driver.page_source
            if 'cl-catalog-link-done' in page_source :
                print('本课程学习完成，即将跳转')
                self.q += 1
                self.clickClassbx()
                break
            elif j > 60:
                self.driver.refresh()
                time.sleep(2)
                print('刷新1次，继续播放')
                # print('时间太长退出')
                try:
                    self.driver.switch_to_frame('iframe_aliplayer')
                    self.driver.find_element_by_class_name('prism-big-play-btn.pause').click()
                    self.driver.switch_to_default_content()
                    print('点击继续播放')
                except:
                    print('未找到元素？')
                    self.clickClassbx()
            else:
                print('本课程未学完，循环查找弹窗并自动刷新')
                for i in range(10):
                    time.sleep(6)
                    page_source = self.driver.page_source
                    if '请完成下方的题目' in page_source:
                        self.driver.refresh()
                        time.sleep(2)
                        print('刷新1次，继续播放')
                        try:
                            self.driver.switch_to_frame('iframe_aliplayer')
                            self.driver.find_element_by_class_name('prism-big-play-btn.pause').click()
                            self.driver.switch_to_default_content()
                            print('点击继续播放')
                        except:
                            print('未找到元素？')
                            self.clickClassbx()
                    else:
                        pass
                j = j + 1
                print(j)
        print('while语句结束。。。')
        time.sleep(100000)
    """
    # def bx_class(self):
    #

    def start_study(self):
        # j = 0
        bx_tab = self.driver.find_element_by_xpath('//*[@id="tab-MUST"]')
        xx_tab = self.driver.find_element_by_xpath('//*[@id="tab-SELECTIVE"]')
        bx_page = self.driver.find_elements_by_xpath('//*[@id="pane-MUST"]/div/div/div[9]/ul/li')
        xx_page = self.driver.find_elements_by_xpath('//*[@id="pane-SELECTIVE"]/div/div/div[9]/ul/li')
        # self.bx_class(elem=bx_tab)
        # 先进入必修循环，遍历page数，
        for i in range(bx_page.count()):
            self.bx_class(elem=bx_tab)
            # 刷新页面
            self.driver.refresh()
            time.sleep(3)
            bx_page[i].click()
            time.sleep(3)
        # 进入选修循环，
        for i in range(xx_page.count()):
            pass


    def bx_class(self, elem):
        print("准备学习--必修课")
        elem.click()
        time.sleep(3)
        bx_lessons = self.driver.find_elements_by_xpath('//*[@id="pane-MUST"]/div/div/div/div')
        bx_lessons_lst = []
        for each in bx_lessons:
            a = each.get_attribute('innerHTML')
            b = BeautifulSoup(a, 'lxml')
            lesson_information = b.find_all('div')
            title = lesson_information[0].text
            statue = lesson_information[1].text
            bx_lessons_lst.append((title, statue))
        print("当前页内课程：")
        to_study_lst = []
        for lesson in bx_lessons_lst:
            print(lesson)
            if '已完成' not in lesson[1]:
                pass
            else:
                to_study_lst.append(lesson)
        if len(to_study_lst) > 0:
            print('本页内发现未完成课程，即将进入学习')
        for lesson in to_study_lst:
            lesson_name = lesson[0].strip()
            print(f"准备学习：{lesson_name}")
            self.driver.find_element_by_xpath(f'//*[@id="pane-MUST"]//div [@title="{lesson_name}"]').click()
            time.sleep(3)
            self.studing_cycle(name=lesson_name)
            time.sleep(2)


    def studing_cycle(self, name):
        window = self.driver.window_handles
        self.driver.switch_to_window(window[2])
        try:
            self.driver.switch_to_frame('iframe_aliplayer')
            self.driver.find_element_by_class_name('prism-big-play-btn').click()
            time.sleep(1)
        except:
            print("点击错误")
        total_time = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div/div/div[6]/div[4]/span[3]').get_attribute('innerHTML')
        print(f"本节课程预计耗时：{total_time}")
        # 对计数时间作2分钟的冗余
        total_count = int(total_time.split(':')[0]) * 6 + 6*2
        # 切换到默认框架
        self.driver.switch_to_default_content()
        time.sleep(1)
        j = 0
        while True:
            page_source = self.driver.page_source
            if '恭喜您已经完成课程' in page_source:
                print('本课程学习完成，即将跳转')
                self.q += 1
                # TODO
                # 这里要做关闭当前页，并切换到window[1]的操作；
                # self.clickClassbx()
                print("关闭学习窗口，回到选课界面")
                self.driver.close()
                self.driver.switch_to_window(window[1])
                break
            # elif j > total_count:
            #     break

            elif j > total_count:
                self.driver.refresh()
                time.sleep(2)
                j = 0
                print('刷新1次，继续播放,重置计数器')
                # print('时间太长退出')
                try:
                    self.driver.switch_to_frame('iframe_aliplayer')
                    self.driver.find_element_by_class_name('prism-big-play-btn').click()
                    self.driver.switch_to_default_content()
                    print('点击继续播放')
                except:
                    print('未找到元素？', "关闭学习窗口，回到选课界面")
                    self.driver.close()
                    self.driver.switch_to_window(window[1])
                    break
            else:
                print('循环查找弹窗第%d次并自动刷新' % (j+1))
                for i in range(10):
                    time.sleep(1)
                    self.driver.switch_to_frame('iframe_aliplayer')
                    page_source = self.driver.page_source
                    self.driver.switch_to_default_content()
                    if 'prism-play-btn playing' in page_source:
                        page_source = self.driver.page_source
                        if '请完成下方的题目' in page_source:
                            self.driver.refresh()
                            time.sleep(2)
                            print('遇到弹窗，刷新1次，继续播放')
                            try:
                                self.driver.switch_to_frame('iframe_aliplayer')
                                # 这里是否为pause还不知道，需要测试；
                                self.driver.find_element_by_class_name('prism-big-play-btn.pause').click()
                                self.driver.switch_to_default_content()
                                print('点击继续播放')
                            except:
                                # self.clickClassbx()
                                print('未找到元素？', "关闭学习窗口，回到选课界面")
                                self.driver.close()
                                self.driver.switch_to_window(window[1])
                                break
                        else:
                            pass
                    else:
                        print('未找到元素？', "关闭学习窗口，回到选课界面")
                        self.driver.close()
                        self.driver.switch_to_window(window[1])
                        break
                j = j + 1


        #
        # while True:
        #     page_source = self.driver.page_source
        #     if '恭喜您已经完成课程' in page_source:
        #         print('本课程学习完成，即将跳转')
        #         self.q += 1
        #         self.clickClassbx()
        #         break
        #     elif j > 60:
        #         self.driver.refresh()
        #         time.sleep(2)
        #         print('刷新1次，继续播放')
        #         # print('时间太长退出')
        #         try:
        #             self.driver.switch_to_frame('iframe_aliplayer')
        #             self.driver.find_element_by_class_name('prism-big-play-btn.pause').click()
        #             self.driver.switch_to_default_content()
        #             print('点击继续播放')
        #         except:
        #             print('未找到元素？')
        #             self.clickClassbx()
        #     else:
        #         print('本课程未学完，循环查找弹窗第%d次并自动刷新' % (j+1))
        #         for i in range(10):
        #             time.sleep(1)
        #             self.driver.switch_to_frame('iframe_aliplayer')
        #             page_source = self.driver.page_source
        #             self.driver.switch_to_default_content()
        #             if 'prism-play-btn playing' in page_source:
        #                 page_source = self.driver.page_source
        #                 if '请完成下方的题目' in page_source:
        #                     self.driver.refresh()
        #                     time.sleep(2)
        #                     print('刷新1次，继续播放')
        #                     try:
        #                         self.driver.switch_to_frame('iframe_aliplayer')
        #                         self.driver.find_element_by_class_name('prism-big-play-btn.pause').click()
        #                         self.driver.switch_to_default_content()
        #                         print('点击继续播放')
        #                     except:
        #                         print('未找到元素？')
        #                         self.clickClassbx()
        #                 else:
        #                     pass
        #             else:
        #                 print('未找到播放元素，重新点击科目')
        #                 self.clickClassbx()
        #         j = j + 1
        #         # print(j)
        # print('while语句结束，学习结束')
        # time.sleep(100000)

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

    def securityCode_and_clientButton(self):
        # securityCode = str(self.baiduOCR())
        # securityCodeID = self.driver.find_element_by_id('securityCode')
        # securityCodeID.click()
        # securityCodeID.clear()
        # securityCodeID.send_keys(securityCode)
        time.sleep(1)
        loginButtonClass = self.driver.find_element_by_xpath('//*[@id="phoneloginForm"]/div[3]/button')
        loginButtonClass.click()
        # self.securityCode_errorCheck()
        print("waitting for 3sec")
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="image-style-1-16268480439201421330264"]/div[2]/div[3]/div/div[1]/div/div/div').click()
        time.sleep(3)
        self.get_studyProject()
        # time.sleep(5555)


    # def securityCode_errorCheck(self):
    #     time.sleep(1)
    #     continueClient = self.check_element('继续登录')
    #     errorID = self.check_element('login-error')
    #     if continueClient is False:
    #         if errorID is True:
    #             self.securityCode_and_clientButton()
    #     else:
    #         print('账号已在别处登陆，强制继续登陆')
    #         continueButtopn = self.driver.find_element_by_xpath(".//*[@class='blue-btn elp-material-btn']")
    #         continueButtopn.click()
    #     self.selentpage()

    def check_element(self, element):
        source = self.driver.page_source
        if element in source:
            return True
        else:
            return False

    def get_pictures(self):
        self.driver.save_screenshot('pictures.png')  # 全屏截图
        page_snap_obj = Image.open('pictures.png')
        img = self.driver.find_element_by_xpath(".//*[@id='validateCodeImg']")  # 验证码元素位置
        time.sleep(1)
        location = img.location
        size = img.size  # 获取验证码的大小参数
        k = 1.25
        left = location['x'] * k
        top = location['y'] * k
        right = left + size['width'] * k
        bottom = top + size['height'] * k
        image_obj = page_snap_obj.crop((left, top, right, bottom))  # 按照验证码的长宽，切割验证码
        image_obj.save('./code.png')
        # image_obj.show()  # 打开切割后的完整验证码
        # self.driver.close()  # 处理完验证码后关闭浏览器
        # return image_obj

    def baiduOCR(self):
        """利用百度api识别文本，并保存提取的文字
        picfile:    图片文件名
        """
        filename = path.basename('./code.png')
        # 你的AppID，APIKey，Secret Key
        self.get_pictures()
        time.sleep(1)
        APP_ID = '22995443'  # 这是你产品服务的appid
        API_KEY = 'kzztY1j5NXT5qWhPKpgwjSc0'  # 这是你产品服务的appkey
        SECRECT_KEY = 'OcoKKRIlMZgsSf2FRbwPE0DbOaZbkZxN'  # 这是你产品服务的secretkey
        client = AipOcr(APP_ID, API_KEY, SECRECT_KEY)
        i = open('./code.png', 'rb')
        img = i.read()
        # i = open(self.picfile, 'rb')
        # img = i.read()
        # print("正在识别图片：\t" + filename)
        # basicGeneral : 通用文字识别
        # basicAccurate : 通用文字识别(高精度版)
        # general : 通用文字识别(含位置信息版)
        # accurate : 通用文字识别(含位置高精度版)
        # enhancedGeneral : 通用文字识别(含生僻字版)
        # webImage : 网络图片文字识别
        # 还有更多参数可选，具体详情可自查Api文档
        # message = client.webImage(img)  # 网络文字识别，每天 50 000 次免费

        message = client.basicAccurate(img)

        try:
            print("验证码识别成功！% s" % (message['words_result'][0]['words']))
        except:
            self.baiduOCR()

        # message = client.basicAccurate(img)   # 通用文字高精度识别，每天 800 次免费
        # 打印信息可注释掉，此处是为了调试
        # print("验证码识别成功！")
        return message['words_result'][0]['words']


if __name__ == '__main__':
    autostudy()
