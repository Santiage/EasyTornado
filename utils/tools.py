# -*- coding: utf-8 -*-

import xmltodict
import json

class tools:
    @staticmethod
    def xml2dict(xmldata:str) -> dict:
        """
        xml字符串转dict
        """
        convertedDict = xmltodict.parse(xmldata)
        # ensure_ascii设置为False，中文可转换
        jsonStr = json.dumps(convertedDict, ensure_ascii=False)
        print (jsonStr)
        return json.loads(jsonStr)

    @staticmethod
    def str2Hump(text, flag=False):
        """
        字段名转驼峰
        """
        if flag == True:
            return ''.join(map(lambda x: x.capitalize(), text.split("_")))
        arr = filter(None, text.lower().split('_'))
        res = ''
        j = 0
        for i in arr:
            if j == 0:
                res = i
            else:
                res = res + i[0].upper() + i[1:]
            j += 1
        return res
