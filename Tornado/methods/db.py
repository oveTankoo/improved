#coding:utf-8
#连接本地sqlite数据库
import sqlite
conn = sqlite.connect(r'E:\Learn\Tornado\sqlite.db')
#建立游标
cur = conn.cursor()