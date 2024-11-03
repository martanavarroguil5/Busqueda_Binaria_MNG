# Busqueda_Binaria_MNG
Inventario de Prendas
Este proyecto implementa un sistema para gestionar el inventario de una tienda de ropa, utilizando la librería networkx para modelar las relaciones entre prendas como un grafo. El sistema permite añadir, eliminar y buscar prendas, así como encontrar prendas relacionadas basadas en criterios específicos.

### Estructura del Código
Clases
Prenda: Representa cada prenda en el inventario con atributos como id, tipo, color, tallas, precio y material.
Funciones
agregar_prenda(prenda, G): Añade una nueva prenda al grafo G y establece las conexiones con otras prendas basadas en los criterios de precio, material y tallas.

eliminar_prenda(id_prenda, G): Elimina una prenda del inventario y del grafo por su ID.

buscar_prendas_relacionadas(id_prenda, G): Busca y devuelve una lista de prendas relacionadas con una prenda dada según los criterios establecidos.

menu(): Proporciona un menú interactivo para que el usuario pueda añadir, eliminar o buscar prendas.

Inventario
Un inventario inicial se crea con un conjunto de 10 prendas predefinidas. Estas se pueden visualizar y gestionar mediante el menú interactivo.

## Instrucciones para la Implementación
En este código estan todos los pasos bastante guiados. Para añadir nuevas prendas intruduzca todos los atributos de la nueva prenda, asegúrese de que no repite el número de id. Para eiminarla simplemente necesita introducir el id de la prenda. Por último, para la búsqueda de prendas simplemente necesita introducir el id de la prenda.

## Análisis de Eficiencia
Complejidad de Tiempo


Agregar Prenda:

Big O: O(n), donde n es el número de prendas en el inventario.
Theta: Θ(n), en el caso promedio se realizan n comparaciones.
Omega: Ω(1), en el caso donde no hay prendas en el inventario.


Eliminar Prenda:

Big O: O(n), porque al eliminar una prenda, el sistema debe verificar y eliminar todas las conexiones de esa prenda en el grafo.
Theta: Θ(n), ya que se revisan las conexiones para cada prenda.
Omega: Ω(1), si no hay conexiones o la prenda no existe.


Buscar Prendas Relacionadas:

Big O: O(d), donde d es el grado del nodo (número de conexiones de la prenda buscada).
Theta: Θ(d), en el caso promedio se accede a d nodos relacionados.
Omega: Ω(1), si no hay conexiones relacionadas.


Complejidad de Espacio
El espacio utilizado es O(n + e), donde n es el número de nodos (prendas) y e es el número de aristas (conexiones) en el grafo.
