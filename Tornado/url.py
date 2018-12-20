#coding:utf-8
"""the url structure of website"""

from handlers.index import IndexHandler

#例：index.py有一个类IndexHandler，约定处理网站根目录的请求
url = [(r'/',IndexHandler),]