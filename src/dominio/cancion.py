class Cancion:

  def __init__ (self, id:int, titulo:str, artista:str, album:str, genero:str, anio:int, duracion_seg:int):
    
    self._id = int(id)
    self._titulo = str(titulo)
    self._artista = str(artista)
    self._album = str(album)
    self._genero = str(genero)
    self._anio = int(anio)
    self._duracion_seg = int(duracion_seg)
     
  def id (self) -> int:
   return self._id 

  def titulo (self) -> str:
   return self._titulo

  def artista (self) -> str:
   return self._artista

  def album (self) -> str:
   return self._album

  def genero (self) -> str:
   return self._genero

  def anio (self) -> int:
   return self._anio

  def duracion_seg (self) -> int:
   return self._duracion_seg

  def duracion_formateada (self) -> str:
   minutos = self._duracion_seg // 60
   segundos = self._duracion_seg % 60
   return f"{minutos}:{segundos:02d}"

  def __str__ (self):
   return f"""[{self._id}]" {self._titulo} - {self._artista} \n
   Álbum: {self._album} | Año de lanzamiento: {self._anio} | Género: {self._genero} | Duración: {self.duracion_formateada()}"""