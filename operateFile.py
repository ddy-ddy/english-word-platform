# -*- coding: utf-8 -*-
# @Time    : 2023/2/6 11:57
# @Author  : ddy
# @FileName: operateFile.py
# @github  : https://github.com/ddy-ddy

import pandas as pd
import json
import pickle


def get_col_data_from_csv(path, col_label):
    '''
    从指定csv文件中获取指定列的数据
    :param path:csv文件路径
    :param row_label:列标签
    :return:该列数据(list)
    '''
    data = pd.read_csv(path)
    return list(data[col_label])


def dump_dict_to_json_file(json_path, dict_info):
    '''
    将dict的数据导入到json文件中
    :param json_path: json文件路径
    :param dict_info: dict数据
    '''
    json_info = json.dumps(dict_info, indent=4, ensure_ascii=False)
    with open(json_path, 'w', encoding="utf-8") as f:
        f.write(json_info)


def get_data_from_json(json_path):
    '''
    从json数据中得到info标签的数据
    :param json_path:json文件
    :return: json数据
    '''
    with open(json_path, 'r', encoding="utf-8") as f:
        data = json.load(f)
    return data


def load_pickle_data(path):
    '''
    加载pickle数据
    :param path:
    :return:
    '''
    with open(path, 'rb') as file:
        return pickle.load(file)
