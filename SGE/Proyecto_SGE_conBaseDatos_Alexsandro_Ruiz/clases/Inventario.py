from clases import conexion

def cargarInventario():

	try:

		conn = conexion.getCon()

		with conn.cursor() as cursor:

			cursor.execute("SELECT * FROM INVENTARIOS")

			data = cursor.fetchall()

			if data is not None:
				return data

	except Exception as e:

		print("Error: ", e)
		
	finally:

		conn.close()

def borrarProducto(idProducto):

	sql = "DELETE FROM INVENTARIOS WHERE id = '%s'" % (idProducto)

	conexion.delete(sql)

def ultimoId():

	sql = "SELECT id FROM INVENTARIOS ORDER BY id DESC LIMIT 1"

	datos = conexion.select(sql)

	if datos is not None:

		return datos[0]

def insertProducto(idp, nombre, tipo, cantidad, precioCompra, precioVenta, controles):

	sql = "INSERT INTO INVENTARIOS(id, nombre, tipo, cantidad, precio_compra, precio_venta, control) VALUES('%d', '%s', '%s', '%s', '%s', '%s', '%s')" % (idp, nombre, tipo, cantidad, precioCompra, precioVenta, controles)

	conexion.insert(sql)

def verProducto(idProducto):

	sql = "SELECT * FROM INVENTARIOS WHERE id = '%s'" % (idProducto)

	data = conexion.select(sql)

	if data is not None:
		return data

def updateProducto(nombre, tipo, cantidad, precioCompra, precioVenta, idProducto):

	try:

		conn = conexion.getCon()

		sql = "UPDATE INVENTARIOS SET nombre = '%s', tipo = '%s', cantidad = '%s', precio_compra = '%s', precio_venta = '%s' WHERE id = '%s'" % (nombre, tipo, cantidad, precioCompra, precioVenta, idProducto)
			
		with conn.cursor() as cursor:
			cursor.execute(sql)

		conn.commit()

	except(Exception) as e:

		conn.rollback
		print(e)

	finally:

		conn.close()

def selectInventario():

	try:

		conn = conexion.getCon()

		with conn.cursor() as cursor:

			cursor.execute("SELECT id, nombre, precio_compra FROM INVENTARIOS")

			data = cursor.fetchall()

			if data is not None:
				return data

	except Exception as e:

		print("Error: ", e)
		
	finally:

		conn.close()

def updateCantidadProducto(cantidad, idProducto):

	try:

		conn = conexion.getCon()

		sql = "SELECT cantidad FROM INVENTARIOS WHERE id = '%s'" % (idProducto)

		with conn.cursor() as cursor:

			cursor.execute(sql)

			data = cursor.fetchone()

		total = int(cantidad) + int(data[0])

		sql = "UPDATE INVENTARIOS SET cantidad = '%s' WHERE id = '%s'" % (total, idProducto)
			
		with conn.cursor() as cursor:
			cursor.execute(sql)

		conn.commit()

	except(Exception) as e:

		conn.rollback
		print(e)

	finally:

		conn.close()

def updateCantidadProductoVenta(cantidad, idProducto):

	try:

		conn = conexion.getCon()

		sql = "SELECT cantidad FROM INVENTARIOS WHERE id = '%s'" % (idProducto)

		with conn.cursor() as cursor:

			cursor.execute(sql)

			data = cursor.fetchone()

		total = int(data[0]) - int(cantidad)

		sql = "UPDATE INVENTARIOS SET cantidad = '%s' WHERE id = '%s'" % (total, idProducto)
			
		with conn.cursor() as cursor:
			cursor.execute(sql)

		conn.commit()

	except(Exception) as e:

		conn.rollback
		print(e)

	finally:

		conn.close()