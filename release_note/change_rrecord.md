# change record

## to do

1. 可以对生成后的case做二次整理，生成一张表格

2. 自动生成统计数据，并且生成所有case的

3. 优化类的导入方式

4. 在case.py里面，现在所有case是一个个列出来的，是否需要通过for循环实现，如果通过for循环，如何解决获取特定case的问题

5. 解决大小写,末尾有空格等问题

6. 采用多线程的方式，提高效率

7. 包装成exe

8. 允许接受外部输入

  **高优**：

7. 设计仿真参数库
8. 用正则表达式，对summary解析出英文参数；
9. 确保参数库与场景库统一来源，初级参数库由场景库生成，高级能够显示更新后的增删改查的点
10. 用tkinter设计GUI，实现对para表格的输入，生成表格，筛选等功能

**中优**

11. excel_parser中为了限制无穷循环，设了固定数字，并不长久
12. 参数库中不要固定5行
13. file_path.yaml中自动生成的文件，路径也让自动生成



## Done


1. 开发一个excel转yaml的工具（高优）
2. relation.yaml 中行列关系，通过自动化抓取的方式实现
3. yaml中增加scenario与case对应关系，便于后期根据scenario提取
4. 增加rm号
5. parser文件夹中case_group也通过建立表格，然后自动化生成，目前还需要手动维护
6. 取消para_group这一级
7. lib_case_parser改为行列parser，并且不绑定case的行列
8. 把tool.yaml转移到parser文件夹下
9. 自动生成prerequisite.yaml， relation.yaml
10. 为什么para的行列只到cc_5
11. 自动生成 case_group.yaml
12. 生成的表格，不要分成多个excel，作为多个表单放在一个表格中
13. 简化 ex_veh_method/veh_feature_f.py
14. 更新工具类介绍的部分


测试