# Especificación de requisitos

## Requisitos funcionales:

* RF01. Registrar una PQRS:                                                               
El sistema debe permitir registrar una PQRS con los datos del solicitante y la información de la solicitud.

* RF02. Generar el número de PQRS:                                                           
El sistema debe asignar automáticamente un número consecutivo a cada PQRS, teniendo una numeración independiente para cada tipo.

* RF03. Validar los datos del solicitante:                   
El sistema debe verificar que los datos del solicitante estén completos y tengan el formato correspondiente.

* RF04. Registrar la información de la PQRS:                    
El sistema debe permitir registrar el tipo de PQRS, la fecha, el canal de recepción, el asunto y la descripción.

* RF05. Registrar información relacionada:                                        
El sistema debe permitir registrar la información de la mascota y el campus cuando sea necesario.

* RF06. Calcular la fecha máxima de respuesta:                                           
El sistema debe calcular la fecha máxima de respuesta, que corresponde a 30 días después de la fecha de registro.

* RF07. Actualizar el estado de la PQRS:                                                     
El sistema debe manejar los estados de la PQRS: Registrada, En proceso y Solucionada.

* RF08. Guardar las PQRS:                             
El sistema debe guardar las PQRS en archivos de texto separados según su tipo: Petición, Queja, Reclamo y Sugerencia.

* RF09. Generar el comprobante:                                           
El sistema debe generar un comprobante de la PQRS en formato TXT con la información correspondiente.

* RF10. Consultar una PQRS:                                                           
El sistema debe permitir consultar una PQRS y conocer su estado.
  
* RF11. Generar estadísticas:                                                             
El sistema debe generar el promedio de días de respuesta y cinco estadísticas adicionales sobre las PQRS registradas.

## Requisitos no funcionales
 
* RNF01. Rendimiento:                                                    
El sistema debe realizar las operaciones de registro, consulta y generación de estadísticas de manera ágil, sin generar demoras innecesarias.

* RNF02. Organización de la información:                                         
  La información de las PQRS debe mantenerse organizada en los archivos correspondientes según el tipo de solicitud.
  
* RNF03. Usabilidad:                         
El sistema debe contar con un menú de consola claro y sencillo que permita al usuario acceder fácilmente a las diferentes opciones.

* RNF04. Confiabilidad:                                  
El sistema debe conservar correctamente la información de las PQRS y mantener la consistencia de los datos registrados.

* RNF05. Compatibilidad:                                                 
El sistema debe funcionar utilizando Python y archivos de texto plano, permitiendo almacenar la información y generar los comprobantes en formato TXT.
 
* RNF06. Mantenibilidad:                                                           
El código debe estar organizado en módulos para facilitar su comprensión y mantenimiento, separando las funciones de validación, manejo de archivos y generación de reportes.
