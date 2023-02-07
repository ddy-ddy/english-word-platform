# -*- coding: utf-8 -*-
# @Time    : 2023/1/10 22:00
# @Author  : ddy
# @FileName: preProcess.py
# @github  : https://github.com/ddy-ddy

import wn
from operateFile import *
from tqdm import tqdm

en = wn.Wordnet('oewn:2021')


# # 查询的词
# query_word = 'implicit'
# # 获得查询词的信息
# word_information = get_word_information(query_word)
# # 将信息保存在json文件中
# dump_dict_to_json_file("data/word_information.json", word_information)

def get_information_by_word(word):
    word_information = []
    for sense in en.senses(word):
        information = {}
        information["id"] = sense.word().id
        information["lemma"] = sense.word().lemma()
        information["pos"] = sense.word().pos
        information["translate"] = sense.translate(lang="cmn-Hans")[0].word().lemma().replace("+", "")
        information["definition"] = sense.synset().definition()
        information["examples"] = sense.synset().examples()
        information["relations"] = []
        for relation, sense_ in sense.relations().items():
            for se in sense_:
                information["relations"].append(({"source_word": sense.word().lemma(),
                                                  "target_word": se.word().lemma(),
                                                  "relation_type": relation,
                                                  "target_id": se.word().id}))
        word_information.append(information)
    return word_information


if __name__ == '__main__':
    all_info = []

    for word in tqdm(wn.words()):
        for sense in word.senses():
            information = {}
            information["id"] = sense.word().id
            information["lemma"] = sense.word().lemma()
            information["pos"] = sense.word().pos
            if sense.translate(lang="cmn-Hans"):
                information["translate"] = sense.translate(lang="cmn-Hans")[0].word().lemma().replace("+", "")
            else:
                information["translate"] = ""
            information["definition"] = sense.synset().definition()
            information["examples"] = sense.synset().examples()
            information["relations"] = []
            for relation, sense_ in sense.relations().items():
                for se in sense_:
                    information["relations"].append(({"source_word": sense.word().lemma(),
                                                      "target_word": se.word().lemma(),
                                                      "relation_type": relation,
                                                      "target_id": se.word().id}))
            all_info.append(information)

    dump_dict_to_json_file("data/word_information.json", all_info)
