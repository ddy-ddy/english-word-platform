## 🌲介绍

## 各系统版本

- java 11
- Neo4j v4.4.18(千万别用Neo4j v5)
- Py2neo==4.3.0

## 一、构建知识图谱

1、运行`backend/utility/extract_info.py`从WordNet中抽取实体和关系，得到三个文件：

- `backend/data/relationships.csv`
- `backend/data/synsets.csv`
- `backend/data/words.csv`

2、将上面三个文件移到`neo4j/import`中，接着运行下面指令：

```shell
cd backend/neo4j/bin
./neo4j-admin import --nodes ../import/words.csv --nodes ../import/synsets.csv --relationships ../import/relationships.csv --skip-duplicate-nodes
```

3、得到下面截图的结果，则表示数据成功的导入到neo4j中
<img src="https://ddy-1310349779.cos.ap-shanghai.myqcloud.com/typora/%E6%88%AA%E5%B1%8F2023-03-04%2020.38.24.jpg" style="zoom:50%;" />

4、运行下面指令启动neo4j

```shell
cd backend/neo4j/bin
./neo4j start
```

5、打开浏览器，登录`http://localhost:7474`，初始Username和Password都是`neo4j`，成功登录后可以看到构建好的知识图谱

<img src="https://ddy-1310349779.cos.ap-shanghai.myqcloud.com/typora/%E6%88%AA%E5%B1%8F2023-03-04%2020.43.30.jpg" style="zoom:30%;" />

<img src="https://ddy-1310349779.cos.ap-shanghai.myqcloud.com/typora/%E6%88%AA%E5%B1%8F2023-03-04%2020.48.59.jpg" style="zoom:50%;" />

## 二、构建在线词典
