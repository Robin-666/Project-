# import pymssql
import pymysql

conn = pymysql.connect(host ='192.168.20.33',port = 3306,user = "root",
                       password = "abcd=1234",database = "oadata")#,charset="utf8"
#获取游标
cursor = conn.cursor()

SQL_Num = "select count(1) from org_member where   IS_ADMIN = 0 and IS_ENABLE = 1 " \
"and IS_DELETED = 0 and ORG_ACCOUNT_ID = -8639625680632198835"

cursor.execute(SQL_Num)#查询操作
Num = cursor.fetchall()
Num_R = str(Num).replace("(","").replace(")","").replace(",","")

print("查询数据为:%s条"%Num_R)
# print(Num_R)
conn.commit()
cursor.close()
conn.close()

