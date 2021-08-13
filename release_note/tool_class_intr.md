# 工具类介绍

## 通用模块：yaml处理模块

/home/cw/Documents/case/general_tool/yaml_parser.py

### 类1

```python
from general_tool import yaml_parser
#实例化
obj = yaml_parser.Tool()
```

#### 方法1：将yaml生成字典格式

```python
#file_path是待转化的yaml文件
dic = obj.yaml_manage(file_path)    
```

#### 方法2：将内容写入并生成yaml

```python
#将content写入yaml,file_path+name组成文件路径.content可以时列表或字典
obj.yaml_generate(content, file_path, name)	 
```

#### 方法3：获取file_path.yaml中路径

```python
#获取file_path.yaml中的预设的文件路径信息
obj.yaml_path()						
```

#### 方法4：将多个yaml合并成一个字典

```python
#test_name是从file_path.yaml中获取的多个yaml的数组
dic = obj.charact_value(test_name)
```



## 通用模块：excel处理模块

/home/cw/Documents/case/general_tool/excel_parser.py

### 类1

```python
from general_tool import excel_parser
#实例化，ws为待解析表单，name为待生成yaml文件名,首行和首列在relation.yaml中预设
obj = excel_parser.Parser(ws, name1, name2, first_column, first_row)	
```

#### 方法：解析行列关系

生成行列关系的yaml文件

```python
obj.combine()
```

### 类2

```python
from general_tool import excel_parser
obj = excel_parser.Excel()
```

#### 方法1：将列表写入excel

```python
#arr是待写入excel的列表，前面需要将case整理成列表的格式。
#feature+odd组成文件路径，生成excel的表头根据titles.yaml
obj.import_data(wb, file_name, arr, odd, feature)	
```

#### 方法2：从路径获取excel

```python
#file_path是待获取的excel路径
wb = obj.wb_get(file_path)
```

#### 方法3：创建新的excel

```python
wb = obj.wb_new()
```

#### 方法4：创建文件路径

```python
obj.create_folder(file_path)
```



## 专用模块：对para表格做解析

/home/cw/Documents/case/parser_tool/lib_para_parser.py

### 类1

```python
from parser_tool import lib_para_parser
#实例化，ws为特征参数表单，name与yaml_path生成文件路径名，yaml_path在代码中预设的部分文件路径
obj = lib_para_parser.Parser(ws, name)
```

#### 方法：解析特征参数表单

1. 生成转化后的yaml文件
2. 特征参数表单中包含多种odd的特征参数

```python
#解析多种odd，比如noload_none，noload_sedan，payload_none
#解析action和odd特征参数
obj.para_group_to_yaml()		
```



## 专用模块：对odd表格做解析

/home/cw/Documents/case/parser_tool/lib_odd_parser.py

### 类1

```python
from parser_tool import lib_odd_parser
#实例化
obj = lib_odd_parser.Parser()		
```

#### 方法：解析odd_pre表单

1. 生成转化后的yaml文件

```python
#将odd_pre表单内容写入yaml
obj.oddpre_to_yamnl()	
```



## 专用模块：解析case和para的行列关系

/home/cw/Documents/case/parser_tool/col_row_parser.py

### 类1

```python
from parser_tool import col_row_parser
#实例化
obj = col_row_parser.Parser()		
```

#### 方法：解析case和para的行列关系

1. 生成转化后的yaml文件

```python
#ws_lib 和 ws_para 用openpyxl解析后的表格
obj.func_combine(ws_lib, ws_para, feature)
```

