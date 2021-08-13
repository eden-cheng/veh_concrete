# ReadMe

## 功能规划：

1. 将 **case库** 展开成 **实车测试** 所需的 **可执行具体case** ，满足多种定制化的需求；（doing）
2. 将 **case库** 展开成 **仿真** 所需的具体case，与VTD实现对接；（to do）
3. 将 **case库** 展开成 **case全集**；（to do）
4. **自动化统计**。既对case库，实车具体case，仿真具体case，case全集等case数量做统计, 又对参数，odd等做统计；（to do）
5. 绑定tag，待定（to do）



## 特点：

1. 六层嵌套满足不同筛选需求，比如：实车or仿真，不同feature，不同case，不同odd
2. 对原始case库的行列关系做解析并生成yaml，为把行列关系写死在代码内，便于变更维护
3. 满足实车测试不同场地，odd，feature，参数组合等定制化需求，采用“特征参数概念，建立特征参数库，并可以从excel解析成yaml格式供代码调用
5. 广泛使用yaml做配置文件，可以方便修改文件路径，标题顺序，行列关系等
5. 便于后续扩展



## 六层嵌套满足不同筛选需求

### **1st: 实车或仿真需求层：**

举例：veh_test还是hill_test
实现：mian函数中做调用

### 2nd: feature层：

举例：比如cc,ilc
实现：通过函数调用或不调用

### 3nd: odd层：

举例：对空载，满载，无目标，轿车目标，卡车目标做展开。
实现：通过遍历预设的参数yaml文件夹

### 4th: case一级目录：

举例：比如cc_3
实现：通过函数调或不调用

### 5th: case二级目录：

举例：比如noload时候，cc_3_1, cc_3_2，但是在payload时候只有cc_3_2或者没有cc_3的case
实现：根据yaml中预设项筛选

### 6th: 单个case的参数层：

举例：比如3%常规坡道情况下，需要对20、40、60kph做测试，但是5%大坡道情况下，仅对40kph做展开。
实现：根据yaml中不同odd参数与action参数的绑定关系
备注：除了上面的几层嵌套，还有yaml本身的嵌套关系。后续看看是否可以做些简化。



## 要求：

### 对case库

1. summary中待替换的参数名，一定要与yaml中参数名保持一直
2. 标题名一定要与输出文件的other.yaml中的标题统一（待定）
3. 统一用 _ 避免用 - ，多个单词之间，尽量用_连接；

### 对yaml

3. para，para_action，para_odd中即使没有是空的，也要写



## 参数yaml结构

para:
   group1:
      para_action:
         tv_initial:
         tv_target:
         tv_acc:
      para_odd:
         deault:
         uphill:
         downhill:
         curve:
   group2:
      para_action:
      para_odd:
tag:
   geo:['default','uphill','downhill','curve']

说明：在实车测试中，tag部分并未起作用，但是在仿真里面可能有用，所以这个结构暂时不做调整