# -*- coding: utf-8 -*-

# @File    : fast_study.py
# @Date    : 2022-06-23
# @Author  : luoyu
import json
import time

import requests
from unit import *


# from rich import print


class FastStudy:

    def __init__(self, cookie_file_name):
        self.cookies = get_cookies(cookie_file_name)
        self.complete_list = []

    def study_cycle(self, courseId):
        """
        从课程(传入的courseId)获取每一个课程的章节(chapter)以及每一个章节的小节(session/Chapter)

        :param courseId:
        :return:
        """
        json_data = {
            'courseId': courseId,
            'providerCorpCode': 'cqrl',
        }
        response = requests.post('https://cqrl.21tb.com/tbc-rms/course/showCourseChapter', cookies=self.cookies, json=json_data).json()
        idList = response['bizResult']
        # print("本课程含有", len(idList), "篇章")
        for index, item in enumerate(idList):
            console.rule(f"学习第{index + 1}篇章课程:{item['chapterName']},[{index + 1}/{len(idList)}]篇章")
            console.print(f"-> 本篇目共有{len(item['resourceDTOS'])}个小节")
            for session in enumerate(item['resourceDTOS']):
                # console.print(f"准备学习: {session[1]['fileName']}")
                sessionInfo = {
                    "timeMax": session[1]['minStudyTime'],
                    "resourceId": session[1]['resourceId'],
                    "recordId": None,
                    "courseId": courseId,
                    "sourceId": courseId,
                    "chapterId": item['chapterId'],
                    "name": session[1]['fileName']
                }
                self.submit_study_record(sessionInfo)

    def submit_study_record(self, sessionInfo: dict):
        """
        提交学习记录到服务器

        :param sessionInfo: 视频文件信息
        :return:
        """
        study_url = 'https://cqrl.21tb.com/tbc-rms/record/updateCourseRecord'
        _progress, _bar = progress_bar((sessionInfo.get("timeMax") - 100), sessionInfo.get('name')[:7])
        _progress.start()
        debug_check_time = 0
        for i in range(100, sessionInfo.get("timeMax"), 20):
            data = {
                'recordId': sessionInfo.get("recordId"),
                'courseId': sessionInfo.get("courseId"),
                'sourceId': sessionInfo.get("sourceId"),
                'providerCorpCode': 'cqrl',
                'chapterId': sessionInfo.get("chapterId"),
                'resourceId': sessionInfo.get("resourceId"),
                'timeToFinish': sessionInfo.get("timeMax"),
                'currentPosition': i,
                'type': 'video',
                'currentStudyTime': i,
                'pageIndex': 0,
            }
            r = requests.post(url=study_url, json=data, cookies=self.cookies)
            if "学霸君" in r.text and debug_check_time < 10:
                i = 100
                debug_check_time += 1
                print("遇到了'学霸君',尝试跳过...")
            else:
                _progress.advance(_bar, advance=20)
        _progress.stop()
        self.complete_list.append(sessionInfo.get('name'))

    def get_course_id_list(self, pageNo: int) -> list:
        """
        从API接口:https://cqrl.21tb.com/nms/html/courseStudy/getCourseDetailByProjectId.do
        获取当前页面每一节课程的courseId，返回一个列表

        :param pageNo: 第几页
        :return:
        """
        params = {
            'pageNo': f'{pageNo}',
            'pageSize': '8',
            'courseStatus': 'ALL',
            # 'stageId': 'd743f8102b1740fb9b20f16b82af3147', this is 2022 id;
            'stageId':'9bc8779c1922455f847c13cb77c2d81c',
            'courseType': 'MUST',
            'eln_session_id': self.cookies.get('eln_session_id'),
            'corpCode': 'cqrl',
        }
        response = requests.get('https://cqrl.21tb.com/nms/html/courseStudy/getCourseDetailByProjectId.do', params=params, cookies=self.cookies)
        return [i['courseId'] for i in response.json()['rows']]

    def start(self, pageNumber: int = 2):
        """
        需要学习多少页的课程，默认前2页
        :return:
        """
        for _ in self.get_course_id_list(pageNumber):
            self.study_cycle(_)
            # self.emulate_open_study_page(_)  目前无效
        self.print_success()

    def emulate_open_study_page(self, course_id):

        def show_course_setting_config_api():
            url = 'https://cqrl.21tb.com/tbc-rms/course/showCourseSettingConfig'
            return requests.post(url=url, cookies=self.cookies, json={'courseId': course_id, })

        def sync_study_record_api():
            url = 'https://cqrl.21tb.com/tbc-rms/record/syncStudyRecord'
            return requests.post(url, cookies=self.cookies, json={'courseId': course_id, 'sourceId': course_id, 'providerCorpCode': 'cqrl', })

        def show_course_chapter_api():
            url = 'https://cqrl.21tb.com/tbc-rms/course/showCourseChapter'
            return requests.post(url=url, cookies=self.cookies, json={'courseId': course_id, 'providerCorpCode': 'cqrl', })

        def get_study_rate_api():
            url = 'https://cqrl.21tb.com/tbc-rms/record/getStudyRate'
            return requests.post(url=url, cookies=self.cookies, json={'courseId': course_id, 'sourceId': course_id, 'providerCorpCode': 'cqrl', })

        def get_study_record_list_api():
            url = 'https://cqrl.21tb.com/tbc-rms/record/getStudyRecordList'
            return requests.post(url=url, cookies=self.cookies, json={
                'courseId': course_id,
                'sourceId': course_id,
                'providerCorpCode': 'cqrl',
            })

        console.print(show_course_setting_config_api())
        console.print(sync_study_record_api())
        console.print(show_course_chapter_api())
        console.print(get_study_rate_api())
        console.print(get_study_record_list_api())

    def print_class_id(self, id_, statue):
        table = Table()
        table.add_column('[yellow]CLASS_ID')
        table.add_column('[yellow]STATUE')
        table.add_row(f'[red]{id_}', f'[yellow]{statue}')
        console.print(table)

    def print_success(self):
        table = Table()
        table.add_column('[yellow]小节')
        table.add_column('[yellow]状态')
        for _ in self.complete_list:
            table.add_row(f'[red]{_}', '[yellow]完成')
        console.print(table)


if __name__ == '__main__':
    FastStudy("18523117701").start(3)
