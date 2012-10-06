#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2012 Sebastian Ramirez <sebas@khal-el>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import _mysql
import MySQLdb

def main():
	db = _mysql.connect('localhost', 'root', 'sebasftw')
	db.query("create database TestDB")
	db.query("use TestDB")
	db.close()
	db = MySQLdb.connect(host='localhost',user='root',passwd='sebasftw',db='TestDB')
	cursor = db.cursor()
	for line in open("scriptCuentasDB.sql"):
		cursor.execute(line)
	cursor.close()
	cursor = db.cursor()
	for line in open("scriptSPCuentas.sql"):
		cursor.execute(line)
	cursor.close()
	db.close()
	print("done")

if __name__ == '__main__':
	main()

