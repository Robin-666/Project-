# import pymssql
import pymysql

conn = pymysql.connect(host ='192.168.20.33',port = 3306,user = "root",
                       password = "abcd=1234",database = "oadata")#,charset="utf8"
#获取游标
cursor = conn.cursor()

SQL_Num = "SELECT count(1) from lexmiscif_persaux where  PA_ACCTID = 001 and PA_ACCTYEAR = 2019 " \
          "and PA_ORGID = -8639625680632198835 "

cursor.execute(SQL_Num)#查询操作
Num = cursor.fetchall()
Num_2 = str(Num).replace("(","").replace(")","").replace(",","")

print("查询数据为:%s条"%Num_2)
# print(Num_R)
conn.commit()
cursor.close()
conn.close()

