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
## 过滤文件
# 列出当前目录下所有目录
#print([x for x in os.listdir('.') if os.path.isdir(x)])
# 列出所有 .py文件
#print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
