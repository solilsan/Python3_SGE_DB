from clases import conexion

def cargarCompras():

	try:

		conn = conexion.getCon()

		with conn.cursor() as cursor:

			cursor.execute("SELECT c.id, i.nombre, p.nombre, c.cantidad, c.precio, c.total, c.control FROM COMPRAS c, INVENTARIOS i, PROVEEDORES p WHERE c.id_producto = i.id AND c.id_proveedor = p.id")

			data = cursor.fetchall()

			if data is not None:
				return data

	except Exception as e:

		print("Error: ", e)
		
	finally:

		conn.close()

def ultimoId():

	sql = "SELECT id FROM COMPRAS ORDER BY id DESC LIMIT 1"

	datos = conexion.select(sql)

	if datos is not None:

		return datos[0]

def insertCompra(idc, id_producto, id_proveedor, cantidad, precio, total, control):

	sql = "INSERT INTO COMPRAS(id, id_producto, id_proveedor, cantidad, precio, total, control) VALUES('%d', '%s', '%s', '%s', '%s', '%s', '%s')" % (idc, id_producto, id_proveedor, cantidad, precio, total, control)

	conexion.insert(sql)

def borrarCompra(idCompra):

	sql = "DELETE FROM COMPRAS WHERE id = '%s'" % (idCompra)

	conexion.delete(sql)

def datosCompra(idCompra):

	sql = "SELECT c.id_producto, c.id_proveedor, c.cantidad, c.precio, c.total, i.nombre FROM COMPRAS c, INVENTARIOS i WHERE i.id = c.id_producto AND c.id = '%s'" % (idCompra)

	datos = conexion.select(sql)

	if datos is not None:

		return datos