# -*- coding: utf-8 -*-
# @Time    : 2023/3/4 15:57
# @Author  : ddy
# @FileName: node_define.py
# @github  : https://github.com/ddy-ddy

'''
实体定义
'''


## 定义同义词集节点
class SynsetNode:
    '''
    同义词集概念节点
    '''

    def __init__(self, id, pos, definition, examples):
        self._label = 'Synset'
        self._id = id
        self._pos = pos
        self._definition = definition
        self._examples = examples

    def __repr__(self):
        return "SynsetNode({})".format(self._id)

    @property
    def get_id(self):
        return self._id

    @property
    def get_pos(self):
        return self._pos

    @property
    def get_definition(self):
        return self._definition

    @property
    def get_label(self):
        return self._label

    @property
    def get_examples(self):
        return self._examples

    def get_row(self):
        return [
            self.get_id,
            self.get_pos,
            self.get_definition,
            self.get_label,
            self.get_examples
        ]


## 定义词汇节点
class WordNode:
    '''
    词汇节点
    '''

    def __init__(self, id, name, pos):
        self._label = "Lemma"
        self._id = id
        self._name = name
        self._pos = pos

    def __repr__(self):
        return "WordNode({})".format(self._id)

    @staticmethod
    def get_header():
        return ['id:ID', 'name', 'pos', ':LABEL']

    def get_row(self):
        return [self._id, self._name, self._pos, self._label]

    @property
    def get_id(self):
        return self._id
