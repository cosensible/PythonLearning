#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#---------本文为Python3笔记-----------#


### 输入和输出
#print('100+200=',100+200)
#name=input('please input your name:')
#print('hello,',name)


### 数据类型和变量
# 整数 
-88 , 0xff00
# 浮点数 
1.23e9
# 字符串
'abc' , "I'm OK!"
# 布尔值  and or not
True , False
# 空值
None

# 不转义 
#print(r"\n")
# 多行内容
#print('''line1
#line2
#line3''')

# 除法
#print(9/3)		# 精确除
#print(10//3)	# 地板除

# 获取字符的整数表示
#print(ord('中'))
# 将编码转换为字符
#print(chr(25991))
# 编码
#print('中文'.encode('utf-8'))
#print('ABC'.encode('ascii'))
# 解码
#print(b'ABC'.decode('ascii'))
#print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
# 计算 str 字符数
#print(len('ABC'))
#print(len('中文'))

# 格式化
#print('%2d--%02d'%(3,1))
# %s 永远起作用  %%-->%


### list 和 tuple  元素的类型可不同
#students=['Tom','Jack','Lucy']		# 列表
#print(len(students))				# 列表元素个数
#print(students[0],students[-1])	# 索引
#students.append('Brack')			# 末尾追加元素
#students.insert(1,'Bob')			# 指定位置插入元素
#print(students.pop())				# 删除末尾元素
#students.pop(1)					# 删除指定元素
#print(students)

# tuple 不可修改
#classes=('A','B','C')		# 元组
#t=(1,)						# 一个元素的元组
#print(t)


### 条件判断
#age_str=input('please input your age:')
#age=int(age_str)
#if age>=18:
#	print('adult!')
#elif age>=10:
#	print('teenager!')
#else:
#	print('child!')


### 循环
#for x in list(range(5)):
#	print(x)

# break continue
#n=5
#while n>0:
#	print(n)
#	n-=1 


### dict 和 set  无序 键不能包含可变对象
# dict
#score_dict={'Tom':95,'Jack':76,'Hansen':100}
#score_dict['Lucy']=87			# 添加数据
#score_dict['Lucy']=88			# 修改数据
# 判断 key 的存在
#print('Thomas' in score_dict)				
# 判断 key 的存在  并返回指定值  默认值为 None
#print(score_dict.get('Thomas',-1))	
#score_dict.pop('Jack')			# 删除键和值
#print(score_dict)
# key类型 : 整型 str
maps={2:'two','one':1}
# set
#s=set([1,1,1,3,3,4])
#s.add(5)		# 添加元素
#s.remove(1)		# 删除元素
#s1=set([2,3,4])	# 集合的交与并
#print(s&s1,s|s1)


### 不可变对象
# 可变对象 list
#a=['c','b','a']
#a.sort()
#print(a)

# 不可变对象 str
#a='abc'
#print(a.replace('a','A'),a)


### 函数
## python 内置函数	
# https://docs.python.org/3/library/functions.html
#print(abs(-1.5))
#print(max(1,4,-5,3))
#int('10')
#float('10.0')
#str(10)
#print(hex(255))
#print(bool(''))
#a=abs
#print(a(-10.0))
#print(isinstance('1',(float,int)))

## 定义函数
#def get_nums():
#	return 1,2
#print(get_nums())	#返回 tuple

## 函数参数
# 位置参数
#def power_pos(x,n):
#	s=1
#	while n>0:
#		n=n-1
#		s=s*x
#	return s
#print(power_pos(2,3))

# 默认参数  必须指向不变对象
#def power_define(x,n=2):
#	pass
# 默认参数为可变对象
#def add_end_change(L=[]):
#	L.append('END')
#	return L
# 不使用默认参数时，正常
#print(add_end_change([1,2,3]))
#print(add_end_change(['a','b']))
# 使用默认参数时，不正常
#print(add_end_change())
#print(add_end_change())
# 原因：默认参数 L 也是变量，且为可变对象
# 改进  使用不变对象初始化
#def add_end_unchange(L=None):
#	if L is None:
#		L=[]
#	L.append('END')
#	return L
#print(add_end_unchange())
#rint(add_end_unchange())

# 可变参数  参数个数可变
# 函数内部接收 tuple
#def calc(*numbers):
#	sum=0
#	for n in numbers:
#		sum=sum+n*n
#	return sum
#print(calc(),calc(1,2))
# 传入 list 或 tuple 作为可变参数
#nums=[1,2,3]
#print(calc(*nums))

# 关键字参数  自动组装为 dict
#def person(name,age,**kw):
#	print('name:',name,'age:',age,'other:',kw)
#person('Tom',20)
#person('Bob',18,city='Beijing')
# 传入 dict 作为关键字参数
#more={'city':'Wuhan','job':'programer'}
#person('Jack',20,**more)
# 形参 kw 获得 more 的拷贝

# 命名关键字参数  限制关键字参数的名字
#def person(name,age,*,city,job):
#	print('* 后的参数为命名关键字参数')
#	print('位置参数 name age :',name,age)
#	print('命名关键字参数 city job :',city,job)
#person('Jack',20,city='Wuhan',job='programer')
# 若函数定义有可变参数，则后面的命名关键字参数不需要 *
#def person(name,age,*args,city='Wuhan',job):
	# 命名关键字参数 city 有默认值 'Wuhan'
#	print(name,age,args,city,job)
#person('Jack',20,'man','birthday',job='programer')

# 参数组合
#def combine(pos,define=0,*args,named_1,named_2,**kw):
#	print('pos=',pos,'define=',define,'args=',args)
#	print('命名关键字参数:',named_1,named_2,'kw=',kw)
#combine(1,2,3,'args_end',named_1='named1',named_2='named2',age=18)
#args=(1,2,3)
#kw={'named_1':'named1','named_2':'named2','age':20,'job':'programer'}
#combine(*args,**kw)


###  递归函数
# 栈溢出  尾递归
# 汉诺塔问题
#def hanoi_tower(n,a,b,c):
#	if n==1:
#		print(a,'-->',c)		
#	else:
#		hanoi_tower(n-1,a,c,b)	# 将n-1个盘子从A借C移到B
#		hanoi_tower(1,a,b,c)	# 将1个盘子从A移到C
#		hanoi_tower(n-1,b,a,c)	# 将n-1个盘子从B借A移到C
#hanoi_tower(3,'A','B','C')


### 高级特性
# 切片
#L=list(range(50))
#print(L[:5])
#print(L[-5:-1])
#print(L[::10])	# 10为步长
#T=tuple(range(10))
#print(T[::2])
#print('ABCDEFG'[::2])

# 迭代
#d={'a':1,'b':2,'c':3}
#for key in d:
#	print(key)
#for value in d.values():
#	print(value)
#for k,v in d.items():
#	print(k,v)
# 迭代对象判断
#from collections import Iterable
#print(isinstance('123',Iterable))
#print(isinstance(123,Iterable))
# list 索引--元素迭代
#for i,value in enumerate('abc'):
#	print(i,value)

# 列表生成式
#print(list(range(1,11)))
#print([x*x for x in range(1,11)])
#print([x*x for x in range(1,11) if x%2==0])
#print([m+n for m in 'ABC' for n in 'XYZ'])
#=['Hello','World','IBM','Apple']
#rint([s.lower() for s in L])
#L=['Hello','World',123,'Apple',None]
#print([s.lower() for s in L if isinstance(s,str)])

# 生成器  generator
# 方法一 列表生成式 [] 改 ()
#g=(x*x for x in range(3))
#print(g)
#print(next(g),next(g),next(g))
#print(next(g))
#for n in g:
#	print(n)

# 方法二 函数 + yield
#def fib(num):
#	n,a,b=0,0,1
#	while n<num:
#		yield b
#		a,b=b,a+b
#		n=n+1
#	return 'done'	
#f=fib(6)
#while True:# 获取生成器返回值
#	try:
#		print('f:',next(f))
#	except StopIteration as e:
#		print('Generator return with:',e.value)
#		break

# 杨辉三角  
#def triangles(n):
#	i,L=0,[1]
#	while i<n:
#		yield L
#		L=[1]+[L[i]+L[i+1] for i in range(len(L)-1)]+[1]
#		i=i+1
#for l in triangles(6):
#	print(l)

# 迭代器 		Iterator 可作用于 next()
# 迭代对象	Iterable 可作用于 for循环
# 生成器都是迭代器
# list dict str 是 Iterable 不是 Iterator
# 用 iter() 函数 变 Iterable 为 Iterator
#from collections import Iterator
#print(isinstance([],Iterator))
#print(isinstance(iter([]),Iterator))


### 函数式编程
## 高阶函数 --复合函数
# 变量可指向函数
# 函数名也是变量
#def add(x,y,f):
#	return f(x)+f(y)
#print(add(-3,5,abs))

## map/reduce
# map 接收两参
# 一为函数 一为 Iterable
# 返回 Iterator
#def f(x):
#	return x*x
#r=map(f,[1,2,3,4,5])
#print(list(r))

# reduce 将函数作用在序列上
# 函数必须接收两个参数
# reduce(f, [x1,x2,x3,x4]) = f(f(f(x1,x2),x3),x4)
#from functools import reduce
#def str2int(ss):
#	def fn(x,y):
#		return x*10+y
#	def char2num(s):
#		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
#	return reduce(fn,map(char2num,ss))
#print(str2int('99')+1)

# str2float
#from functools import reduce
#def char2num(s):
#	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
#def str2float(ss):
#	block=ss.split('.')
#	print(block)
#	inter=reduce(lambda x,y :x*10+y,map(char2num,block[0]))	
#	floator=reduce(lambda x,y:x*0.1+y,map(char2num,block[1][::-1]))
#	return inter+floator*0.1
#print(str2float('10.1'))	

## filter	返回 Iterator
# 接收一个函数和序列
# 返回值为真保留元素
#def not_empty(s):
#	return s and s.strip()	# 剔除指定字符
#print(list(filter(not_empty,['A','B C','',None,'  '])))

# 用 filter 求素数
#def not_divisible(n):	# 筛选函数
#	return lambda x:x%n>0
#def odd_iter():		# 构造奇数序列
#	n=1
#	while True:
#		n=n+2
#		yield n
#def primers():	#返回素数
#	yield 2
#	it=odd_iter()
#	while True:
#		n=next(it)
#		yield n
#		it=filter(not_divisible(n),it)
#for n in primers():	# 打印 50 内的素数
#	if n<50:
#		print(n)
#	else:
#		break

## sorted 
#print(sorted([-5,4,3,-2,1]))
#print(sorted([-5,4,3,-2,1],key=abs))	# 据绝对值排序
#print(sorted([-5,4,3,-2,1],key=abs,reverse=True)) #反向排序

'''
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
	return t[0]
def by_score(t):
	return t[1]
print(sorted(L,key=by_name))
print(sorted(L,key=by_score))
'''

## 返回函数
# 返回的函数并未执行
'''
def count():
	fs=[]
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs
f1,f2,f3=count()
print(f1(),f2(),f3())
'''
'''
def improve():
	def f(j):
		def g():
			return j*j
		return g
	fs=[]
	for i in range(1,4):
		fs.append(f(i))
	return fs
f1,f2,f3=improve()
print(f1(),f2(),f3())
'''
## 匿名函数 lambda
# 以下两者等价
#lambda x:x*x
#def f(x):
#	return x*x

## 装饰器
