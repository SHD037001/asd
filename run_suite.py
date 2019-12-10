# 创建测试套件
import unittest

from tools.HTMLTestReportCN import HTMLTestRunner

suite = unittest.defaultTestLoader.discover("./scripts")

# 运行测试套件
with open("./report/login.html","wb") as f:
    HTMLTestRunner(f).run(suite)
# unittest.TextTestRunner().run(suite)