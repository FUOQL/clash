import time
from CashAI import CashAI

def demo():
    # 创建CashAI实例
    ai = CashAI(api_key="demo_api_key", initial_balance=10000)
    
    # 显示初始状态
    print("初始状态:")
    print(ai.get_status())
    
    # 执行几次模拟交易
    print("\n执行模拟交易...")
    for i in range(5):
        ai.execute_trade("BTC/USD")
        time.sleep(1)  # 模拟时间间隔
    
    # 显示最终状态
    print("\n最终状态:")
    print(ai.get_status())
    
    # 显示交易历史
    print("\n交易历史:")
    for trade in ai.get_trade_history():
        print(trade)

if __name__ == "__main__":
    demo()
