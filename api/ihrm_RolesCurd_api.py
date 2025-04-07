import requests
from SelfStudy.FrameWork.apiAutoFramworkIhrm.common.get_Token_util import TokenFetcher

# 获取 token
token = TokenFetcher.get_token("13800000002", "hm#qd@23!")


class IhrmRolesApi(object):
    # 添加角色
    @classmethod
    def addRoles(cls, json_data):
        url = "https://heimahr.itheima.net/api/sys/role"
        header = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        resp = requests.post(url=url, headers=header, json=json_data)
        return resp

    # 修改角色
    @classmethod
    def updateRoles(cls, json_data,role_id):
        # print(f"调用 updateRoles 方法时传递的 role_id: {role_id}")
        # print(f"调用 updateRoles 方法时传递的 json_data: {json_data}")
        url = f"https://heimahr.itheima.net/api/sys/role/{role_id}"
        header = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        resp = requests.put(url=url, headers=header, json=json_data)
        return resp

    # 删除角色
    @classmethod
    def deleteRoles(cls, role_id):
        url = f"https://heimahr.itheima.net/api/sys/role/{role_id}"
        header = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        resp = requests.delete(url=url, headers=header)
        return resp




# # 示例：如何调用接口
# if __name__ == '__main__':
#     # 添加角色的请求数据
#     json_data = {"name": "13", "description": "hm#qd@23!", "state": 0}
#
#     # 添加角色
#     resp = IhrmRolesApi.addRoles(json_data)
#
#     # 获取新添加角色的 ID（假设成功响应中包含 id）
#     role_id = resp.json().get('data', {}).get('id')
#
#     if role_id:
#         # 示例：修改角色
#         update_data = { "id": role_id,"name": "12","state": 0,"description": "hm#qd@23!"}
#         # update_resp = IhrmRolesApi.updateRoles(update_data, role_id)
#         update_resp = IhrmRolesApi.updateRoles(update_data)
#         print("====",role_id)
#         print(f"修改后的角色信息: {update_resp.json()}")
#
#         # 示例：删除角色
#         delete_resp = IhrmRolesApi.deleteRoles(role_id)
#         print(f"删除角色的响应: {delete_resp.json()}")
#     else:
#         print("添加角色失败，未能获取到角色 ID。")
