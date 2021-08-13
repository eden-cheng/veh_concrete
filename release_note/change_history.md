# Change HIstory

## 0316（程伟）

1. 调整了case库文件的格式，比如
      1）区分实车测试和HILL测试的推荐测试
    2）推荐参数区分为odd和action
    3）将action和通过条件部分，从格式上往前移，避免后期tag频繁变更，需要调整行列关系
2. yaml中调整
    1）调整了relation.yaml中的行列对应关系；
    2) 原para改为para_odd和para_action；
    3）para_odd部分“1% uphill”改为“1%”，“500m curve”改为“500m“；
3， 代码调整
    1）针对上面的yaml调整，对rule.py做修改；
    2）原先para_action部分也采用追加形式，现在修改为参数替换replace的方式。前一种方式，不同case需要不同的追加描述，后者适应性更好;
    3）通过上一步的改进，rule.py的适用性更好，不仅可以使用cc,而且可以使用ilc

## 0317（程伟）

1. ralation.yaml 中增加了case
2. concrete_cc.py 增加了判断，如果relation.yaml中缺少了某个case，依然可以正常输出
3. concrete_cc.py 中对case的遍历，采用了for循环的方式
4. 调整了参数yaml的格式，将空载，无目标，轿车目标，卡车目标等前提因素单独作为一个yaml

## 0318（程伟）

1.为了满足同一个case，在同一个弯道或坡道odd下，不同曲率或不同坡度情况下，对action参数做不同程度展开。
  这里的group体现的时不同odd参数与不同action参数之间的绑定关系 
  调整了参数yaml的结构，原来para_action,para_odd,geo_tag。调整为para_group: [group1: [para_odd, para_action], group2: [para_odd, para_action]]
2.因为上面的更改，原本对“平直路”的设计也需要做调整，新增default的tag
3.将坡道的1%，3%，5%和500m,700m, 900m替换为汉语的程度表达

## 0319（程伟）

1. 调整了文件名和目录结构，cc实例化和ilc实例化分别归在两个目录下
2. 将原tool文件下的两个类，拆分成了Tool类和veh_expand类
3. 将cc_prerequiste.yaml的文件路径，放到file.yaml中，便于后期维护

## 0322（程伟）

1. 新增了rm,keywords列
2. 参数yaml中去除了tag，实际上para_group也可以去掉，但是后面在仿真部分这个结构可能还是有用的，但是不做调整
3. 将输出列的顺序调整到了relation.yaml中，方便调整和修改

## 0323（程伟）

1. 增加了case库的parser功能，可以自动化对表格行标题和列标题与行列做对应，在lib_form_parser文件夹
2. 调整了目录结构和命名，使其看起来更加条理清晰
3. 增加自动化生成特征参数yaml的功能

## 0324（程伟）

1. 删除了para_group
2. 将file_path.yaml， other.yaml转移出来
3. yaml_generate方法中增加了对路径的判断，如果没有文件夹会自动创建

## 0406（程伟）

1. 调整了目录结构
2. 把tool.yaml转移到parser文件夹下
3. 自动生成prerequisite.yaml， relation.yaml
4. 为什么para的行列只到cc_5，debug
5. 自动生成 case_group.yaml
6. 生成的表格，不要分成多个excel，作为多个表单放在一个表格中
7. 简化 ex_veh_method/veh_feature_f.py