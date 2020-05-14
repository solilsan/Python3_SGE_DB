from clases import conexion

def insertHistoricoCompra(id_producto, id_proveedor, cantidad, precio, total, fecha, nombrep):

	sql = "INSERT INTO HISTORICOCOMPRAS(id_producto, id_proveedor, cantidad, precio, total, fecha, nombrep) VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (id_producto, id_proveedor, cantidad, precio, total, fecha, nombrep)

	conexion.insert(sql)


def historicoCompras():

	try:

		conn = conexion.getCon()

		with conn.cursor() as cursor:

			cursor.execute("SELECT id, id_producto, id_proveedor, SUM(cantidad), precio, SUM(total), fecha, nombrep FROM HISTORICOCOMPRAS GROUP By nombrep")

			data = cursor.fetchall()

			if data is not None:
				return data

	except Exception as e:

		print("Error: ", e)
		
	finally:

		conn.close()