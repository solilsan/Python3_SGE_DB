from clases import conexion

def selectProveedor():

	try:

		conn = conexion.getCon()

		with conn.cursor() as cursor:

			cursor.execute("SELECT id, nombre FROM PROVEEDORES")

			data = cursor.fetchall()

			if data is not None:
				return data

	except Exception as e:

		print("Error: ", e)
		
	finally:

		conn.close()

def cargarProveedores():

	try:

		conn = conexion.getCon()

		with conn.cursor() as cursor:

			cursor.execute("SELECT * FROM PROVEEDORES")

			data = cursor.fetchall()

			if data is not None:
				return data

	except Exception as e:

		print("Error: ", e)
		
	finally:

		conn.close()

def ultimoId():

	sql = "SELECT id FROM PROVEEDORES ORDER BY id DESC LIMIT 1"

	datos = conexion.select(sql)

	if datos is not None:

		return datos[0]

def insertProveedor(idpr, nombre, direccion, telefono, control):

	sql = "INSERT INTO PROVEEDORES(id, nombre, direccion, telefono, control) VALUES('%s', '%s', '%s', '%s', '%s')" % (idpr, nombre, direccion, telefono, control)

	conexion.insert(sql)

def borrarProveedor(idProveedor):

	sql = "DELETE FROM PROVEEDORES WHERE id = '%s'" % (idProveedor)

	conexion.delete(sql)

def verProveedor(idProveedor):

	sql = "SELECT * FROM PROVEEDORES WHERE id = '%s'" % (idProveedor)

	data = conexion.select(sql)

	if data is not None:
		return data

def updateProveedor(nombre, direccion, telefono, idProveedor):

	try:

		conn = conexion.getCon()

		sql = "UPDATE PROVEEDORES SET nombre = '%s', direccion = '%s', telefono = '%s' WHERE id = '%s'" % (nombre, direccion, telefono, idProveedor)
			
		with conn.cursor() as cursor:
			cursor.execute(sql)

		conn.commit()

	except(Exception) as e:

		conn.rollback
		print(e)

	finally:

		conn.close()