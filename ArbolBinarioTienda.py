import networkx as nx

#Primero vamos a crear el inventario de nuestra tienda, creamos una clase Prenda
# y creamos atributos que puedan distinguir nustras prendas
class Prenda:
    def __init__(self, id, tipo, color, tallas, precio, material):
        self.id = id
        self.tipo = tipo
        self.color = color
        self.tallas = tallas
        self.precio = precio
        self.material = material

    #Para ver los atributos del inventario
    def __str__(self):
        return f"ID: {self.id}, Tipo: {self.tipo}, Color: {self.color}, Tallas: {self.tallas}, Precio: {self.precio}€, Material: {self.material}"

# Crear el inventario de prendas (lo hemos hecho pequeño, solo 10 prendas)
inventario = [
    Prenda(1, "Camiseta", "Blanco", ["XS", "S", "M", "L", "XL"], 15.99, "Algodón"),
    Prenda(2, "Pantalón vaquero", "Azul", ["34", "36", "38", "40", "42"], 29.99, "Denim"),
    Prenda(3, "Vestido", "Rojo", ["S", "M", "L"], 39.99, "Poliéster"),
    Prenda(4, "Chaqueta", "Negro", ["M", "L", "XL"], 49.99, "Cuero sintético"),
    Prenda(5, "Falda", "Verde", ["XS", "S", "M"], 25.99, "Lino"),
    Prenda(6, "Blusa", "Beige", ["S", "M", "L", "XL"], 19.99, "Seda"),
    Prenda(7, "Abrigo", "Gris", ["M", "L", "XL"], 59.99, "Lana"),
    Prenda(8, "Shorts", "Negro", ["34", "36", "38", "40"], 22.99, "Algodón"),
    Prenda(9, "Sudadera", "Rosa", ["S", "M", "L"], 27.99, "Mezcla de algodón"),
    Prenda(10, "Mono", "Marrón", ["S", "M", "L"], 45.99, "Viscosa")
]

# Mostrar el inventario
#for prenda in inventario:
#    print(prenda)


'''
La jerarquía del codigo consiste en un menú en el que puedes seleccionar 3 
funciones:
Añadir prenda
Eliminar prenda
Buscar prenda

Para añadir prendas hacemos una función que vaya pidiendo inputs para los 
atributos de la nueva prenda y añadirá la prenda al inventario y al grafo
generando nuevas aristas (conexiones) entre prendas.

La opción de eleminar prenda pedirá un id como input y eliminará la prenda del
inventario y del grafo, asi como sus aristas.

Para crear el algoritmo que relacione los distintos atributos de las prendas
entre ellas para la busqueda de prendas similares voy a hacer lo siguiente:

Agregar nodos: Cada prenda en el inventario es un nodo en el grafo, y lo 
identificamos por su id. También almacenamos el objeto Prenda completo como 
atributo del nodo para facilitar el acceso.

Agregar aristas: Conectamos los nodos (prendas) con aristas (relaciones) basadas
en dos criterios:

Precio cercano: Si la diferencia de precio entre dos prendas es de ±5 euros, se 
crea una conexión.
Material idéntico: Si dos prendas están hechas del mismo material, se crea una 
conexión.
Talla: Si dos prendas comparten al menos una talla igual

Función de búsqueda de prendas relacionadas: Usamos G.neighbors(id_prenda) para 
obtener los nodos conectados a un nodo específico (prenda). Esto devuelve una 
lista de prendas relacionadas de acuerdo con las conexiones que definimos.



'''

# Crear el grafo
G = nx.Graph()

# Añadir nodos (las prendas) al grafo
for prenda in inventario:
    G.add_node(prenda.id, objeto_prenda=prenda)

# Añadir aristas basadas en los criterios que hemos definido
for prenda1 in inventario:
    for prenda2 in inventario:
        if prenda1 != prenda2:
            # Crear conexión si el precio está en un rango similar (por ejemplo, 
            # ±5 euros)
            if abs(prenda1.precio - prenda2.precio) <= 5:
                G.add_edge(prenda1.id, prenda2.id)

            # Crear conexión si el material es el mismo
            if prenda1.material == prenda2.material:
                G.add_edge(prenda1.id, prenda2.id)
            
            # Crear conexión si hay tallas en común
            if set(prenda1.tallas).intersection(set(prenda2.tallas)):
                G.add_edge(prenda1.id, prenda2.id)


# Función para agregar una prenda y actualizar conexiones
def agregar_prenda(prenda, G):
    G.add_node(prenda.id, objeto_prenda=prenda)
    # Añadir conexiones según los criterios
    for other_id in G.nodes:
        if other_id != prenda.id:
            other_prenda = G.nodes[other_id]['objeto_prenda']
            # Criterio de precio
            if abs(prenda.precio - other_prenda.precio) <= 5:
                G.add_edge(prenda.id, other_id)
            # Criterio de material
            if prenda.material == other_prenda.material:
                G.add_edge(prenda.id, other_id)
            # Criterio de tallas
            if set(prenda.tallas).intersection(set(other_prenda.tallas)):
                G.add_edge(prenda.id, other_id)


# Función para eliminar una prenda y sus conexiones
def eliminar_prenda(id_prenda, G):
    if id_prenda in G:
        G.remove_node(id_prenda)
        print(f"Prenda con ID {id_prenda} eliminada.")
    else:
        print("Prenda no encontrada.")



# Función para buscar prendas relacionadas
def buscar_prendas_relacionadas(id_prenda, G):
    # Encuentra todos los nodos conectados en el grafo G al nodo con ID id_prenda
    if id_prenda in G:
        relacionados_ids = list(G.neighbors(id_prenda))
        relacionados = [G.nodes[nodo_id]['objeto_prenda'] for nodo_id in relacionados_ids]
        return relacionados
    else:
        print("Prenda no encontrada.")
        return []
    

# Función para mostrar el menú
def menu():
    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Agregar una prenda")
        print("2. Eliminar una prenda")
        print("3. Buscar prenda y mostrar relacionadas")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            # Agregar una prenda
            id = int(input("ID de la prenda: "))
            tipo = input("Tipo de prenda: ")
            color = input("Color: ")
            tallas = input("Tallas (separadas por coma, ej: S,M,L): ").split(',')
            precio = float(input("Precio (€): "))
            material = input("Material: ")
            
            nueva_prenda = Prenda(id, tipo, color, tallas, precio, material)
            agregar_prenda(nueva_prenda, G)
            print("Prenda agregada exitosamente.")
        
        elif opcion == "2":
            # Eliminar una prenda
            id = int(input("ID de la prenda a eliminar: "))
            eliminar_prenda(id, G)
        
        elif opcion == "3":
            # Buscar una prenda y mostrar las relacionadas
            id = int(input("ID de la prenda a buscar: "))
            prenda_relacionadas = buscar_prendas_relacionadas(id, G)
            if prenda_relacionadas:
                print(f"\nPrendas relacionadas con la prenda de ID {id}:")
                for prenda in prenda_relacionadas:
                    print(prenda)
        
        else:
            print("Opción no válida. Intente de nuevo.")


# Iniciar el menú
menu()


# Ejemplo de búsqueda de prendas relacionadas con la prenda de ID 2
id_busqueda = 2 
prendas_relacionadas = buscar_prendas_relacionadas(id_busqueda, G)

# Mostrar resultados
print(f"Prendas relacionadas con la prenda de ID {id_busqueda}:")
for prenda in prendas_relacionadas:
    print(prenda)
