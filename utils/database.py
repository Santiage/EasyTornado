# -*- coding: utf-8 -*-

import pymysql


class db:

    database = {
        "host": None,
        "port": None,
        "databasename": None,
        "username": None,
        "password": None
    }

    def __init__ (self, database:dict):
        self.database = database
    # def __del__ (self):
    #     if self.db is not None:
    #         self.db.close()
    #         self.db = None

    def connection(self):
        """
        根据类变更database中的数据，连接数据库。
        """
        try:
            self.db = pymysql.connect(host=self.database['host'], user=self.database['username'], password=self.database['password'], db=self.database['databasename'])
            if self.db is None:
                return False
        except:
            print("数据库连接失败！")
            return False

        return True

    @staticmethod
    def databaseExist(dbinfo):
        """
        测试数据库是否存在
        """
        pass

    def getAllTables(self):
        """
        查询当着数据库下所有的表信息
        """
        sql = f'''
            SELECT
                t.table_catalog, 
                t.table_schema, 
                t.table_name, 
                table_type,
                t.table_comment
            FROM
                information_schema.TABLES t 
            WHERE
                t.table_schema='{self.database['databasename']}'
        '''
        res = self.execute(sql)
        print(res)
        return res

    def getTable(self, tableName):
        """
        查询当前数据库下的表信息
        """
        sql = f'''
            SELECT
                t.table_catalog,
                t.table_schema,
                t.table_name,
                t.table_type,
                t.table_comment
            FROM
                information_schema.TABLES t
            WHERE
                t.table_schema = '{self.database['databasename']}' and t.table_name = '{tableName}'
        '''
        res = self.execute(sql)
        if len(res) > 0:
            return res[0]
        return {}

    def getTableLike(self, tableName):
        """
        查询数据数据库以tableName为前缀的表信息
        """
        sql = f'''
            SELECT
                t.table_catalog,
                t.table_schema,
                t.table_name,
                t.table_type,
                t.table_comment
            FROM
                information_schema.TABLES t
            WHERE
                t.table_schema = '{self.database['databasename']}' and t.table_name like '{tableName}%'
        '''
        res = self.execute(sql)
        return res

    def getTableComment(self, tableName):
        """
        获取表注释
        """
        sql = f'''
            show table status where NAME='{tableName}'
        '''

        res = self.execute(sql)
        if len(res) > 0:
            return {
                "name":res[0].get("name",res[0].get("Name",res[0].get("NAME",''))),
                "comment": res[0].get("comment",res[0].get("Comment",res[0].get("COMMENT",'')))
            }
        return {}
    
    def getPrimaryColumns(self, tableName):
        """
        获取当前数据库指定表的主键列
        """
        sql = f'''
            SELECT
                k.column_name
            FROM
                information_schema.table_constraints t
                join information_schema.key_column_usage k
                using (constraint_name, table_schema, table_name)
            WHERE
                t.constraint_type='PRIMARY KEY'
                and t.table_schema='{self.database['databasename']}' and t.table_name='{tableName}'
        '''
        res = self.execute(sql)
        return res

    def getTableColumns(self, tableName):
        """
        获得当前数据指定表的所有列
        """
        sql = f'''
            SELECT
                t.table_schema,
                t.table_name,
                t.column_name,
                t.column_default,
                t.is_nullable,
                t.data_type,
                t.character_maximum_length,
                t.numeric_precision,
                t.numeric_scale,
                t.column_type,
                t.column_key,
                t.column_comment
            FROM
                information_schema.columns t
            WHERE
                t.table_schema='{self.database['databasename']}' and t.table_name='{tableName}'
        '''
        res = self.execute(sql)
        return res

    def execute(self, sql):
        """
        执行sql
        """
        if (self.db is None):
            return False

        cursor = self.db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        index_dict = {}
        index = 0
        for desc in cursor.description:
            index_dict[desc[0]]=index
            index = index + 1
        res = []
        for datai in data:
            item = {}
            for idx in index_dict:
                item[idx] = datai[index_dict[idx]]
            res.append(item)
        return res




if __name__ == '__main__':
    dbinfo = {
        "host": "127.0.0.1",
        "port": "3306",
        "databasename": "test",
        "username": "root",
        "password": "123456"
    }
    dbc = db(dbinfo) 
    print (dbc.connection())
    rr = dbc.getAllTables()
    print (dbc.getTable('t_user'))
    print(dbc.getTableLike('t_'))
    print(dbc.getTableComment('t_user'))
    print(dbc.getPrimaryColumns('t_user'))
    print(dbc.getTableColumns('t_user'))
