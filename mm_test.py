# encoding=utf-8
from sqlhelper import SqlHelper

sql = SqlHelper()

def insert_data_to_users():
	command = ("INSERT IGNORE INTO users "
						"(id, name,  remark)"
						"VALUES(%s, %s, %s)")
	return command


command = insert_data_to_users()

msg = ( "112", "11", "",)

sql.insert_data(command, msg, commit = True)

print ('created user success')
