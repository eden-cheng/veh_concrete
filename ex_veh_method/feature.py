from ex_veh_method import case
from general_tool import yaml_parser
from general_tool import excel_parser
from parser_tool import lib_para_parser
from parser_tool import col_row_parser
import openpyxl

yaml_path_file = "file_path.yaml"
relation = "./parser_tool/relation.yaml"
file_path = "./parser_result/"

class Feature_ex():
    def __init__(self, lib_path, feature):
        self.e_obj = excel_parser.Excel()
        self.y_obj = yaml_parser.Parser()

        self.wb_lib = openpyxl.load_workbook(lib_path)
        self.feature = feature

        self.dic = {}

    def test(self):
        print('@@@@@@@@@@@@@ ', self.feature, ' is parsering @@@@@@@@@@@@')
        
        #1）对case库和para库做行列解析；2）提取para库中的参数
        self.func01(self.feature, 'case_lib', 'para_recommend_lib')
        
        # #将多个准备文件的yaml地址放到一个yaml中
        # catalogue_file = self.feature + '_catalogue.yaml'
        # self.y_obj.yaml_generate(self.dic, file_path, catalogue_file)
        
        # #1）创建excel；2）解析或展开后的内容，写入excel中
        # output_name = self.feature + '_veh_temp.xlsx'
        # para_yaml_key = Self.feature + '_values'
        # self.func02(self.feature, 'case_lib', output_name, para_yaml_key)


    def func01(self, feature, case_ws_name, para_ws_name):
        """
        目的：
        1）对case库做行列解析，生成两个yaml，一个行yaml，一个列yaml；
        2）对para库做行列解析，生成两个yaml，一个行yaml，一个列yaml。后面只用行yaml；
        3）将para库中参数做提取，生成若干个yaml，para参数表中填了多少odd，就生成多少个yaml；
        4）将上面的yaml地址汇总到 self.dic，后面会将地址放到yaml里
        """
        #实例化各种类
        cr_obj = col_row_parser.Parser()
        #step1：获取场景库和参数库
        ws_lib = self.wb_lib[case_ws_name]
        ws_para =  self.wb_lib[para_ws_name]
        #step2：对场景库和参数库的行列关系做解析        
        cr_obj.func(ws_lib, feature, 'case')
        cr_obj.func(ws_para, feature, 'para')
        #step3: 参数库由excel转化为yaml
        obj = lib_para_parser.Parser(ws_para, feature)
        obj.para_group_to_yaml()


        for key, value in cr_obj.dic.items():
            self.dic[key] = value

        for key, value in obj.dic01.items():
            self.dic[key] = value
        print(self.dic)

    def func02(self, feature, case_ws_name,  file_name, yaml_group):
        """
        1）创建excel
        2）解析或展开后的内容填入excel
        """
        ws_lib = self.wb_lib[case_ws_name]
         #step4: 创建输出文件excel的路径，表格，文件名
        out_path = (self.y_obj.yaml_manage(yaml_path_file))['out_path']
        self.e_obj.create_folder(out_path)
        wb = self.e_obj.wb_new()
        file_name = out_path + file_name
        #step5：外层循环是空载，满载，卡车目标
        #前面将参数库从excel提取到yaml，这里将yaml的内容以字典的形式取出
        veh_value = self.y_obj.charact_value(yaml_group)
        for key,value in veh_value.items():
            # print(key)
            #对不同odd做展开
            obj = case.Case_ex(feature, ws_lib, key, value)
            obj.case_ex()
            arr = obj.ex_obj.arr    #将case展开成字典格式
            # print(arr)
            self.e_obj.import_data(wb, file_name, arr, key, feature)    #写入excel中