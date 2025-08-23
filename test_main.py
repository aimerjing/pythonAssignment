     import subprocess
     import sys
     import re
     
     def test_output():
         """测试程序输出是否为 hello world"""
         # 运行学生的代码
         result = subprocess.run(
             [sys.executable, 'main.py'], 
             capture_output=True,
             text=True,
             timeout=5
         )
         
         # 获取输出内容并标准化
         output = result.stdout.strip().lower()
         
         # 检查输出是否包含 hello world
         assert "hello world" in output, f"输出应为 'hello world'，但实际输出是 '{output}'"
         
         # 检查输出是否只有 hello world（没有额外内容）
         assert re.fullmatch(r"hello world", output), f"输出应仅为 'hello world'，但实际输出是 '{output}'"
