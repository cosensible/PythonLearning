#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test moudle'

__author__='MrLi'

import sys

def hello():
	args=sys.argv
	if len(args)==1:
		print('Hello world!')
	elif len(args)==2:
		print('Hello %s!'%args[1])
	else:
		print('Too many arguments!')

if __name__=='__main__':
	hello()

# 第四行是模块的文档注释，模块代码的第一个字符串
# 第六行是注明作者名	
# 命令行运行模块时 __name__=='__main__'
# 导入模块时 	__name__!='__main__'