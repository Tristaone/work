# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/12/5 上午9:39
# @Author : tangtain
# @File : get_token.py
# @Software: PyCharm


from config.config_path import *
import requests


# 获取指定用户token
def get_header_token():
    login_data = {"phone": user_phone, "code": code}
    res = requests.request(method='post',
                           url=dev_login_url,
                           data=login_data
                           )
    token = res.json()['data']['api_token']
    header_token = {'authorization': 'Bearer ' + token}
    return header_token

