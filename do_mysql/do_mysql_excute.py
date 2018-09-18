#!/usr/bin/python
#coding:utf8

import MySQLdb



class LinkMysql():
    def __init__(self,host,port):
        self.host = host
        self.port = int(port)

    def do_mysql_db_excute_select_one(self):
        db_conn = MySQLdb.connect(host = self.host,port = self.port, user = "root",
                                  passwd = 'mima', db = "db_name",
                                  charset = 'utf8')
        db_cursor = db_conn.cursor()
        sql_select = "select * from park_in where id = 15;"
        db_cursor.execute(sql_select)
        select_data = db_cursor.fetchone()
        print(select_data[0])
        db_conn.close()

    def do_mysql_do_excute_select_all(self):
        db_conn = MySQLdb.connect(host=self.host, port=self.port, user="root",
                                  passwd='mima', db="db_name",
                                  charset='utf8')
        db_cursor = db_conn.cursor()
        sql_select = "select * from project_conf;"
        db_cursor.execute(sql_select)
        select_data = db_cursor.fetchall()
        print(select_data[0])
        db_conn.close()

    def do_mysql_do_update(self):
        db_conn = MySQLdb.connect(host=self.host, port=self.port, user="root",
                                  passwd='mima', db="db_name",
                                  charset='utf8')
        db_cursor = db_conn.cursor()
        update_select = "update park_in set in_time = '2018-09-17 16:00:00' where id = 15 ;"
        db_cursor.execute(update_select)
        db_conn.commit()
        db_conn.close()

    def do_mysql_do_delete(self):
        db_conn = MySQLdb.connect(host=self.host, port=self.port, user="root",
                                  passwd='mima', db="db_name",
                                  charset='utf8')
        db_cursor = db_conn.cursor()
        update_select = "delete from  park_in where id = 15 ;"
        db_cursor.execute(update_select)
        db_conn.commit()
        db_conn.close()





if __name__ == '__main__':
    do_db_object = LinkMysql("192.168.55.57",3306)
    # do_db_object.do_mysql_db_excute_select_one()
    # do_db_object.do_mysql_do_excute_select_all()
    # do_db_object.do_mysql_do_update()
    # do_db_object.do_mysql_do_delete()
