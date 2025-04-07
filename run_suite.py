# import unittest
# from htmltestreport import HTMLTestReport
# from SelfStudy.FrameWork.apiAutoFramworkIhrm.scripts.test_ihrm_login import TestIhrmLogin
# from SelfStudy.FrameWork.apiAutoFramworkIhrm.scripts.test_ihrm_RolesCurd import TestIhrmRoles
# #创建sutie实例
# suite = unittest.TestSuite()
# #指定测试类，添加，测试方法
# suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestIhrmLogin1))
# #创建HTMLTestReport实例
# runner = HTMLTestReport("测试报告1.html")
#
# #调用run（）传入suite
# runner.run(suite)



import unittest
import time
import os
from htmltestreport import HTMLTestReport
from SelfStudy.FrameWork.apiAutoFramworkIhrm.scripts.test_ihrm_login import TestIhrmLogin
from SelfStudy.FrameWork.apiAutoFramworkIhrm.scripts.test_ihrm_RolesCurd import TestIhrmRoles

# 指定测试报告存放的目录（你自己的绝对路径）
report_dir = r"D:\Python\pythonProject\SelfStudy\FrameWork\apiAutoFramworkIhrm\report"

# 确保目录存在（如果没有就创建）
os.makedirs(report_dir, exist_ok=True)

def generate_test_report(test_case_class):
    """生成单个测试类的报告"""
    report_name = os.path.join(
        report_dir,
        f"测试报告_{test_case_class.__name__}_{time.strftime('%Y%m%d_%H%M%S')}.html"
    )
    suite = unittest.TestLoader().loadTestsFromTestCase(test_case_class)
    runner = HTMLTestReport(report_name)
    runner.run(suite)

if __name__ == "__main__":
    # 为所有测试类生成独立报告
    for test_class in [TestIhrmLogin, TestIhrmRoles]:
        generate_test_report(test_class)
