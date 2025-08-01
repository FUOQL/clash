#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CashAI 测试脚本
用于测试CashAI Coding Agent的各项功能
"""

import os
import sys
import subprocess
import tempfile
import shutil

def run_test(test_name: str, command: str, expected_files: list = None):
    """运行单个测试"""
    print(f"\n{'='*50}")
    print(f"测试: {test_name}")
    print(f"命令: {command}")
    print(f"{'='*50}")
    
    try:
        # 运行命令
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        print("输出:")
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(f"错误: {result.stderr}")
        
        # 检查预期文件
        if expected_files:
            print("\n检查文件:")
            for file_path in expected_files:
                if os.path.exists(file_path):
                    print(f"✓ {file_path} 存在")
                    if file_path.endswith('.py'):
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            print(f"  内容: {content[:100]}...")
                else:
                    print(f"✗ {file_path} 不存在")
        
        print(f"测试 {test_name} 完成")
        return True
        
    except Exception as e:
        print(f"测试 {test_name} 失败: {e}")
        return False

def main():
    """主测试函数"""
    print("CashAI Coding Agent 功能测试")
    print("="*50)
    
    # 测试1: 创建Python文件
    test1_success = run_test(
        "创建Python文件",
        'python CashAI.py -m "create a python file called main.py"',
        ['main.py']
    )
    
    # 测试2: 复制Python文件
    test2_success = run_test(
        "复制Python文件",
        'python CashAI.py -m "duplicate all python files in the current directory by adding -dup prefix to them"',
        ['main.py', 'main-dup.py']
    )
    
    # 测试3: 编辑文件内容
    test3_success = run_test(
        "编辑文件内容",
        'python CashAI.py -m "print Hello World 100 times inside main.py"',
        ['main.py']
    )
    
    # 测试4: Git操作
    test4_success = run_test(
        "Git操作",
        'python CashAI.py -m "create a commit with a message about testing and push it into github"',
        []
    )
    
    # 测试5: Django项目创建
    test5_success = run_test(
        "创建Django项目",
        'python CashAI.py -m "create a django project for an online store website"',
        ['online_store']
    )
    
    # 总结
    print(f"\n{'='*50}")
    print("测试总结:")
    print(f"测试1 (创建Python文件): {'通过' if test1_success else '失败'}")
    print(f"测试2 (复制Python文件): {'通过' if test2_success else '失败'}")
    print(f"测试3 (编辑文件内容): {'通过' if test3_success else '失败'}")
    print(f"测试4 (Git操作): {'通过' if test4_success else '失败'}")
    print(f"测试5 (Django项目): {'通过' if test5_success else '失败'}")
    print(f"{'='*50}")

if __name__ == '__main__':
    main() 