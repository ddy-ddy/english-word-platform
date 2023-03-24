# -*- coding: utf-8 -*-
# @Time    : 2023/3/5 10:33
# @Author  : ddy
# @FileName: main.py
# @github  : https://github.com/ddy-ddy

from py2neo import Graph
import json

graph = Graph("bolt://localhost:7687", auth=("neo4j", "aAabcdefg123"))


def get_query_data(query):
    '''
    获取查询数据
    :param query: Cypher查询语句
    :return: json格式数据
    '''
    data = graph.run(query, node_id=1).data()
    return data


def construct_data(synset=None, lemma=None, status="", relation=""):
    '''
    构建节点数据
    :param synset:
    :param lemma:
    :param status:
    :param relation:
    :return:
    '''
    id = synset['id'] if synset else ""
    name = lemma["name"] if lemma else ""
    pos = synset['pos'] if synset else ""
    definition = synset["definition"] if synset else ""
    examples = synset['examples'] if synset else ""
    label = f"({pos}){definition}" if pos and definition else ""
    data = {"id": id,
            "name": name,
            "status": status,
            "relation": relation,
            "pos": pos,
            "examples": examples,
            "definition": definition,
            "label": label,
            "children": []
            }
    return id, data


def construct_full_name_data(synset_id):
    '''
    构建完整的Synset的name
    :param synset_id:
    :return:
    '''
    query = "MATCH p=(a:Lemma)-[b:InSynset]->(c:Synset{id:'" + synset_id + "'}) RETURN a,b,c"
    data = get_query_data(query)
    full_name = ""
    for item in data:
        synset, lemma = item["c"], item["a"]
        full_name = full_name + lemma["name"] + ", "
    full_name = full_name[:-2]
    return full_name


# 构建Cypher查询语句
input_query = "implicit"

# 构建初始数据
data, all_node_id = {"id": "0",
                     "nodeType": "query",
                     "name": input_query,
                     "status": "R",
                     "relation": "",
                     "pos": "",
                     "examples": "",
                     "definition": "",
                     "children": []
                     }, []

query = "MATCH p=(a:Lemma{name:'"+input_query+"'})-[b:InSynset]->(c:Synset) RETURN a,b,c"
json_data = get_query_data(query)

for item in json_data:
    synset, lemma = item["c"], item["a"]

    # 获取一级节点(正向)
    id, info = construct_data(synset=synset, lemma=lemma, status="R", relation="Has_Lemma")
    all_node_id.append(id)
    Synset_name = info["name"]  # Synset的name是由该Synset的所有Lemma的name组成

    # 获取一级节点(方向)
    query = "MATCH p=(a:Lemma{name:'" + input_query + "'})-[b:InSynset]->(c:Synset{id:'" + id + "'})<-[d:InSynset]-(e:Lemma)  RETURN c,e"
    first_data = get_query_data(query)
    if first_data:
        for _ in first_data:
            temp_synset, temp_lemma = _["c"], _["e"]
            temp_id, temp_info = construct_data(synset=temp_synset, lemma=temp_lemma, status="B", relation="Has_Lemma")
            all_node_id.append(temp_id)
            Synset_name = Synset_name + ", " + (temp_info["name"])

    info["name"] = Synset_name  # 更新Synset的name

    # 获取二级节点(正向指向)
    query = "MATCH p=(Synset{id:'" + id + "'})-[r]->(b:Synset) RETURN r,b"
    second_data = get_query_data(query)
    if second_data:
        for _ in second_data:
            relation, temp_synset = _["r"], _["b"]
            temp_id, temp_info = construct_data(synset=temp_synset, status="G",
                                                relation=type(_["r"]).__name__)
            temp_info["name"] = construct_full_name_data(temp_id)
            if temp_id in all_node_id:
                continue
            else:
                all_node_id.append(temp_id)

            # 获取三级节点(正向指向)
            query = "MATCH p=(Synset{id:'" + temp_id + "'})-[r]->(b:Synset) RETURN r,b"
            third_data, third_info = get_query_data(query), []
            if third_data:
                for _ in third_data:
                    third_relation, third_synset = _["r"], _["b"]
                    third_id, third_temp_info = construct_data(synset=third_synset, status="G",
                                                               relation=type(_["r"]).__name__)
                    if third_id in all_node_id:
                        continue
                    else:
                        all_node_id.append(third_id)
                    third_temp_info["name"] = construct_full_name_data(third_id)
                    third_info.append(third_temp_info)
            temp_info["children"] = third_info

            # 获取三级节点(反向指向)
            query = "MATCH p=(b:Synset)-[r]->(Synset{id:'" + temp_id + "'}) RETURN r,b"
            third_data, third_info = get_query_data(query), []
            if third_data:
                for _ in third_data:
                    third_relation, third_synset = _["r"], _["b"]
                    third_id, third_temp_info = construct_data(synset=third_synset, status="G",
                                                               relation=type(_["r"]).__name__)
                    if third_id in all_node_id:
                        continue
                    else:
                        all_node_id.append(third_id)
                    third_temp_info["name"] = construct_full_name_data(third_id)
                    third_info.append(third_temp_info)
            temp_info["children"] = third_info

            info["children"].append(temp_info)

    # 获取二级节点(反向指向)
    query = "MATCH p=(b:Synset)-[r]->(Synset{id:'" + id + "'}) RETURN r,b"
    second_data = get_query_data(query)
    if second_data:
        for _ in second_data:
            relation, temp_synset = _["r"], _["b"]
            temp_id, temp_info = construct_data(synset=temp_synset, status="G",
                                                relation=type(_["r"]).__name__)
            temp_info["name"] = construct_full_name_data(temp_id)
            if temp_id in all_node_id:
                continue
            else:
                all_node_id.append(temp_id)

            # 获取三级节点(正向指向)
            query = "MATCH p=(Synset{id:'" + temp_id + "'})-[r]->(b:Synset) RETURN r,b"
            third_data, third_info = get_query_data(query), []
            if third_data:
                for _ in third_data:
                    third_relation, third_synset = _["r"], _["b"]
                    third_id, third_temp_info = construct_data(synset=third_synset, status="G",
                                                               relation=type(_["r"]).__name__)
                    if third_id in all_node_id:
                        continue
                    else:
                        all_node_id.append(third_id)
                    third_temp_info["name"] = construct_full_name_data(third_id)
                    third_info.append(third_temp_info)
            temp_info["children"] = third_info

            # 获取三级节点(反向指向)
            query = "MATCH p=(b:Synset)-[r]->(Synset{id:'" + temp_id + "'}) RETURN r,b"
            third_data, third_info = get_query_data(query), []
            if third_data:
                for _ in third_data:
                    third_relation, third_synset = _["r"], _["b"]
                    third_id, third_temp_info = construct_data(synset=third_synset, status="G",
                                                               relation=type(_["r"]).__name__)
                    if third_id in all_node_id:
                        continue
                    else:
                        all_node_id.append(third_id)
                    third_temp_info["name"] = construct_full_name_data(third_id)
                    third_info.append(third_temp_info)
            temp_info["children"] = third_info

            info["children"].append(temp_info)

    data["children"].append(info)

print(data)
