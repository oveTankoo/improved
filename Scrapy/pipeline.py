#edited:180606
import pymongo

class MongoPipeline(object):
	"""docstring for MongoPipeline"""
	collection_name = 'scrapy_items'
	def __init__(self,mongo_uri,mongo_db):
		self.mongo_uri = mongo_uri
		self.mongo_db = mongo_db

	@classmethod
	#可选方法
	def from_crawler(cls,crawler):
		return cls(mongo_uri = crawler.settings.get('MONGO_URI'),
					mongo_db = crawler.settings.get('MONGO_DATABASE','items'))

	#可选方法
	def open_spider(self,spider):
		self.client = pymongo.MongoClient(self.mongo_uri)
		self.db = self.client[self.mongo_db]

	#可选方法
	def close_spider(self,spider):
		self.client.close()

	#必要方法
	def process_item(self,item,spider):
		self.db[self.collection_name].insert_one(dict(item))
		return item;