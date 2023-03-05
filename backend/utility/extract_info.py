# -*- coding: utf-8 -*-
# @Time    : 2023/3/4 15:29
# @Author  : ddy
# @FileName: extract_info.py
# @github  : https://github.com/ddy-ddy

'''
信息抽取
'''

import csv
import nltk
import random
import warnings
from backend.utility.node_define import SynsetNode, WordNode

warnings.simplefilter("ignore")

relationship_index = {}
relationships = []  # 关系
synsets = []  # 同义词集概念节点构造的实体
lemmas = []  # 词汇构造的实体
visited_ids = set()

all_synsets = list(nltk.corpus.wordnet.all_synsets())


# 抽取Lemma实体并建立Lemma和Synset之间的关系
def extract_lemmas(synset):
    '''
    抽取词汇实体Lemma(WordNode)
    建立Lemma(WordNode)实体和Synset(SynsetNode)实体之间InSynset关系
    '''
    for lemma in synset.lemmas():
        id = ('%s.%s' % (lemma.name().lower(), synset.pos())).lower()
        if id not in visited_ids:
            visited_ids.add(id)
        lemmas.append(WordNode(id, lemma.name().lower(), synset.pos()))
        add_relationship(id, synset.name(), 'InSynset')


# 抽取Synset实体之间的关系
def extract_relationships(synset):
    '''
    抽取Synset实体之间的关系
    '''
    # 上位概念（名词，动词）
    for related_node in synset.hypernyms():
        add_relationship(synset.name(), related_node.name(), 'IsA')
    # 下位概念（名词，动词）
    for related_node in synset.hyponyms():
        add_relationship(related_node.name(), synset.name(), 'IsA')
    # 上位整体概念（名词）
    for related_node in synset.member_holonyms():
        add_relationship(synset.name(), related_node.name(), 'PartOf')
    for related_node in synset.substance_holonyms():
        add_relationship(synset.name(), related_node.name(), 'PartOf')
    for related_node in synset.part_holonyms():
        add_relationship(synset.name(), related_node.name(), 'PartOf')
    # 下位部件概念（名词）
    for related_node in synset.member_meronyms():
        add_relationship(related_node.name(), synset.name(), 'PartOf')
    for related_node in synset.substance_meronyms():
        add_relationship(related_node.name(), synset.name(), 'PartOf')
    for related_node in synset.part_meronyms():
        add_relationship(related_node.name(), synset.name(), 'PartOf')
    # 主题域（名词，动词）
    # topic_domains
    for related_node in synset.topic_domains():
        add_relationship(synset.name(), related_node.name(), 'Domain')
    # region_domains
    for related_node in synset.region_domains():
        add_relationship(synset.name(), related_node.name(), 'Domain')
    # usage_domains
    for related_node in synset.usage_domains():
        add_relationship(synset.name(), related_node.name(), 'Domain')
    # 属性
    for related_node in synset.attributes():
        add_relationship(synset.name(), related_node.name(), 'Attribute')
    # 因果
    for related_node in synset.causes():
        add_relationship(synset.name(), related_node.name(), 'Cause')
    # similar_tos
    for related_node in synset.similar_tos():
        add_relationship(synset.name(), related_node.name(), 'SimilarTo')
    # 反义（形容词）
    for lemma in synset.lemmas():
        for related_node in lemma.antonyms():
            add_relationship(synset.name(), related_node.synset().name(), 'Antonym')
    # entailment（动词）
    for entailment in synset.entailments():
        add_relationship(synset.name(), entailment.name(), 'Entailment')


# 索引关系
def index_relationship(start, end, rel_type):
    '''
    索引关系
    '''
    relationship_index.setdefault(start, {})
    relationship_index[start].setdefault(end, {})
    relationship_index[start][end] = rel_type


# 添加关系，移除重复关系
def add_relationship(start, end, rel_type):
    '''
    添加关系，移除重复关系
    '''
    if (start in relationship_index and end in relationship_index[start] and rel_type in relationship_index[start][
        end]) or \
            (end in relationship_index and start in relationship_index[end] and rel_type in relationship_index[end][
                start]):
        pass
    else:
        index_relationship(start, end, rel_type)
        index_relationship(end, start, rel_type)
        relationships.append([start, end, rel_type])


def extract():
    for i, synset in enumerate(all_synsets):
        # 实体抽取-同义词集概念节点Concept Node
        synsets.append(SynsetNode(synset.name(), synset.pos(), synset.definition(), synset.examples()))
        # 概念关系抽取
        extract_relationships(synset)
        if i % 10000 == 0:
            print(f'{i} Synsets extracted')

    for i, synset in enumerate(all_synsets):
        extract_lemmas(synset)
        if i % 10000 == 0:
            print("Extracted lemmas for {} Synsets".format(i))

    # 关系数，词汇实体数，同义词集实体数
    len(relationships), len(lemmas), len(synsets)

    # 随机输出10个关系
    for i in [random.randint(0, len(relationships) - 1) for _ in range(10)]:
        print(relationships[i])

    # 随机输出10个同义词集概念实体
    for i in [random.randint(0, len(synsets) - 1) for _ in range(10)]:
        print(synsets[i])

    # 随机输出10个词汇实体
    for i in [random.randint(0, len(lemmas) - 1) for _ in range(10)]:
        print(lemmas[i])


def save_data():
    print('Writing synsets...', end='')
    with open('../data/synsets.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id:ID', 'pos:string', 'definition:string', ':LABEL', 'examples:string'])
        for synset in synsets:
            writer.writerow(synset.get_row())
    print('Done')

    print('Writing words...', end='')
    with open('../data/words.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(WordNode.get_header())
        for word in lemmas:
            writer.writerow(word.get_row())
    print('Done')

    print('Writing relationships...', end='')
    with open('../data/relationships.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([':START_ID', ':END_ID', ':TYPE'])
        for relationship in relationships:
            writer.writerow(relationship)
    print('Done')


if __name__ == '__main__':
    extract()
    save_data()
