# 🏛️ Ancient Architecture Dashboard

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.0-green.svg)](https://flask.palletsprojects.com/)
[![ECharts](https://img.shields.io/badge/ECharts-5.4.3-yellow.svg)](https://echarts.apache.org/)

**主题合规的中国古代建筑结构健康监测大屏**，仅针对四大类建筑（民居、官府、皇宫、桥梁）进行可视化展示。

## 📁 项目结构
ancient-architecture-dashboard/
├── README.md # 项目说明
├── requirements.txt # Python依赖库
├── app.py # 主程序入口
├── data.py # 数据源
├── .gitignore # Git忽略文件
├── LICENSE # MIT许可证
├── templates/
│ └── index.html # 大屏页面模板
├── static/
│ ├── css/
│ │ └── style.css # 大屏样式
│ └── js/
│ └── echarts.min.js # ECharts库
├── data/
│ ├── raw/ # 原始数据
│ └── processed/ # 清洗后数据
├── scripts/
│ └── data_processor.py # 数据预处理脚本
└── notebooks/
└── data_exploration.ipynb # 数据分析笔记

## 🚀 快速开始

### 安装依赖
bash
pip install -r requirements.txt

### 运行项目
bash
python app.py
打开浏览器访问 [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 📊 数据说明
- 数据来源：历史文献、公开数据库
- 时间范围：1911年前
- 建筑类型：仅限民居、官府、皇宫、桥梁
- 核心指标：梁柱直径、斗拱密度、年代、朝代

## 🎨 大屏功能
- 建筑类型分布饼图
- 结构参数散点图
- 各类建筑平均直径柱状图
- 实时时间显示
- 响应式布局

## 🏆 比赛说明
本项目为**2026年中国大学生计算机设计大赛**（4C）参赛作品，符合大赛主题“中国古代建筑成就”要求。

## 📄 许可证
[MIT License](LICENSE)
