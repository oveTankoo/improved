# author: adam
# 命名元组：元组的子类，既可以通过名称（使用.name）访问其中的值，也可以通过位置（使用[offset]）访问
# 现在将前面的Duck类改写成命名元组，简洁起见，把bill和tail作为字符串而不是类
# 导入有关模块

from collections import namedtuple

# print(help(namedtuple))
# namedtuple(typename, field_names, *, verbose=False, rename=False, module=None)
Duck = namedtuple('Duck', ['bill', 'tail'])
duck = Duck('wide orange', 'long')

# 打印 Point 类的文档
print('Point类文档:', Duck.__doc__)
# 打印实例 duck
print('实例 duck:', duck)
# 通过名称（.name）访问
print('通过名称（.name）访问:%s,%s'%(duck.bill, duck.tail))
# 通过位置（[offset]）访问
print('通过位置（[offset]）访问:%s,%s'%(duck[0], duck[1]))

# 转化为字典（orderedDict）
d = duck._asdict()
print('转化为字典后:', d)

# 命名元组是不可变对象，但你可以替换某个属性的值来产生一个新的命名元组
bule_duck = duck._replace(bill = 'bule')
print('新的命名元组:', bule_duck)