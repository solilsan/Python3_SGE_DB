from clases import conexion

class Usuario:

	def __init__(self, nombre, password):
		self.id = id
		self.nombre = nombre
		self.password = password

	def login(self):
		datos = conexion.select("SELECT id, nombre, pass FROM USUARIOS WHERE nombre = '%s' AND pass = '%s';" % (self.nombre, self.password))
		if datos is not None:
			return datos[0]
		else:
			return False