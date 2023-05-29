import json
import re
import os

def clear_console() -> None:
    """
    Esta función borra la pantalla de la consola en Python esperando la entrada del usuario y luego
    llamando al comando "cls" desde el sistema operativo.
    """

    _ = input('Press a key to continue...')
    os.system('cls')

def leer_archivo_json(ruta: str) -> list:
    """
    Esta función lee un archivo JSON de una ruta determinada y devuelve una lista de héroes.

    Parametro 
        -ruta:  es una cadena que representa la ruta del archivo JSON que contiene
        los datos a leer

    :return: una lista de héroes leída de un archivo JSON ubicado en la ruta especificada.

    """
    with open(ruta, 'r', encoding='utf-8') as archivo:
        contenido = json.load(archivo)
        lista_jugadores = contenido['jugadores']
    return lista_jugadores

def guardar_archivo_csv(nombre_archivo: str, contenido: str) -> bool:
    """
    Esta función guarda el contenido de una cadena en un archivo con el nombre de archivo dado y
    devuelve un valor booleano que indica si la operación fue exitosa o no.

    Parametros: 
        -nombre_archivo: Una cadena que representa el nombre del archivo que se va a crear o
        sobrescribir

        -contenido: El contenido que se escribirá en el archivo. Debería ser una cadena

    :retorno: 
        -un valor booleano, ya sea True o False, según si el archivo se creó correctamente o no.
    """
 
    with open(nombre_archivo, 'w+') as archivo:
        resultado = None 
        resultado = archivo.write(contenido)
    if resultado:
        print("Se creó el archivo: {0}".format(nombre_archivo))
        return True

    print("Error al crear el archivo: {0}".format(nombre_archivo))
    return False

def validar_opcion_expresion(expresion: str, ingreso_teclado: str) -> bool| int:
    """
    Valida una entrada de usuario contra una expresión regular y devuelve un booleano o un entero.

    :param expresion: Patrón de expresión regular que debe coincidir con la entrada del usuario para considerarse válido.
    :type expresion: str
    :param ingreso_teclado: Cadena de entrada del usuario desde el teclado para validar contra el patrón de expresión regular.
    :type ingreso_teclado: str
    :return: Valor booleano (falso) o entero (si la cadena de entrada coincide con la expresión regular).
    """

    opcion_validada = False
    if re.match(expresion, ingreso_teclado):
        opcion_validada =int(ingreso_teclado)

    return opcion_validada

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
        0) Para salir de programa.
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
        23) Bonus: (Homenaje al gran...."Mauricio")
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


def obtener_nombre_estadisticas(lista_jugadores: list[dict])-> dict:
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

    if lista_jugadores:

        indice = input("Seleccione un jugador por su índice para ver sus estadísticas: ")
        indice = validar_opcion_expresion(r'^[0-9]{1,2}$', indice)

        if indice >= 0 and indice < len(lista_jugadores):
            jugador_ese_indice = lista_jugadores[indice]

            dicionario_estadisticas = {}
            dicionario_estadisticas = jugador_ese_indice["estadisticas"]

            print(jugador_ese_indice["nombre"])
            for clave, valor in dicionario_estadisticas.items():
                print(clave, valor)
        else:
            print("Error indice invadilo {0}".format(indice))

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

    valor_ingresado = input("Ingresa un valor: ")
    valor_ingresado = validar_opcion_expresion(r'^[0-9]{1,2}$', valor_ingresado)
    no_encontrado = True

    if valor_ingresado:
        for jugador in lista_jugadores:
            if jugador["estadisticas"][clave_estadistica] > valor_ingresado:
                jugadores_filtrados.append(jugador)
                no_encontrado = False

        if no_encontrado:
            print("No se encontró ningún jugador con más puntos por partido que {0}".format(valor_ingresado))

    return jugadores_filtrados

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


def imprimir_jugador_maximo(jugador_maximo: dict, clave_jugador:str, clave_valor: str):
    """
    Esta función encuentra el jugador que tiene el valor máximo de una clave específica en la lista de jugadores
    y imprime los datos del jugador y el valor máximo.

    :param lista_jugadores: una lista de diccionarios, donde cada diccionario representa a un jugador y
    contiene su nombre y estadísticas
    :param clave_jugador: la clave del diccionario que se utilizará para encontrar el valor máximo
    :param clave_valor: la clave dentro de la clave anterior que se utilizará para obtener el valor específico
    """
    if jugador_maximo:
        valor_maximo = jugador_maximo[clave_jugador][clave_valor]
        nombre_jugador = jugador_maximo["nombre"]
        clave_str = clave_valor.replace("_", " ")
        print("Jugador con el valor máximo de {}:".format(clave_str))
        print("Nombre: {}".format(nombre_jugador))
        print("{}: {}".format(clave_str, valor_maximo))

    else:
        print("No se  ningún jugador.")

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


def imprimir_guarda_tabla_jugadores(lista_jugadores: list[dict])-> None:

    """
    Esta función imprime una tabla de estadísticas de jugadores y la guarda en un archivo CSV.
    
    :param lista_jugadores: Una lista de diccionarios que representan a los jugadores de baloncesto y
    sus estadísticas. Cada diccionario contiene las claves "nombre" y "estadisticas" que es otro
    diccionario que contiene las claves "puntos_totales" (total de puntos), "rebotes_totales" (total de
    rebotes), "
    :type lista_jugadores: list[dict]
    """

    nombre_archivo = "informe_jugadores.csv"
    texto_generado = generar_texto(lista_jugadores)
    
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
    guardar_archivo_csv(nombre_archivo, texto_generado)


def generar_texto(data):
    
    """
    La función genera una representación de texto de los datos del jugador de baloncesto en formato de
    lista o de diccionario.
    
    :param data: Los datos de entrada que pueden ser un diccionario o una lista de diccionarios que
    contienen información sobre los jugadores de baloncesto y sus estadísticas
    :return: La función `generar_texto` devuelve una cadena que contiene datos en un formato específico.
    El formato depende del tipo de `datos` de entrada. Si `data` es una lista de diccionarios, la
    función devuelve una cadena con valores separados por comas para cada diccionario de la lista. Si
    `data` es un diccionario, la función devuelve una cadena con valores separados por comas para las
    claves y valores en el diccionario
    """

    if isinstance(data, list):
        lista_claves = ["nombre", "posicion", "puntos_totales", "rebotes_totales", "robos_totales"]
        filas = []

        for jugador in data:
            valores = [str(jugador["nombre"]),
                       str(jugador["estadisticas"]["puntos_totales"]),
                       str(jugador["estadisticas"]["rebotes_totales"]),
                       str(jugador["estadisticas"]["robos_totales"])]
            fila = ",".join(valores)
            filas.append(fila)

        claves_str = ",".join(lista_claves)
        datos = "{0}\n{1}".format(claves_str, "\n".join(filas))

        return datos

    elif isinstance(data, dict):
        lista_claves = ["nombre", "posicion"]
        lista_valores = []

        jugador_estadisticas = data["estadisticas"]
        nombre_posicion = "{0}, {1}".format(data["nombre"], data["posicion"])

        for clave, valor in jugador_estadisticas.items():
            lista_claves.append(clave)
            lista_valores.append(str(valor))

        claves_str = ",".join(lista_claves)
        valores_str = ",".join(lista_valores)

        datos_str = "{0}\n{1},{2}".format(claves_str, nombre_posicion, valores_str)
        return datos_str

    else:
        return "Error: El tipo de entrada no es compatible."

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
