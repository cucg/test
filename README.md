# 服务器游戏排名rank
```
Python版本: 3.7.1
Django版本: 2.2.1
Mysql版本: 8.0.16
```

一、准备工作
---
> 1. 安装依赖: pip install -r requirements.txt
> 2. 安装并启动mysql,迁移
> 3. 初始化
>   * python manage.py init_rank --settings=mytest.settings


二、模块介绍
---
```
mytest: 项目配置和路由入口
rank:   排名子应用
	views        视图层
	operate      数据操作层
	service      业务逻辑层
	logs/pro.log 日志记录
	doc          接口文档
	postman测试结果在接口文档返回实例有写,谢谢!
```

三、附加题
---
```
bonus_question.py   附加题
```


