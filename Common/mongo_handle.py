# updated:180614
# 此模块主要功能：对 mongodb 进行日常操作
import pymongo
from bson.objectid import ObjectId
from read_deploy import gain_info

class MongoHandle(object):

	def __init__(self,type,filepath = r'E:\Learn\Common\database_info.ini'):
		#初始化数据库		
		self.ids = list()
		self.receipt = False
		self.count = 0
		try:
			info = gain_info(filepath, type)
			self.conn = pymongo.MongoClient(info[0])
			self.db = self.conn[info[1]]
		except Exception as e:
			raise e

	def __close(self):
		return self.conn.close()

	def insert_one(self,col_name,data):
		"""新增一条文档"""
		try:
			coll = self.db[col_name]
			result = coll.insert_one(data)
			self.receipt = result.acknowledged
			self.ids = str(result.inserted_id)
			#print('新增成功：{0}\n成功id：{1}\n'.format(self.receipt,self.ids))
		except Exception as e:
			raise e
		finally:
			self.__close()
		return self.receipt,self.ids

	def insert_many(self,col_name,datas):
		"""新增多条文档"""
		try:
			coll = self.db[col_name]
			result = coll.insert_many(datas)
			self.receipt = result.acknowledged
			self.ids = [str(x) for x in result.inserted_ids]
			print('新增成功：{0}\n成功ids：{1}\n'.format(self.receipt,self.ids))
		except Exception as e:
			raise e
		return self.receipt,self.ids

	def del_one(self,col_name,data):
		"""删除一条文档"""
		try:
			coll = self.db[col_name]
			result = coll.delete_one(data)
			self.receipt = result.acknowledged
			self.count = result.deleted_count
			print('删除成功：{0}\n成功数目：{1}\n'.format(self.receipt,self.count))
		except Exception as e:
			raise e
		return self.receipt,self.count

	def del_many(self,col_name,query = {},projection = {},order = {}):
		"""删除多条文档"""
		try:
			coll = self.db[col_name]
			result = coll.delete_many(query)
			self.receipt = result.acknowledged
			self.count = result.deleted_count
			print('删除成功：{0}\n成功数目：{1}\n'.format(self.receipt,self.count))
		except Exception as e:
			raise e
		return self.receipt,self.count

	def find_one(self, col_name, filter, projection):
		"""查找符合条件的一条文档"""
		try:
			coll = self.db[col_name]
			result = coll.find_one(filter, projection)
			#print(dir(result))
			#print('查得数据:\n%s'%result)
		except Exception as e:
			raise e
		finally:
			self.__close()
		return result;

	def find_many(self,col_name,filter = {},projection = {},skip = None,limit = None):
		"""查找符合条件的多个文档"""
		try:
			coll = self.db[col_name]
			result = coll.find(filter=filter,projection=projection,skip=skip,limit = limit)
			items = [x for x in result]
			#print(['{}\n'.format(x) for x in result])
			#print('查得数目：{0}条\n查得items：{1}\n'.format(result.count(), items))
		except Exception as e:
			raise e
		finally:
			self.__close()
		return result.count(),items;

	def close(self):
		"""关闭mongo连接"""
		return self.conn.close()

if __name__ == '__main__':
	mong = MongoHandle(type = 'mongo_local_admin')
	data = {'who':'me','when':'now','where':'here','how':'testing'}
	#result = mong.insert_one('test', data)
	mong.find_one('test', {}, {'_id':False})
	#projection = {'_id':False, 'category':True, 'title':True, 'download':True}
	#mong.find_many('movie', {}, projection, 1, 100)