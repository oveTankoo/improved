# author: adam
# 
class word():

	def __init__(self, text):
	 	self.text = text

	def __eq__(self, word2):
	 	return self.text.lower() == word2.text.lower()

	def __str__(self):
		return self.text

	def __repr__(self):
		return 'word(%s)'%self.text

first = word('ha')
second = word('HA')
third = word('huh')

print(first)

print(first == third)