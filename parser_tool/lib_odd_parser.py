from general_tool import yaml_parser
from general_tool import excel_parser

relation = "relation.yaml"
file_path = "./parser_result/"
file_name = "odd_pre.yaml"

"""
用途：将odd表格中的内容提取到yaml，供后面使用
传入参数：无
输出：odd_pre.yaml文件
说明：比如键 noload_none，对应的值为列表 [load,illumination, tv, speed_limit]
"""

class Parser:
    def __init__(self):
        self.y_obj = yaml_parser.Parser()
        e_obj = excel_parser.Excel()
        odd_path = self.y_obj.yaml_path()['odd_path']
        self.wb = e_obj.wb_get(odd_path)

    def oddpre_to_yaml(self):
        ws = self.wb['odd_pre']
        columns = self.y_obj.yaml_manage(relation)['lib_odd']
        flag = 1
        num = 2
        arr = {} 
        while flag:
            group_name = ws.cell(row = num, column = 1).value
            temp = {}
            for key,value in columns.items():
                # print(key)
                # print(value)
                cell = ws.cell(row = num, column = value)
                if cell.value:
                    temp[key] = cell.value
                else:
                    # print('空白')
                    flag = 0
                    break
            if group_name:
                arr[group_name] = temp
                num += 1
        # print(arr)
        self.y_obj.yaml_generate(arr, file_path, file_name)
