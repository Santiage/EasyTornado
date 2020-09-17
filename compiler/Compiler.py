# -*- coding: utf-8 -*-

from jinja2 import FileSystemLoader, Environment
# import xml.sax
from xml.dom.minidom import parseString
import xml.dom.minidom

from utils.database import db
from utils.tools import tools

class Compiler:
    # 存入xml文件原始数据
    xmldata = dict()

    # 存放从excel读出的database标签信息
    database = []


    def __init__(self):
        pass


    def load(self, xmldata):
        self.xmldata = tools.xml2dict(xmldata)
        # 读取数据库信息
        ret, database  = self.readLabel(self.xmldata, "database")
        print (database)
        dbinfo = {
            "host": database['host'],
            "port": database['port'],
            'name': database['name'],
            'username': database['username'],
            'password': database['password']
        }

        # 测试数据库是否正常

        

    def exec(self):
        # 测试数据库连接

        



    
    
    def readLabel(self, xmldata, labelname):
        """
        函数名称：readLabel
        入参：  xmldata - xml原始数据
            type - 要读取的数据类型
        出参：  dict()
        """
        if xmldata is None:
            return False, None
        
        DOMTree = parseString(xmldata)

        
        return True, retval['webservice'][labelname]



