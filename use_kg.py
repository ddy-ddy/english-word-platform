# -*- coding: utf-8 -*-
# @Time    : 2023/2/12 21:55
# @Author  : ddy
# @FileName: use_kg.py
# @github  : https://github.com/ddy-ddy

from py2neo import Graph, Node, Relationship, NodeMatcher, RelationshipMatcher


def knowledge_inference(wordnet_graph, question):
    n_matcher = NodeMatcher(wordnet_graph)
    r_matcher = RelationshipMatcher(wordnet_graph)

    word = question.split(" ")[-1]
    print("Find knowledge for {}......\n\n".format(word))
    entity_node = n_matcher.match("Lemma", name=word).first()

    for r in r_matcher.match([entity_node], r_type="InSynset"):
        concept_node = r.end_node
        print("Definition: \n")
        print("-- {} is {}".format(word, concept_node["definition"]))
        print("\n" + "*" * 50 + "\n")

        print("Part of relations")
        for isa_r in r_matcher.match([concept_node], r_type="PartOf"):
            end = isa_r.end_node
            for isa_r in r_matcher.match([None, end], r_type="InSynset"):
                start = isa_r.start_node
                print("-- {} is part of {}".format(word, start["name"]))
            break

        for isa_r in r_matcher.match([None, concept_node], r_type="PartOf"):
            end = isa_r.end_node
            for isa_r in r_matcher.match([None, end], r_type="InSynset"):
                start = isa_r.start_node
                print("-- {} is part of {}".format(start["name"], word))
            break

        print("\n" + "*" * 50 + "\n")

        print("For examples: \n")
        for i, isa_r in enumerate(
                r_matcher.match([None, concept_node], r_type="IsA")):
            start = isa_r.start_node
            print("{}. {} is a {} which means {}\n".format(
                i + 1, start['id'].split(".")[0], word, start["definition"]))
        print("\n" + "*" * 50 + "\n")

        print("Similar Things: \n")
        for i, isa_r in enumerate(
                r_matcher.match([concept_node], r_type="SimilarTo")):
            end = isa_r.end_node
            print("{}".format(end["id"].split(".")[0]))

        for i, isa_r in enumerate(
                r_matcher.match([None, concept_node], r_type="SimilarTo")):
            start = isa_r.start_node
            print("{}".format(start["id"].split(".")[0]))

        print("\n" + "*" * 50 + "\n")

        print("Same domain words: \n")
        for i, isa_r in enumerate(
                r_matcher.match([concept_node], r_type="Domain")):
            end = isa_r.end_node
            print("{}".format(end["id"].split(".")[0]))

        for i, isa_r in enumerate(
                r_matcher.match([None, concept_node], r_type="Domain")):
            start = isa_r.start_node
            print("{}".format(start["id"].split(".")[0]))

        print("\n" + "*" * 50 + "\n")
        break


if __name__ == '__main__':
    uri = "http://localhost:7474"
    user = "neo4j"
    password = "12345678"
    wordnet_graph = Graph(uri=uri, user=user, password=password)

    question = "what is computer"
    knowledge_inference(wordnet_graph, question)
