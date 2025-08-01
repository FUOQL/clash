# CashAI

CashAI 是一个基于Python的自动化交易机器人项目，它能够连接到加密货币交易所API，执行自动交易，并提供Web界面来监控和控制交易过程。

## 功能特性

- 自动化交易执行
- 实时监控交易状态
- Web API接口控制
- 可扩展的交易策略

## 技术栈

- Python 3.x
- Flask
- requests
- threading

## 安装

```bash
pip install -r requirements.txt
```

## 使用方法

1. 配置API密钥
2. 运行程序: `python CashAI.py`
3. 通过Web API控制机器人

## API接口

- `GET /status` - 获取机器人状态
- `GET /history` - 获取交易历史
- `POST /start` - 启动交易机器人
- `POST /stop` - 停止交易机器人

## 文件说明

- `CashAI.py`: 核心实现文件
- `requirements.txt`: 依赖列表
- `USAGE.md`: 使用指南
- `demo.py`: 演示程序
- `test_cashai.py`: 测试文件

## 注意事项

- 当前实现使用随机策略，仅用于演示目的
- 在生产环境中需要实现更复杂的交易策略
- 需要配置有效的API密钥才能连接到真实交易所
