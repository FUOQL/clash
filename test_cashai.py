import unittest
from unittest.mock import patch, MagicMock
from CashAI import CashAI

class TestCashAI(unittest.TestCase):
    def setUp(self):
        self.ai = CashAI(api_key="test_key", initial_balance=10000)
    
    def test_initialization(self):
        self.assertEqual(self.ai.api_key, "test_key")
        self.assertEqual(self.ai.balance, 10000)
        self.assertFalse(self.ai.is_running)
        self.assertEqual(self.ai.trade_history, [])
        self.assertEqual(self.ai.profit_loss, 0)
    
    @patch('CashAI.requests.get')
    def test_get_market_data_success(self, mock_get):
        # 模拟成功的API响应
        mock_response = MagicMock()
        mock_response.json.return_value = {"price": 50000}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        
        result = self.ai.get_market_data("BTC/USD")
        self.assertEqual(result, {"price": 50000})
    
    @patch('CashAI.requests.get')
    def test_get_market_data_failure(self, mock_get):
        # 模拟API请求失败
        mock_get.side_effect = Exception("网络错误")
        
        result = self.ai.get_market_data("BTC/USD")
        self.assertIsNone(result)
    
    def test_get_status(self):
        status = self.ai.get_status()
        self.assertEqual(status["balance"], 10000)
        self.assertFalse(status["is_running"])
        self.assertEqual(status["profit_loss"], 0)
        self.assertEqual(status["trade_count"], 0)
    
    def test_get_trade_history(self):
        # 添加一些模拟交易记录
        self.ai.trade_history.append({"symbol": "BTC/USD", "side": "buy", "quantity": 0.1, "price": 50000})
        history = self.ai.get_trade_history()
        self.assertEqual(len(history), 1)
        self.assertEqual(history[0]["symbol"], "BTC/USD")

if __name__ == '__main__':
    unittest.main()
