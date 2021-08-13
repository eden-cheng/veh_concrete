from general_tool import yaml_parser
from ex_veh_method import case_expand

parser_path = 'parser_result/catalogue.yaml'

class Case_ex():
    def __init__(self, feature, ws, yaml_title, yaml_content):
        #提取relations yaml中的行列对应关系
        self.y_obj = yaml_parser.Parser()
        self.feature = feature
        # row_name = feature + '_lib_row'
        # feature_row = self.y_obj.yaml_path()[row_name]
        feature_row = self.y_obj.yaml_manage(parser_path)[feature + '_case_relation'][feature + '_case_row']
        # print(feature_row)        
        self.row_relation = self.y_obj.yaml_manage(feature_row)
        #实例化yaml_parser文件中的Tool类，方便后面调用case的展开方法
        self.ex_obj = case_expand.Expand(ws, yaml_title, yaml_content)

    def func(self, name):
        if name in self.row_relation.keys():
            print(name)
            relation = self.row_relation[name]
            self.ex_obj.expand_group(relation, self.feature)

    def case_ex(self):
        for i in range(1, 200):
            # print(self.feature + '_' + str(i))
            self.func(self.feature + '_' + str(i))