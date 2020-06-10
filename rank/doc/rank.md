## 1、客户端排名记录

**请求URL：** 

- ` /api/rank/v1/rank_record/`

**请求方式：**

- POST

**参数：** 

| 参数名     | 必选 | 类型 | 说明       |
| :--------- | :--- | :--- | ---------- |
| rank_name  | 必选 | str  | 客户端名称 |
| rank_score | 必选 | int  | 客户端分数 |

 **返回示例**

```
{
    "code": 200,
    "msg": "数据添加成功"
}
```

##  

## 2、客户端排名展示

**请求URL：** 

- ` /api/rank/v1/rank_list/`

**请求方式：**

- GET

**参数：** 

| 参数名      | 必选 | 类型 | 说明       |
| :---------- | :--- | :--- | ---------- |
| rank_name   | 必选 | str  | 客户端名称 |
| score_start | 可选 | int  | 起始分数   |
| score_end   | 可选 | int  | 结束分数   |

 **返回示例**

```
{
    "code": 200,
    "msg": {
        "rank_list": [   # 客户端排名
            {
                "rank_name": "客户端2",
                "rank_score": 45614
            },
            {
                "rank_name": "客户端1",
                "rank_score": 24614
            },
            {
                "rank_name": "客户端3",
                "rank_score": 6789
            }
        ],
        "rank_current": {  # 当前客户端
            "rank_name": "客户端5",
            "rank_score": 666
        }
    }
}
```



## 