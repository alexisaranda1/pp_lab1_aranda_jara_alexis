def imprimir_dato(cadena_caracteres: str)-> None:
    """
    La función "imprimir_dato" comprueba si la entrada es un string y lo imprime, en caso contrario
    imprime un mensaje indicando que no es un string.
    
    :param cadena_caracteres: una variable de cadena que se pasa como argumento a la función
    :type cadena_caracteres: str
    """

    if type(cadena_caracteres) == str:
        print(cadena_caracteres)
    else:
        print("No es una cadena de texto")

def imprimir_menu()-> None:

    """
    Esta función imprime un menú con diferentes opciones para un programa de un equipo de baloncesto.
    """

    menu = '''\n\t------------------- Menu---------------------------------------\n
    
        1) Mostrar la lista de todos los jugadores del Dream Team.
        2) selecciona un jugador por su índice y mostrar sus estadísticas.
        3) guardar el jugador selecionado en el punto anterior.
        4) buscar un jugador por su nombre y mostrar sus logros.
        5) Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team,
           ordenado por nombre de manera ascendente. 
        6) ingresar el nombre de un jugador y mostrar si ese jugador es miembro del
            Salón de la Fama del Baloncesto.
        7) Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.
        8) alcular y mostrar el jugador con el mayor porcentaje de tiros de campo.
        9) Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.
        10)ingresar un valor y mostrar los jugadores que han promediado más
        puntos por partido que ese valor.
        11)ingresar un valor y mostrar los jugadores que han promediado más
        rebotes por partido que ese valor.
        12) ingresar un valor y mostrar los jugadores que han promediado más 
        asistencias por partido que ese valor
        13) Calcular y mostrar el jugador con la mayor cantidad de robos totales.
        14)Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.
        15)Permitir al usuario ingresar un valor y mostrar los jugadores que hayan 
        tenido un porcentaje de tiros libres superior a ese valor.
        16)Calcular y mostrar el promedio de puntos por partido del equipo excluyendo
          al jugador con la menor cantidad de puntos por partido.
        17)Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos
        18)Permitir al usuario ingresar un valor y mostrar los jugadores que hayan
        tenido un porcentaje de tiros triples superior a ese valor.
        19)Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas
        20) ingresar un valor y mostrar los jugadores , ordenados por posición en la cancha, 
        que hayan tenido un porcentaje de tiros de campo superior a ese valor.
        21) Para salir de programa.
        23) Bonus:
    '''
    imprimir_dato(menu)

def imprimir_lista_jugadores(lista_jugadores: list) -> None:
    """
    Esta función toma una lista de jugadores e imprime su índice, nombre y posición.
    
    :param lista_jugadores: Una lista de diccionarios que representan a los jugadores de un equipo
    deportivo. Cada diccionario contiene las claves "nombre" y "posición" con sus respectivos valores
    :type lista_jugadores: list
    """

    mensaje = "Error!"
    if lista_jugadores:
        mensaje = "indice - Nombre - Posición\n"
        for indice in range(len(lista_jugadores)):
            jugador = lista_jugadores[indice]
            mensaje += "{0} - {1} - {2}".format(indice, jugador["nombre"], jugador["posicion"]) + "\n"

    imprimir_dato(mensaje)

def imprimir_datos_jugadores(lista_jugadores: list[dict])-> None:
    """
    La función imprime los logros de una lista de jugadores si coinciden con un parámetro de búsqueda, o
    imprime un mensaje si ningún jugador coincide con el parámetro.
    
    :param lista_jugadores: una lista de diccionarios que representan a los jugadores y sus logros. Cada
    diccionario contiene información sobre un solo jugador, incluido su nombre, edad, equipo y una lista
    de sus logros (logros en español). La función imprime los logros de todos los jugadores de la lista
    que coinciden con un determinado parámetro de búsqueda. Si no
    :type lista_jugadores: list[dict]
    """


    if lista_jugadores:
        print(f"{len(lista_jugadores)} jugadores coinciden con el parámetro de búsqueda:")
        for jugador in lista_jugadores:
            logros = jugador["logros"]
            for logro in logros:
                print(logro)
    else:
        print("No se encontraron jugadores que coincidan con el parámetro de búsqueda.")


def imprimir_datos_jugadores_salon(lista_jugadores: list[dict])-> None:
    """
    Esta función imprime los nombres de los jugadores de baloncesto que son miembros del Salón de la
    Fama, dada una lista de diccionarios de jugadores.
    
    :param lista_jugadores: Una lista de diccionarios que representan a los jugadores de baloncesto y
    sus logros
    :type lista_jugadores: list[dict]
    """


    if lista_jugadores:
        for jugador in lista_jugadores:
            logros = jugador["logros"]
            flag = True
            for logro in logros:
                if "Miembro del Salon de la Fama del Baloncesto" == logro:
                    print(jugador["nombre"], logro)
                    flag = False
            if flag:
                print("el jugador no pertenece al salon de la fama")
    else:
        print("No se encontraron jugadores que coincidan con el parámetro de búsqueda.")

#7,8,13,14
def imprimir_jugador_maximo(jugador_maximo: dict, clave_jugador: str, clave_valor: str):
    """
    Esta función encuentra el jugador que tiene el valor máximo de una clave específica en la lista de jugadores
    y imprime los datos del jugador y el valor máximo.

    :param jugador_maximo: un diccionario que representa al jugador con el valor máximo
    :param clave_jugador: la clave del diccionario que se utilizará para obtener el valor máximo
    :param clave_valor: la clave dentro del diccionario del jugador que se utilizará para obtener el valor específico
    """
    if jugador_maximo:
        valor_maximo = jugador_maximo[clave_jugador][clave_valor]
        nombre_jugador = jugador_maximo["nombre"]
        clave_str = clave_valor.replace("_", " ")
        print("Jugador con el valor máximo de {}:".format(clave_str))
        print("Nombre: {}".format(nombre_jugador))
        print("{}: {}".format(clave_str, valor_maximo))
    else:
        print("No se encontró ningún jugador.")

# 10,11,12,12,15,18
def imprimir_jugadores(lista_jugadores: list[dict], clave_estadistica: str)-> None:

    """
    Esta función recorre una lista de jugadores y imprime el nombre y el valor de una estadística específica de cada jugador.
    
    :param lista_jugadores: La lista de jugadores que se desea imprimir
    :param clave_estadistica: La clave de la estadística que se desea imprimir (por ejemplo, "promedio_puntos_por_partido")
    """
    clave_estadistica_str = clave_estadistica.replace("_"," ")

    for jugador in lista_jugadores:
        nombre = jugador["nombre"]
        valor_estadistica = jugador["estadisticas"][clave_estadistica]
        if valor_estadistica:
            print("{0}, {1}: {2}".format(nombre, clave_estadistica_str, valor_estadistica))

#23
def imprimir_guarda_tabla_jugadores(lista_jugadores: list[dict])-> None:

    """
    Esta función imprime una tabla de estadísticas de jugadores y la guarda en un archivo CSV.
    
    :param lista_jugadores: Una lista de diccionarios que representan a los jugadores de baloncesto y
    sus estadísticas. Cada diccionario contiene las claves "nombre" y "estadisticas" que es otro
    diccionario que contiene las claves "puntos_totales" (total de puntos), "rebotes_totales" (total de
    rebotes), "
    :type lista_jugadores: list[dict]
    """

    print("---------------------------------------------------------------------------")
    print("|     Jugador          |    Puntos  |   Rebotes |  Asistencias  |  Robos  |")
    print("---------------------------------------------------------------------------")
    for jugador in lista_jugadores:
        print("|  {:19s} | {:^10d} | {:^9d} | {:^13d} | {:^7d} |".format(
            jugador["nombre"],
            jugador["estadisticas"]["puntos_totales"],
            jugador["estadisticas"]["rebotes_totales"],
            jugador["estadisticas"]["asistencias_totales"],
            jugador["estadisticas"]["robos_totales"])
        )
    print("---------------------------------------------------------------------------")
  
