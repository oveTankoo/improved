#edited:180524

from scrapy import Selector
#引入第三方库：pyquery
from pyquery import PyQuery

with open('selector.html',encoding='utf-8') as f:
	text = f.read()

"""通过Selector自带方法，获取元素"""
sel = Selector(text=text)
#print(sel.css('li > div').extract())
print(sel.xpath('/html/body/ul/li/a/div/text()').extract())

"""通过pyquery获取"""
jpy = PyQuery(text)
#查找class = 'top'的元素的文本
print(jpy('.top').text())
#查找class = 'top'的元素的class属性
print(jpy('.top').attr('class'))
#查找li标签下所有的文本
print([x.text() for x in jpy('li').items()])
#查找li标签下所有的class属性
print([x.attr('class') for x in jpy('li').items()])