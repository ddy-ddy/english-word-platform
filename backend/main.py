# -*- coding: utf-8 -*-
# @Time    : 2023/3/5 10:33
# @Author  : ddy
# @FileName: main.py
# @github  : https://github.com/ddy-ddy

from py2neo import Graph, Node, Relationship, NodeMatcher, RelationshipMatcher


uri = "http://localhost:7474"
user = "neo4j"
password = "aAabcdefg123"
wordnet_graph = Graph(uri=uri, user=user, password=password)
