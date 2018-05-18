#!/usr/bin/env python
# -*- coding:UTF-8 -*-
__author__ = 'miaochenliang'

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# import++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# ↓+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
from PyInstaller.__main__ import run

if __name__ == '__main__':
    opts = ['***.py', '-F', r'--distpath=**', r'--workpath=**', r'--specpath=**', r'--icon=**']
    run(opts)


"""
　　代码中，opts= 后面的列表里的就是一系列参数，详解如下：

　　第一个***.py就是你要编译的文件名，必填 [之后的参数全部为选填]

　　第二个-F就是生成单文件的参数

　　第三个--distpath=**意思是dist文件夹（最后输出文件所在地）的路径，**为路径，比如D:\My Programs\Python\输出\dist，默认为当前目录下的dist文件夹内

　　第四个--workpath=**意思是build文件夹（临时文件）的路径，**为路径，比如D:\My Programs\Python\输出\build，默认为当前目录下的build文件夹内

　　第五个--specpath=**意思是***.spec文件（临时文件）的路径，**为路径，比如D:\My Programs\Python\输出\，默认为当前目录

　　第六个--icon=**意思是输出的exe文件的图标路径，**为路径，比如D:\My Programs\Python\icon.ico
"""