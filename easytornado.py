# -*- coding: utf-8 -*-

# from compiler.Compiler import Compiler
from editor.databaseTools import dbTools



if __name__ == '__main__':
    # cc = Compiler()
    # 读取xml文件
    # with open("./test.xml", encoding="utf-8") as fp:
    #     content = fp.read()
    #     cc.load(content)
    #     fp.close()
    #     cc.exec()
    dbinfo = {
        "host": "172.16.8.7",
        "port": "3306",
        "databasename": "test",
        "username": "root",
        "password": "123456"
    }
    ret, xmldata = dbTools.db2xml(database = dbinfo)
    print (xmldata)
        
    