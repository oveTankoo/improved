#edited:180519
#coding:utf-8

import pymongo

class mongodb(object):
	"""usual handle of mongodb"""
	def __init__(self,uri='mongodb://localhost:27017/test',dbname='test'):
		#self.uri = 'mongodb://localhost:27017/test'
		self.conn = pymongo.MongoClient(uri)
		self.db = self.conn[dbname]
	
	def __connect(self,dbname,collection):
		try:
			conn = pymongo.MongoClient(self.uri)
			db = conn[dbname]
			col = db[collection]
		except Exception as e:
			raise e
		return col

	#@staticmethod
	def find_many(self,filter,projection=None):
		col = self.__connect('test','test')
		result = [x for x in col.find(filter,projection)]
		print(dir(result))
		print('查询后返回:{}\n'.format(result))
		return result

	def insert_one(self, collection, doc):
		try:
			col = self.db[collection]
			result = col.insert_one(doc)
			print('插入成功:{0}\n生成的id:{1}\n'.format(result.acknowledged,result.inserted_id))
		except Exception as e:
			raise e
		return result

	def insert_many(self,docs,filter):
		try:
			col = self.__connect('test','test')
			result = col.insert_many(docs)
			print('插入成功:{0}\n生成ids:{1}\n'.format(result.acknowledged,result.inserted_ids))
		except Exception as e:
			raise e	
		return result

	def del_many(self,filter,query):
		try:
			col = self.__connect('test','test')
			result = col.delete_many(filter)
			print('删除成功:{0}\n删除数目:{1}\n'.format(result.acknowledged,result.deleted_count))
		except Exception as e:
			raise e

	def drop_col(self,collection):
		"""删除某个集合"""
		col = self.db[collection]
		col.drop()

	def close(self):
		return self.conn.close()

if __name__ == '__main__':
	m = mongodb()
	doc = {'name':'小米','phone':'13800001000','sex':'male','age':17}
	docs = [{'name':'小黑','phone':'13800001001','sex':'male','age':18},{'name':'小陈','phone':'13800001002','sex':'female','age':15},
			{'name':'小刘','phone':'13800001002','sex':'female','age':14},{'name':'小王','phone':'13800001002','sex':'male','age':16}]
	m.insert_one('test',doc)
	#m.insert_many(docs,{'name':'小黑'})
	#m.find_many(filter={},projection={'_id':False})
	#m.del_many({'sex':'male'},{'sex':'female'})
	# 清空 test 集合
	m.drop_col('test')
	m.close()