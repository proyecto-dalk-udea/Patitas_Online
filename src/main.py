
from datetime import datetime, timedelta
from validaciones import c_validaciones
from archivos import c_archivos
from reportes import c_reportes


class c_main:

    def __init__(self):
        self.validaciones = c_validaciones()
        self.archivos = c_archivos()
        self.reportes = c_reportes()

    def registrar_pqrs(self):
        print("\nTIPO DE SOLICITUD")
        print("1. Petición")
        print("2. Queja")
        print("3. Reclamo")
        print("4. Sugerencia")

        opcion = input("Seleccione una opción: ")
        tipos = {
            "1": "Peticion",
            "2": "Queja",
            "3": "Reclamo",
            "4": "Sugerencia"
        }

        if opcion not in tipos:
            print("Opción no válida.")
            return

        tipo = tipos[opcion]

        nombre = input("Nombre completo: ")
        while not self.validaciones.validar_nombre(nombre):
            print("Nombre no válido.")
            nombre = input("Ingrese nuevamente el nombre: ")

        tipo_documento = input("Tipo de documento (CC, TI, CE, PP, NIT): ").upper()
        while tipo_documento not in ["CC", "TI", "CE", "PP", "NIT"]:
            tipo_documento = input("Tipo no válido. Intente nuevamente: ").upper()

        documento = input("Número de documento: ")
        while not self.validaciones.validar_documento(documento):
            documento = input("Número no válido. Ingrese nuevamente: ")

        tipo_telefono = input("Tipo de teléfono (Celular, Fijo, Corporativo, Otro): ").capitalize()
        while tipo_telefono not in ["Celular", "Fijo", "Corporativo", "Otro"]:
            tipo_telefono = input("Tipo no válido. Intente nuevamente: ").capitalize()

        telefono = input("Teléfono de 10 dígitos: ")
        while not self.validaciones.validar_telefono(telefono):
            telefono = input("Teléfono no válido. Intente nuevamente: ")

        correo = input("Correo electrónico: ")
        while not self.validaciones.validar_correo(correo):
            correo = input("Correo no válido. Intente nuevamente: ")

        direccion = input("Dirección (opcional): ")
        while not self.validaciones.validar_direccion(direccion):
            direccion = input("Dirección no válida. Intente nuevamente: ")

        fecha = input("Fecha de registro (DD/MM/AAAA): ")
        while not self.validaciones.validar_fecha(fecha):
            fecha = input("Fecha no válida. Intente nuevamente: ")

        print("\nCANALES DE ATENCIÓN")
        canales = ["Presencial", "Correo electrónico", "Página web",
                   "Teléfono", "Redes sociales", "Otro"]

        for i, canal in enumerate(canales, 1):
            print(i, canal)

        opcion_canal = input("Seleccione el canal: ")
        while not opcion_canal.isdigit() or not 1 <= int(opcion_canal) <= len(canales):
            opcion_canal = input("Opción no válida. Intente nuevamente: ")

        canal = canales[int(opcion_canal) - 1]

        asunto = input("Asunto: ")
        while not self.validaciones.validar_asunto(asunto):
            asunto = input("Asunto no válido. Intente nuevamente: ")

        descripcion = input("Descripción de la solicitud: ")
        while not self.validaciones.validar_descripcion(descripcion):
            descripcion = input("La descripción debe tener entre 20 y 2000 caracteres: ")

        mascota = input("Tipo de mascota (Perro/Gato): ").capitalize()
        while mascota not in ["Perro", "Gato"]:
            mascota = input("Ingrese Perro o Gato: ").capitalize()

        campus = [
            "Campus Medellín - Ciudad Universitaria",
            "Campus Medellín - Ciudadela Robledo",
            "Campus en el Área de la salud",
            "Campus Medellín - Sede de Posgrado",
            "Campus Medellín - Edificio San Ignacio",
            "Campus Medellín - Antigua Escuela de Derecho",
            "Campus Medellín - Casas Patrimoniales",
            "Campus Medellín - Edificio de Extensión"
        ]

        print("\nCAMPUS")
        for i, nombre_campus in enumerate(campus, 1):
            print(i, nombre_campus)

        opcion_campus = input("Seleccione el campus: ")
        while not opcion_campus.isdigit() or not 1 <= int(opcion_campus) <= len(campus):
            opcion_campus = input("Opción no válida. Intente nuevamente: ")

        campus_seleccionado = campus[int(opcion_campus) - 1]

        identificacion = self.archivos.generar_id(tipo)
        fecha_limite = datetime.strptime(fecha, "%d/%m/%Y") + timedelta(days=30)

        datos = [
            str(identificacion), nombre, tipo_documento, documento,
            tipo_telefono, telefono, correo, direccion, tipo, fecha,
            canal, asunto, descripcion.replace("|", "/"), mascota,
            campus_seleccionado, "Registrada",
            fecha_limite.strftime("%d/%m/%Y"), ""
        ]

        self.archivos.guardar_pqrs(tipo, datos)

        print("\nPQRS registrada correctamente.")
        self.imprimir_comprobante(datos)

    def imprimir_comprobante(self, datos):
        linea = "-" * 120

        print("\n" + linea)
        print("PATITAS ONLINE".center(120))
        print("COMPROBANTE DE REGISTRO DE PQRS".center(120))
        print(linea)
        print("Número de registro:", datos[0])
        print("Fecha de registro:", datos[9])
        print("Estado:", datos[15])
        print("Fecha límite de respuesta:", datos[16])
        print(linea)
        print("DATOS DEL SOLICITANTE".center(120))
        print("Nombre:", datos[1])
        print("Documento:", datos[2], datos[3])
        print("Teléfono:", datos[5])
        print("Correo:", datos[6])
        print("Dirección:", datos[7] if datos[7] else "N/A")
        print(linea)
        print("CLASIFICACIÓN DE LA SOLICITUD".center(120))
        print("Tipo:", datos[8])
        print("Canal:", datos[10])
        print("Mascota:", datos[13])
        print("Campus:", datos[14])
        print("Asunto:", datos[11])
        print(linea)

    def consultar_pqrs(self):
        tipos = ["Peticion", "Queja", "Reclamo", "Sugerencia"]

        for tipo in tipos:
            registros = self.archivos.consultar_pqrs(tipo)

            for registro in registros:
                print("\nID:", registro[0])
                print("Tipo:", registro[8])
                print("Nombre:", registro[1])
                print("Asunto:", registro[11])
                print("Estado:", registro[15])

    def cambiar_estado(self):
        tipo = input("Tipo de PQRS (Peticion, Queja, Reclamo, Sugerencia): ").capitalize()

        if tipo not in ["Peticion", "Queja", "Reclamo", "Sugerencia"]:
            print("Tipo de PQRS no válido.")
            return

        identificacion = input("Número de registro: ")
        registros = self.archivos.consultar_pqrs(tipo)

        for registro in registros:
            if registro[0] == identificacion:
                if registro[15] == "Registrada":
                    nuevo_estado = "En proceso"
                elif registro[15] == "En proceso":
                    nuevo_estado = "Solucionada"
                else:
                    print("Esta solicitud ya está solucionada.")
                    return

                self.archivos.actualizar_pqrs(tipo, identificacion, nuevo_estado)
                print("Estado actualizado a:", nuevo_estado)
                return

        print("No se encontró el registro.")

    def menu(self):
        opcion = ""

        while opcion != "5":
            print("\n===== PATITAS ONLINE =====")
            print("1. Registrar PQRS")
            print("2. Consultar PQRS")
            print("3. Cambiar estado de PQRS")
            print("4. Generar reporte")
            print("5. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.registrar_pqrs()
            elif opcion == "2":
                self.consultar_pqrs()
            elif opcion == "3":
                self.cambiar_estado()
            elif opcion == "4":
                self.reportes.generar_reporte(self.archivos)
            elif opcion == "5":
                print("Gracias por utilizar Patitas Online.")
            else:
                print("Opción no válida.")


programa = c_main()
programa.menu()
