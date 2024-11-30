# 图数据库Neo4j本地安装

1. docker安装，详见[此仓库](https://github.com/1517005260/Innovation-Project/tree/master/main/graphrag)

2. windows安装

首先确认装好了java：

```bash
(base) PS C:\Users\Administrator\Desktop\ai-learning> java --version
java 17.0.12 2024-07-16 LTS
Java(TM) SE Runtime Environment (build 17.0.12+8-LTS-286)
Java HotSpot(TM) 64-Bit Server VM (build 17.0.12+8-LTS-286, mixed mode, sharing)
```

然后在 https://neo4j.com/download-center/  选择 Graph Database Self-Managed ==> community  即可，[链接](https://go.neo4j.com/download-thanks.html?edition=community&release=5.25.1&flavour=winzip)

下载解压后进入neo4j主文件夹的cmd里：

```bash
C:\Program Files (x86)\neo4j-community-5.25.1>bin\neo4j.bat windows-service install
Neo4j service installed.
```

启动、停止、重启、查询：

```bash
neo4j start
neo4j stop
neo4j restart
neo4j status
```

3. 访问数据库

- 浏览器访问：`http://localhost:7474/  auth=(neo4j, neo4j)`

- Py2neo访问：`neo4j://localhost:7687`

4. 默认数据库

```
# neo4j/conf/neo4j.conf
initial.dbms.default_database=neo4j
```

5. 向图数据库导入csv文件

先修改当前数据库为test，即：`initial.dbms.default_database=test`，测试文件在[test](./test/)文件夹下

将test文件夹整个复制到`neo4j/import`下，导入时，先导入节点，再导入关系。

```cypher
<!-- 导入节点 -->
LOAD CSV WITH HEADERS FROM 'file:///test/nodes/Category.csv' as row
CREATE (:Category {name:row.name});

LOAD CSV WITH HEADERS FROM 'file:///test/nodes/Check.csv' as row
CREATE (:Check {name:row.name});

LOAD CSV WITH HEADERS FROM 'file:///test/nodes/Cureway.csv' as row
CREATE (:Cureway {name:row.name});

LOAD CSV WITH HEADERS FROM 'file:///test/nodes/Department.csv' as row
CREATE (:Department {name:row.name});

LOAD CSV WITH HEADERS FROM 'file:///test/nodes/Disease.csv' as row
CREATE (:Disease {name:row.name, desc:row.desc, prevent:row.prevent, cause:row.cause, yibao_status:row.yibao_status, get_prob:row.get_prob, get_way:row.get_way, cure_lasttime:row.cure_lasttime, cured_prob:row.cured_prob, cost_money:row.cost_money});

LOAD CSV WITH HEADERS FROM 'file:///test/nodes/Dishes.csv' as row
CREATE (:Dishes {name:row.name});

LOAD CSV WITH HEADERS FROM 'file:///test/nodes/Drug.csv' as row
CREATE (:Drug {name:row.name});

LOAD CSV WITH HEADERS FROM 'file:///test/nodes/Food.csv' as row
CREATE (:Food {name:row.name});

LOAD CSV WITH HEADERS FROM 'file:///test/nodes/Symptom.csv' as row
CREATE (:Symptom {name:row.name});

<!-- 创建索引，加速关系导入过程 -->
CREATE INDEX FOR (n:Category) ON (n.name);
CREATE INDEX FOR (n:Check) ON (n.name);
CREATE INDEX FOR (n:Cureway) ON (n.name);
CREATE INDEX FOR (n:Department) ON (n.name);
CREATE INDEX FOR (n:Disease) ON (n.name);
CREATE INDEX FOR (n:Dishes) ON (n.name);
CREATE INDEX FOR (n:Drug) ON (n.name);
CREATE INDEX FOR (n:Food) ON (n.name);
CREATE INDEX FOR (n:Symptom) ON (n.name);

<!-- 导入关系 -->
LOAD CSV WITH HEADERS FROM 'file:///test/relations/DISEASE_ACOMPANY.csv' as row
MATCH (m:Disease {name:row.from}), (n:Disease {name:row.to})
MERGE (m)-[:DISEASE_ACOMPANY]->(n);
    
LOAD CSV WITH HEADERS FROM 'file:///test/relations/DISEASE_CATEGORY.csv' as row
MATCH (m:Disease {name:row.from}), (n:Category {name:row.to})
MERGE (m)-[:DISEASE_CATEGORY]->(n);

LOAD CSV WITH HEADERS FROM 'file:///test/relations/DISEASE_CHECK.csv' as row
MATCH (m:Disease {name:row.from}), (n:Check {name:row.to})
MERGE (m)-[:DISEASE_CHECK]->(n);

LOAD CSV WITH HEADERS FROM 'file:///test/relations/DISEASE_CUREWAY.csv' as row
MATCH (m:Disease {name:row.from}), (n:Cureway {name:row.to})
MERGE (m)-[:DISEASE_CUREWAY]->(n);

LOAD CSV WITH HEADERS FROM 'file:///test/relations/DISEASE_DEPARTMENT.csv' as row
MATCH (m:Disease {name:row.from}), (n:Department {name:row.to})
MERGE (m)-[:DISEASE_DEPARTMENT]->(n);

LOAD CSV WITH HEADERS FROM 'file:///test/relations/DISEASE_DISHES.csv' as row
MATCH (m:Disease {name:row.from}), (n:Dishes {name:row.to})
MERGE (m)-[:DISEASE_DISHES]->(n);

LOAD CSV WITH HEADERS FROM 'file:///test/relations/DISEASE_DO_EAT.csv' as row
MATCH (m:Disease {name:row.from}), (n:Food {name:row.to})
MERGE (m)-[:DISEASE_DO_EAT]->(n);

LOAD CSV WITH HEADERS FROM 'file:///test/relations/DISEASE_DRUG.csv' as row
MATCH (m:Disease {name:row.from}), (n:Drug {name:row.to})
MERGE (m)-[:DISEASE_DRUG]->(n);

LOAD CSV WITH HEADERS FROM 'file:///test/relations/DISEASE_NOT_EAT.csv' as row
MATCH (m:Disease {name:row.from}), (n:Food {name:row.to})
MERGE (m)-[:DISEASE_NOT_EAT]->(n);

LOAD CSV WITH HEADERS FROM 'file:///test/relations/DISEASE_SYMPTOM.csv' as row
MATCH (m:Disease {name:row.from}), (n:Symptom {name:row.to})
MERGE (m)-[:DISEASE_SYMPTOM]->(n);
```