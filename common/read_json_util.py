# import json
# def load_test_data():
#     list_data=[]
#     # 加载 login1_data.json 文件
#     # file_path = r'D:\Python\pythonProject\SelfStudy\FrameWork\apiAutoFramworkIhrm\data\login1_data.json'
#     with open('../data/login1_data.json','r', encoding='utf-8') as file:
#     # with open(file_path,'r', encoding='utf-8') as file:
#         data = json.load(file)
#     # 将数据转换为元组列表，以适配 parameterized.expand
#         for item in data:
#             tmp=tuple(item.values())
#             list_data.append(tmp)
#     return list_data
#
#


import json


def load_test_data(file_path: str) -> list:
    """
    从 JSON 文件加载测试数据，并将其转换为元组列表。

    :param file_path: JSON 文件的路径
    :return: 返回一个元组列表，每个元组表示一个测试用例
    """
    list_data = []

    try:
        # 打开并读取 JSON 文件
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

            # 将数据转换为元组列表
            for item in data:
                tmp = tuple(item.values())
                list_data.append(tmp)
    except FileNotFoundError:
        print(f"错误：文件 {file_path} 未找到。")
    except json.JSONDecodeError:
        print("错误：文件内容无法解析为有效的 JSON 格式。")
    except Exception as e:
        print(f"发生错误：{e}")

    return list_data

