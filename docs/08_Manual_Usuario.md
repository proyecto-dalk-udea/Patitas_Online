
# MANUAL DE USUARIO – PATITAS ONLINE

## 1. Introducción

**Patitas Online** es un programa desarrollado en Python para registrar, consultar y realizar seguimiento a las Peticiones, Quejas, Reclamos y Sugerencias (PQRS) relacionadas con la atención del Movimiento Estudiantil de Perros y Gatos (MEPEGA) de la Universidad de Antioquia.

El programa funciona mediante un menú de opciones y almacena la información en archivos de texto.

## 2. Objetivo del manual

Explicar de manera sencilla cómo utilizar las funciones principales del programa Patitas Online.

## 3. Requisitos para ejecutar el programa

Para utilizar Patitas Online se necesita:

- Tener instalado **Python 3** o utilizar **Google Colab**.
- Contar con los archivos del proyecto.
- Mantener los archivos `main.py`, `validaciones.py`, `archivos.py` y `reportes.py` dentro de la carpeta `src`.
- Conservar la carpeta `data`, donde se almacenan las solicitudes.

## 4. Ejecución del programa

Para iniciar Patitas Online, se debe ejecutar el archivo `main.py`.

Desde una terminal ubicada en la carpeta principal del proyecto, se utiliza el siguiente comando:

    python src/main.py

También es posible ejecutarlo en Google Colab después de cargar y descomprimir el proyecto.

### 4.1. Menú principal

Al iniciar el programa, aparece el siguiente menú:

    ===== PATITAS ONLINE =====
    1. Registrar PQRS
    2. Consultar PQRS
    3. Cambiar estado de PQRS
    4. Generar reporte
    5. Salir

El usuario debe escribir el número correspondiente a la opción que desea utilizar.

## 5. Registrar una PQRS

Para registrar una solicitud:

1. Seleccionar la opción **1. Registrar PQRS**.
2. Elegir el tipo de solicitud: Petición, Queja, Reclamo o Sugerencia.
3. Ingresar los datos personales solicitados.
4. Indicar la fecha de registro y el canal de atención.
5. Escribir el asunto y la descripción de la solicitud.
6. Seleccionar el tipo de mascota: Perro o Gato.
7. Elegir el campus correspondiente.

### 5.1. Validación de información

El programa verifica que los datos ingresados cumplan los requisitos establecidos.

Por ejemplo:

- El nombre debe contener entre 3 y 100 caracteres permitidos.
- El documento debe contener entre 3 y 15 dígitos.
- El teléfono debe contener 10 dígitos.
- El correo electrónico debe tener un formato válido.
- El asunto debe contener entre 5 y 150 caracteres.
- La descripción debe contener entre 20 y 2000 caracteres.
- La fecha de registro no puede ser futura.

Si algún dato es incorrecto, el programa solicita ingresarlo nuevamente.

### 5.2. Confirmación del registro

Cuando la solicitud se registra correctamente, el sistema:

- Asigna un **número de radicado**.
- Establece el estado inicial **Registrada**.
- Calcula la fecha máxima de respuesta, correspondiente a 30 días después del registro.
- Guarda la solicitud en el archivo de texto correspondiente.
- Genera y muestra un comprobante de registro.

El comprobante también se guarda en formato `.txt` dentro de la carpeta `data/comprobantes`.

## 6. Consultar una PQRS

Para consultar las solicitudes registradas:

1. Seleccionar la opción **2. Consultar PQRS**.
2. Revisar la información de las solicitudes que aparece en pantalla.
3. Si se desea consultar un radicado específico, responder **S**.
4. Ingresar los datos que solicita el programa para identificar el registro.

### 6.1. Información de la consulta

La consulta general muestra información como:

- Número de radicado.
- Tipo de solicitud.
- Nombre del solicitante.
- Asunto.
- Estado actual.

El programa también permite visualizar el comprobante de una solicitud específica.

## 7. Cambiar el estado de una PQRS

Para actualizar el estado de una solicitud:

1. Seleccionar la opción **3. Cambiar estado de PQRS**.
2. Escribir el tipo de solicitud.
3. Ingresar el número de radicado.
4. Revisar el mensaje de confirmación.

### 7.1. Estados de las solicitudes

El programa utiliza tres estados:

- **Registrada:** la solicitud fue recibida y almacenada.
- **En proceso:** la solicitud está siendo atendida.
- **Solucionada:** la solicitud ha finalizado su proceso de atención.

Los estados cambian en el siguiente orden:

**Registrada → En proceso → Solucionada**

Cuando una solicitud pasa al estado **Solucionada**, el programa registra automáticamente la fecha de solución.

Una solicitud solucionada no puede volver a cambiar de estado.

## 8. Generar reportes

Para consultar las estadísticas:

1. Seleccionar la opción **4. Generar reporte**.
2. Revisar los resultados que aparecen en pantalla.

### 8.1. Información del reporte

El reporte presenta:

1. **Total de solicitudes:** cantidad general de PQRS registradas.
2. **Solicitudes por tipo:** cantidad de peticiones, quejas, reclamos y sugerencias.
3. **Solicitudes por estado:** cantidad de solicitudes registradas, en proceso y solucionadas.
4. **Solicitudes por mascota:** cantidad de solicitudes relacionadas con perros y gatos.
5. **Gestión de vencimientos:** solicitudes vencidas y próximas a vencer.
6. **Promedio de días de respuesta:** tiempo promedio utilizado para solucionar las solicitudes.
7. **Solicitud activa más antigua:** identificación de la solicitud pendiente con mayor antigüedad.

Estas estadísticas permiten realizar seguimiento a la gestión de las PQRS.

## 9. Salir del programa

Para finalizar la ejecución:

1. Seleccionar la opción **5. Salir**.
2. El sistema muestra un mensaje de despedida.
3. El programa termina su ejecución.

## 10. Almacenamiento de información

El programa almacena las solicitudes en cuatro archivos independientes:

- `data/Peticion.txt`
- `data/Queja.txt`
- `data/Reclamo.txt`
- `data/Sugerencia.txt`

Cada archivo corresponde a un tipo de solicitud.

### 10.1. Números de radicado

Los números de radicado se generan de manera independiente para cada tipo de PQRS.

Por ejemplo:

- Petición: radicado 1.
- Queja: radicado 1.
- Reclamo: radicado 1.
- Sugerencia: radicado 1.

Por esta razón, para identificar correctamente una solicitud es necesario conocer tanto el **tipo de PQRS** como su **número de radicado**.

### 10.2. Comprobantes

Los comprobantes se almacenan en la carpeta `data/comprobantes`.

Cada comprobante contiene información del registro, datos del solicitante y clasificación de la solicitud.

## 11. Recomendaciones para el usuario

- Ingresar información verdadera y completa.
- Revisar los datos antes de finalizar un registro.
- Conservar los archivos almacenados en la carpeta `data`.
- No modificar manualmente los registros guardados.
- Utilizar el tipo de solicitud y el número de radicado para identificar una PQRS.
- Consultar periódicamente los reportes para hacer seguimiento a las solicitudes.

## 12. Conclusión

**Patitas Online** facilita el registro, la consulta y el seguimiento de las solicitudes relacionadas con la atención de perros y gatos del Movimiento Estudiantil de Perros y Gatos (MEPEGA) de la Universidad de Antioquia.

Mediante sus diferentes funciones, el programa permite organizar la información, consultar el estado de las solicitudes y generar estadísticas que apoyan la gestión de las PQRS.
