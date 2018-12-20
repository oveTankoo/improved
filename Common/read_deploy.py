#coding=utf-8
#updated:2018-07-20
import configparser as cparser

def gain_info(file_path, type):
	"""读取数据库配置文件，得到所需信息"""
	uri, dbname = '', ''
	try:
		cf = cparser.ConfigParser()
		cf.read(file_path, encoding='utf-8')
		host = cf.get(type, "host")
		port = cf.get(type, "port")
		dbname = cf.get(type, "dbname")
		user = cf.get(type, "user")
		password = cf.get(type, "password")
		uri = 'mongodb://{0}:{1}@{2}:{3}/{4}'.format(user,password,host,port,dbname)
		#print('%s\n'%uri)
		return uri,dbname
	except Exception as e:
		raise e

if __name__ == '__main__':
	path = r'.\database_info.ini'
	cc = gain_info(path, 'mongo_local_admin')