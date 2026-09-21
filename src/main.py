from src.config import TEMA
from src.dominio.musica import cargar_biblioteca
from src.excepciones import ItemNoEncontradoError

TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}

def mostrar_versiones (biblioteca):
    try:
        cancion_id = int (input("Ingresa el ID correspondiente a la canción:"))

        cancion = biblioteca.obtener_cancion (cancion_id)
        derivadas = biblioteca.obtener_canciones_derivadas (cancion_id)

        print (f"\n Versiones derivadas de: {cancion.titulo()}")

        if not derivadas:
            print ("Esta canción no posee versiones derivadas de ella.")
        else:
            for derivada in derivadas:
                print (derivada)

    except ValueError:
     print ("El ID debe ser un número")
    except ItemNoEncontradoError as error:
     print (error)
        
def pendiente():
    print("Todavía no está implementado. Completar en la entrega que corresponde.")

def listar_catalogo(biblioteca):
    print("\n --- Catalogo de Canciones ---")
    for cancion in biblioteca.obtener_todas_las_canciones():
        print("---------------------------------")
        print(f"Id:                     {cancion.id()}")
        print(f"Título:                 {cancion.titulo()}")
        print(f"Artista:                {cancion.artista()}")
        print(f"Álbum:                  {cancion.album()}")
        print(f"Año de lanzamiento:   {cancion.anio()}")
        print(f"Duración:               {cancion.duracion_formateada()}")
        print("---------------------------------")

def operacion_recursiva():
    pass

def mostrar_menu():
    nombre = TEMAS.get(TEMA, TEMA or "(sin tema)")
    print()
    print(f"=== {nombre} — AyED C2 2026 ===")
    print("1. Listar catálogo")
    print("2. Ver detalle")
    print("3. Buscar")
    print("4. Ordenar")
    print("5. Operación recursiva")
    print("6. Colección principal (equipo / menú / playlist)")
    print("7. Historial (pila)")
    print("8. Cola")
    print("9. Guardar / cargar archivos")
    print("0. Salir")

def main():
    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return

    biblioteca = cargar_biblioteca()

    opcion = None
    while opcion != "0":
        mostrar_menu()
        opcion = input("> ").strip()
        if opcion == "0":
            print("Chau.")
        elif opcion == "1": 
            listar_catalogo(biblioteca) 
        elif opcion == "5":
            mostrar_versiones (biblioteca)
        elif opcion in {"2", "3", "4", "6", "7", "8", "9"}:
            pendiente()
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
