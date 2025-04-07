import unittest
from parameterized import parameterized
from SelfStudy.FrameWork.apiAutoFramworkIhrm.api.ihrm_login_api import IhrmLoginApi
from SelfStudy.FrameWork.apiAutoFramworkIhrm.common.assert_util import common_assert
from SelfStudy.FrameWork.apiAutoFramworkIhrm.common.read_json_util import load_test_data
from SelfStudy.FrameWork.apiAutoFramworkIhrm.config import BASE_DIR
# from SelfStudy.FrameWork.apiAutoFramworkIhrm.common.log_util import get_logger

class TestIhrmLogin(unittest.TestCase):
    # 使用从 JSON 文件加载的数据进行参数化
    # @parameterized.expand是一个装饰器，用来实现 参数化测试，即在同一个测试方法上运行多组数据。
    data_path=BASE_DIR +'\data'+'\login1_data.json'
    print(data_path)
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
