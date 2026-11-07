
validaciones:

    def validar_nombre(self, nombre):
        if len(nombre) < 3 or len(nombre) > 100:
            return False
        return nombre.replace(" ", "").replace("-", "").replace("'", "").isalpha()

    def validar_documento(self, documento):
        return documento.isdigit() and 3 <= len(documento) <= 15

    def validar_telefono(self, telefono):
        return telefono.isdigit() and len(telefono) == 10

    def validar_correo(self, correo):
        return "@" in correo and "." in correo.split("@")[-1] and len(correo) <= 254

    def validar_direccion(self, direccion):
        return direccion == "" or 5 <= len(direccion) <= 200

    def validar_asunto(self, asunto):
        return 5 <= len(asunto) <= 150

    def validar_descripcion(self, descripcion):
        return 20 <= len(descripcion) <= 2000

    def validar_fecha(self, fecha):
        from datetime import datetime

        try:
            fecha_ingresada = datetime.strptime(fecha, "%d/%m/%Y").date()
            return fecha_ingresada <= datetime.now().date()
        except ValueError:
            return False


