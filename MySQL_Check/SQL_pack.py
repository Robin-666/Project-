import pymysql


class DB:
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1',
                    port=3306,
                    user='root',
                    passwd='123456',   # passwd 不是 password
                    db='api_test')
        self.cur = self.conn.cursor()
        
    def __del__(self): # 析构函数，实例删除时触发
        self.cur.close()
        self.conn.close()
        
    def query(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()
    
    def exec(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(str(e))
    
    def check_user(self,name):
        result = self.query("select * from user where name='{}'".format(name))
        return True if result else False
        
    def del_user(self, name)
        self.exec("delete from user where name='{}'".format(name))
        
        
        
        
#   SQL语句代码封装
#from db2 import DB:

#db = DB()  # 实例化一个数据库操作对象
#if db.check_user("张三"):
#    db.del_user("张三")