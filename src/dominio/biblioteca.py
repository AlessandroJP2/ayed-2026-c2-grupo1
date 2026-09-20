from src.dominio.cancion import Cancion 

class Biblioteca:

  def __init__(self):
    
    self._cancion_por_id = {}
    self._versiones_por_origen = {}
    self.copy = {}



