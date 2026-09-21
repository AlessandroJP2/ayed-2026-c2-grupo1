import csv 
from src.dominio.biblioteca import Biblioteca
from src.dominio.cancion import Cancion

def cargar_biblioteca():
  biblioteca = Biblioteca()

  with open("data/canciones.csv", encoding="utf-8") as archivo:
    lector = csv.DictReader (archivo)

    for fila in lector:
        cancion = Cancion (
            fila["id"],
            fila["titulo"],
            fila["artista"],
            fila["album"],
            fila["genero"],
            fila["anio"],
            fila["duracion_seg"]
        )
        biblioteca.agregar_cancion(cancion)

  with open("data/versiones.csv", encoding="utf-8") as archivo:
    lector = csv.DictReader (archivo)

    for fila in lector:
      biblioteca.agregar_version(
        int(fila["cancion_id"]),
        int(fila["version_de_id"]),
        fila["tipo"]
      )

  return biblioteca