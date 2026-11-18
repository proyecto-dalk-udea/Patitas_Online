
import os
from datetime import date


class c_archivos:

    # Crear y localizar la carpeta de datos
    def __init__(self):
        self.ruta = os.path.join(
            os.path.dirname(__file__), "..", "data"
        )

        if not os.path.exists(self.ruta):
            os.makedirs(self.ruta)

    # Obtener la ruta del archivo correspondiente
    def obtener_archivo(self, tipo):
        tipos = ["Peticion", "Queja", "Reclamo", "Sugerencia"]

        if tipo not in tipos:
            raise ValueError("Tipo de PQRS no válido.")

        return os.path.join(self.ruta, tipo + ".txt")

    # Guardar un nuevo registro
    def guardar_pqrs(self, tipo, datos):
        archivo = self.obtener_archivo(tipo)

        with open(archivo, "a", encoding="utf-8") as documento:
            documento.write("|".join(datos) + "\n")

    # Consultar los registros almacenados
    def consultar_pqrs(self, tipo):
        archivo = self.obtener_archivo(tipo)
        registros = []

        if os.path.exists(archivo):
            with open(archivo, "r", encoding="utf-8") as documento:
                for linea in documento:
                    if linea.strip():
                        registro = linea.rstrip("\n").split("|")

                        if len(registro) == 18:
                            registros.append(registro)

        return registros

    # Generar un número consecutivo independiente
    def generar_id(self, tipo):
        registros = self.consultar_pqrs(tipo)

        if len(registros) == 0:
            return 1

        return max(int(registro[0]) for registro in registros) + 1

    # Actualizar el estado de una solicitud
    def actualizar_pqrs(self, tipo, identificacion, nuevo_estado):
        registros = self.consultar_pqrs(tipo)
        actualizado = False

        for registro in registros:
            if registro[0] == identificacion:

                if registro[15] == "Registrada" and nuevo_estado == "En proceso":
                    registro[15] = nuevo_estado
                    actualizado = True

                elif registro[15] == "En proceso" and nuevo_estado == "Solucionada":
                    registro[15] = nuevo_estado
                    registro[17] = date.today().strftime("%d/%m/%Y")
                    actualizado = True

                break

        if actualizado:
            archivo = self.obtener_archivo(tipo)

            with open(archivo, "w", encoding="utf-8") as documento:
                for registro in registros:
                    documento.write("|".join(registro) + "\n")

        return actualizado
