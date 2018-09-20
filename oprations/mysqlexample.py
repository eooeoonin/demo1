#!/usr/bin/env python
#coding=utf-8

import time,traceback,logging,pymysql

class DBOperateAction:
    def __init__(self,dbhost,dbaccount,dbpasswd,dbname,port=3306,charset="utf8"):
        self.dbhost=dbhost
        self.dbaccount=dbaccount
       # self.dbpasswd=dbpasswd[::-1]   #翻转字符串
        self.dbpasswd = dbpasswd
        self.dbname=dbname
        self.charset=charset
        self.port=port
        self.db_conn=""
        self.db_cursor=""
    
    def connect(self):
        try:
            self.db_conn=pymysql.connect(host=self.dbhost,user=self.dbaccount,passwd=self.dbpasswd,
                                        db=self.dbname,port=self.port,charset=self.charset, connect_timeout = 30)
            self.db_cursor=self.db_conn.cursor()    #获得游标
            return True
        except pymysql.OperationalError:
            logging.error("Connect to "+self.dbhost+" Failed")
            logging.exception("exception message:")
            return False

    def re_connect(self):
        logging.error("connect to mysql server failed, reconnect")
        try:
            self.db_conn=pymysql.connect(host=self.dbhost,user=self.dbaccount,passwd=self.dbpasswd,
                                         db=self.dbname,port=self.port,charset="utf8")
            self.db_cursor=self.db_conn.cursor()
            return True
        except pymysql.OperationalError:
            logging.error("Reconnect MySQL failed")
            return False

        
    def get_all_result(self,sql):
        try:
            #logging.info("Execute sql: "+sql[:500])
            logging.info("Execute sql: "+sql)
            self.db_cursor.execute(sql)
            self.db_conn.commit()
            result=self.db_cursor.fetchall()
            return result
        except pymysql.OperationalError:
            for i in range(0,3):
                time.sleep(5)
                if self.re_connect():
                    logging.info("reconnect to "+self.dbhost+"database successfully")
                    return False
        except pymysql.ProgrammingError:
            logging.exception("exception message:")
            return False
    
    def get_one_result(self,sql):
        try:
           logging.info("Execute sql: "+sql[:500])
           self.db_cursor.execute(sql)
           self.db_conn.commit()
           result=self.db_cursor.fetchone()
           return result
        except pymysql.OperationalError:
            traceback.print_exc()
            for i in range(0,3):
                time.sleep(5)
                if self.re_connect():
                    self.db_cursor.execute(sql)
                    self.db_conn.commit()
                    result=self.db_cursor.fetchone()
                    logging.warn("Reconnect to "+self.dbhost+" successfully")
                    return result
            return False
    def close_connection(self):
        self.db_conn.close()

if __name__=="__main__":

    host = "180.76.50.253"
    db_account = "root"
    db_passwd = "root"
    db_name = "user"

    db_operation = DBOperateAction(host, db_account, db_passwd, db_name)
    db_conn =db_operation.connect()

    select_sql="INSERT INTO `user`.`t_wx_info` VALUES ('20180920000000000000000000000003', '003', '20180914C064330000000000000000BT', NULL, " \
               "'QOWWlOWWlFlZ', 'WOMAN', NULL, '朝阳', '中国', 'http://thirdwx.qlogo.cn/mmopen/vi_32/Gm43xPqia7POib3kvPYkKa6axVM6Tqd5wRCXqvL5xDKUk7Ctyiaia8cBJTcuprr3vqeyaUoMG4NZOib4zgUsibR0LbmQ/132'," \
               " NULL, 'oXsBKwJCmzZOalFmFi436YVBTvKs', '13_bkuW7cV_BD2W9H8Kxq6FcT07gATOaBMzp_rrsKK04rTj_IAf-TX1q13H_EXkn7F-vLQrP9ZZfyFPetpux42qzOQONqeyKkMPKnBr0DNHXgI', " \
               "NULL, NULL, 'snsapi_userinfo', NULL, '0', NULL, NULL, '2018-09-14 15:47:03', '2018-09-14 15:57:52');"
    print(select_sql)
    #results=db_operation.get_all_result(select_sql)

    select_sql="select c_id,c_openid from t_wx_info where c_user_id='20180914C064330000000000000000BT'"
    print(select_sql)
    results=db_operation.get_all_result(select_sql)
    print("get_all_result:", results)
    results=db_operation.get_one_result(select_sql)
    print("get_one_result:", results)

    db_operation.close_connection()
