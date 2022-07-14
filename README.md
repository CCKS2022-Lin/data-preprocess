# CCKS任务四数据预处理

## 构建镜像

因为镜像文件实在太大了（19G），如果不想传输的话可以自己构建，可能会快很多。构建之前准备好`./data/triple.txt`也就是知识库文件。

```bash
docker pull pkumod/gstore
docker build -t mygstore .
```

如果需要导出镜像的话：

```bash
docker save mygstore -o mygstore.docker
```

## 建立数据库

导入docker镜像：

```bash
docker load < mygstore.docker
```

创建并运行容器：

```bash
docker run --name mygstore -p 9000:9000 -d mygstore
```

等待http://localhost:9000能够返回页面后说明容器启动成功。

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
python encode_data.py split_datasets/验证集问题.txt --is_test
```

然后将`split_datasets`下生成的.bin文件移动到预测模型的项目中。
