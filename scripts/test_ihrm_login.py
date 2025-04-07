import unittest
from parameterized import parameterized
from SelfStudy.FrameWork.apiAutoFramworkIhrm.api.ihrm_login_api import IhrmLoginApi
from SelfStudy.FrameWork.apiAutoFramworkIhrm.common.assert_util import common_assert
from SelfStudy.FrameWork.apiAutoFramworkIhrm.common.read_json_util import load_test_data

class TestIhrmLogin(unittest.TestCase):
    # 使用从 JSON 文件加载的数据进行参数化
    # @parameterized.expand是一个装饰器，用来实现 参数化测试，即在同一个测试方法上运行多组数据。
    data_path=r'D:\Python\pythonProject\SelfStudy\FrameWork\apiAutoFramworkIhrm\data\login1_data.json'
    @parameterized.expand(load_test_data(data_path))
    def test_login(self, name, json_data, expected_status, expected_success, expected_code, expected_message):
        """
               登录测试方法，使用从 JSON 文件加载的测试数据
        """
        # 调用自己封装的接口
        resp = IhrmLoginApi().login(json_data)
        print(f"Test {name} response: ", resp.json())

        # 断言
        common_assert(self, resp, expected_status, expected_success, expected_code, expected_message)





    # # 手机号为空
    # def test02_login_mobile_none(self):
    #     # 组织请求数据
    #     json_data = {"mobile": "", "password": "hm#qd@23!"}
    #     # 调用自己封装的接口
    #     resp = IhrmLoginApi().login(json_data)
    #     print("手机号为空", resp.json())
    #
    #     # 断言
    #     common_assert(self,resp,200,False,10000,'用户名或密码不能为空')
    #
    #
    # # 密码错误
    # def test03_login_password_false(self):
    #     # 组织请求数据
    #     json_data = {"mobile": "13800000002", "password": "hmqd@23!"}
    #     # 调用自己封装的接口
    #     resp = IhrmLoginApi().login(json_data)
    #     print("密码错误", resp.json())
    #
    #     # 断言
    #     common_assert(self,resp,200,False,10000,'用户名或密码错误')