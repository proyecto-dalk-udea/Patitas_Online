
from datetime import datetime, date


class c_reportes:

    def generar_reporte(self, archivos):

        tipos = ["Peticion", "Queja", "Reclamo", "Sugerencia"]

        total = 0
        estados = {
            "Registrada": 0,
            "En proceso": 0,
            "Solucionada": 0
        }

        mascotas = {"Perro": 0, "Gato": 0}
        cantidad_tipos = {}
        tiempos = []
        vencidas = 0
        proximas_vencer = 0
        solicitudes_activas = []

        hoy = date.today()

        for tipo in tipos:

            registros = archivos.consultar_pqrs(tipo)
            cantidad_tipos[tipo] = len(registros)
            total += len(registros)

            for registro in registros:

                estado = registro[15]

                # Contar solicitudes por estado
                if estado in estados:
                    estados[estado] += 1

                # Contar solicitudes por mascota
                if registro[13] in mascotas:
                    mascotas[registro[13]] += 1

                # Calcular días de respuesta
                if estado == "Solucionada" and registro[17]:

                    try:
                        fecha_inicio = datetime.strptime(
                            registro[9], "%d/%m/%Y"
                        ).date()

                        fecha_fin = datetime.strptime(
                            registro[17], "%d/%m/%Y"
                        ).date()

                        dias = (fecha_fin - fecha_inicio).days

                        if dias >= 0:
                            tiempos.append(dias)

                    except ValueError:
                        print("Se encontró una fecha incorrecta.")

                # Revisar solicitudes pendientes
                if estado != "Solucionada":

                    try:
                        fecha_limite = datetime.strptime(
                            registro[16], "%d/%m/%Y"
                        ).date()

                        fecha_registro = datetime.strptime(
                            registro[9], "%d/%m/%Y"
                        ).date()

                        dias_restantes = (fecha_limite - hoy).days

                        if dias_restantes < 0:
                            vencidas += 1

                        elif 0 <= dias_restantes <= 5:
                            proximas_vencer += 1

                        solicitudes_activas.append(
                            (fecha_registro, tipo, registro[0])
                        )

                    except ValueError:
                        print("Se encontró una fecha incorrecta.")

        # Mostrar resultados
        print("\n========== REPORTE DE PQRS ==========")

        print("\n1. TOTAL DE SOLICITUDES")
        print("Total de PQRS:", total)

        print("\n2. SOLICITUDES POR TIPO")
        for tipo, cantidad in cantidad_tipos.items():
            print(tipo + ":", cantidad)

        print("\n3. SOLICITUDES POR ESTADO")
        for estado, cantidad in estados.items():
            print(estado + ":", cantidad)

        print("\n4. SOLICITUDES POR MASCOTA")
        print("Perros:", mascotas["Perro"])
        print("Gatos:", mascotas["Gato"])

        print("\n5. GESTIÓN DE VENCIMIENTOS")
        print("Solicitudes vencidas:", vencidas)
        print("Próximas a vencer (5 días o menos):", proximas_vencer)

        print("\n6. PROMEDIO DE DÍAS DE RESPUESTA")

        if tiempos:
            promedio = sum(tiempos) / len(tiempos)
            print("Promedio:", round(promedio), "días")
        else:
            print("No hay solicitudes solucionadas.")

        print("\n7. SOLICITUD ACTIVA MÁS ANTIGUA")

        if solicitudes_activas:
            mas_antigua = min(solicitudes_activas)

            print("Tipo:", mas_antigua[1])
            print("ID:", mas_antigua[2])
            print(
                "Fecha:",
                mas_antigua[0].strftime("%d/%m/%Y")
            )
        else:
            print("No hay solicitudes activas.")

        print("\n====================================")

