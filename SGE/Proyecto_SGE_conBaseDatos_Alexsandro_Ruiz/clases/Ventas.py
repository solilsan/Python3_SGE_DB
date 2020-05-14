from clases import conexion

def cargarVentas():

	try:

		conn = conexion.getCon()

		with conn.cursor() as cursor:

			cursor.execute("SELECT v.id, i.nombre, c.nombre, v.cantidad, v.precio, v.total, v.control FROM VENTAS v, INVENTARIOS i, CLIENTES c WHERE v.id_producto = i.id AND v.id_cliente = c.id")

			data = cursor.fetchall()

			if data is not None:
				return data

	except Exception as e:

		print("Error: ", e)
		
	finally:

		conn.close()

def ultimoId():

	sql = "SELECT id FROM VENTAS ORDER BY id DESC LIMIT 1"

	datos = conexion.select(sql)

	if datos is not None:

		return datos[0]

def insertVenta(idve, id_producto, id_cliente, cantidad, precio, total, control):

	sql = "INSERT INTO VENTAS(id, id_producto, id_cliente, cantidad, precio, total, control) VALUES('%d', '%s', '%s', '%s', '%s', '%s', '%s')" % (idve, id_producto, id_cliente, cantidad, precio, total, control)

	conexion.insert(sql)

def borrarVenta(idVenta):

	sql = "DELETE FROM VENTAS WHERE id = '%s'" % (idVenta)

	conexion.delete(sql)

def datosVenta(idVenta):

	sql = "SELECT v.cantidad, i.id FROM VENTAS v, INVENTARIOS i WHERE i.id = v.id_producto AND v.id = '%s'" % (idVenta)

	datos = conexion.select(sql)

	if datos is not None:

		return datos