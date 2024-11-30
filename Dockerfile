# 基于 Python 3.9 slim 镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制项目到容器中
COPY . /app

# 安装依赖
RUN pip install --upgrade pip && pip install -r requirements.txt

# 设置默认命令（如果需要）
CMD ["bash"]

