#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#------python3笔记-----#


### IO编程  同步  异步

## 文件读写
# 写文件  创建文件
# open() 传入'w'或'wb'表示写文本文件或二进制文件
#with open('./io_test.txt','w',encoding='utf-8') as f:
#	f.write('hello,中国！')
""" 
# 读文件
try:
	f=open('./io_test.txt','r',encoding='utf-8') #读文件
	print(f.read())
finally:
	if f:
		f.close() #关闭文件
"""
"""
# 改进：引入 with语句自动调用 close()
# 和 try ... finally 一样
with open('./io_test.txt','r',encoding='utf-8') as f:
	#print(f.read())		#读取所有内容
	#print(f.read(6)) 		#读取最多20个字节
	#print(f.readline())	#读取一行内容
	#for line in f.readlines():  #读取所有内容按行返回 list
	#	print(line.strip())		# 删掉末尾 '\n'
"""
# file-like Object
# 像open()返回的有个read()方法的对象,只要有read()就行

# 读取二进制文件 	'rb'
# 字符编码			encoding参数
# 编码错误处理 		errors参数
#with open('./io_test.txt','r',encoding='utf-8',errors='ignore') as f:
#	pass

## StringIO和BytesIO
""" StringIO
from io import StringIO
f_write=StringIO() 					  #写操作
print(f_write.write('hello,中国!'))   #返回字符个数
print(f_write.getvalue())	 		  #获得写入后的str

f_read=StringIO('Hello\nHi\nGoodbye') #读操作
for s in f_read.readlines():
	print(s.strip())
"""
""" BytesIO
from io import BytesIO
f_write=BytesIO()
print(f_write.write('中文'.encode('utf-8'))) #返回字节数
print(f_write.getvalue())

f_read=BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f_read.read())
"""

## 操作文件和目录
#import os
#print(os.name)	#返回操作系统类型
# 'posix': Linux Unix 或 Mac OS X
# 'nt' 	: Windows
#print(os.uname()) 	#系统详细信息,Windows不提供
#print(os.environ)	#全部环境变量
#print(os.environ.get('PATH')) #PATH环境变量值
"""
print(os.path.abspath('.')) #当前目录绝对路径
os.mkdir('./testdir')		#创建目录
os.rmdir('./testdir')		#删除目录
print(os.path.join('\\usr\\me','hello'))	#合成路径
print(os.path.split('/usr/me/test.txt'))	#拆分路径
print(os.path.splitext('/usr/me/test.txt'))	#得到文件扩展名
# 以上合并拆分路径的函数不要求路径真实存在
#os.rename('io_test.txt','atest.py')	#文件重命名
#os.remove('atest.py')					#删除文件
# 复制文件：shutil模块提供的copyfile()
"""
# 过滤文件
# 列出当前目录下所有目录
#print([x for x in os.listdir('.') if os.path.isdir(x)])
# 列出所有 .py文件
#print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

"""
## 序列化：变量从内存变为可存储或传输的过程
import pickle
d=dict(name='Bob',age=20,score=88)
bytes_1=pickle.dumps(d)  #将d序列化为bytes
f=open('dump.txt','wb')
f.write(bytes_1)  #将bytes写入文件	
pickle.dump(d,f)  #直接将对象序列化后写入文件
f.close()

f1=open('dump.txt','rb')
d1=pickle.load(f1)	#从f1中直接反序列化出对象
bytes_2=f1.read()
d2=pickle.loads(bytes_2)
print(d1,d2)
f1.close()
"""
## JSON
"""
import json
d=dict(name='Bob',age=20,score=88)
print(json.dumps(d)) 
#这里dumps()返回一个str,内容为标准JSON -->dump()
json_str='{"name": "Bob", "age": 20, "score": 88}' #JSON字符串
d1=json.loads(json_str) #将JSON字符串反序列化
print(d1)				#load()从文件读取字符串并反序列化
"""
"""
# JSON进阶
import json
class Student(object):
	def __init__(self,name,age,score):
		self.name=name
		self.age=age
		self.score=score
s=Student('Bob',20,88)
#print(json.dumps(s)) #报错

def student2dict(std):
	return {
		'name':std.name,
		'age':std.age,
		'score':std.score
	}
print(json.dumps(s,default=student2dict))
print(json.dumps(s,default=lambda obj:obj.__dict__)) #适用于更多实例
# 通常class实例都有__dict__属性,就是一个dict,用于存储变量

def dict2Student(d):
	return Student(d['name'],d['age'],d['score'])
json_str='{"name": "Bob", "age": 20, "score": 88}'
print(json.loads(json_str,object_hook=dict2Student))
"""

### 进程和线程
## 多进程
# Unix/Linux：fork()
# 跨平台支持多进程 multiprocessing
"""
from multiprocessing import Process
import os

#子进程待执行代码
def run_proc(name):
	print('Run child process "%s" : %s ...'%(name,os.getpid()))
if __name__ == '__main__':
	print('Parent process %s...'%os.getpid())
	p=Process(target=run_proc,args=('ChildProcess',))
	print('Child process will start.')
	p.start()  #启动一个进程实例
	p.join()   #父进程等待子进程
	print('Child process ended.')
"""
"""
# Pool 进程池
from multiprocessing import Pool
import os,time,random

def long_time_task(name):
	print('Run task "%s" : %s ...'%(name,os.getpid()))
	start=time.time()
	time.sleep(random.random()*3)
	end=time.time()
	print('Task %s runs %0.2f seconds.'%(name,(end-start)))
if __name__ == '__main__':
	print('Parent process %s.'%os.getpid())
	p=Pool(4)  #最多可同时跑4个进程
	for i in range(5): #为进程池添加5个进程
		p.apply_async(long_time_task,args=(i,))
	print('Waiting for all subprocesses done...')
	p.close()  #使进程池不能再添加进程
	p.join()   #等待所有子进程
	print('All subprocesses have done.')
"""
"""
# subprocess模块：启动子进程,控制其输入输出
import subprocess
#在Python代码中运行命令：nslookup www.baidu.com
r=subprocess.call(['nslookup','www.baidu.com'])
print('Exit code:',r)
#提供子进程输入 --> communicate()
p=subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,err=p.communicate(b'set q=mx\nbaidu.com\nexit\n')
print(output.decode('gbk'))
print('Exit code :',p.returncode)
"""

# 进程间通信 Queue Pipes
from multiprocessing import Process,Queue
import os,time,random
''' 以Queue为例,在父进程创建两个子进程,
	一个往Queue写数据,一个从Queue读数据 '''

#写数据进程执行代码
def write_data(q):
	print('Process to write:%s'%os.getpid())
	for value in ['A','B','C']:
		print('Puts %s to queue...'%value)
		q.put(value)
		time.sleep(random.random())
#读数据进程执行代码
def read_data(q):
	print('Process to read:%s'%os.getpid())
	while True:
		value=q.get(True)
		print('Gets %s from queue...'%value)

if __name__ == '__main__':
	q=Queue()
	pw=Process(target=write_data,args=(q,))
	pr=Process(target=read_data,args=(q,))
	pw.start()
	pr.start()
	pw.join()
	pr.terminate()	#pr进程为死循环,只能强行终止
