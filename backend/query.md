<!--
 * @Author: ddy 58058861+ddy-ddy@users.noreply.github.com
 * @Date: 2023-03-22 09:46:06
 * @LastEditTime: 2023-03-25 20:20:38
 * @Github: https://github.com/ddy-ddy
 * @Website: https://ddy-ddy.com
-->
### 情况1
- 匹配一个以Lemma名为'implicit'的节点作为起点，以这个节点与其他节点之间的边形成的路径p作为结果。
- 这些边是从起点到终点的，且边的类型为'InSynset'。
- 返回所有终点节点Synset和它们的Lemma节点。
```python
input_query = "implicit"
query = "MATCH p=(a:Lemma{name:'查询词'})-[b:InSynset]->(c:Synset) RETURN b,c"
```

### 情况2
```python
input_query = "implicit"
query = "MATCH p=(a:Lemma{name:'查询词'})-[b:InSynset]->(c:Synset{id:'查询词ID'})<-[d:InSynset]-(e:Lemma)  RETURN c,d"
```