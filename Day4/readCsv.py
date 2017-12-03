# 读取csv文件:新建一个date包,右键选择Show in Explorer,找到date文件夹,在文件夹中新建一个excle,填写用例,另存为为.csv格式,然后在以记事本方式打开该文件,编辑后保存即可;此时date包里就会出现2个文件;
import csv # 导包
path = r"E:\Weekend112\date\member_info.csv" # 读取文件路径,r表示反斜杠是普通字符,不是转义字符
file = open(path, 'r') # 打开文件
date_table = csv.reader(file) # 通过csv去读内容,返回数据到数据表date_table

# 遍历date_table,分别打印每一行数据
for row in date_table:
    print(row)

