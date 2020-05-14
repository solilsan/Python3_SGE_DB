from clases import conexion

def comprobarAsignado(idDepart, idUser):
	datos = conexion.select("SELECT u.nombre FROM USUARIOS u, DEPARTAMENTOS d, USUDEPART ud WHERE ud.id_departamento = '%s' AND ud.id_usuario = '%s';" % (idDepart, idUser))

	if datos is not None:
		return True
	else:
		return False