
import os


class c_archivos:

    def __init__(self):
        self.ruta = os.path.join(os.path.dirname(__file__), "..", "data")

        if not os.path.exists(self.ruta):
            os.makedirs(self.ruta)

    def obtener_archivo(self, tipo):
        return os.path.join(self.ruta, tipo + ".txt")

    def guardar_pqrs(self, tipo, datos):
        archivo = self.obtener_archivo(tipo)

        with open(archivo, "a", encoding="utf-8") as documento:
            documento.write("|".join(datos) + "\n")

    def consultar_pqrs(self, tipo):
        archivo = self.obtener_archivo(tipo)
        registros = []

        if os.path.exists(archivo):
            with open(archivo, "r", encoding="utf-8") as documento:
                for linea in documento:
                    registros.append(linea.strip().split("|"))

        return registros

    def generar_id(self, tipo):
        registros = self.consultar_pqrs(tipo)

        if len(registros) == 0:
            return 1

        return max(int(registro[0]) for registro in registros) + 1

    def actualizar_pqrs(self, tipo, identificacion, nuevo_estado):
        registros = self.consultar_pqrs(tipo)
        actualizado = False

        for registro in registros:
            if registro[0] == identificacion:
                registro[15] = nuevo_estado

                if nuevo_estado == "Solucionada":
                    from datetime import date
                    registro[17] = date.today().strftime("%d/%m/%Y")

                actualizado = True

        if actualizado:
            archivo = self.obtener_archivo(tipo)

            with open(archivo, "w", encoding="utf-8") as documento:
                for registro in registros:
                    documento.write("|".join(registro) + "\n")

        return actualizado

