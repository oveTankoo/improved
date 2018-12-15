# author: adam
# 一个 ThreadLocal 变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。
# ThreadLocal解决了参数在一个线程中各个函数间互相传递的问题。
# ThreadLocal最常用的地方是，为每一个线程绑定一个数据库连接、HTTP请求、用户身份信息等，
# 这样一个线程的所有调用到的处理函数，都可以非常方便地访问这些资源。
import threading

# 创建全局ThreadLocal对象，这样每个 Thread 对它都可以进行属性读写，互不影响。
local_school = threading.local()

def process_study():
	# 获取当前线程关联的student & teacher属性的值:
	std = local_school.student
	tch = local_school.teacher
	print("In %s, %s's teacher is %s !"%(threading.current_thread().name, std, tch))

def process_thread(student, teacher):
	# 绑定ThreadLocal的student:
	# 可以理解为全局变量 local_school 是一个dict，添加新的键值方式是local_school.key = value
	local_school.student = student
	local_school.teacher = teacher
	process_study()

# 创建2个子线程，并给予不同的args和name值
t1 = threading.Thread(target = process_thread, args = ('Alice','Tom'), name = 'Thread-A')
t2 = threading.Thread(target = process_thread, args = ('Adam','Kolin'), name = 'Thread-B')

t1.start()
t2.start()
t1.join()
t2.join()