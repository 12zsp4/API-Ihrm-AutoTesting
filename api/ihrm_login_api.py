import requests
from SelfStudy.FrameWork.apiAutoFramworkIhrm.common.log_util import get_logger # 引入你封装好的日志工具

log = get_logger("login_api")  # 创建一个日志对象

class IhrmLoginApi(object):
    # 登录方法
    @classmethod
    def login(cls, json_data):
        url = "https://heimahr.itheima.net/api/sys/login"
        headers = {"Content-Type": "application/json"}

        log.info("开始执行登录请求")
        log.debug(f"请求地址: {url}")
        log.debug(f"请求头: {headers}")
        log.debug(f"请求数据: {json_data}")

        try:
            resp = requests.post(url=url, headers=headers, json=json_data)
            log.debug(f"响应状态码: {resp.status_code}")
            log.debug(f"响应内容: {resp.text}")
            return resp
        except Exception as e:
            log.error(f"登录请求异常: {e}")
            raise  # 异常抛出方便测试框架捕获
