import os
import sys

def verify_project():
    """验证项目文件结构和基本功能"""
    # 检查必要的文件是否存在
    required_files = [
        "CashAI.py",
        "requirements.txt",
        "README.md",
        "USAGE.md",
        "demo.py",
        "test_cashai.py"
    ]
    
    print("正在验证项目文件...")
    missing_files = []
    for file in required_files:
        if os.path.exists(file):
            print(f"✓ {file} 存在")
        else:
            print(f"✗ {file} 不存在")
            missing_files.append(file)
    
    if missing_files:
        print(f"\n缺少 {len(missing_files)} 个必要文件:")
        for file in missing_files:
            print(f"  - {file}")
        return False
    
    # 尝试导入模块
    try:
        import CashAI
        print("✓ CashAI 模块可以正常导入")
    except ImportError as e:
        print(f"✗ CashAI 模块导入失败: {e}")
        return False
    
    # 检查依赖是否可以安装
    try:
        import flask
        import requests
        print("✓ 依赖库已安装")
    except ImportError as e:
        print(f"⚠ 依赖库未安装: {e}")
        print("  请运行 'pip install -r requirements.txt' 安装依赖")
    
    print("\n项目验证完成!")
    return True

if __name__ == "__main__":
    success = verify_project()
    sys.exit(0 if success else 1)
