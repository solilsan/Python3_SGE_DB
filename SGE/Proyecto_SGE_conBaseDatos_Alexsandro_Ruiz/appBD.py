from flask import Flask, request, session, render_template
import json, csv, os, datetime

#iniciando app para la redirección de html.
app = Flask(__name__)

app.secret_key = 'esto-es-una-clave-muy-secreta' #encriptar session.

@app.errorhandler(404)
def page_not_found(e):

    if 'loginC' in session:
    	if session['loginC']:
    		return render_template('inicio.html')
    	else:
    		return render_template('index.html')
    else:
    	return render_template('index.html')

@app.errorhandler(405)
def method_not_allowed(e):

    if 'loginC' in session:
    	if session['loginC']:
    		return render_template('inventario.html')
    	else:
    		return render_template('index.html')
    else:
    	return render_template('index.html')

#Redirección a /index.html.
@app.route('/index.html')
def index():
	#Comprobamos si existe la session 'loginC'.
	#Si existe comprobamos si es True o False, si es True cargamos la página.
	#Si no exite la creamos en False y hacemos una redirección a index.html.
	if 'loginC' in session:
		if session['loginC']:
			return render_template('inicio.html')
		else:
			return render_template('index.html')
	else:
		return render_template('index.html')

#Redirección a /inicio.html.
@app.route('/inicio.html')
def inicio():
	#Comprobamos si 'loginC' es True
	if session['loginC']:
		return render_template('inicio.html')

	else:
		return render_template('index.html')

@app.route('/login', methods=['POST'])
def signUpUser():
    #Abrimos el archivo listaUsuarios.csv y comprobamos si esta el usuario

    from clases.Usuario import Usuario

    session['loginC'] = False

    usu = Usuario(request.form['username'], request.form['password'])

    data = usu.login()

    if data != False:
    	session['idUser'] = data
    	session['loginC'] = True

    if session['loginC']:
    	return json.dumps(1);

    else:
    	return json.dumps(0);

@app.route('/logout', methods=['POST'])
def logoutUser():

    if session['loginC']:

    	session['loginC'] = False
    	return json.dumps(1);

    else:
    	return json.dumps(0);

#---------------------------------------INVENTARIO-----------------------------------------
#Redireccion a /inventario.html
@app.route('/inventario.html')
def inventario():
	if 'loginC' in session:

		if session['loginC']:

			valido = False

			from clases import Departamento

			data = Departamento.comprobarAsignado("1", session['idUser'])

			if data:
				valido = True

			if valido:
				return render_template('inventario.html')

			else:
				return render_template('inicio.html')

		else:
			return render_template('index.html')

	else:
		return render_template('index.html')

#Cargar la lista de los productos
@app.route('/cargarInventario', methods=['POST'])
def cargarInventario():

	from clases import Inventario

	datos = Inventario.cargarInventario()

	return json.dumps({'datos':datos})

#Borrar un producto seleccionado
@app.route('/borrarInventario', methods=['POST'])
def borrarInventario():

	from clases import Inventario

	Inventario.borrarProducto(request.form['idInventario'])

	return json.dumps(1);

@app.route('/selectInventario', methods=['POST'])
def selectInventario():

	from clases import Inventario

	listaDatos = Inventario.selectInventario()

	return json.dumps({'datos':listaDatos})

#Crear un producto
@app.route('/crearProducto', methods=['POST'])
def crearProducto():

	from clases import Inventario

	idv = Inventario.ultimoId()

	ID = 0

	try:
		ID = int((int(idv) + 1)) #Recogemos ultimo id y le sumamos 1
	except Exception:
		ID = 1

	idp = ID
	nombre = request.form['nombreP']
	tipo = request.form['tipoP']
	cantidad = request.form['contidadP']
	precioCompra = str(request.form['precioCompraP']) + "$"
	precioVenta = str(request.form['precioVentaP']) + "$"
	controles = '<button onclick="modificar({})" class="btn btn btn-outline-warning" type="button">Modificar</button><button onclick="borrar({})" class="btn btn btn-outline-danger mt-2" type="button">Borrar</button>'.format(ID, ID)

	Inventario.insertProducto(idp, nombre, tipo, cantidad, precioCompra, precioVenta, controles)

	return json.dumps(1);

#Cargar datos de un produto seleccionado
@app.route('/verProducto', methods=['POST'])
def verProducto():

	from clases import Inventario

	datos = Inventario.verProducto(request.form['idInventario'])

	datosP = []

	datosP.append(datos[0])
	datosP.append(datos[1])
	datosP.append(datos[2])
	datosP.append(datos[3])
	datosP.append(datos[4][:-1])
	datosP.append(datos[5][:-1])

	return json.dumps({'datos':datosP}) #Devolvemos los datos en forma json

#Modificar datos de un producto seleccionado
@app.route('/actualizarProducto', methods=['POST'])
def actualizarProducto():

	from clases import Inventario

	precioCompra = request.form['precioCompraAP']
	precioVenta = request.form['precioVentaAP']

	Inventario.updateProducto(request.form['nombreAP'], request.form['tipoAP'], request.form['contidadAP'], str(precioCompra) + "$", str(precioVenta) + "$", request.form['idAP'])

	return json.dumps(1);

#---------------------------------------INVENTARIO-----------------------------------------


#---------------------------------------PROVEEDOR-----------------------------------------
@app.route('/selectProveedor', methods=['POST'])
def selectProveedor():

	from clases import Proveedor

	listaDatos = Proveedor.selectProveedor()

	return json.dumps({'datos':listaDatos})

@app.route('/proveedor.html')
def proveedor():
	if 'loginC' in session:

		if session['loginC']:

			valido = False

			from clases import Departamento

			data = Departamento.comprobarAsignado("2", session['idUser'])

			if data:
				valido = True

			if valido:
				return render_template('proveedor.html')

			else:
				return render_template('inicio.html')

		else:
			return render_template('index.html')

	else:
		return render_template('index.html')

@app.route('/cargarProveedores', methods=['POST'])
def cargarProveedores():

	from clases import Proveedor

	listaDatos = Proveedor.cargarProveedores()

	return json.dumps({'datos':listaDatos})

@app.route('/newProveedor', methods=['POST'])
def crearProveedor():

	from clases import Proveedor
	
	idv = Proveedor.ultimoId()

	ID = 0

	try:
		ID = int((int(idv) + 1)) #Recogemos ultimo id y le sumamos 1
	except Exception:
		ID = 1

	idpr = ID
	nombre = request.form['nombreProveedor']
	direccion = request.form['calleProveedor']
	telefono = request.form['telefonoProveedor']
	controles = '<button onclick="modificar({})" class="btn btn btn-outline-warning" type="button">Modificar</button><button onclick="borrar({})" class="btn btn btn-outline-danger mt-2" type="button">Borrar</button>'.format(ID, ID)

	Proveedor.insertProveedor(idpr, nombre, direccion, telefono, controles)

	return json.dumps(1);

@app.route('/borrarProveedor', methods=['POST'])
def borrarProveedor():

	from clases import Proveedor

	Proveedor.borrarProveedor(request.form['idProveedor'])

	return json.dumps(1);

@app.route('/verProveedor', methods=['POST'])
def verProveedor():

	from clases import Proveedor

	datos = Proveedor.verProveedor(request.form['idProveedor'])

	datosP = []

	datosP.append(datos[0])
	datosP.append(datos[1])
	datosP.append(datos[2])
	datosP.append(datos[3])

	return json.dumps({'datos':datosP}) #Devolvemos los datos en forma json

@app.route('/actualizarProveedor', methods=['POST'])
def actualizarProveedor():

	from clases import Proveedor

	Proveedor.updateProveedor(request.form['nProveedor'], request.form['cProveedor'], request.form['tProveedor'], request.form['idProveedor'])

	return json.dumps(1);

#---------------------------------------PROVEEDOR-----------------------------------------


#---------------------------------------COMPRAS-----------------------------------------
@app.route('/compras.html')
def compras():
	if 'loginC' in session:

		if session['loginC']:

			valido = False

			from clases import Departamento

			data = Departamento.comprobarAsignado("2", session['idUser'])

			if data:
				valido = True

			if valido:
				return render_template('compras.html')

			else:
				return render_template('inicio.html')

		else:
			return render_template('index.html')

	else:
		return render_template('index.html')

#Cargar la lista de los productos
@app.route('/cargarCompras', methods=['POST'])
def cargarCompras():

	from clases import Compras

	listaDatos = Compras.cargarCompras()

	return json.dumps({'datos':listaDatos})

@app.route('/crearCompra', methods=['POST'])
def crearCompra():

	from clases import Compras
	
	idv = Compras.ultimoId()

	ID = 0

	try:
		ID = int((int(idv) + 1)) #Recogemos ultimo id y le sumamos 1
	except Exception:
		ID = 1
	
	idc = ID
	producto = request.form['sProductos']
	proveedor = request.form['sProveedor']
	cantidad = str(request.form['cantidadCP'])
	precio = str(request.form['precioCP']) + "$"
	total = str(request.form['totalCP']) + "$"
	controles = '<button onclick="comprar({})" class="btn btn btn-outline-warning" type="button">Comprar</button><button onclick="borrar({})" class="btn btn btn-outline-danger mt-2" type="button">Borrar</button>'.format(ID, ID)

	Compras.insertCompra(idc, producto, proveedor, cantidad, precio, total, controles)

	return json.dumps(1);

@app.route('/borrarCompra', methods=['POST'])
def borrarCompra():

	from clases import Compras

	Compras.borrarCompra(request.form['idCompra'])

	return json.dumps(1);

@app.route('/comprarCompra', methods=['POST'])
def comprarCompra():

	from clases import Compras
	from clases import Inventario
	from clases import HistoricoCompra

	try:

		datosCompra = Compras.datosCompra(request.form['idCompra'])
	
		Inventario.updateCantidadProducto(datosCompra[2], datosCompra[0])
	
		now = datetime.datetime.now()
	
		fecha = (str(now.day) + "/" + str(now.month) + "/" + str(now.year))
	
		HistoricoCompra.insertHistoricoCompra(datosCompra[0], datosCompra[1], datosCompra[2], datosCompra[3], datosCompra[4], fecha, datosCompra[5])
	
		Compras.borrarCompra(request.form['idCompra'])

	except Exception:

		print("Error", e)

	return json.dumps(1);

#---------------------------------------COMPRAS-----------------------------------------


#---------------------------------------HISTORICOCOMPRAS-----------------------------------------

@app.route('/historicoCompras.html')
def historicoCompras():
	if 'loginC' in session:

		if session['loginC']:

			valido = False

			from clases import Departamento

			data = Departamento.comprobarAsignado("2", session['idUser'])

			if data:
				valido = True

			if valido:
				return render_template('historicoCompras.html')

			else:
				return render_template('inicio.html')

		else:
			return render_template('index.html')

	else:
		return render_template('index.html')

@app.route('/cargarHistorialCompras', methods=['POST'])
def cargarHistorialCompras():

	from clases import HistoricoCompra

	index = 0

	datos = HistoricoCompra.historicoCompras()

	listaDatos = []

	for rowlc in datos:

		nDatos = []

		nDatos.append(rowlc[1])
		nDatos.append(rowlc[3])
		nDatos.append(rowlc[4])
		nDatos.append(rowlc[5])
		nDatos.append(rowlc[6][3:-5])
		nDatos.append(rowlc[7])

		listaDatos.append(nDatos)

	return json.dumps({'datos':listaDatos})

#---------------------------------------HISTORICOCOMPRAS-----------------------------------------


#---------------------------------------CLIENTES-----------------------------------------

@app.route('/selectCliente', methods=['POST'])
def selectCliente():

	from clases import Cliente

	listaDatos = Cliente.selectCliente()

	return json.dumps({'datos':listaDatos})

@app.route('/cliente.html')
def cliente():
	if 'loginC' in session:

		if session['loginC']:

			valido = False

			from clases import Departamento

			data = Departamento.comprobarAsignado("3", session['idUser'])

			if data:
				valido = True

			if valido:
				return render_template('cliente.html')

			else:
				return render_template('inicio.html')

		else:
			return render_template('index.html')

	else:
		return render_template('index.html')

@app.route('/cargarClientes', methods=['POST'])
def cargarClientes():

	from clases import Cliente

	listaDatos = Cliente.cargarClientes()

	return json.dumps({'datos':listaDatos})

@app.route('/newCliente', methods=['POST'])
def newCliente():

	from clases import Cliente
	
	idv = Cliente.ultimoId()

	ID = 0

	try:
		ID = int((int(idv) + 1)) #Recogemos ultimo id y le sumamos 1
	except Exception:
		ID = 1

	idc = ID
	nombre = request.form['nombreCliente']
	direccion = request.form['calleCliente']
	telefono = request.form['telefonoCliente']
	controles = '<button onclick="modificar({})" class="btn btn btn-outline-warning" type="button">Modificar</button><button onclick="borrar({})" class="btn btn btn-outline-danger mt-2" type="button">Borrar</button>'.format(ID, ID)

	Cliente.insertCliente(idc, nombre, direccion, telefono, controles)

	return json.dumps(1);

@app.route('/borrarCliente', methods=['POST'])
def borrarCliente():

	from clases import Cliente

	Cliente.borrarCliente(request.form['idCliente'])

	return json.dumps(1);

@app.route('/verCliente', methods=['POST'])
def verCliente():

	from clases import Cliente

	datos = Cliente.verCliente(request.form['idCliente'])

	datosP = []

	datosP.append(datos[0])
	datosP.append(datos[1])
	datosP.append(datos[2])
	datosP.append(datos[3])

	return json.dumps({'datos':datosP}) #Devolvemos los datos en forma json

@app.route('/actualizarCliente', methods=['POST'])
def actualizarCliente():

	from clases import Cliente

	Cliente.updateCliente(request.form['nCliente'], request.form['cCliente'], request.form['tCliente'], request.form['idCliente'])

	return json.dumps(1);

#---------------------------------------CLIENTES-----------------------------------------


#---------------------------------------VENTAS-----------------------------------------

@app.route('/ventas.html')
def ventas():
	if 'loginC' in session:

		if session['loginC']:

			valido = False

			from clases import Departamento

			data = Departamento.comprobarAsignado("3", session['idUser'])

			if data:
				valido = True

			if valido:
				return render_template('ventas.html')

			else:
				return render_template('inicio.html')

		else:
			return render_template('index.html')

	else:
		return render_template('index.html')

@app.route('/cargarVentas', methods=['POST'])
def cargarVentas():

	from clases import Ventas

	listaDatos = Ventas.cargarVentas()

	return json.dumps({'datos':listaDatos})

@app.route('/crearVenta', methods=['POST'])
def crearVenta():

	from clases import Ventas

	idv = Ventas.ultimoId()

	ID = 0

	try:
		ID = int((int(idv) + 1)) #Recogemos ultimo id y le sumamos 1
	except Exception:
		ID = 1
	
	idve = ID
	producto = request.form['sProductos']
	cliente = request.form['sCliente']
	cantidad = str(request.form['cantidadCP'])
	precio = str(request.form['precioCP']) + "$"
	total = str(request.form['totalCP']) + "$"
	controles = '<button onclick="vender({})" class="btn btn btn-outline-warning" type="button">Vender</button><button onclick="borrar({})" class="btn btn btn-outline-danger mt-2" type="button">Borrar</button>'.format(ID, ID)

	Ventas.insertVenta(idve, producto, cliente, cantidad, precio, total, controles)

	return json.dumps(1);

@app.route('/borrarVenta', methods=['POST'])
def borrarVenta():

	from clases import Ventas

	Ventas.borrarVenta(request.form['idVenta'])

	return json.dumps(1);

@app.route('/realizarVenta', methods=['POST'])
def realizarVenta():

	from clases import Ventas
	from clases import Inventario

	datosVenta = Ventas.datosVenta(request.form['idVenta'])

	Inventario.updateCantidadProductoVenta(datosVenta[0], datosVenta[1])

	Ventas.borrarVenta(request.form['idVenta'])

	return json.dumps(1);

#---------------------------------------VENTAS-----------------------------------------

#Inicio de la aplicación.
if __name__ == "__main__":
    app.run()