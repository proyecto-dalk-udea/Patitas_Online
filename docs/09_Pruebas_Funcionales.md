
# PRUEBAS FUNCIONALES – PATITAS ONLINE

## 1. Introducción

Este documento presenta las pruebas funcionales realizadas al programa **Patitas Online**, desarrollado en Python para gestionar las Peticiones, Quejas, Reclamos y Sugerencias (PQRS) relacionadas con la atención del Movimiento Estudiantil de Perros y Gatos (MEPEGA) de la Universidad de Antioquia.

Las pruebas se realizaron utilizando **Google Colab**, con el propósito de verificar el funcionamiento de las principales opciones del sistema.

## 2. Objetivo

Comprobar que las funciones de registro, consulta, actualización de estados, generación de reportes y validación de datos funcionen de acuerdo con los requisitos establecidos para el proyecto.

## 3. Entorno de pruebas

- **Lenguaje de programación:** Python 3.
- **Herramienta de ejecución:** Google Colab.
- **Repositorio:** GitHub.
- **Proyecto:** Patitas Online.
- **Tipo de aplicación:** Programa de consola.
- **Almacenamiento:** Archivos de texto (.txt).
- **Fecha de las pruebas:** 18 de noviembre de 2026.

## 4. Pruebas realizadas

### 4.1. Prueba 1: ejecución del programa

**Objetivo:** Verificar que el programa inicie correctamente.

**Procedimiento:**

1. Descargar el proyecto desde GitHub.
2. Cargar el archivo comprimido en Google Colab.
3. Descomprimir el proyecto.
4. Ejecutar el archivo `src/main.py`.

**Resultado esperado:** El programa muestra el menú principal con cinco opciones.

**Resultado obtenido:** El menú principal se mostró correctamente.

**Estado:** Aprobada.

### 4.2. Prueba 2: registro de una PQRS

**Objetivo:** Verificar que el programa permita registrar solicitudes.

**Procedimiento:**

1. Seleccionar la opción `1. Registrar PQRS`.
2. Elegir el tipo de solicitud.
3. Ingresar los datos solicitados.
4. Finalizar el registro.

**Resultado esperado:** El programa guarda la solicitud, asigna un radicado y genera un comprobante.

**Resultado obtenido:** Se registraron solicitudes y se generaron comprobantes en formato `.txt`.

**Estado:** Aprobada.

### 4.3. Prueba 3: registro de los cuatro tipos de PQRS

**Objetivo:** Verificar que el sistema permita registrar los cuatro tipos de solicitudes.

**Tipos evaluados:**

- Petición.
- Queja.
- Reclamo.
- Sugerencia.

**Resultado esperado:** Cada solicitud se almacena en su archivo correspondiente.

**Resultado obtenido:** Se registraron solicitudes de los cuatro tipos y se verificó su almacenamiento.

**Estado:** Aprobada.

### 4.4. Prueba 4: generación de radicados

**Objetivo:** Verificar que los números de radicado se asignen de forma independiente por tipo de solicitud.

**Procedimiento:**

1. Registrar dos peticiones.
2. Registrar una queja.
3. Registrar un reclamo.
4. Registrar una sugerencia.
5. Revisar los números asignados.

**Resultado esperado:** Los radicados comienzan en 1 para cada tipo y aumentan cuando se registra una nueva solicitud del mismo tipo.

**Resultado obtenido:**

| Tipo de PQRS | Cantidad registrada | Radicados |
|---|---:|---|
| Petición | 2 | 1 y 2 |
| Queja | 1 | 1 |
| Reclamo | 1 | 1 |
| Sugerencia | 1 | 1 |
| **Total** | **5** | |

**Estado:** Aprobada.

### 4.5. Prueba 5: consulta de solicitudes

**Objetivo:** Verificar que el programa muestre las solicitudes registradas.

**Procedimiento:**

1. Seleccionar la opción `2. Consultar PQRS`.
2. Revisar la información mostrada.
3. Consultar un radicado específico.

**Resultado esperado:** El programa muestra las solicitudes almacenadas y permite consultar un registro particular.

**Resultado obtenido:** Se visualizaron los datos de las solicitudes y el comprobante de un radicado específico.

**Estado:** Aprobada.

### 4.6. Prueba 6: actualización de estados

**Objetivo:** Verificar que las solicitudes cambien de estado correctamente.

**Procedimiento:**

1. Registrar una petición.
2. Seleccionar la opción `3. Cambiar estado de PQRS`.
3. Cambiar el estado de `Registrada` a `En proceso`.
4. Repetir el procedimiento para cambiar de `En proceso` a `Solucionada`.

**Resultado esperado:** Los estados cambian en el orden establecido y se registra la fecha de solución.

**Resultado obtenido:** La solicitud cambió correctamente a `En proceso` y posteriormente a `Solucionada`.

**Estado:** Aprobada.

### 4.7. Prueba 7: impedir cambios en solicitudes solucionadas

**Objetivo:** Verificar que una solicitud solucionada no pueda volver a cambiar de estado.

**Procedimiento:**

1. Seleccionar la opción `3`.
2. Ingresar el tipo y el radicado de una solicitud solucionada.
3. Intentar actualizar nuevamente su estado.

**Resultado esperado:** El programa informa que la solicitud ya está solucionada.

**Resultado obtenido:** Se mostró el mensaje `Esta solicitud ya está solucionada.`

**Estado:** Aprobada.

### 4.8. Prueba 8: generación de reportes

**Objetivo:** Verificar el funcionamiento de las estadísticas.

**Procedimiento:**

1. Seleccionar la opción `4. Generar reporte`.
2. Revisar los indicadores presentados.

**Resultado esperado:** El programa muestra las cantidades por tipo, estado y mascota, además de los indicadores de vencimiento y tiempo de respuesta.

**Resultado obtenido:** El reporte mostró los indicadores correspondientes a las solicitudes registradas.

**Estado:** Aprobada.

### 4.9. Prueba 9: validación de datos

**Objetivo:** Verificar que el programa identifique datos incorrectos.

**Datos evaluados:**

| Validación | Dato evaluado | Resultado obtenido |
|---|---|---|
| Nombre | Nombre demasiado corto | Rechazado |
| Nombre | Nombre válido | Aceptado |
| Documento | Documento con letras | Rechazado |
| Documento | Documento numérico válido | Aceptado |
| Teléfono | Número demasiado corto | Rechazado |
| Teléfono | Número de 10 dígitos | Aceptado |
| Correo | Correo con formato incorrecto | Rechazado |
| Correo | Correo con formato correcto | Aceptado |
| Descripción | Texto demasiado corto | Rechazado |
| Descripción | Texto con longitud válida | Aceptado |
| Fecha | Fecha futura | Rechazada |
| Fecha | Fecha actual | Aceptada |

**Resultado esperado:** Las funciones de validación devuelven `False` para datos incorrectos y `True` para datos válidos.

**Resultado obtenido:** Las validaciones respondieron correctamente en los casos evaluados.

**Estado:** Aprobada.

### 4.10. Prueba 10: clasificación de vencimientos

**Objetivo:** Verificar la clasificación de solicitudes según su fecha límite.

**Casos evaluados:**

- Fecha límite anterior a la fecha actual.
- Fecha límite dentro de los próximos cinco días.
- Fecha límite con más de cinco días restantes.

**Resultado esperado:** Clasificar las solicitudes como vencidas, próximas a vencer o dentro del plazo.

**Resultado obtenido:** Los tres casos se clasificaron correctamente en la prueba realizada.

**Estado:** Aprobada.

### 4.11. Prueba 11: cálculo del promedio de respuesta

**Objetivo:** Verificar el cálculo del tiempo promedio de respuesta.

**Procedimiento:**

1. Registrar una solicitud con fecha actual.
2. Cambiar su estado a `En proceso`.
3. Cambiar su estado a `Solucionada`.
4. Generar el reporte.

**Resultado esperado:** El programa calcula la diferencia entre la fecha de registro y la fecha de solución.

**Resultado obtenido:** El reporte mostró un promedio de `0 días` para una solicitud registrada y solucionada el mismo día.

**Estado:** Aprobada.

## 5. Resumen de resultados

| N.º | Prueba funcional | Estado |
|---|---|---|
| 1 | Ejecución del programa | Aprobada |
| 2 | Registro de PQRS | Aprobada |
| 3 | Registro de los cuatro tipos | Aprobada |
| 4 | Generación de radicados | Aprobada |
| 5 | Consulta de solicitudes | Aprobada |
| 6 | Actualización de estados | Aprobada |
| 7 | Bloqueo de solicitudes solucionadas | Aprobada |
| 8 | Generación de reportes | Aprobada |
| 9 | Validación de datos | Aprobada |
| 10 | Clasificación de vencimientos | Aprobada |
| 11 | Promedio de días de respuesta | Aprobada |

**Total de pruebas documentadas:** 11.

**Pruebas aprobadas:** 11.

**Pruebas fallidas:** 0.

## 6. Observaciones

Durante las pruebas se verificó que:

- Los archivos de texto permiten almacenar las solicitudes de manera independiente.
- Los radicados se generan según el tipo de PQRS.
- Los estados siguen la secuencia establecida.
- El sistema registra la fecha de solución cuando corresponde.
- Los reportes presentan información de las solicitudes almacenadas.
- Las funciones de validación identifican los datos incorrectos en los casos evaluados.

Las pruebas corresponden a los escenarios ejecutados y no representan una evaluación exhaustiva de todas las entradas posibles.

## 7. Conclusión

Las pruebas funcionales realizadas en Google Colab permitieron comprobar el funcionamiento de las principales características de **Patitas Online**.

En los escenarios evaluados, el programa permitió registrar, consultar y actualizar solicitudes, generar comprobantes, validar información y presentar reportes estadísticos.

Los resultados obtenidos constituyen evidencia del funcionamiento del programa durante la segunda entrega del proyecto integrador.
