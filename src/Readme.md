# Gestion de vehiculos y facturas en un lavado de autos.

## Descripción detallada
El código va a estar enfocado principalmente en recibir y gestionar todos los detalles presentados por el cliente en el lavado de carros. Como primer objetivo se le da la bienvenida al ususario y se le pregunta por el tipo de vehiculo que va a lavar, como segundo punto se le otorgará al usuario la lista de precio según el vehiculo a lavar y si desea continuar con el proceso, despues se le dará al usuario la opción de elegir que plan de lavado desea según su necesidad y por ultimo se le dará el precio de todo el servicio al usuario.

Para el dueño del lavadero(la persona que ejecute el código) esto va a ser muy util ya que al preguntarle al usuario se va anotando lo que el usuario pidió y queda registro de el lavado de ese día, la cantidad de carros que se pudo lavar ese día y así mismo la cantidad de carros por mes.

Este sistema es de mucha utilidad a la hora de manejar cualquier servicio al cliente para mantener un orden y claridad en el proceso que se va a hacer con un cliente, en mi caso se trata de organizar de manera simple pero eficaz el proceso de un lavado de autos y los procesos que se le pueden realizar al auto con tal de que el usuario lo tenga en cuenta y que de esta manera cada proceso tenga unda duración eficiente para la gestión de otros vehiculos.

# Alcance/funciones del programa.
El programa tendrá como funciones darle la bienvenida al usuario del vehiculo, preguntaler que tipo de vehiculo va a lavar y ya definido el vehiculo se le presentará una tabla de precios según el vehiculo, se le preguntará al usuario si desea continuar con el proceso y si es así se le brindará una lista de maneras en las que se podria lavar su vehiculo como lo puede ser una limpieza superficial, Limpieza externa e interna o una limpieza total la cual incluye una limpieza más detallada de la tapiceria, los neumaticos y rines y un encerado para el vehiculo. Por ultimo se le pregunta al usuario su siguiente paso que puede ser acabar la funcion seguir registrando o revisar registros

#    **Estructuras de Datos Utilizadas:**
para el desarrollo del código se piensa usar principalmente los diccionarios ya que es un sistema eficiente para el tipo de problema planteado, en el cual por el uso de estas el usuario tendra una información simplificada del el proceso a realizar.


# Pseudocódigo
Inicio
    Dar la bienvenida al usuario
    preguntar por el tipo de vehiculo a lavar 
    si el usuario da su vehiculo se le presenta la tabla de precios
        leer lista
    Si el usuario continua el proceso 
        leer lista de tipo de lavados
    Si el tipo de lavado se elige
        leer la factura del proceso completo
    Preguntar al usuario su siguiente proceso
    Si usuario repite el proceso 
        iniciar otro registro
    Si usuario elige finalizar
        Gracias por su preferencia
    Si usuario decide buscar registros
        Ingrese el nombre
        leer registro
    fin si 
    fin si
    fin si
    fin si
    fin si
    fin si
fin
