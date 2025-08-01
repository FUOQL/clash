# 使用指南

## 快速开始

1. 安装依赖:
   ```bash
   pip install -r requirements.txt
   ```

2. 配置API密钥:
   在 `CashAI.py` 文件中找到以下行并替换为你的API密钥:
   ```python
   ai = CashAI(api_key="your_api_key_here", initial_balance=10000)
   ```

3. 运行程序:
   ```bash
   python CashAI.py
   ```

4. 访问Web界面:
   打开浏览器访问 `http://localhost:5000`

## API使用

### 获取机器人状态

```bash
curl http://localhost:5000/status
```

### 获取交易历史

```bash
curl http://localhost:5000/history
```

### 启动交易机器人

```bash
curl -X POST http://localhost:5000/start -H "Content-Type: application/json" -d '{"symbol": "BTC/USD", "interval": 5}'
```

### 停止交易机器人

```bash
curl -X POST http://localhost:5000/stop
```

## 配置说明

- `api_key`: 交易所API密钥
- `initial_balance`: 初始余额
- `interval`: 交易间隔时间(秒)

## 策略开发

要实现自定义交易策略，请修改 `CashAI.py` 中的 `execute_trade` 方法。

## 注意事项

- 请勿在生产环境中使用默认的随机策略
- 确保API密钥的安全性
- 在真实交易前请充分测试策略
