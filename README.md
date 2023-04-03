## 基于知识图谱的可视化英语词典
![](https://ddy-1310349779.cos.ap-shanghai.myqcloud.com/typora/%E6%88%AA%E5%B1%8F2023-04-03%2016.10.32.jpg)

## 各系统版本
- java 11
- Neo4j v4.4.18
- Py2neo==4.3.0
- Python3.7+
- Sveltekit

## 1. 构建知识图谱

**Step1:** 运行`backend/utility/extract_info.py`, 从WordNet中抽取实体和关系, 得到三个文件:

- `backend/data/relationships.csv`
- `backend/data/synsets.csv`
- `backend/data/words.csv`

**Step2:** 将上面三个文件移到`neo4j/import`中, 接着运行下面指令:

```shell
cd backend/neo4j-v4/bin
./neo4j-admin import --nodes ../import/words.csv --nodes ../import/synsets.csv --relationships ../import/relationships.csv --skip-duplicate-nodes
```

**Step3:** 得到下面截图的结果,则表示数据成功的导入到neo4j中

<div style="text-align:center"><img src="https://ddy-1310349779.cos.ap-shanghai.myqcloud.com/typora/%E6%88%AA%E5%B1%8F2023-03-04%2020.38.24.jpg" style="zoom:50%" /></div>

**Step4:** 运行下面指令启动neo4j

```shell
cd backend/neo4j-v4/bin
./neo4j start
```

**Step5:** 打开浏览器，访问`http://localhost:7474`，初始Username和Password都是`neo4j`，成功登录后可以看到构建好的知识图谱

<img src="https://ddy-1310349779.cos.ap-shanghai.myqcloud.com/typora/%E6%88%AA%E5%B1%8F2023-03-04%2020.43.30.jpg" style="zoom:30%;" />

<img src="https://ddy-1310349779.cos.ap-shanghai.myqcloud.com/typora/%E6%88%AA%E5%B1%8F2023-03-04%2020.48.59.jpg" style="zoom:50%;" />



## 2. 构建可视化在线词典

**Step1:** 本项目使用python去连接已经构建好的知识图谱，第一步需要先启动neo4j

```shell
cd backend/neo4j-v4/bin
./neo4j start
```

**Step2:** 挂起neo4j后，使用python的py2neo去连接知识图谱并且启动flask后端程序

```shell
cd backend
python app.py
```

**Step3:** 启动前端程序

```shell
cd frontend
npm run dev
```
