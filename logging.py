# !/usr/bin/env python3
# Assignment 2 - 
# Author: Lyssette Williams

import sqlite3
import os
import logging

def debug_config():
logging.basicConfig(level=logging.DEBUG,format = "[Artists]:%(asctime)s:%(levelname)s:%(message)s")  #DEBUG,INFO,ERROR,WARNING,CRITICAL

def db_checkfile(dbfilename):
	if os.path.exists(dbfilename) and os.path.getsize(dbfilename) > 0:
		logging.debug("{a} found and not zero size".format(a=dbfilename))
	else:
		logging.error("{a} not found or zero size".format(a=dbfilename))

def db_connect(dbfilename):
	con = sqlite3.connect.(dbfilename)
	logging.debug("DB Connected".format())
	return con

def db_cursor(con):
	cur = con.cursor()
	logging.debug('Cursor set'.format())
	return cur

def db_runquery(cur, query):
	cur.execute(query)
	result = cur.execute.fetchall()
	logging.debug('DB Query executed and returned'.format())
	return result

def display():
	print('Program Logging')
	print('  ')

def main():
	dbfilename = 'whatever.db'
	debug_config()
	display()
	db_checkfile(dbfilename)
	try:
		con = db_connect(dbfilename)
		cur = db_cursor(con)
		query = 'Select Sqlite Version()'
		res = db_runquery(cur, query)
		print('Sqlite version: ' res[0][0])
	except sqlite3.error as error:
		logging.error('Error executing query')
	finally:
		if con:
			con.close()
			logging.debug('[Info] DB closed',format())		


if __name__ == "__main__":
  main() 

