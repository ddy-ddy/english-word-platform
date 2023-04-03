# -*- coding: utf-8 -*-
# @Time    : 2023/3/5 10:33
# @Author  : ddy
# @FileName: main.py
# @github  : https://github.com/ddy-ddy

from py2neo import Graph


class Word_kg():
    search_word, data, all_node_id = "", {}, []

    def __init__(self):
        self.graph = Graph("bolt://localhost:7687", auth=("neo4j", "aAabcdefg123"))

    def construct_node_data(self, synset=None, lemma=None, status="", relation=""):
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

    def construct_full_name_data(self, synset_id):
        '''
        构建完整的Synset的name
        :param synset_id: Synset的id
        :return:
        '''
        query = "MATCH p=(a:Lemma)-[b:InSynset]->(c:Synset{id:$synset_id}) RETURN a,b,c"
        data = self.graph.run(query, synset_id=synset_id).data()
        full_name = ""
        for item in data:
            synset, lemma = item["c"], item["a"]
            full_name = full_name + lemma["name"] + ", "
        full_name = full_name[:-2]
        return full_name

    def is_repeat_node(self, temp_id):
        '''
        判断节点是否重复
        :param temp_id: 节点的id
        :return:
        '''
        if temp_id in self.all_node_id:
            temp_id = str(temp_id) + str(len(self.all_node_id))
            self.all_node_id.append(temp_id)
        else:
            self.all_node_id.append(temp_id)
        return temp_id

    def get_first_level_data(self, synset, lemma):
        # 获取一级节点信息
        id, info = self.construct_node_data(synset=synset, lemma=lemma, status="R", relation="InSynset")
        info["collapsed"] = "true"
        self.all_node_id.append(id)
        Synset_name = info["name"]  # Synset的name是由该Synset的所有Lemma的name组成

        # 获取一级节点名字
        query = "MATCH p=(a:Lemma{name:$search_word})-[b:InSynset]->(c:Synset{id:$id})<-[d:InSynset]-(e:Lemma)  RETURN c,e"
        first_data = self.graph.run(query, search_word=self.search_word, id=id).data()
        if first_data:
            for _ in first_data:
                temp_synset, temp_lemma = _["c"], _["e"]
                temp_id, temp_info = self.construct_node_data(synset=temp_synset, lemma=temp_lemma, status="B",
                                                              relation="InSynset")
                self.all_node_id.append(temp_id)
                Synset_name = Synset_name + ", " + (temp_info["name"])

        info["name"] = Synset_name  # 更新Synset的name
        return id, info

    def get_second_level_data(self, id, info):
        # 获取二级节点(正向指向)
        query = "MATCH p=(Synset{id:$id})-[r*1]->(b:Synset) RETURN r,b"
        second_data = self.graph.run(query, id=id).data()
        if second_data:
            for _ in second_data:
                relation, temp_synset = _["r"], _["b"]
                temp_id, temp_info = self.construct_node_data(synset=temp_synset, status="G",
                                                              relation=type(_["r"][0]).__name__)
                temp_info["name"] = self.construct_full_name_data(temp_id)
                # 设置为折叠状态
                temp_info["collapsed"] = "true"

                # 获取三级节点名字(正向&反向)
                temp_info = self.get_third_level_data(temp_id, temp_info)
                info["children"].append(temp_info)

        # 获取二级节点(反向指向)
        query = "MATCH p=(b:Synset)-[r*1]->(Synset{id:$id}) RETURN r,b"
        second_data = self.graph.run(query, id=id).data()
        if second_data:
            for _ in second_data:
                relation, temp_synset = _["r"], _["b"]
                temp_id, temp_info = self.construct_node_data(synset=temp_synset, status="G",
                                                              relation=type(_["r"][0]).__name__)
                temp_info["name"] = self.construct_full_name_data(temp_id)
                # 设置为折叠状态
                temp_info["collapsed"] = "true"

                # 获取三级节点名字(正向&反向)
                temp_info = self.get_third_level_data(temp_id, temp_info)
                info["children"].append(temp_info)

        self.data["children"].append(info)

    def get_third_level_data(self, temp_id, temp_info):
        '''
        获取三级节点数据
        :return:
        '''
        # 获取三级节点名字(正向指向)
        query = "MATCH p=(Synset{id:$temp_id})-[r*1]->(b:Synset) RETURN r,b"
        third_data, third_info = self.graph.run(query, temp_id=temp_id).data(), []
        if third_data:
            for _ in third_data:
                third_relation, third_synset = _["r"], _["b"]
                third_id, third_temp_info = self.construct_node_data(synset=third_synset, status="G",
                                                                     relation=type(_["r"][0]).__name__)
                third_temp_info["name"] = self.construct_full_name_data(third_id)
                # 保证id不重复
                third_temp_info["id"] = self.is_repeat_node(third_id)
                third_info.append(third_temp_info)
        temp_info["children"].extend(third_info)

        # 获取三级节点名字(反向指向)
        query = "MATCH p=(b:Synset)-[r*1]->(Synset{id:$temp_id}) RETURN r,b"
        third_data, third_info = self.graph.run(query, temp_id=temp_id).data(), []
        if third_data:
            for _ in third_data:
                third_relation, third_synset = _["r"], _["b"]
                third_id, third_temp_info = self.construct_node_data(synset=third_synset, status="G",
                                                                     relation=type(_["r"][0]).__name__)
                third_temp_info["name"] = self.construct_full_name_data(third_id)
                # 保证id不重复
                third_temp_info["id"] = self.is_repeat_node(third_id)
                third_info.append(third_temp_info)
        temp_info["children"].extend(third_info)
        # 保证id不重复
        temp_info["id"] = self.is_repeat_node(temp_id)

        return temp_info

    def search(self, search_word):
        self.search_word = search_word
        self.data = {"id": "0",
                     "nodeType": "query",
                     "name": search_word,
                     "status": "B",
                     "relation": "",
                     "pos": "",
                     "examples": "",
                     "definition": "",
                     "children": []
                     }
        self.all_node_id = []

        query = "MATCH p=(a:Lemma{name:$name})-[b:InSynset]->(c:Synset) RETURN a,b,c"
        json_data = self.graph.run(query, name=self.search_word).data()

        for item in json_data:
            synset, lemma = item["c"], item["a"]

            # 获取一级节点信息
            id, info = self.get_first_level_data(synset, lemma)

            # 获取二级节点(正向&反向)
            self.get_second_level_data(id, info)

if __name__ == '__main__':
    use = Word_kg()
    use.search(search_word="beauty")
    print(use.data)
