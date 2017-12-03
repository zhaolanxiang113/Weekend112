# 1.导入pymysql代码库

import pymysql

def connectDb():
    # 1.链接数据库:ip地址.数据库的名称.端口号.用户名和密码等
    conn = pymysql.Connect(host="127.0.0.1", user="root", password="root", database="pirate", port=3306, charset='utf8')
    # 查询hd_user表中所有的数据,并且倒序打印
    sql = "select * from hd_user order by id desc"
    # 在代码中执行这条sql语句,首先要获取数据库中的游标cursor
    curs = conn.cursor()
    # 通过游标来执行sql语句
    curs.execute(sql)
    # 要想获取数据库中最新的记录,首先要把数据库所有记录倒序排列,然后用fetchone()方法取获取第一条最新的记录
    result = curs.fetchone()
    # 想要获取所有的查询结果,用fetchall()
    # result = curs.fetchall()
    return  result

if __name__ == '__main__':
    print(connectDb())