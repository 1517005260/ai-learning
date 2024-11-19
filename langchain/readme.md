# Langchain 学习

LLM的解决方案：oneapi转接，可以集成各种模型

```bash
docker run --name one-api -d --restart always -p 13000:3000 -e TZ=Asia/Shanghai -v /home/ubuntu/data/one-api:/data justsong/one-api
```

本地LLM模型：qwen2:7B：

```bash
C:\Users\Administrator>ollama run qwen2:7b
>>> nihao
你好！你问了“nihao”，这是中文里的“你好”的拼音。在中国的普通话中，“你好”就是这么打招呼的。有什么我可以帮助你的
吗？
```

本地embedding模型：m3e

```bash
docker run -d -p 6008:6008 --gpus all registry.cn-hangzhou.aliyuncs.com/fastgpt_docker/m3e-large-api:latest
```