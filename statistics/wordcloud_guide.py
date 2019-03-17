"""
using wordcloud example
"""
from os import path
from wordcloud import WordCloud  #生成词云图片
import matplotlib.pyplot as plt  #打开图片
import jieba  #首先进行分词，将一个句子分割成一个个的词语

# 读取整个文本
path = r'C:/Users/Administrator/Desktop/'
text = open(path + 'wordcloud.txt').read()

cut = jieba.cut(text)
string = ' '.join(cut)
#print(string)

# 生成一个词云图像(默认参数)
#wordcloud = WordCloud().generate(text)

wordcloud = WordCloud(max_font_size  = 100,	#最大字体大小
					min_font_size = 4,		#最小字体大小
					width = 400,	#设置宽度，默认400
					height = 400,	#设置高度，默认200
					max_words = 10	#设置词语最大数量，默认200
					).generate(text)
# 创建一个新图片，num为数字，标题为Figure num；num为字符串，则标题为该字符串
plt.figure(num = 1)
plt.imshow(wordcloud, interpolation = 'bilinear')	#用plt显示图片
plt.axis("off")		#不显示坐标轴
plt.savefig(path + 'wordcloud.png', dpi = 200)
plt.show()		#显示图片