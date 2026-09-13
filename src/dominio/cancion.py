class Cancion:

  def __init__ (self, id:int, titulo:str, artista:str, album:str, genero:str, anio:int, duracion_seg:int):
    
    self._id = int(id)
    self._titulo = str(titulo)
    self._artista = str(artista)
    self._album = str(album)
    self._genero = str(genero)
    self._anio = int(anio)
    self._duracion_seg = int(duracion_seg)
     
