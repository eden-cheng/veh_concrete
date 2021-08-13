六层嵌套满足不同筛选需求

1. 实车或仿真需求层：

   举例：veh_test还是hill_test

   实现：mian函数中做调用

   ![img](file:///C:/Users/siqi.shen/Documents/WXWork/1688851038247614/Cache/Image/2021-03/企业微信截图_16165919919401.png)

2. feature层：

   举例：比如cc,ilc

   实现：通过函数调用或不调用

   ![image-20210325103257995](C:\Users\siqi.shen\AppData\Roaming\Typora\typora-user-images\image-20210325103257995.png)

3. odd层：

   举例：对空载，满载，无目标，轿车目标，卡车目标做展开。

   实现：通过遍历预设的参数yaml文件夹

   ![img](file:///C:/Users/siqi.shen/Documents/WXWork/1688851038247614/Cache/Image/2021-03/企业微信截图_1616593154543.png)

4. case一级目录：

   举例：比如cc_3

   实现：通过函数调或不调用

   ![img](file:///C:/Users/siqi.shen/Documents/WXWork/1688851038247614/Cache/Image/2021-03/企业微信截图_16165930418086.png)

5. case二级目录：

   举例：比如noload时候，cc_3_1, cc_3_2，但是在payload时候只有cc_3_2或者没有cc_3的case

   实现：根据yaml中预设项筛选

   ![image-20210325103456627](C:\Users\siqi.shen\AppData\Roaming\Typora\typora-user-images\image-20210325103456627.png)

6. 单个case的参数层：

   举例：比如3%常规坡道情况下，需要对20、40、60kph做测试，但是5%大坡道情况下，仅对40kph做展开。

   实现：根据yaml中不同odd参数与action参数的绑定关系

![img](file:///C:/Users/SIQI~1.SHE/AppData/Local/Temp/企业微信截图_16165954096815.png)