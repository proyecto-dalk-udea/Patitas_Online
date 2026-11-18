# Validaciones del programa Patitas Online

from datetime import datetime
import re


class c_validaciones:

    # Validar el nombre completo
    def validar_nombre(self, nombre):
        if len(nombre) < 3 or len(nombre) > 100:
            return False

        nombre = nombre.replace(" ", "").replace("-", "").replace("'", "")
        return nombre.isalpha()

    # Validar el número de documento
    def validar_documento(self, documento):
        return documento.isdecimal() and documento.isascii() and 3 <= len(documento) <= 15

    # Validar el teléfono
    def validar_telefono(self, telefono):
        return telefono.isascii() and telefono.isdecimal() and len(telefono) == 10

    # Validar el correo electrónico
    def validar_correo(self, correo):
        patron = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+"

        return (
            len(correo) <= 254
            and re.fullmatch(patron, correo) is not None
        )

    # Validar la dirección opcional
    def validar_direccion(self, direccion):
        if direccion == "":
            return True

        patron = r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9 #./-]+"

        return (
            5 <= len(direccion) <= 200
            and re.fullmatch(patron, direccion) is not None
            and direccion.strip() != ""
        )

    # Validar el asunto
    def validar_asunto(self, asunto):
        return 5 <= len(asunto) <= 150 and asunto.strip() != ""

    # Validar la descripción
    def validar_descripcion(self, descripcion):
        return 20 <= len(descripcion) <= 2000 and descripcion.strip() != ""

    # Validar la fecha
    def validar_fecha(self, fecha):
        try:
            fecha_ingresada = datetime.strptime(fecha, "%d/%m/%Y").date()
            return fecha_ingresada <= datetime.now().date()

        except ValueError:
            return False
            
