# -*- coding: utf-8 -*-

from compiler.Compiler import Compiler




if __name__ == '__main__':
    cc = Compiler()
    # 读取xml文件
    with open("./test.xml") as fp:
        content = fp.read()
        cc.load(content)
        fp.close()
        cc.run()

        
    