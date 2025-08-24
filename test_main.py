import subprocess
import sys

def test_output():
    """测试程序输出是否为hello world"""
    try:
        # 运行学生的main.py（使用当前Python环境）
        result = subprocess.run(
            [sys.executable, "main.py"],
            capture_output=True,
            text=True,
            timeout=5 # 防止无限循环
        )
        # 标准化输出（去除空格、小写）
        output = result.stdout.strip().lower()
        # 断言输出是否符合要求
        assert "hello world" in output, f"预期输出'hello world'，实际输出：{output}"
    except Exception as e:
        # 捕获异常并标记测试失败
        assert False, f"测试执行失败：{str(e)}"
