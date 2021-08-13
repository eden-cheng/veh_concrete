from ex_veh_method import feature
from parser_tool import lib_odd_parser

from ex_veh_method import case
from general_tool import excel_parser
from general_tool import yaml_parser
from parser_tool import lib_para_parser
from parser_tool import col_row_parser
import openpyxl
import gather

y_obj = yaml_parser.Parser()
e_obj = excel_parser.Excel()
cr_obj = col_row_parser.Parser()
para_obj = lib_para_parser.Parser()

def func_relation():
    path_dic = {}
    for key, content in case_list.items():
        path = content['path']
        feature_name = content['feature']
        print(feature_name, ' is parsering column and row relation')

        wb = openpyxl.load_workbook(path)
        ws_case = wb['case_lib']
        ws_para = wb['para_recommend_lib']
        
        # 解析case表的行列，生成一个行关系yaml，一个列关系yaml
        cr_obj.func(ws_case, feature_name, 'case')
        # 解析para表的行列，生成一个行关系yaml，一个列关系yaml
        cr_obj.func(ws_para, feature_name, 'para')
        # 解析para表，将其中每组odd参数生成若干yaml
        para_obj.para_group_to_yaml(ws_para, content['feature'])

    for key, value in cr_obj.dic.items():
        path_dic[key] = value

    for key, value in para_obj.dic01.items():
        path_dic[key] = value

    catalogue_file = 'catalogue.yaml'
    catalogue_path = "./parser_result/"
    y_obj.yaml_generate(path_dic, catalogue_path, catalogue_file)

def func(wb_lib, feature_name, case_ws_name,  output_file_name, yaml_group_key):
    """
    1）创建excel
    2）解析或展开后的内容填入excel
    """
    yaml_path_file = "file_path.yaml"

    ws_lib = wb_lib[case_ws_name]
    # 创建输出文件excel的路径，表格，文件名
    out_path = (y_obj.yaml_manage(yaml_path_file))['out_path']
    e_obj.create_folder(out_path)
    wb = e_obj.wb_new()
    file_name = out_path + output_file_name
    # 外层循环是空载，满载，卡车目标
    # 前面将参数库从excel提取到yaml，这里将yaml的内容以字典的形式取出
    veh_value = y_obj.charact_value(yaml_group_key)
    for key,value in veh_value.items():
        print("#### odd: ", key)
        #对不同odd做展开
        obj = case.Case_ex(feature_name, ws_lib, key, value)
        obj.case_ex()
        arr = obj.ex_obj.arr    #将case展开成字典格式
        # print(arr)
        e_obj.import_data(wb, file_name, arr, key, feature_name)    #写入excel中



case_list = y_obj.yaml_manage('case_list.yaml')
# print(case_list)

#对odd表格做解析，生成文件 parser_result/odd_pre.yaml，供后面调用
obj = lib_odd_parser.Parser()
obj.oddpre_to_yaml()

print('@@@@@@@@@@@ start parsering column and row relation @@@@@@@@@@@@@@@')
func_relation()    #调试时可以注释

print('\n@@@@@@@@@@@ start generating testcase @@@@@@@@@@@@@@@')

for key, content in case_list.items():
    path = content['path']
    feature_name = content['feature']
    wb_lib = openpyxl.load_workbook(path)
    output_name = feature_name + '_veh_temp.xlsx'
    yaml_group_key = feature_name + '_values'
    print(feature_name, ' is generating testcase')
    func(wb_lib, feature_name, 'case_lib', output_name, yaml_group_key)

print('\n@@@@@@@@@@@ start composing @@@@@@@@@@@@@@@')

for key, content in case_list.items():
    path = content['path']
    feature_name = content['feature']
    print(feature_name, ' is composing ')
    g_obj = gather.Gather(feature_name)
    g_obj.func()