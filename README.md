# CCKS任务四数据预处理

## 建立数据库

使用Docker+MongoDB存储三元组数据。

导入数据：

```bash
./start.sh
python kb.py
```

[使用python查询MongoDB](https://www.mongodb.com/languages/python)

[使用mongo镜像](https://hub.docker.com/_/mongo)

## 分割训练集与验证集

我上传了我分割好的结果，可以跳过这一步。

```bash
python split_datasets.py
```

## 预处理训练数据

使用Bert计算出问题的CLS嵌入，缩短数据加载时间。

```bash
python encode_data.py split_datasets/train.txt
python encode_data.py split_datasets/val.txt
```
