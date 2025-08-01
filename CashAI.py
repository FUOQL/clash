import random
import time
import threading
import requests
from flask import Flask, jsonify, request
class CashAI:
    def __init__(self, api_key, initial_balance=10000):
        self.api_key = api_key
        self.balance = initial_balance
        self.is_running = False
        self.trading_thread = None
        self.trade_history = []
        self.profit_loss = 0
        self.base_url = "https://api.example.com/v1"
    
    def get_market_data(self, symbol):
        """获取市场数据"""
        try:
            response = requests.get(f"{self.base_url}/market/{symbol}", headers={"Authorization": f"Bearer {self.api_key}"})
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"获取市场数据失败: {e}")
            return None
    
    def place_order(self, symbol, side, quantity, price):
        """下单"""
        try:
            order_data = {
                "symbol": symbol,
                "side": side,
                "quantity": quantity,
                "price": price
            }
            response = requests.post(f"{self.base_url}/orders", json=order_data, headers={"Authorization": f"Bearer {self.api_key}"})
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"下单失败: {e}")
            return None
    
    def execute_trade(self, symbol):
        """执行交易逻辑"""
        market_data = self.get_market_data(symbol)
        if not market_data:
            return
        
        current_price = market_data['price']
        # 简单的交易策略：随机决策
        if random.random() > 0.5:
            side = "buy"
            quantity = round(random.uniform(0.1, 1.0), 2)
        else:
            side = "sell"
            quantity = round(random.uniform(0.1, 1.0), 2)
        
        order_result = self.place_order(symbol, side, quantity, current_price)
        if order_result:
            trade = {
                "symbol": symbol,
                "side": side,
                "quantity": quantity,
                "price": current_price,
                "timestamp": time.time()
            }
            self.trade_history.append(trade)
            # 更新余额和盈亏
            if side == "buy":
                self.balance -= quantity * current_price
            else:
                self.balance += quantity * current_price
            self.profit_loss += quantity * current_price * (1 if side == "sell" else -1)
            print(f"执行交易: {side} {quantity} {symbol} @ {current_price}")
    
    def start_trading(self, symbol, interval=5):
        """开始自动交易"""
        if self.is_running:
            print("交易机器人已在运行中")
            return
        
        self.is_running = True
        def trading_loop():
            while self.is_running:
                self.execute_trade(symbol)
                time.sleep(interval)
        
        self.trading_thread = threading.Thread(target=trading_loop)
        self.trading_thread.start()
        print("交易机器人已启动")
    
    def stop_trading(self):
        """停止自动交易"""
        if not self.is_running:
            print("交易机器人未在运行")
            return
        
        self.is_running = False
        if self.trading_thread:
            self.trading_thread.join()
        print("交易机器人已停止")
    
    def get_status(self):
        """获取机器人状态"""
        return {
            "balance": self.balance,
            "is_running": self.is_running,
            "profit_loss": self.profit_loss,
            "trade_count": len(self.trade_history)
        }
    
    def get_trade_history(self):
        """获取交易历史"""
        return self.trade_history

def create_app(ai_instance):
    app = Flask(__name__)
    
    @app.route('/status', methods=['GET'])
    def get_status():
        return jsonify(ai_instance.get_status())
    
    @app.route('/history', methods=['GET'])
    def get_history():
        return jsonify(ai_instance.get_trade_history())
    
    @app.route('/start', methods=['POST'])
    def start_trading():
        data = request.json
        symbol = data.get('symbol', 'BTC/USD')
        interval = data.get('interval', 5)
        ai_instance.start_trading(symbol, interval)
        return jsonify({"message": "交易机器人已启动"})
    
    @app.route('/stop', methods=['POST'])
    def stop_trading():
        ai_instance.stop_trading()
        return jsonify({"message": "交易机器人已停止"})
    
    return app

if __name__ == "__main__":
    # 初始化CashAI实例
    ai = CashAI(api_key="your_api_key_here", initial_balance=10000)
    
    # 创建Flask应用
    app = create_app(ai)
    
    # 启动Flask服务
    app.run(host='0.0.0.0', port=5000, debug=True)
