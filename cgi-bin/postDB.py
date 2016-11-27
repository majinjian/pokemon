import pymysql

dbpass = '931119ma'

create_post_table = '''CREATE TABLE IF NOT EXISTS post (
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	author VARCHAR(50) NOT NULL,
	content CHAR(255) NOT NULL,
	date DATETIME NOT NULL,
	likes INT,
	likers TEXT
)'''

def  connect():

	try:
		conn = pymysql.connect(host = 'localhost' , user = 'root' , password = dbpass , db = 'web_pokemon')
		return conn
	except Exception :
		print 'An error has ocurred when trying to connect to the database' 
		return None

def excute(sql):
	con = connect()
	if con == None:
		return 'Error'
	try:
		with con.cursor() as cursor:
			s = cursor.execute(sql);
			con.commit()
			result = cursor.fetchone()
			con.close()
			return result
	except Exception as e:
		print 'can not excute the sql command'
		con.close()
		return 'Error'


