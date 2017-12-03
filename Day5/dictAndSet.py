# dict 是字典的缩写,用大括号表示{}
# set 是集合的缩写,用大括号表示{}
# python中的元祖用小括号表示()
# python的列表用中括号表示[]
# 描述一个学生信息
# 元组
stu = ("001","小猫","男",23)
# 列表
stu = ["001","小猫","男",23]
# 元组和列表的区别:1.元组是只读,不能修改; 2.列表是可以进行增删改查的,是最常用饿数据格式
# 元组和数组的区别:1.数组可以修改元素内容,不能增加和删除;2.数组中的所有元素的类型都一样;3.元组只读,元素的类型不固定
# find_elements()返回的就是列表

# 集合
stu = {"001","小猫","男",23}
# 元组和集合的区别:1.集合是无序的,不能用下标(索引)的方式查找元素;2.集合是不可重复的,重复的元素自动清除

#字典
stu = {"id":"001","姓名":"小猫","性别":"男","年龄":23}
#字典和集合的区别:1.字典冒号前面的部分叫Key值,后面的部分叫value;2.集合中的key不能重复.value可以重复
# 打印集合中的id值
print(stu['id'])