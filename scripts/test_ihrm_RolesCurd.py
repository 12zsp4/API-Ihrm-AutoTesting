import unittest
from parameterized import parameterized
from SelfStudy.FrameWork.apiAutoFramworkIhrm.api.ihrm_RolesCurd_api import IhrmRolesApi
from SelfStudy.FrameWork.apiAutoFramworkIhrm.common.assert_util import common_assert
from SelfStudy.FrameWork.apiAutoFramworkIhrm.common.read_json_util import load_test_data

class TestIhrmRoles(unittest.TestCase):
    role_id = None  # 类变量，用于共享role_id
    # 添加角色
    data_path=r'D:\Python\pythonProject\SelfStudy\FrameWork\apiAutoFramworkIhrm\data\addRoles_data.json'
    @parameterized.expand(load_test_data(data_path))
    def test01_add_roles(self,json_data,status_code,success,code,message):
        # 添加角色的请求数据
        # json_data = {"name": "8", "description": "hm#qd@23!", "state": 0}

        # 添加角色
        resp=IhrmRolesApi.addRoles(json_data)
        print(resp.json())
        # 提取并保存role_id到类变量
        TestIhrmRoles.role_id = resp.json().get("data", {}).get("id")
        print("新增角色ID:", self.role_id)
        common_assert(self,resp,200,True,40001,'新增角色成功')


    # 修改角色
    def test02_modify_roles(self):
        update_data = {"id": self.role_id, "name": "12", "state": 0, "description": "hm#qd@23!"}
        update_resp=IhrmRolesApi.updateRoles(update_data,self.role_id)
        print(f"修改后的角色信息: {update_resp.json()}")
        common_assert(self, update_resp, 200, True, 10000, '更新角色详情成功')

    # 删除角色
    def test03_delete_roles(self):
        delete_resp = IhrmRolesApi.deleteRoles(self.role_id)
        print(f"删除角色的响应: {delete_resp.json()}")
        common_assert(self, delete_resp, 200, True, 10000, '删除角色成功')

