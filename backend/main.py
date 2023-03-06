# -*- coding: utf-8 -*-
# @Time    : 2023/3/5 10:33
# @Author  : ddy
# @FileName: main.py
# @github  : https://github.com/ddy-ddy

from py2neo import Graph
import json

graph = Graph("bolt://localhost:7687", auth=("neo4j", "aAabcdefg123"))

# 构建Cypher查询语句
query = "MATCH p=(Lemma{name:'implicit'})-[InSynset]->(Synset) RETURN p"

# 执行查询
json_data = graph.run(query, node_id=1).data()
print(json_data)
