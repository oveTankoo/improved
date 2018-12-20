# coding: utf-8
from flask import Flask, render_template, request

app = Flask(__name__)#, static_folder='.', static_url_path='')

#@app.route('/')
#def home():
#	return app.send_static_file('index.html')

# 1.把参数当成URL的一部分，这种方法可以直接扩展URL本身
#@app.route('/echo/<thing>/<place>')
#def echo(thing, place):
#	return render_template('temp2.html', thing = thing, place = place)

# 2.还可以用GET参数来传递参数
@app.route('/echo/')
def echo():
	#thing = request.args.get('thing')
	#place = request.args.get('place')
	# 使用字典的 **操作符来向模板一次性传入字典的多个值(参数多时可以省时)
	kwargs = {}
	kwargs['thing'] = request.args.get('thing')
	kwargs['place'] = request.args.get('place')
	#return render_template('temp2.html', thing = thing, place = place)
	return render_template('temp2.html', **kwargs)

app.run(port = 9999, debug = True)