# 1.之前的readCsv不能被调用,应该将这段代码封装到一个方法里;
# 2.每个测试用例的路径不同,所以path应该作为参数传入到这个方法中

import  csv
import os


def read(file_name):
    current_file_path = os.path.dirname(__file__)  # 操作系统目录的文件
    # print(current_file__path)
    path = current_file_path.replace("Day4", "date/" + file_name)
    # file = open(path, 'r')
    # with代码块可以字段关闭with中声明的变量file
    result = []   # 声明一个列表保存关闭的数据,作为返回值
    with open(path, 'r') as file:
        date_table = csv.reader(file)
        for row in date_table:
            result.append(row)
            # print(row) # 关闭后数据小时,可以单独声明一个列表叫result,来保存里面的数据,最后返回
    return result

        # 若在打开与关闭程序间的代码发生异常,导致不能执行后续代码,不能关闭文件         ,此时应该用with语句实现关闭;
        # file.close()# 关闭文件,避免程序崩溃


# 调用(通过输入main,然后回车实现)
if __name__ == '__main__':
    # path = r"E:\Weekend112\date\member_info.csv"# 该路径是绝对路径
    # 在代码中自动找到路径的方法:通过当前代码文件路径,根据相对位置找到csv文件;即首先找到当前文件路径(current)

    # current_file_path = os.path.dirname(__file__)# 操作系统目录的文件
    # print(current_file__path)
    # path = current_file_path.replace("Day4", "date/" + file_name)
    # path = current_file_path.replace("Day4", "date/"member_info.csv")
    # print(path)
    member_info = read("member_info.csv")
    # print(member_info) # 打印出的返回值,打印所有的
    for row in member_info:  # 只打印第一行
        print(row[0])
