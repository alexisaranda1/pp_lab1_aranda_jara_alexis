from manejo_archivos import*
import re
import os

def clear_console() -> None:
    """
    Esta función borra la pantalla de la consola en Python esperando la entrada del usuario y luego
    llamando al comando "cls" desde el sistema operativo.
    """

    _ = input('\n\nPresiona enter para continuar...')
    os.system('cls')

def validar_opcion_expresion(expresion: str, ingreso_teclado: str) -> bool or int:
    """
    Esta función valida si la entrada de un usuario coincide con una expresión regular determinada y
    devuelve la entrada como un número entero o Falso.
    
    :param expresion: un patrón de expresión regular que la entrada del usuario debe coincidir para que
    se considere válido
    :type expresion: str
    :param ingreso_teclado: La cadena de entrada que el usuario ingresa a través del teclado
    :type ingreso_teclado: str
    :return: ya sea un número entero (si la entrada coincide con la expresión regular) o Falso (si la
    entrada no coincide con la expresión regular).
    """
    if ingreso_teclado == "":
        return False
    elif re.match(expresion, ingreso_teclado):
        return int(ingreso_teclado)
    else:
        return False

#2
def obtener_nombre_estadisticas(lista_jugadores: list[dict]) -> dict:
    """
    Esta función toma una lista de diccionarios que contienen información del jugador y devuelve las
    estadísticas de un jugador seleccionado en función de su índice.
    
    :param lista_jugadores: Una lista de diccionarios que representan a los jugadores y sus
    estadísticas. Cada diccionario contiene las claves "nombre" (nombre) y "estadisticas"
    (estadísticas). El valor de "estadisticas" es otro diccionario que contiene las estadísticas del
    jugador
    :type lista_jugadores: list[dict]
    :return: el diccionario de estadísticas para el jugador seleccionado, pero solo si el índice de
    entrada es válido y la lista de jugadores no está vacía. Si el índice de entrada no es válido o la
    lista está vacía, la función no devolverá nada.
    """
    jugador_ese_indice = None
    if lista_jugadores:
        indice = input("Seleccione un jugador por su índice para ver sus estadísticas: ")
        indice = validar_opcion_expresion(r'^(?:[0-9]|1[0-1])$', indice)

        if indice is not False:
            jugador_ese_indice = lista_jugadores[indice]
            dicionario_estadisticas = jugador_ese_indice["estadisticas"]

            print(jugador_ese_indice["nombre"])
            for clave, valor in dicionario_estadisticas.items():
                print(clave, valor)
        else:
            print("Error, el índice debe ser un número válido del 0 al 11.")

    return jugador_ese_indice




def buscar_jugador_por_nombre(lista_jugadores: list[dict]) -> list:

    """
    Esta función toma una lista de diccionarios que representan a los jugadores y devuelve una lista
    filtrada de jugadores basada en una búsqueda de nombre ingresada por el usuario.
    
    :param lista_jugadores: Una lista de diccionarios que representan a los jugadores, donde cada
    diccionario contiene información sobre un jugador, como su nombre, edad, posición, etc
    :type lista_jugadores: list[dict]
    :return: una lista de diccionarios que contienen información sobre los jugadores cuyos nombres
    coinciden con la entrada proporcionada por el usuario.
    """


    lista_filtrada = []

    if lista_jugadores:
        ingresado_teclado = input("Ingrese el nombre del jugador: ")

        patron = r".*{}.*".format(ingresado_teclado)
        for jugador in lista_jugadores:
            if re.search(patron, jugador["nombre"], re.IGNORECASE):
                lista_filtrada.append(jugador)

    return lista_filtrada


def calula_promedio(jugadores: list[dict], primera_clave: str, segunda_clave: str) -> float:
    """
    Calcula el valor promedio de una clave específica dentro de una lista de diccionarios.

    :param jugadores: Una lista de diccionarios que representan a los jugadores y sus estadísticas.
    :param primera_clave: La clave del diccionario de primer nivel en la lista de jugadores.
    :param segunda_clave: La clave utilizada para acceder al valor en el diccionario anidado dentro de cada jugador.
    :return: Un valor flotante que es el promedio de un valor específico para cada jugador en la lista de diccionarios.
             Si la lista está vacía, devuelve None.
    """


    if jugadores:
        acumulador = 0
        contador = 0
        for jugador in jugadores:
            acumulador += jugador[primera_clave][segunda_clave]
            contador += 1
        if contador > 0:
            promedio = acumulador / contador
            return promedio
    return None


#5
def lista_jugadores_alfabeticamente(jugadores:list)-> None:
    """
    Esta función toma una lista de jugadores y los ordena alfabéticamente por nombre, al mismo tiempo
    que calcula e imprime el puntaje promedio del equipo y el puntaje promedio de cada jugador.
    
    :param jugadores: El parámetro "jugadores" es una lista de diccionarios, donde cada diccionario
    representa a un jugador y contiene información sobre su nombre y estadísticas
    :type jugadores: list
    """

    if jugadores:
        lista_odenada = []
        promedio = calula_promedio(jugadores,"estadisticas" ,"promedio_puntos_por_partido")
        lista_odenada = ordenar_por_clave(jugadores , "nombre", True)
        print("promedio del equipo: {0:.2f}".format(promedio))
        for jugador in lista_odenada:
            print("{0}, promedio puntos por partido {1}".format(jugador["nombre"], jugador["estadisticas"]["promedio_puntos_por_partido"]))
    else:
        print("Error")

#5,20
def ordenar_por_clave(lista: list[dict], clave: str, flag_orden: bool)->list[dict]:
    """
    Ordena una lista de diccionarios por una clave específica en orden ascendente o descendente.

    :param lista: Una lista de diccionarios que se ordenarán según el valor de una clave específica en cada diccionario.
    :param clave: La clave o atributo de los diccionarios en la lista que se utilizará para ordenar la lista.
    :param flag_orden: Indicador booleano que determina si la lista debe ordenarse en orden ascendente o descendente.
                       True para orden ascendente, False para orden descendente.
    :return: Una nueva lista que contiene los mismos diccionarios que la lista de entrada, pero ordenados según el valor de
             la clave específica. El orden de clasificación está determinado por la bandera booleana `flag_orden`.
    """

    lista_nueva = lista[:]
    rango_a = len(lista) -1 
    flag_swap = True

    while flag_swap:
        flag_swap = False
        for indice_A in range(rango_a): 
            if (flag_orden == True and lista_nueva[indice_A][clave] > lista_nueva[indice_A+1][clave]) \
                    or (flag_orden == False and lista_nueva[indice_A][clave] < lista_nueva[indice_A+1][clave]):
                lista_nueva[indice_A], lista_nueva[indice_A+1] = lista_nueva[indice_A+1], lista_nueva[indice_A]
                flag_swap = True

    return lista_nueva

#16
def encontrar_jugador_menor_promedio(jugadores):
    """
    Esta función encuentra al jugador con el promedio de puntos más bajo por juego de una lista de
    jugadores.
    
    :param jugadores: una lista de diccionarios, donde cada diccionario representa a un jugador y
    contiene información sobre sus estadísticas, como su nombre, edad y puntos promedio por juego
    :return: el jugador con el promedio de puntos más bajo por juego de una lista de jugadores.
    """
    jugador_menor = None
    menor_promedio = None

    for jugador in jugadores:
        promedio = jugador["estadisticas"]["promedio_puntos_por_partido"]
        if menor_promedio is None or promedio < menor_promedio:
            menor_promedio = promedio
            jugador_menor = jugador 
    return jugador_menor
#16
def obtener_jugadores_sin_menor(jugadores:list[dict], jugador_menor: dict)-> list[dict]:
    """
    La función obtiene una lista de jugadores sin el jugador con la puntuación más baja.
    
    :param jugadores: una lista de jugadores
    :param jugador_menor: El parámetro "jugador_menor" es una variable que representa al jugador con
    menor puntuación o rendimiento en un partido o competición. La función "obtener_jugadores_sin_menor"
    toma dos parámetros: "jugadores", que es una lista de jugadores, y "jugador_menor
    :return: una lista de jugadores (jugadores_sin_menor) que excluye al jugador con la puntuación más
    baja (jugador_menor) de la lista original de jugadores (jugadores).
    """
    jugadores_sin_menor = []
    for jugador in jugadores:
        if jugador != jugador_menor:
            jugadores_sin_menor.append(jugador)
    return jugadores_sin_menor
#16
def procesar_jugadores(lista_jugadores: list[dict])-> None:

    """
    Esta función procesa una lista de jugadores, encuentra al jugador con el puntaje promedio más bajo,
    calcula el puntaje promedio de todos los jugadores e imprime los nombres de todos los jugadores
    excepto el que tiene el puntaje promedio más bajo.
    
    :param jugadores: Es una lista de diccionarios, donde cada diccionario representa a un jugador y
    contiene información como su nombre, edad, posición y promedio de puntos por juego
    """

    jugador_menor = encontrar_jugador_menor_promedio(lista_jugadores)

    jugadores_sin_menor = obtener_jugadores_sin_menor(lista_jugadores, jugador_menor)

    promedio_puntos = calula_promedio(jugadores_sin_menor,"estadisticas" ,"promedio_puntos_por_partido")

    print(f"El promedio de puntos por partido es: {promedio_puntos:.2f}")
    print("Jugadores sin el jugador con el menor promedio:")
    for jugador in jugadores_sin_menor:
        print(jugador["nombre"], jugador["estadisticas"]["promedio_puntos_por_partido"])


#7,8,13,14
def encontrar_maximo(lista_jugadores, clave_jugador, clave_valor):
    """
    La función encuentra el valor máximo de una clave específica en la lista de jugadores y devuelve
    el jugador que tiene ese valor máximo, junto con el valor mismo, en forma de diccionario.

    :param lista_jugadores: una lista de diccionarios, donde cada diccionario representa a un jugador y
    contiene su nombre y estadísticas
    :param clave_jugador: la clave del diccionario que se utilizará para encontrar el valor máximo
    :param clave_valor: la clave dentro de la clave anterior que se utilizará para obtener el valor específico
    :return: un diccionario con la información del jugador que tiene el valor máximo de la clave especificada
    y el valor máximo mismo.
    """
    maximo = 0
    jugador_maximo = None
    
    for jugador in lista_jugadores:
        valor = jugador[clave_jugador][clave_valor]
        if jugador_maximo is None or valor > maximo:
            maximo = valor
            jugador_maximo = jugador

    return jugador_maximo


# 10,11,12,12,15,18
def filtrar_jugadores_por_estadistica(lista_jugadores: list[dict], clave_estadistica: str)->list[dict]:
    """
    Esta función filtra una lista de jugadores en función de su promedio de puntos y retorna una lista
    con los jugadores cuyo promedio de puntos es mayor que un valor dado.

    :param lista_jugadores: una lista de diccionarios, donde cada diccionario representa a un jugador y
    contiene información como su nombre, edad y puntos promedio por juego
    :param clave_estadistica: La clave de la estadística que se utilizará para filtrar (por ejemplo, "promedio_puntos_por_partido")
    :return: una lista con los jugadores que cumplen la condición
    """
    jugadores_filtrados = []

    valor_ingresado = input("Ingresa un valor entre (1 a 99) : ")
    valor_ingresado = validar_opcion_expresion(r'^[1-9]{1,2}$', valor_ingresado)
    no_encontrado = True

    if valor_ingresado:
        for jugador in lista_jugadores:
            if jugador["estadisticas"][clave_estadistica] > valor_ingresado:
                jugadores_filtrados.append(jugador)
                no_encontrado = False

        if no_encontrado:
            print("No se encontró ningún jugador con más puntos por partido que {0}".format(valor_ingresado))
    else:
        print("Error, numero incorrecto ")
    return jugadores_filtrados


#17
def obtener_jugador_mayor_logros(lista_jugadores: list[dict])-> str:

    """
    La función devuelve el nombre del jugador con más logros de una lista de jugadores.
    
    :param lista_jugadores: una lista de diccionarios, donde cada diccionario representa a un jugador y
    contiene su nombre y una lista de sus logros
    :return: el nombre del jugador con más logros en la lista de jugadores proporcionada como entrada.
    """
    jugador_mayor_logros = None
    mayor_cantidad_logros = 0
    
    for jugador in lista_jugadores:

        cantidad_logros = len(jugador["logros"])
        if cantidad_logros > mayor_cantidad_logros:
            mayor_cantidad_logros = cantidad_logros
            jugador_mayor_logros = jugador["nombre"]

    return jugador_mayor_logros

#19
def jugador_con_mas_temporadas(jugadores):
    """
    Esta función encuentra al jugador(es) con la mayor cantidad de temporadas jugadas en base a una
    lista de diccionarios de jugadores y los imprime uno a la vez junto con su cantidad de temporadas.

    :param jugadores: una lista de diccionarios que representan a los jugadores, donde cada diccionario
    contiene información sobre el jugador, como su nombre y estadísticas
    """

    jugador_max_temporadas = encontrar_maximo(jugadores, "estadisticas", "temporadas")

    temporadas_max = jugador_max_temporadas["estadisticas"]["temporadas"]
    jugadores_max_temporadas = []

    for jugador in jugadores:
            temporadas = jugador["estadisticas"]["temporadas"]
            if temporadas == temporadas_max:
                jugadores_max_temporadas.append((jugador["nombre"], temporadas))

    print("Jugadores con la mayor cantidad de temporadas jugadas:")
    for jugador, temporadas in jugadores_max_temporadas:
        print("Jugador: {} | Temporadas: {}".format(jugador, temporadas))


#20
def ordenados_posicion_cancha(lista_jugadores: list[dict])-> None:
    """
    Esta función toma una lista de jugadores, los filtra por su porcentaje de tiros de campo, los ordena
    por su posición en la cancha e imprime su nombre y posición.
    
    :param lista_jugadores: una lista de diccionarios que representan a los jugadores de baloncesto, con
    claves como "nombre" (nombre), "posición" (posición) y "porcentaje_tiros_de_campo" (porcentaje de
    tiros de campo)
    """

    lista_filtrada = filtrar_jugadores_por_estadistica(lista_jugadores,"porcentaje_tiros_de_campo")

    lista_odenada = ordenar_por_clave(lista_filtrada , "posicion", True)

    for jugador in lista_odenada:

        posicion = jugador["posicion"]
        nombre =jugador["nombre"]
        porcentaje_tiros_de_campo = jugador["estadisticas"]["porcentaje_tiros_de_campo"]
      
        print("{0}, {1} porcentaje tiros decampo: {2}".format(posicion, nombre, porcentaje_tiros_de_campo))


def ordenar_por_clave_doble(lista: list[dict], clave1: str, clave2: str, flag_orden: bool) -> list[dict]:
    """
    La función ordena una lista de diccionarios por dos claves específicas en orden ascendente o descendente.

    :param lista: Una lista de diccionarios que se ordenarán según los valores de dos claves específicas en cada diccionario.
    :type lista: list[dict]
    :param clave1: La primera clave o atributo de los diccionarios en la lista que se utilizará para ordenarla.
    :type clave1: str
    :param clave2: La segunda clave o atributo de los diccionarios en la lista que se utilizará para ordenarla.
    :type clave2: str
    :param flag_orden: Indica si la lista debe ordenarse en orden ascendente (True) o descendente (False)
    :type flag_orden: bool
    :return: Una nueva lista que contiene los mismos diccionarios que la lista de entrada, pero ordenados
             según los valores de las claves especificadas y el orden indicado por el flag_orden.
    """

    lista_nueva = lista[:]
    n = len(lista_nueva)
    flag_swap = True

    while flag_swap:
        flag_swap = False
        for indice_A in range(n - 1):
            if (flag_orden and lista_nueva[indice_A][clave1][clave2] > lista_nueva[indice_A + 1][clave1][clave2]) or \
                    (not flag_orden and lista_nueva[indice_A][clave1][clave2] < lista_nueva[indice_A + 1][clave1][clave2]):
                lista_nueva[indice_A], lista_nueva[indice_A + 1] = lista_nueva[indice_A + 1], lista_nueva[indice_A]
                flag_swap = True

    return lista_nueva

#23
def obtener_jugadores_con_estadisticas_ordenadas(lista_jugadores:list[dict])-> list[dict]:
    """
    Esta función toma una lista de diccionarios que representan a los jugadores de baloncesto y sus
    estadísticas, ordena a los jugadores por diferentes estadísticas y devuelve una nueva lista de
    diccionarios con los nombres de los jugadores y sus clasificaciones en cada estadística.
    
    :param lista_jugadores: Una lista de diccionarios que representan a los jugadores de baloncesto y
    sus estadísticas
    :type lista_jugadores: list[dict]
    :return: una lista de diccionarios con las estadísticas modificadas de los jugadores, donde cada
    diccionario contiene el nombre del jugador y sus estadísticas actualizadas para cada categoría
    (rebotes, asistencias, robos y puntos).
    """

    lista_estadisticas = ["rebotes_totales", "asistencias_totales", "robos_totales", "puntos_totales"]
    for estadistaca in lista_estadisticas:
        lista_ordenada = ordenar_por_clave_doble(lista_jugadores,"estadisticas" ,estadistaca , False)
        jugadores_con_estadisticas = []

        for i in range(len(lista_ordenada)):
            jugador = lista_ordenada[i]
            nombre = jugador["nombre"]
            jugador["estadisticas"][estadistaca] = i + 1
            jugador_modificado = {
                "nombre": nombre,
                "estadisticas": jugador["estadisticas"]
            }
            jugadores_con_estadisticas.append(jugador_modificado)


    return jugadores_con_estadisticas
