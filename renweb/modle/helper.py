#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql



class User(object):
    def __init__(self,**kwargs):
        self.values = kwargs
        for key, val in kwargs.items():
            setattr(self, key, val)

    def getvalues(self):
        return self.values



class SubManager(object):
    def __init__(self):
        self.conn = self.connect()

    def connect(self):
        return pymysql.connect(host=HOST, port=PORT, user=USER, passwd=PASS, db=DB, charset='utf8')

    def close(self):
        self.conn.close()
        del self.conn

    def commit(self):
        self.conn.commit()

    def get(self,phone,fee_app_code):
        sql = "SELECT * FROM wzcx_sub WHERE MOBILE_SN='{}' and FEE_APP_CODE='{}'".format(phone,fee_app_code)

        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        rows = cursor.execute(sql)
        if rows:
            columns = cursor.fetchone()
            cursor.close()
            return User(**columns)
        cursor.close()
        return None

    def save(self):
        pass

    def uodate(self):
        pass

    def filter(self):
        pass

    def delete(self):
        pass

if __name__ == "__main__":
    a  = SubManager()
    print a.get("13163097213","GENERAL_WZCX_5")


