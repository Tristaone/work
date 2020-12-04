# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/12/4 下午2:34
# @Author : tangtain
# @File : order_many.py
# @Software: PyCharm


import requests
from config.config_path import *
from openpyxl import load_workbook
from scripts.get_excel_order_data import get_excel_data
import json


def order_many(token):
    method = 'post'
    url = dev_order_url
    header = {'authorization': 'Bearer' + ' ' + token}

    sh = get_excel_data(excel_data_path, 'order_many')
    for i in range(1, sh.max_row + 1):
        data = json.loads(sh.cell(i, 1).value)
        res = requests.request(method=method, url=url, data=data, headers=header)
        print(res.status_code)


token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9' \
        '.eyJpc3MiOiJodHRwOlwvXC9kZXYtYXBpLW1haW4udGVzdC5kbWwtZXhwcmVzcy5jb21cL2FwaVwvdXNlclwvc2Vzc2lvbiIsImlhdCI6MTYwNzA2Mzg0NywiZXhwIjoxNjA3NjY4NjQ3LCJuYmYiOjE2MDcwNjM4NDcsImp0aSI6Ink1OE1Ca0ZKNlNVckpjMEYiLCJzdWIiOjMwMjc0LCJwcnYiOiJhMGIxY2NmNDRlMjRjYTQ3NzJjYTgzNDYyZDE5ZjNlMGIzNmZmYWZmIn0.wbQC5S12_WioNjgUCu0wQOBPEik7KeiX4sPR10aQXtc '

order_many(token)




