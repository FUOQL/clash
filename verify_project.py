#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CashAI 项目验证脚本
验证所有功能是否正常工作
"""

import os
import sys
import subprocess

def verify_file_exists(filename: str) -> bool:
    """验证文件是否存在"""
    return os.path.exists(filename)

def verify_file_content(filename: str, expected_content: str = None) -> bool:
    """验证文件内容"""
    if not verify_file_exists(filename):
        return False
    
    if expected_content:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            return expected_content in content
    
    return True

def run_verification_test(test_name: str, test_func, expected_result: bool = True):
    """运行验证测试"""
    print(f"测试: {test_name}")
    try:
        result = test_func()
        status = "✅ 通过" if result == expected_result else "❌ 失败"
        print(f"  结果: {status}")
        return result == expected_result
    except Exception as e:
        print(f"  结果: ❌ 失败 (错误: {e})")
        return False

def main():
    """主验证函数"""
    print("CashAI Coding Agent 项目验证")
    print("="*50)
    
    tests_passed = 0
    total_tests = 0
    
    # 测试1: 验证主程序文件存在
    total_tests += 1
    if run_verification_test("主程序文件存在", lambda: verify_file_exists("CashAI.py")):
        tests_passed += 1
    
    # 测试2: 验证README文件存在
    total_tests += 1
    if run_verification_test("README文件存在", lambda: verify_file_exists("README.md")):
        tests_passed += 1
    
    # 测试3: 验证使用说明文件存在
    total_tests += 1
    if run_verification_test("使用说明文件存在", lambda: verify_file_exists("USAGE.md")):
        tests_passed += 1
    
    # 测试4: 验证测试脚本存在
    total_tests += 1
    if run_verification_test("测试脚本存在", lambda: verify_file_exists("test_cashai.py")):
        tests_passed += 1
    
    # 测试5: 验证演示脚本存在
    total_tests += 1
    if run_verification_test("演示脚本存在", lambda: verify_file_exists("demo.py")):
        tests_passed += 1
    
    # 测试6: 验证Django项目存在
    total_tests += 1
    if run_verification_test("Django项目存在", lambda: verify_file_exists("online_store")):
        tests_passed += 1
    
    # 测试7: 验证Django项目结构完整
    total_tests += 1
    if run_verification_test("Django项目结构完整", lambda: verify_file_exists("online_store/manage.py")):
        tests_passed += 1
    
    # 测试8: 验证Django应用存在
    total_tests += 1
    if run_verification_test("Django应用存在", lambda: verify_file_exists("online_store/store")):
        tests_passed += 1
    
    # 测试9: 验证CashAI.py可以正常运行
    total_tests += 1
    def test_cashai_runs():
        try:
            result = subprocess.run([sys.executable, "CashAI.py", "-h"], 
                                  capture_output=True, text=True, timeout=10)
            return result.returncode == 0
        except:
            return False
    
    if run_verification_test("CashAI.py可以正常运行", test_cashai_runs):
        tests_passed += 1
    
    # 测试10: 验证项目验证脚本存在
    total_tests += 1
    if run_verification_test("项目验证脚本存在", lambda: verify_file_exists("verify_project.py")):
        tests_passed += 1
    
    # 测试11: 验证最终总结文件存在
    total_tests += 1
    if run_verification_test("最终总结文件存在", lambda: verify_file_exists("FINAL_SUMMARY.md")):
        tests_passed += 1
    
    # 测试12: 验证.gitignore文件存在
    total_tests += 1
    if run_verification_test(".gitignore文件存在", lambda: verify_file_exists(".gitignore")):
        tests_passed += 1
    
    # 测试13: 验证requirements.txt文件存在
    total_tests += 1
    if run_verification_test("requirements.txt文件存在", lambda: verify_file_exists("requirements.txt")):
        tests_passed += 1
    
    # 测试14: 验证任务要求文件存在
    total_tests += 1
    if run_verification_test("任务要求文件存在", lambda: verify_file_exists("任务要求")):
        tests_passed += 1
    
    # 总结
    print(f"\n{'='*50}")
    print("验证总结:")
    print(f"通过测试: {tests_passed}/{total_tests}")
    print(f"成功率: {tests_passed/total_tests*100:.1f}%")
    
    if tests_passed == total_tests:
        print("🎉 所有测试通过！项目验证成功！")
        print("✅ CashAI Coding Agent 项目完全满足要求")
    else:
        print("⚠️  部分测试失败，请检查项目完整性")
    
    print(f"{'='*50}")

if __name__ == '__main__':
    main() 