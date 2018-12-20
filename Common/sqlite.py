# coding:utf-8
# author:testoo
import os
import sys
import sqlite3

class SqliteHandle(object):
	"""该类主要进行Sqlite数据库操作"""
	def __connect(self, dbpath = r"Test.db"):
		"""操作初始化"""
		try:
			self.conn = sqlite3.connect(dbpath)
			self.cur = self.conn.cursor()
		except Exception as e:
			raise e

	def __disconnect(self):
		"""断开数据库连接"""
		self.cur.close()
		self.conn.close()

	@staticmethod
	def trans_dict(input):
		output = None
		if isinstance(input, dict):
			items = list(input.items())
			if len(items) > 1:
				output = " and ".join(["{0}={1}".format(x[0], x[1]) for x in items])
			else:
				output = "{0}={1}".format(items[0][0], items[0][1])
		else:
			print('请输入 dict 类型的对象!')
		return output

	@staticmethod
	def trans_tuple(input):
		"""转化元组或列表成字符串"""
		output = None
		if isinstance(input, (tuple, list)):
			if len(input) > 1:
				output = ",".join(input)
			else:
				output = str(input[0])
		else:
			print('请输入 tuple或list 类型的对象!')
		return output

	def setup(self, table = 'cookies'):
		"""创建一个表格，并定义 name 为主键"""
		try:
			self.__connect()
			self.cur.execute("create table %s (name text,value text,unique (name) on conflict replace)"%table)
		except Exception as e:
			raise e
		finally:
			self.__disconnect()

	def query(self,  fields, filter, table = 'cookies'):
		"""查询数据"""
		result = None
		self.__connect()
		try:
			if filter:
				# 判断查询条件对象，是否为 dict 类型
				if isinstance(filter, dict):
					trans_filter = self.trans_dict(filter)
					print(trans_filter)
					# 判断字段对象，是否为 tupel/list 类型
					if isinstance(fields, (tuple, list)):
						trans_fields = self.trans_tuple(fields)
						print(trans_fields)
						query = "select %s from %s where %s"%(trans_fields, table, trans_filter)
						result = self.cur.execute(query).fetchall()
					else:
						print('即将返回 全部数据！')
						result = self.cur.execute("select * from %s"%table).fetchall()
				else:
					print('please input dict-category filter !')
			else:
				# 判断字段对象，是否为 tupel/list 类型
				if isinstance(fields, (tuple, list)):
					trans_fields = self.trans_tuple(fields)
					result = self.cur.execute("select %s from %s"%(trans_fields, table)).fetchall()
				else:
					print('即将返回 全部数据！')
					result = self.cur.execute("select * from %s"%table).fetchall()
		except Exception as e:
			raise e
		finally:
			self.__disconnect()
		return result
	
	def update_or_query(self, name, value=None, table = 'cookies'):
		"""用来查询或更新 想要的值"""
		wanted = None
		self.__connect()
		print('self.cur - dir:', dir(self.cur))
		try:
			if value == None:
				#仅有value时查询
				wanted = self.cur.execute("select value from %s where name = '%s'"%(table, name)).fetchone()[0]
				print('wanted - dir:', dir(wanted))
			else:
				names = self.cur.execute("select name from %s"%table).fetchall()
				if name not in names:
					#如果不存在该值的记录，则新增
					self.cur.execute('insert into %s (name,value) values("%s","%s")'%(table, name, value))
					wanted = self.cur.execute("select value from %s where name = '%s'"%(table, name)).fetchone()[0]
					self.conn.commit()
				else:
					#如果存在该值的记录，则更新
					self.cur.execute('update %s set value = "%s" where name = "%s"'%(table, name, value))
					wanted = self.cur.execute("select value from %s where name = '%s'"%(table, name)).fetchone()[0]
					self.conn.commit()
		except Exception as e:
			raise e
		finally:
			self.__disconnect()
		#返回当前对应该name的value值
		return wanted
	
	def teardown(self):
		"""删除表格，并销毁数据库"""
		try:
			self.__connect()
			self.cur.execute("drop table cookies")
			self.__disconnect()
			os.unlink("Test.db")
		except Exception as err:
			raise err

if __name__=='__main__':
	sq = SqliteHandle()
	#sq.teardown()
	#sq.setup()
	#print(sq.trans_dict({'1':2}))
	wanted = sq.query(('name', 'value'), {'value':'having'})
	print(wanted)
	#sq.teardown()