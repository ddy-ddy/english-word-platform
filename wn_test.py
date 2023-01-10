# -*- coding: utf-8 -*-
# @Time    : 2023/1/10 22:00
# @Author  : ddy
# @FileName: wn_test.py
# @github  : https://github.com/ddy-ddy


import wn
en =wn.Wordnet('oewn:2021')
print(en.synsets('implicit'))