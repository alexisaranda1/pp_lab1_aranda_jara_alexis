import json
import re
import os

def clear_console() -> None:
    """
    Esta función borra la pantalla de la consola en Python esperando la entrada del usuario y luego
    llamando al comando 'cls' para borrar la pantalla.
    """
    _ = input('Press a key to continue...')
    os.system('cls')

def leer_archivo_sjon(ruta: str) -> list:
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
    print("Nombre archivo".format(nombre_archivo))
    print("datos: ".format(contenido))

    with open(nombre_archivo, 'w+') as archivo:
        resultado = None 
        resultado = archivo.write(contenido)
    if resultado:
        print("Se creó el archivo: {0}".format(nombre_archivo))
        return True

    print("Error al crear el archivo: {0}".format(nombre_archivo))
    return False

def generar_texto(lista_diccionarios : list[dict])->str:
    """
    Esta función toma una lista de diccionarios y devuelve una cadena con las claves como primera línea
    y los valores de cada diccionario como líneas subsiguientes separadas por comas.

    Parametros:
        lista_diccionarios (list[dict]): Una lista de diccionarios, donde cada diccionario representa una fila de
            datos y las claves representan los nombres de las columnas.

    Returno:
        str: Una cadena que contiene las claves de los diccionarios en la lista de entrada separadas por
            comas en la primera línea, y los valores de cada diccionario en la lista de entrada separados por
            comas y nuevas líneas en las líneas siguientes.
    """
    texto_generado = ""

    if lista_diccionarios:

        primer_diccionario = lista_diccionarios[0]
        claves = []
        for clave in primer_diccionario.keys():
            claves.append(clave)

        texto_claves = ','.join(claves) 

        texto_valores = ''
        for diccionario in lista_diccionarios:
            valores = []
            for valor in diccionario.values():
                valores.append(str(valor))
            texto_valores += ','.join(valores) + '\n'  

        texto_generado = texto_claves + '\n' + texto_valores 
    return texto_generado

def validar_opcion_expresion(expresion: str, ingreso_teclado: str, busqueda = False) -> str:
    """
    Valida una opción utilizando una expresión regular y devuelve la opción si coincide;
    de lo contrario, devuelve "-1".
    
    Parametros: 
        -expresion: La expresión regular utilizada para validar la opción.
        -opcion: La opción de entrada del usuario.
        -usar_search: Indica si se debe utilizar el método `search` (True) o `match` (False) para
          la validación.

    Retorno: 
        La opción validada como una cadena. Si la opción no coincide con la expresión
        regular utilizando el método especificado, se devuelve "-1".
    """
    opcion_validada = False

    if busqueda:
        if re.search(expresion, ingreso_teclado):
            opcion_validada = ingreso_teclado
    else:
        if re.match(expresion, ingreso_teclado):
            opcion_validada =int(ingreso_teclado)

    return opcion_validada

def imprimir_dato(cadena_caracteres: str):

    """
    La función "imprimir_dato" comprueba si la entrada es una cadena y la imprime, de lo contrario,
    imprime un mensaje diciendo que no es una cadena.
    
    @param cadena_caracteres una variable de tipo cadena que representa una secuencia de caracteres.
    """
    if type(cadena_caracteres) == str:
        print(cadena_caracteres)
    else:
        print("No es una cadena de texto")

def imprimir_menu_Desafio()-> None:



    """
    Esta función imprime un menú con diferentes opciones.
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

20)
21) para salir!
    '''
    imprimir_dato(menu)

def buscar_nombre_posicion(lista_jugadores: list)->str:

    """
    Esta función toma una lista de jugadores y devuelve una cadena con sus nombres y posiciones.
    
    :param lista_jugadores: Una lista de diccionarios que contienen información sobre los jugadores,
    incluido su nombre y posición
    :type lista_jugadores: list
    :return: una cadena que contiene los nombres y posiciones de los jugadores en la lista de entrada.
    """

    mensaje = "Error!"
    if lista_jugadores:
        mensaje = "indice - Nombre - Posición\n"
        for indice in range(len(lista_jugadores)):
            jugador = lista_jugadores[indice]
            mensaje += "{0} - {1} - {2}".format(indice, jugador["nombre"], jugador["posicion"]) + "\n"

    imprimir_dato(mensaje)

def obtener_nombre_estadisticas(lista_jugadores: list[dict], indice)-> str:
    """
    Esta función toma una lista de diccionarios que contienen información del jugador y un índice, y
    devuelve una cadena con el nombre del jugador y sus estadísticas separados por comas.
    
    :param lista_jugadores: Una lista de diccionarios que contienen información sobre los jugadores y
    sus estadísticas
    :type lista_jugadores: list[dict]
    :param indice: El parámetro "índice" es un número entero que representa el índice del jugador en la
    lista de jugadores cuyo nombre y estadísticas queremos obtener
    :return: una cadena que contiene el nombre de un jugador y sus estadísticas, separados por comas. Si
    la lista de entrada está vacía, se devuelve una cadena vacía.
    """

    datos = ""

    if lista_jugadores:

        jugador_indice_ingresado = lista_jugadores[indice]

        jugador_estadisticas = jugador_indice_ingresado["estadisticas"]
        nombre_posicion = "{0}, {1}".format(jugador_indice_ingresado["nombre"], \
                                            jugador_indice_ingresado["posicion"])

        lista_claves = ["nombre", "posicion"]
        lista_valores = []

        print("{0}".format(nombre_posicion))

        for clave, valor in jugador_estadisticas.items():
            print("{0} : {1}".format(clave, valor))
            lista_claves.append(clave)
            lista_valores.append(str(valor))

        claves_str = ",".join(lista_claves)
        valores_str = ",".join(lista_valores)

        datos ="{0}\n{1},{2}".format(claves_str ,nombre_posicion ,valores_str) 

    return datos

def buscar_jugador_por_nombre(lista_jugadores: list[dict]) -> list:
    """
    Esta función toma una lista de diccionarios que contienen información sobre los jugadores y devuelve
    una lista filtrada de jugadores basada en una búsqueda de nombre ingresada por el usuario.
    
    :param lista_jugadores: Una lista de diccionarios que representan a los jugadores, donde cada
    diccionario contiene información sobre un jugador, como su nombre, edad, posición, etc
    :type lista_jugadores: list[dict]
    :return: una lista de diccionarios que contienen información sobre los jugadores cuyos nombres
    coinciden con la entrada de búsqueda proporcionada por el usuario.
    """

    lista_filtrada = []

    if lista_jugadores:
        nombre_busqueda = input("Ingrese el nombre del jugador: ")
        patron = r".*" + nombre_busqueda + r".*"
        for jugador in lista_jugadores:
            if re.search(patron, jugador["nombre"], re.IGNORECASE):
                lista_filtrada.append(jugador)

    return lista_filtrada

def imprimir_datos_jugadores(lista_jugadores: list[dict])-> None:
    """
    Esta función imprime los logros de una lista de jugadores de baloncesto y, opcionalmente, puede
    filtrar por aquellos en el Salón de la Fama.
    :param lista_jugadores: Una lista de diccionarios que contienen información sobre jugadores de
    baloncesto
    :type lista_jugadores: list[dict]
    :param salon_de_la_fama: Un parámetro booleano que determina si solo se imprimen los logros de los
    jugadores que son miembros del Salón de la Fama del Baloncesto o no. Si se establece en Verdadero,
    solo se imprimirán los logros de los jugadores del Salón de la Fama. Si se establece en False, se
    imprimirán todos los logros de los jugadores de la lista, defaults to False
    :type salon_de_la_fama: bool (optional)
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
    Fama del Baloncesto de una lista de jugadores.
    
    :param lista_jugadores: Una lista de diccionarios que representan a jugadores de baloncesto, donde
    cada diccionario contiene información sobre un jugador, como su nombre, equipo, posición y logros
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

def calula_promedio(jugadores:list[dict],clave:str)-> float:
    """
    Esta función calcula el valor promedio de una subclave específica en una lista de diccionarios que
    contienen estadísticas de jugadores.
    
    :param jugadores: una lista de diccionarios que representan a los jugadores, donde cada diccionario
    contiene información sobre un jugador, incluidas sus estadísticas
    :type jugadores: list[dict]
    :param sub_clave: sub_clave es un parámetro de cadena que representa la subclave de la clave
    "estadisticas" en el diccionario de cada jugador. Esta sub-clave se utiliza para acceder a una
    estadística específica del jugador, como "puntos" (puntos), "rebotes" (rebotes), o
    :type sub_clave: str
    :return: un valor flotante que representa el promedio de una estadística específica (sub_clave) para
    una lista de jugadores (jugadores) con diccionarios anidados que contienen información y
    estadísticas del jugador. Si la lista está vacía o no se encuentra la estadística, la función
    devuelve Ninguno.
    """
    if jugadores:
        acumulador = 0
        contador = 0
        for jugador in jugadores:
            acumulador += jugador["estadisticas"][clave]
            contador +=1
        if contador > 0:
            promedio = acumulador / contador
            return promedio
    return None

def lista_jugadores_alfabeticamente(jugadores:list)-> None:

    if jugadores:
        lista_odenada = []
        promedio = calula_promedio(jugadores, "promedio_puntos_por_partido")
        lista_odenada = ordenar_por_clave(jugadores , "nombre", True)
        print("promedio del equipo: {0:.2f}".format(promedio))
        for jugador in lista_odenada:
            print(jugador["nombre"], jugador["estadisticas"]["promedio_puntos_por_partido"])
    else:
        print("Error")

def ordenar_por_clave(lista: list[dict], clave: str, flag_orden: bool):
    """
    La función ordena una lista de diccionarios por una clave específica en orden ascendente o
    descendente.
    
    :param lista: Una lista de diccionarios que se ordenarán según el valor de una clave específica en
    cada diccionario
    :type lista: list[dict]
    :param clave: "clave" es un parámetro de cadena que representa la clave o atributo de los
    diccionarios en la lista que se utilizará para ordenar la lista
    :type clave: str
    :param flag_orden: El parámetro flag_orden es un indicador booleano que determina si la lista de
    diccionarios debe ordenarse en orden ascendente o descendente según el valor de la clave
    especificada. Si flag_orden es True, la lista se ordenará en orden ascendente. Si flag_orden es
    falso, la lista será
    :type flag_orden: bool
    :return: La función `ordenar_por_clave` devuelve una nueva lista que contiene los mismos
    diccionarios que la lista de entrada, pero ordenados según el valor de una clave específica en cada
    diccionario. El orden de clasificación está determinado por una bandera booleana (`flag_orden`),
    donde `True` significa orden ascendente y `False` significa orden descendente.
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


def filtrar_jugadores_por_estadistica(lista_jugadores : list, clave_estadistica: str):
    """
    Esta función filtra una lista de jugadores en función de su promedio de puntos y muestra en pantalla
    los jugadores cuyo promedio de puntos es mayor que un valor dado.
    
    :param lista_jugadores: una lista de diccionarios, donde cada diccionario representa a un jugador y
    contiene información como su nombre, edad y puntos promedio por juego
    :param clave_estadistica: La clave de la estadística que se utilizará para filtrar (por ejemplo, "promedio_puntos_por_partido")
    """

    flag = True
    valor_ingresado = input("Ingresa un valor: ")
    valor_ingresado = validar_opcion_expresion(r'^[0-9]{1,2}$', valor_ingresado)
    if valor_ingresado:
        
        for jugador in lista_jugadores:
            if jugador["estadisticas"][clave_estadistica] > valor_ingresado:
                clave_estadistica_str = clave_estadistica.replace("_", " ")
                print("Nombre: {0}, {1}: {2}".format(jugador["nombre"], clave_estadistica_str, jugador["estadisticas"][clave_estadistica]))
                flag = False

    if flag:
        print("No se encontraron jugadores con un {0} mayor que {1}.".format(clave_estadistica, valor_ingresado))

def obtener_jugadores_sin_menor(jugadores, jugador_menor):
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
        if jugador["nombre"] != jugador_menor:
            jugadores_sin_menor.append(jugador)
    return jugadores_sin_menor

def procesar_jugadores(jugadores):

    """
    Esta función procesa una lista de jugadores, encuentra al jugador con el puntaje promedio más bajo,
    calcula el puntaje promedio de todos los jugadores e imprime los nombres de todos los jugadores
    excepto el que tiene el puntaje promedio más bajo.
    
    :param jugadores: Es una lista de diccionarios, donde cada diccionario representa a un jugador y
    contiene información como su nombre, edad, posición y promedio de puntos por juego
    """
    jugador_menor = encontrar_jugador_menor_promedio(jugadores)
    jugadores_sin_menor = obtener_jugadores_sin_menor(jugadores, jugador_menor)
    promedio_puntos = calula_promedio(jugadores_sin_menor, "promedio_puntos_por_partido")

    print(f"El promedio de puntos por partido es: {promedio_puntos:.2f}")
    print("Jugadores sin el jugador con el menor promedio:")
    for jugador in jugadores_sin_menor:
        print(jugador["nombre"], jugador["estadisticas"]["promedio_puntos_por_partido"])
    
def encontrar_jugador_menor_promedio(jugadores):
    """
    Esta función encuentra al jugador con el promedio de puntos más bajo por juego de una lista de
    jugadores.
    
    :param jugadores: una lista de diccionarios, donde cada diccionario representa a un jugador y
    contiene información sobre sus estadísticas, como su nombre, edad y puntos promedio por juego
    :return: el jugador con el promedio de puntos más bajo por juego de una lista de jugadores.
    """
    jugador_menor = None
    menor_promedio = float('inf')
    for jugador in jugadores:
        promedio = jugador["estadisticas"]["promedio_puntos_por_partido"]
        if promedio < menor_promedio:
            menor_promedio = promedio
            jugador_menor = jugador["nombre"]
    print("jugador menor ",jugador_menor)
    return jugador_menor

def encontrar_maximo(jugadores: list, clave_jugador, clave_valor: str):
    """
    La función encuentra el valor máximo de una clave específica en la lista de jugadores y devuelve
    el nombre del jugador que tiene ese valor máximo, junto con el valor mismo, en forma de cadena de texto.
    
    :param jugadores: una lista de diccionarios, donde cada diccionario representa a un jugador y
    contiene su nombre y estadísticas
    :param clave_jugador: la clave del diccionario que se utilizará para encontrar el valor máximo
    :param clave_valor: la clave dentro de la clave anterior que se utilizará para obtener el valor específico
    :return: una cadena de texto con el nombre del jugador que tiene el valor máximo de la clave especificada
    y el valor máximo mismo.
    """
    nombre_maximo = None
    maximo = 0
    for jugador in jugadores:
        valor = jugador[clave_jugador][clave_valor]
        if nombre_maximo is None or valor > maximo:
            maximo = valor
            nombre_maximo = jugador["nombre"]
    clave_valor = clave_valor.replace("_", " ")

    return "El jugador {0}  tiene la mayor cantidad de {1} : {2}.".format(nombre_maximo, clave_valor, maximo)
    
def obtener_jugador_mayor_logros(lista_jugadores):
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

def jugador_con_mas_temporadas(jugadores):
    """
    Esta función encuentra al jugador(es) con la mayor cantidad de temporadas jugadas en base a una
    lista de diccionarios de jugadores.
    
    :param jugadores: una lista de diccionarios que representan a los jugadores, donde cada diccionario
    contiene información sobre el jugador, como su nombre y estadísticas
    """
    max_temporadas = 0
    jugadores_max_temporadas = []

    for jugador in jugadores:
        temporadas = jugador["estadisticas"]["temporadas"]
        if temporadas > max_temporadas:
            max_temporadas = temporadas
            jugadores_max_temporadas = [jugador["nombre"]]
        elif temporadas == max_temporadas:
            jugadores_max_temporadas.append(jugador["nombre"])

    print("Jugadores con la mayor cantidad de temporadas jugadas:", jugadores_max_temporadas)



