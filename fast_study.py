# -*- coding: utf-8 -*-

# @File    : fast_study.py
# @Date    : 2022-06-23
# @Author  : luoyu
import json
import time

import requests
from unit import *
from rich import print


class FastStudy:
    def __init__(self):
        self.cookies = get_cookies()

    def get_record_list(self, courseId: str, sourceId: str) -> list:
        json_data = {
            'courseId': courseId,
            'sourceId': sourceId,
            'providerCorpCode': 'cqrl',
        }
        response = requests.post('https://cqrl.21tb.com/tbc-rms/record/getStudyRecordList', cookies=self.cookies, json=json_data)
        return [{'recordId': i['recordId'], 'courseId': i['courseId'], 'chapterId': i['chapterId'], 'resourceId': i['resourceId'], 'timeToFinish': i['timeToFinish'], 'corpCode': i['corpCode']}
                for i in response.json()['bizResult']
                if i['confirmFinish'] != 1]

    def get_course_id_list(self, pageNo: int) -> list:
        params = {
            'pageNo': f'{pageNo}',
            'pageSize': '8',
            'courseStatus': 'ALL',
            'stageId': 'd743f8102b1740fb9b20f16b82af3147',
            'courseType': 'MUST',
            'eln_session_id': self.cookies.get('eln_session_id'),
            'corpCode': 'cqrl',
        }
        response = requests.get('https://cqrl.21tb.com/nms/html/courseStudy/getCourseDetailByProjectId.do', params=params, cookies=self.cookies)
        print([i['courseId'] for i in response.json()['rows']])
        return [i['courseId'] for i in response.json()['rows']]

    def submit_study_record(self, session: dict):
        study_url = 'https://cqrl.21tb.com/tbc-rms/record/updateCourseRecord'
        time_max = session.get('timeToFinish')
        _progress, _bar = progress_bar((time_max - 100), session['recordId'])
        _progress.start()
        for i in range(100, time_max, 20):
            data = {
                'recordId': session.get('recordId'),
                'courseId': session.get('courseId'),
                'sourceId': session.get('courseId'),
                'providerCorpCode': 'cqrl',
                'chapterId': session.get('chapterId'),
                'resourceId': session.get('resourceId'),
                'timeToFinish': session.get('timeToFinish'),
                'currentPosition': i,
                'type': 'video',
                'currentStudyTime': i,
                'pageIndex': 0,
            }
            r = requests.post(url=study_url, json=data, cookies=self.cookies)
            # print(r.text, i)
            _progress.advance(_bar, advance=20)
        _progress.stop()

    def click_class_url(self, url: str):
        try:
            requests.get(url)
        except Exception:
            print(f"{url} 的链接访问失败，请手动访问页面1次以获取学分！")

    def build_class_url(self, courseId: str):
        return f"https://cqrl.21tb.com/els/html/courseStudyItem/courseStudyItem.learn.do?courseId={courseId}&courseType=NEW_COURSE_CENTER&vb_server=http%3A%2F%2F21tb-video.21tb.com&eln_session_id={self.cookies['eln_session_id']}"

    def print_class_id(self, id_, statue):
        table = Table()
        table.add_column('[yellow]CLASS_ID')
        table.add_column('[yellow]STATUE')
        table.add_row(f'[red]{id_}', f'[yellow]{statue}')
        console.print(table)

    def main(self, page: int):
        console.print(Panel('[blue]SUBJECTS OF SCIENTIFIC 2022[/]'))
        for id_ in self.get_course_id_list(page):
            self.print_class_id(id_, "UN")
            recordList = self.get_record_list(id_, id_)
            for record in recordList:
                self.submit_study_record(record)
            self.click_class_url(self.build_class_url(id_))
            self.print_class_id(id_, "DONE")


if __name__ == '__main__':
    FastStudy().main(3)
