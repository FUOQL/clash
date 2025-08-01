#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CashAI 演示脚本
展示CashAI Coding Agent的各种功能
"""

import os
import sys
import subprocess

def run_demo_command(command: str, description: str):
    """运行演示命令"""
    print(f"\n{'='*60}")
    print(f"演示: {description}")
    print(f"命令: {command}")
    print(f"{'='*60}")
    
    try:
        # 运行命令
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        print("输出:")
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(f"错误: {result.stderr}")
            
    except Exception as e:
        print(f"演示失败: {e}")

def main():
    """主演示函数"""
    print("CashAI Coding Agent 功能演示")
    print("="*60)
    
    # 演示1: 创建Python文件
    run_demo_command(
        'python CashAI.py -m "create a python file called main.py and add it to git and make a commit"',
        "创建Python文件并提交到Git"
    )
    
    # 演示2: 复制Python文件
    run_demo_command(
        'python CashAI.py -m "duplicate all python files in the current directory by adding -dup prefix to them and commit all of them with a proper message"',
        "复制所有Python文件并提交"
    )
    
    # 演示3: 编辑文件内容
    run_demo_command(
        'python CashAI.py -m "print Hello World 100 times inside main.py"',
        "在main.py中打印Hello World 100次"
    )
    
    # 演示4: 创建Django项目
    run_demo_command(
        'python CashAI.py -m "create a django project for an online store website"',
        "创建在线商店Django项目"
    )
    
    # 演示5: Git操作
    run_demo_command(
        'python CashAI.py -m "create a commit with a message about fixing bugs and push it into github"',
        "创建修复bug的commit并推送到GitHub"
    )
    
    print(f"\n{'='*60}")
    print("演示完成！")
    print("CashAI支持以下功能:")
    print("1. 执行简单终端命令")
    print("2. 上下文感知的终端命令")
    print("3. 文件编辑和更改管理")
    print("4. 项目执行")
    print("5. 用户批准机制")
    print(f"{'='*60}")

if __name__ == '__main__':
    main() 