# coding: utf-8
from bottle import route, run, static_file

@route('/')
#def home():
#	return "It isn't fancy, but it's my home page!"
def main():
	return static_file('index.html', root= '.')

@route('/echo/<thing>')
def echo(thing):
	return "Say hello to my little friend: %s!" % thing

run(host = 'localhost', port = 9999)