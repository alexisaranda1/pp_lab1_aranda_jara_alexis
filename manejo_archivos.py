import json

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