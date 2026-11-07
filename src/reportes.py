
from datetime import datetime


class c_reportes:

    def generar_reporte(self, archivos):
        tipos = ["Peticion", "Queja", "Reclamo", "Sugerencia"]

        total = 0
        registradas = 0
        en_proceso = 0
        solucionadas = 0
        mascotas = {"Perro": 0, "Gato": 0}
        tiempos = []

        for tipo in tipos:
            registros = archivos.consultar_pqrs(tipo)
            total += len(registros)

            for registro in registros:
                estado = registro[15]

                if estado == "Registrada":
                    registradas += 1
                elif estado == "En proceso":
                    en_proceso += 1
                elif estado == "Solucionada":
                    solucionadas += 1

                if registro[13] in mascotas:
                    mascotas[registro[13]] += 1

                if registro[17] != "":
                    fecha_inicio = datetime.strptime(registro[9], "%d/%m/%Y")
                    fecha_fin = datetime.strptime(registro[17], "%d/%m/%Y")
                    tiempos.append((fecha_fin - fecha_inicio).days)

        print("\n----- REPORTE DE PQRS -----")
        print("Total de PQRS:", total)
        print("Registradas:", registradas)
        print("En proceso:", en_proceso)
        print("Solucionadas:", solucionadas)
        print("Solicitudes de perros:", mascotas["Perro"])
        print("Solicitudes de gatos:", mascotas["Gato"])

        if len(tiempos) > 0:
            promedio = sum(tiempos) / len(tiempos)
            print("Promedio de días de respuesta:", round(promedio, 2))
        else:
            print("Promedio de días de respuesta: No hay datos")
