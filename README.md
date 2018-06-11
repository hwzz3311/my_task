### 三级菜单设计思路

- 编译环境：Python 2.7
- 创建一个多层嵌套的字典作为菜单的存储
- 使用while循环创建循环体，创建province变量用于接收用户输入的以及菜单，判断用户输入的一级菜单是否存在，如果一级菜单不存在本次循环结束，让用户重新输入，如果存在则进入二级菜单循环体，如果为退出关键字则跳出循环体，程序结束
- 二级菜单循环体内创建ciry变量用于接收用户输入的二级菜单，判断用户输入的二级菜单是否存在，如果二级菜单存在则打印对应的三级菜单，本次循环结束，如果二级菜单不存在，本次循环结束，如果用户输入为退出二级菜单关键字则跳出二级菜单循环体，返回一级菜单循环体。
![](https://github.com/hwzz3311/my_task/blob/master/three_level_menu.png)

### 二分法设计思路
- 编译环境：Python 3.6
####第一种思路：
- 先得到list的总长度确定范围，然后判断关键字是否存在list中，不存在直接返回没有找到
- 然后的到中间值，要查找的关键字和中间值比较
- 就可以得到关键字的新范围
- 一直重复这个操作直到找到关键字的索引值
####第二种思路：
- 从外部传入list和关键字list的范围(min,max)
- 函数内接受只执行比大小
- 并返回新的list范围(new_min,new_max)
- 再次调用二分法函数
- 这次传入的list和关键字不变，list的范围(new_min,new_max)
- 重复这些操作
- 然后将代码优化为递归，递归主要是将接受到的new_min,new_max传入下次函数调用