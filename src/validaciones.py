
def validar_nombre(nombre):
    if len(nombre) >= 3 and nombre.isalpha():
        return True
    else:
        return False


def validar_documento(numero):
    if numero.isdigit():
        return True
    else:
        return False


def validar_telefono(telefono):
    if telefono.isdigit() and len(telefono) == 10:
        return True
    else:
        return False


def validar_correo(correo):
    if "@" in correo and "." in correo:
        return True
    else:
        return False


def validar_tipo(tipo):
    tipos = ["Peticion", "Queja", "Reclamo", "Sugerencia"]

    if tipo in tipos:
        return True
    else:
        return False


def validar_mascota(mascota):
    mascotas = ["Perro", "Gato"]

    if mascota in mascotas:
        return True
    else:
        return False


def validar_estado(estado):
    estados = ["Registrada", "En proceso", "Solucionada"]

    if estado in estados:
        return True
    else:
        return False

