# -*- coding: utf-8 -*-
# @Time    : 2023/1/10 15:39
# @Author  : ddy
# @FileName: xml2json.py
# @github  : https://github.com/ddy-ddy

'''
1.convert the xml file to json file
2.format large json file
    python -mjson.tool data/english-wordnet-2021.json > formatted.json
'''


import xmltodict, json

if __name__ == '__main__':
    with open("data/english-wordnet-2021.xml", 'r') as rf:
        obj = xmltodict.parse(rf.read())
    print("Finished convert")
    with open("data/english-wordnet-2021.json", 'w') as wf:
        wf.write(json.dumps(obj))
    print("Finished storing the data in a json file")
