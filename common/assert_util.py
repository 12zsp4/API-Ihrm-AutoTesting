#定义通用断言方法
def common_assert(self, resp, status_code, success, code, message):
    # 断言响应的状态码
    self.assertEqual(resp.status_code, status_code)

    # 断言响应中的 "success" 字段
    self.assertEqual(resp.json().get("success"), success)

    # 断言响应中的 "code" 字段
    self.assertEqual(resp.json().get("code"), code)

    # 断言响应中的 "message" 字段
    self.assertEqual(resp.json().get("message"), message)

