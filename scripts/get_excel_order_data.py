# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/12/4 下午3:28
# @Author : tangtain
# @File : get_excel_order_data.py
# @Software: PyCharm


from openpyxl import load_workbook
from config.config_path import *


def get_excel_data(excel_path, sheet_name):
    wb = load_workbook(excel_path)
    sh = wb[sheet_name]
    return sh


if __name__ == '__main__':
    print(get_excel_data(excel_data_path, 'order_many'))



