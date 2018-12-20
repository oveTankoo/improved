#edited:180522
#coding:utf-8
"""
抓取流程：1.进入四虎主页，确定抓取目标
		2.观察页面，获取3大推荐版块的链接
		3.进入各推荐电影的详情页面，抓取其名称，分类，更新时间，资源地址
		4.分别进入队列，下载资源
"""
#该页分别负责解析：首页，各推荐电影详情页
import requests
import json
from pyquery import PyQuery

def homepage_parse(res):
	"""
	抓取首页：http://www.204sihu.com
	返回各推荐版块-电影的url
	"""
	jpy = PyQuery(res.text)
	print(dir(jpy))
	print(help(jpy.html))
	print(jpy('body > div:nth-child(15) > div > ul > li:nth-child(1) > a > img').attr('title'))
	'body > div:nth-child(17) > div > div > h1 > a'
	tr_list = jpy('body > div:nth-child(15) > div').items()
	#print([x.attr('href') for x in tr_list])
	#result = set()
	#for tr in tr_list:
	#	url = tr('a').attr('href')#div > h1 > 
	#	result.add(url)
	#print(result)
	
if __name__ == '__main__':
	url = 'https://www.6685a.com'
	res = requests.get(url)
	res.encoding = 'utf-8'
	#homepage_parse(res)
	baidu = 'https://infocenter.gfgroup.com.hk/user/captcha'
	headers = {'Cookie':'captcha_id=201805282152290'}
	#s = requests.session()
	r = requests.get(baidu,headers=headers,verify=False)
	r.encoding = 'utf-8'
	print(r.text)
	print(dir(r.cookies),r.cookies.values())
	#print(res.headers)