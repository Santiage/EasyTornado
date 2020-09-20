# -*- coding: utf-8 -*-

from utils.database import db
import dicttoxml


class dbTools:
    @staticmethod
    def db2xml(database:dict):
        # 判断参数是否齐全
        if ('host' not in database.keys() or 'databasename' not in database.keys() or 'username' not in database.keys()):
            return False, None

        # 用于生成xml的字典变量
        dbinfo = {}
        dbinfo['type'] = "mysql"
        dbinfo['host'] = database['host']
        dbinfo['databasename'] = database['databasename']
        dbinfo['username'] = database['username']
        if ('port' not in database.keys()):
            dbinfo['port'] = 3306
        if ('password' not in database.keys()):
            dbinfo['password'] = ''
        dbinfo['schema'] = []

        dbclient = db(database)
        dbclient.connection()

        # 获得当前数据库下所有表信息
        tlist = dbclient.getAllTables()
        print (tlist)
        for titem in tlist:
            table = {}
            table['name'] = titem['table_name']
            table['comment'] = titem['table_comment']
            table['fields'] = []
            # 获得当前表所有字段
            fields = dbclient.getTableColumns(titem['table_name'])
            for fitem in fields:
                field = {}
                field['name'] = fitem['column_name']
                field['type'] = fitem['column_type'][0: fitem['column_type'].find("(")]
                field['length'] = fitem['column_type'][fitem['column_type'].find("(")+1:fitem['column_type'].find(")")]
                if (fitem['column_key'] == 'PRI'):
                    field['primary_key'] = 1
                else:
                    field['primary_key'] = 0
                field['description'] = fitem['column_comment']
                table['fields'].append(field)

            dbinfo['schema'].append(table)
        dbinfo = {"database": dbinfo}
        dbxml = dicttoxml.dicttoxml(dbinfo, custom_root="database", root=False).decode("utf-8")
        return True, dbxml




if __name__ == '__main__':
    dbinfo = {
        "host": "172.16.8.7",
        "port": "3306",
        "databasename": "test",
        "username": "root",
        "password": "123456"
    }
    ret, xmldata = dbTools.db2xml(dbinfo)
    print (xmldata)
