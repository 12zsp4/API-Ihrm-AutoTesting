import unittest
import os
from htmltestreport import HTMLTestReport
from SelfStudy.FrameWork.apiAutoFramworkIhrm.scripts.test_ihrm_login import TestIhrmLogin
from SelfStudy.FrameWork.apiAutoFramworkIhrm.scripts.test_ihrm_RolesCurd import TestIhrmRoles

# 1. 创建测试套件
suite = unittest.TestSuite()

# 2. 加载测试用例（现代写法）
loader = unittest.TestLoader()
suite.addTests(loader.loadTestsFromTestCase(TestIhrmLogin))
suite.addTests(loader.loadTestsFromTestCase(TestIhrmRoles))

# 3. 配置报告路径
report_dir = r'D:\Python\pythonProject\SelfStudy\FrameWork\apiAutoFramworkIhrm\report'
os.makedirs(report_dir, exist_ok=True)  # 确保目录存在
report_file = os.path.join(report_dir, 'ihrm_report.html')

# 4. 运行测试
runner = HTMLTestReport(
    report_file,  # 必须是文件路径
    description='IHRM系统自动化测试报告',
    title='IHRM测试结果'
)
runner.run(suite)