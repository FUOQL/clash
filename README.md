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

## 安装说明

1. 克隆仓库:
   ```
   git clone https://github.com/FUOQL/clash.git
   ```
2. 进入项目目录:
   ```
   cd clash
   ```
3. 安装依赖:
   ```
   pip install -r requirements.txt
   ```

## 使用方法

1. 运行演示程序:
   ```
   python demo.py
   ```
2. 运行测试:
   ```
   python -m unittest test_cashai.py
   ```
3. 验证项目:
   ```
   python verify_project.py
   ```

## API接口

- `GET /status` - 获取机器人状态
- `GET /history` - 获取交易历史
- `POST /start` - 启动交易机器人
- `POST /stop` - 停止交易机器人

## 项目结构

- `CashAI.py`: 核心实现文件
- `requirements.txt`: 依赖列表
- `README.md`: 项目说明文档
- `USAGE.md`: 使用指南
- `FINAL_SUMMARY.md`: 项目总结
- `demo.py`: 演示程序
- `test_cashai.py`: 测试文件
- `verify_project.py`: 项目验证脚本
- `.gitignore`: Git忽略文件配置

## 注意事项

- 当前实现使用随机策略，仅用于演示目的
- 在生产环境中需要实现更复杂的交易策略
- 需要配置有效的API密钥才能连接到真实交易所
- 请确保已安装Python 3.8或更高版本
- 本系统仅供学习和研究使用，不构成任何投资建议

## 许可证

本项目采用MIT许可证，详情请见[LICENSE](LICENSE)文件。