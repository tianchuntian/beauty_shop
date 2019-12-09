'''
run_case.py
1.将需要执行的测试用例,添加到测试套件中
2.将用例执行结果生成HTML格式的测试报告
HTMLTestRunnerPlugins.py文件放置在python安装目录中的Lib目录中
备注:
    run_case.py运行结果三种
    ok  表示用例执行通过
    F   表示用例执行失败
    E   表示代码错误
'''
import time
import unittest
import HTMLTestRunnerPlugins
# 1确定测试用例存放路径
case_path='./script'
# 2将测试文件夹中的测试用例添加到测试套件中
discover = unittest.defaultTestLoader.discover(case_path,pattern="test_*.py")

# 执行测试用例并生成测试报告
#     1确定测试报告存放路径
report_path = './report'
#     2确定测试报告名称
now = time.strftime('%Y_%m_%d %H-%M-%S')
# 测试报告文件名
report_file = report_path +"/" +now+'report.html'
# 打开文件并写入
with open(report_file,'wb') as fp:
    runner = HTMLTestRunnerPlugins.HTMLTestRunner(
        title='ECShop项目web自动化测试报告',
        description='ECShops回顾测试',
        stream=fp)
    runner.run(discover)
    # ok  表示用例执行通过   正常
    # F   表示用例执行失败   正常
    # E   表示代码错误      失败



