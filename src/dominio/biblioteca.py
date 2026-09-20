from src.dominio.cancion import Cancion 
from src.excepciones import ItemNoEncontradoError

class Biblioteca:

  def __init__(self):
    
    self._cancion_por_id = {}
    self._versiones_por_origen = {}

  def agregar_cancion (self, cancion: Cancion):
    self._cancion_por_id [cancion.id()] = cancion
  
  def agregar_version (self,cancion_id:int, version_de_id: int, tipo: str):
      relacion = {
        "cancion_id": int (cancion_id),
        "tipo": tipo
      }

      if version_de_id not in self._versiones_por_origen:
        self._versiones_por_origen [version_de_id] = []
      
      self._versiones_por_origen [version_de_id].append (relacion)
  
  def obtener_cancion (self, cancion_id:int) -> Cancion:
    if cancion_id not in self._cancion_por_id:
      raise ItemNoEncontradoError ("No existe una canción con ese id.")
    
    return self._cancion_por_id [cancion_id]

  def obtener_canciones_derivadas(self, origen_id: int) -> list[Cancion]:
    derivadas = []

    for relacion in self._versiones_por_origen.get(origen_id, []):
        id_derivada = relacion ["cancion_id"]
        cancion_derivada = self.obtener_cancion (id_derivada)

        derivadas.append (cancion_derivada)
        derivadas.extend(
          self.obtener_canciones_derivadas (id_derivada)
        )

    return derivadas

  def obtener_todas_las_canciones (self) -> list [Cancion]:
    return list(self._cancion_por_id.values())



         