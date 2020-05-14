from clases import conexion

def selectCliente():

	try:

		conn = conexion.getCon()

		with conn.cursor() as cursor:

			cursor.execute("SELECT id, nombre FROM CLIENTES")

			data = cursor.fetchall()

			if data is not None:
				return data

	except Exception as e:

		print("Error: ", e)
		
	finally:

		conn.close()

def cargarClientes():

	try:

		conn = conexion.getCon()

		with conn.cursor() as cursor:

			cursor.execute("SELECT * FROM CLIENTES")

			data = cursor.fetchall()

			if data is not None:
				return data

	except Exception as e:

		print("Error: ", e)
		
	finally:

		conn.close()

def ultimoId():

	sql = "SELECT id FROM CLIENTES ORDER BY id DESC LIMIT 1"

	datos = conexion.select(sql)

	if datos is not None:

		return datos[0]

def insertCliente(idc, nombre, direccion, telefono, control):

	sql = "INSERT INTO CLIENTES(id, nombre, direccion, telefono, control) VALUES('%s', '%s', '%s', '%s', '%s')" % (idc, nombre, direccion, telefono, control)

	conexion.insert(sql)

def borrarCliente(idCliente):

	sql = "DELETE FROM CLIENTES WHERE id = '%s'" % (idCliente)

	conexion.delete(sql)

def verCliente(idCliente):

	sql = "SELECT * FROM CLIENTES WHERE id = '%s'" % (idCliente)

	data = conexion.select(sql)

	if data is not None:
		return data

def updateCliente(nombre, direccion, telefono, idCliente):

	try:

		conn = conexion.getCon()

		sql = "UPDATE CLIENTES SET nombre = '%s', direccion = '%s', telefono = '%s' WHERE id = '%s'" % (nombre, direccion, telefono, idCliente)
			
		with conn.cursor() as cursor:
			cursor.execute(sql)

		conn.commit()

	except(Exception) as e:

		conn.rollback
		print(e)

	finally:

		conn.close()