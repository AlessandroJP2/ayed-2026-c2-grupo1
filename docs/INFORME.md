# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- Tema: Biblioteca Musical 
- Por qué lo eligieron (5–8 líneas):
Elegimos el tema Biblioteca musical porque nos resultó interesante poder trabajar con información relacionada a canciones, artistas y géneros, aplicando los conceptos vistos durante la materia. Consideramos que este tema nos permitirá enfocarnos especialmente en el manejo y organización de datos mediante diferentes métodos, funciones y operaciones, permitiéndonos comprender cómo estos pueden integrarse en un programa funcional a través de un menú interactivo. También nos resultó interesante poder trabajar con GitHub como herramienta para organizar, compartir y realizar un seguimiento de los avances del equipo. De esta manera, buscamos no sólo aplicar los contenidos de la materia, sino también adquirir una mayor experiencia en el desarrollo conjunto de un proyecto. 

## 2. Modelo

Qué es un ítem del catálogo. Qué es mutable y qué no (E1). Cómo se relacionan catálogo, colección principal, pila y cola.

Todo lo que contiene cada canción, sus atributos: título, artista, album, fecha de lanzamiento y duración, son datos inmutables, no deberían modificarse a lo largo del tiempo. Nosotros para representarlas elegimos un Diccionario, por una cuestión de mejor legibilidad y claridad. El catálogo (y futuras playlists), serán mutables, ya que se podrán agregar, eliminar y reordenar las canciones contenidas. Por lo tanto, serán representados mediante listas. 

```text
(pueden pegar un diagrama ASCII o una lista de clases)
```

## 3. Recursión (E2)

- Función: obtener_canciones_derivadas (origen_id).
- Caso base: si la canción citada no cuenta con versiones derivadas entonces la biblioteca no encuentra relaciones asociadas a su ID, se devuelve una lista vacía y finaliza esa rama de búsqueda. 
- Caso recursivo: Cuando una canción posee una o más versiones derivadas, la función incorpora cada versión de estas encontrada a una lista de resultados y vuelve a llamarse utilizando el ID con el objetivo de verificar si existen nuevas versiones hasta alcanzar una canción sin versiones derivadas nuevas. 
- Traza de un ejemplo real del dataset: al consultar la canción número 1, se encuentra la relación: 62 -> 1. Por lo que se agrega "De Música Ligera (Unplugged)" y se consulta si la canción correspondiente a ese ID (en este caso de esta canción), tiene más canciones derivadas. Como no tiene, en este caso, se alcanza el caso base. 

## 4. TADs (E3)

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada |  |  |
| Pila |  |  |
| Cola |  |  |

Dónde se usa cada uno en el dominio.

## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
|  |  |  |  |

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
|  |  |  |

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
