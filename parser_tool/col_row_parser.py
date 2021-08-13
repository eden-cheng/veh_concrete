from openpyxl.descriptors.serialisable import KEYWORDS
from general_tool import yaml_parser
from general_tool import excel_parser
relation = "relation.yaml"

class Parser:
    def __init__(self):
        y_obj = yaml_parser.Parser()
        self.content = y_obj.yaml_manage(relation)
        self.dic = {}

    def func(self, ws_lib, feature, keywords):
        case_first_col = (self.content['lib_' + keywords + '_first'])['id_column']
        case_first_row = (self.content['lib_' + keywords + '_first'])['title_row']
        e_obj = excel_parser.Parser(ws_lib, feature, keywords, case_first_col, case_first_row)
        e_obj.combine()
        self.dic[feature + '_' + keywords + '_relation'] = e_obj.dic

    # def func_para(self, ws_para, feature):
    #     case_first_col = (self.content['lib_para_first'])['id_column']
    #     case_first_row = (self.content['lib_para_first'])['title_row']
    #     e_obj = excel_parser.Parser(ws_para, feature, keywords, case_first_col, case_first_row)
    #     e_obj.combine()
    #     self.dic[feature + '_para_relation'] = e_obj.dic