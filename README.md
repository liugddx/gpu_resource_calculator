# 大模型推理GPU资源计算器

这是一个使用Flask搭建的简单网页应用，用于计算大模型推理所需的GPU资源。

## 功能

- 输入模型的层数、隐藏大小、精度、输出标记数量、并发请求数量以及KV缓存占GPU内存的比例。
- 计算并显示每个标记的KV缓存内存、总KV缓存内存以及估算所需的GPU内存。

## 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/liugddx/gpu_resource_calculator.git
cd gpu_resource_calculator
```

### 2.创建并激活虚拟环境

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 运行应用

```bash
python app.py
```
