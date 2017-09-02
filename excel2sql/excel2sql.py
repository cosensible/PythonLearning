#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql,xlrd

def read_excel():
	L=[]
	data=xlrd.open_workbook(r'./test.xlsx')
	table=data.sheet_by_index(0)
	for irow in range(table.nrows):
		for icol in range(table.ncols):
			vcell=table.cell(irow,icol).value
			if vcell!='':
				L.append(vcell)
				break
	return L

def db_init():
	db = pymysql.connect("127.0.0.1","root","lcg","test",charset='utf8' )
	dbc=db.cursor()
	dbc.execute("DROP TABLE IF EXISTS myfile")

	sql="""CREATE TABLE myfile (
			id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
			name CHAR(50) NOT NULL
		); """
	dbc.execute(sql)
	db.close()

def db_write():
	db = pymysql.connect("127.0.0.1","root","lcg","test",charset='utf8' )
	dbc=db.cursor()
	for item in read_excel():
		sql="INSERT INTO myfile(name) VALUES (%s)"
		dbc.execute(sql,item)
		db.commit()
	# 关闭数据库连接
	db.close()

def db_read():
	db = pymysql.connect("127.0.0.1","root","lcg","test",charset='utf8' )
	dbc=db.cursor()
	sql = "SELECT * FROM myfile"
	try:
		dbc.execute(sql)
		res=dbc.fetchall()
		for row in res:
			print(row)
	except:
		print("Error: unable to fetch data")
	# 关闭数据库连接
	db.close()

if __name__ == '__main__':
	db_init()
	db_write()
	db_read()