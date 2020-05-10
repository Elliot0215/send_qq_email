#coding=utf-8

import configparser

file = 'config.ini'

def readConfig(item):
    ##  创建配置文件对象
    con = configparser.ConfigParser()
    ##  读取文件
    con.read(file, encoding='utf-8')
    ##  获取所有section
    sections = con.sections()
    for section in sections:
        items = con.items(section)
        items = dict(items)
        for key,value in items.items():
            if key == item:
                return value