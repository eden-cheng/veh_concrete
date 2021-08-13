#实现对参数库的自动化解析
from general_tool import yaml_parser

relation = "relation.yaml"
path_row = "./parser_result/"    
path_test = "./yaml_para"

class Parser():
    def __init__(self):
        # self.ws = ws
        # self.name = name
        # self.file_row = path_row + name +'_para_row.yaml'
        
        self.y_obj = yaml_parser.Parser()

        self.dic01 = {}
        self.dic02 = {}

    def para_group_to_yaml(self, ws, name):
        self.dic = {}
        odd_arr = ['noload_none', 'noload_sedan', 'noload_truck',
                    'payload_none', 'payload_sedan', 'payload_truck',
                    'night_none', 'night_sedan', 'night_truck', 
                    'night_payload_none', 'night_payload_sedan', 'night_payload_truck', 
                    'sedan_sedan', 'sedan_truck', 'truck_truck', 'night_sedan_sedan', 'night_sedan_truck', 'night_truck_truck', 
                    'tunnel_entering', 'tunnel_exiting', 'tunnel_middle',
                    'day_sunny_highway_noload', 'day_sunny_highway_payload', 'day_sunny_tunnel_noload',
                    'dawn_sunny_highway_noload', 'night_sunny_highway_noload', 'night&lamp_sunny_highway_noload',
                    'day_rainy_highway_noload', 'day_heavyrainy_highway_noload',
                    'night&lamp_rainy_highway_noload', 'day_rainy_highway_payload']
        for i in odd_arr:
            self.combin(i, ws, name)
        # str1 = "noload_none"
        # str2 = "noload_sedan"
        # str3 = "noload_truck"
        # self.combin(str1)
        # self.combin(str2)
        # self.combin(str3)
        key01 = name + "_values"
        self.dic01[key01] = self.dic02
        # print(self.dic01)
        self.dic02 = {}
        # print(self.dic)

    def combin(self, string, ws, name):
        if self.action(string, name):
            return self.para_to_yaml(self.action(string, name), self.odd(string, name), string, ws, name)

    def action(self, string, name):
        if name.split('&')[0] in ['CC', 'ILC', 'nudge', 'ALC']:
            temp = self.y_obj.yaml_manage(relation)['basic_para']
            # print(temp)
        elif name.split('&')[0] == 'odd':
            temp = self.y_obj.yaml_manage(relation)['odd_para']
        else:
            # print(name.split('&')[0])
            temp = self.y_obj.yaml_manage(relation)['unbasic_para']
        if (string + '_action') in temp.keys():
            # print("string: ", string)
            # print(temp[string + '_action'])
            return temp[string + '_action']

    def odd(self, string, name):
        if name.split('&')[0] in ['CC', 'ILC', 'nudge', 'ALC']:
            temp = self.y_obj.yaml_manage(relation)['basic_para']
        elif name.split('&')[0] == 'odd':
            temp = self.y_obj.yaml_manage(relation)['odd_para']
        else:
            temp = self.y_obj.yaml_manage(relation)['unbasic_para']
    
        if (string + '_odd') in temp.keys():
            # print("string: ", string)
            # print(temp[string + '_odd'])
            return temp[string + '_odd']

    def para_to_yaml(self, action, odd, string, ws, name):
        result = {}
        temp = {}
        file_row = path_row + name +'_para_row.yaml'
        # print(file_row)
        dic = self.y_obj.yaml_manage(file_row)
        for id_1st in dic:
            temp = dic[id_1st]
            for id_2nd in temp:
                row_num = temp[id_2nd]
                dic_g = {}
                j = 0
                for i in range(5):
                    # print("@@@@@@@@@@@", row_num)
                    # print("@@@@@@@@@@@", action)
                    cell_action = ws.cell(row = row_num, column = action).value
                    cell_odd = ws.cell(row = row_num, column = odd).value
                    row_num += 1
                    #将字符串转化为字典格式
                    dic_action = self.func(cell_action)
                    dic_odd = self.func(cell_odd)
                    #如果action或odd任一不为空
                    if dic_action or dic_odd:
                        j += 1
                        dic_g['group'+str(j)] = self.arrange_para(dic_action, dic_odd)
                if dic_g:
                    result[id_2nd] = dic_g
        # print(result)
        if result:
            file_path =  path_test + "/"
            file_name = name + "_" + string + ".yaml"
            self.y_obj.yaml_generate(result, file_path, file_name)
            #
            key02 = string
            value = file_path + file_name
            self.dic02[key02] = value


    def arrange_para(slef, action, odd):
        temp = {}
        temp['para_action'] = action
        temp['para_odd'] = odd
        return temp

    #将下面形式转化成列表和字典嵌套格式
    #调用三面的三个方法
    # A:1;2;3;
    # B:1;2;
    # C:0;1;2;3;4;
    def func(self, string):
        if not string:    #空白
            return
        arr01 = self.func_arr_01(string)
        dic = {}
        for i in arr01:
            for key,value in self.func_dic(i).items():
                arr = self.func_arr_02(value)
                dic[key] = arr
        return dic

    #将 A：B 字符串转成字典结构
    def func_dic(self, string):
        key = ''
        temp = ''
        dic = {} 
        for i in string:
            if i == ":" or i == "：":
                key = temp
                temp = ''
                continue
            temp += i
        dic[key] = temp
        return dic

    # 将下面形式字符串转换成列表结构
    # a
    # b
    # c
    def func_arr_01(self, string):
        arr = []
        str = ""
        k = 0
        for i in string:
            k += 1
            if i == "\n":
                # print(str)
                arr.append(str)
                str = ""
                continue
            str += i
            if k == len(string):
                arr.append(str)
                break
        return arr

    #将a;b;c;转换成列表结构
    def func_arr_02(self, string):
        arr = []
        temp = ''
        for i in string:
            if i == ';' or i == '；':
                arr.append(temp)
                temp = ''
                continue
            temp += i
        return arr