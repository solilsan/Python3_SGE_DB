import pymysql

#Base de datos online, va muy lenta asi que con calma, ya que es un entorno de pruebas gratis
"""
def getCon():
	try:

		conexion = pymysql.connect(	
			host='www.db4free.net',
	   	    user='solilsan',
	   	    password='12345Abcde',
	   	    db='basedatossge'
	   	)

		return conexion

	except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
		print("Ocurrió un error al conectar: ", e)
"""

#Base de datos local, necesitamos xampp o algun server con mysql
def getCon():
	try:

		conexion = pymysql.connect(	
			host='localhost',
	   	    user='root',
	   	    password='',
	   	    db='basedatossge'
	   	)

		return conexion

	except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
		print("Ocurrió un error al conectar: ", e)

def select(sql):

	try:

		conn = getCon()

		with conn.cursor() as cursor:

			cursor.execute(sql)

			data = cursor.fetchone()

			return data

	except Exception as e:

		print("Error: ", e)
		
	finally:

		conn.close()

def delete(sql):

	try:

		conn = getCon()

		cursor = conn.cursor()

		cursor.execute(sql)

		conn.commit()

	except Exception as e:

		print("Error: ", e)
		
	finally:

		conn.close()

def insert(sql):

	try:

		conn = getCon()
			
		with conn.cursor() as cursor:
			cursor.execute(sql)

		conn.commit()

	except(Exception) as e:

		conn.rollback
		print(e)

	finally:

		conn.close()