import requests


class TokenFetcher(object):
    @classmethod
    def get_token(cls, mobile, password):
        """
        获取登录 Token
        :param mobile: 用户名
        :param password: 密码
        :return: 返回获取的 token，如果请求失败则返回 None
        """
        # 登录接口 URL
        url = "https://heimahr.itheima.net/api/sys/login"

        # 请求头，设置 Content-Type 为 application/json
        headers = {"Content-Type": "application/json"}

        # 请求体数据
        data = {
            "mobile":mobile,
            "password":password
        }

        # 发送 POST 请求，获取响应
        try:
            resp = requests.post(url=url, headers=headers, json=data)

            # 判断响应状态码是否为 200，表示请求成功
            if resp.status_code == 200:
                # 如果响应成功，提取 token 并返回
                response_json = resp.json()
                if "data" in response_json:
                    return response_json["data"]
                else:
                    print("错误：响应中没有 data 字段")
                    return None
            else:
                print(f"错误：请求失败，状态码 {resp.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"请求异常：{e}")
            return None

#
# # 示例用法
# if __name__ == '__main__':
#     # 输入用户名和密码
#     mobile = "13800000002"  # 替换为你的用户名
#     password = "hm#qd@23!"  # 替换为你的密码
#
#     # 获取 Token
#     token = TokenFetcher.get_token(mobile, password)
#
#     if token:
#         print(f"成功获取 Token: {token}")
#     else:
#         print("获取 Token 失败")
