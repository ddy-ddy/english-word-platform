# -*- coding: utf-8 -*-
# @Time    : 2023/3/5 10:33
# @Author  : ddy
# @FileName: main.py
# @github  : https://github.com/ddy-ddy

from py2neo import Graph
import json

graph = Graph("bolt://localhost:7687", auth=("neo4j", "aAabcdefg123"))
query = "MATCH (Lemma)-[]->(Synset) WHERE Lemma.name = 'implicit' RETURN *"
result = graph.run(query)
json_result = json.dumps(result.data(), ensure_ascii=False)

with open('result.json', 'w') as f:
    f.write(json_result)

print(json_result)
