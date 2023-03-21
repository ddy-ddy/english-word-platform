# -*- coding: utf-8 -*-
# @Time    : 2023/3/5 10:33
# @Author  : ddy
# @FileName: main.py
# @github  : https://github.com/ddy-ddy

from py2neo import Graph
import json

graph = Graph("bolt://localhost:7687", auth=("neo4j", "aAabcdefg123"))

# 构建Cypher查询语句
input_query = "implicit"
query = "MATCH p=(Lemma{name:'implicit'})-[InSynset]->(Synset) RETURN Synset,Lemma"

# 执行查询
json_data = graph.run(query, node_id=1).data()

data = {"id": "0",
        "nodeType": "query",
        "name": input_query,
        "status": "B",
        "relation": "",
        "pos": "",
        "examples": "",
        "definition": "",
        "children": []
        }

for item in json_data:
    synset, lemma = item['Synset'], item["Lemma"]
    id = synset['id']
    top_id = id
    name = lemma["name"]
    pos = synset['pos']
    definition = synset["definition"]
    examples = synset['examples']
    if pos and definition:
        label = f"({pos}){definition}"
    else:
        label = ""

    # 获取一级节点
    info = {"id": id,
            "name": name,
            "status": "R",
            "relation": "Has_Lemma",
            "pos": pos,
            "examples": examples,
            "definition": definition,
            "label": label,
            "children": []
            }

    # 获取二级节点(正向指向)
    second_query = "MATCH p=(Synset{id:'" + top_id + "'})-[r]->(b) RETURN r,b"
    second_query_data = graph.run(second_query, node_id=1).data()
    if second_query_data:
        for _ in second_query_data:
            synset = _["b"]
            id = synset["id"]
            name = id.split(".")[0]
            relation_name = type(_["r"]).__name__
            definition = synset["definition"]
            examples = synset["examples"]
            pos = synset["pos"]
            if pos and definition:
                label = f"({pos}){definition}"
            else:
                label = ""
            second_info = {"id": id,
                           "name": name,
                           "status": "G",
                           "relation": relation_name,
                           "pos": pos,
                           "examples": examples,
                           "definition": definition,
                           "label": label,
                           "children": []
                           }
            info["children"].append(second_info)

    # 获取二级节点(反向指向)
    second_converse_query = "MATCH p=(b)-[r:Antonym]->(Synset{id:'" + top_id + "'}) RETURN r,b"
    second_converse_query_data = graph.run(second_converse_query, node_id=1).data()
    if second_converse_query_data:
        for _ in second_converse_query_data:
            synset = _["b"]
            id = synset["id"]
            name = id.split(".")[0]
            relation_name = type(_["r"]).__name__
            definition = synset["definition"]
            examples = synset["examples"]
            pos = synset["pos"]
            if pos and definition:
                label = f"({pos}){definition}"
            else:
                label = ""
            second_converse_info = {"id": id,
                           "name": name,
                           "status": "G",
                           "relation": relation_name,
                           "pos": pos,
                           "examples": examples,
                           "definition": definition,
                           "label": label,
                           "children": []
                           }
            info["children"].append(second_converse_info)

    data["children"].append(info)

print(data)

'''
注意：二级节点的时候设置：
collapsed: true
'''
