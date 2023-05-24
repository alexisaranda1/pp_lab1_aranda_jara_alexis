
import json
import os
import re

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

    with open(ruta, 'r') as archivo:
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
    
    if nombre_archivo is str and  contenido is str: 
        with open(nombre_archivo, 'w+') as archivo:
            resultado = None # 
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
    opcion_validada = "-1"

    if busqueda:
        if re.search(expresion, ingreso_teclado):
            opcion_validada = ingreso_teclado
    else:
        if re.match(expresion, ingreso_teclado):
            opcion_validada = ingreso_teclado

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

def imprimir_menu_Desafio():
    """
    Esta función imprime un menú con diferentes opciones.
    """
    menu = '''\n\t------------------- Menu---------------------------------------\n
        1)Mostrar la lista de todos los jugadores del Dream Team. Con el formato:
        Nombre Jugador - Posición. Ejemplo:
        Michael Jordan - Escolta

        2)Permitir al usuario seleccionar un jugador por su índice y mostrar sus estadísticas 
        completas, incluyendo temporadas jugadas, puntos totales, promedio de puntos por 
        partido, rebotes totales, promedio de rebotes por partido, asistencias totales, 
        promedio de asistencias por partido, robos totales, bloqueos totales, porcentaje de
        tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples.

3)
4)
5)
6)
7)
8)
9)
10)
11)
12)
13)
14)
15)
16)
17)
18)
19)
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

    mensaje = ""
    if lista_jugadores:
        for jugador in lista_jugadores:
            mensaje += "Nombre : {0} | posioción : {1}".format(jugador["nombre"], jugador["posicion"]) +"\n"
    return mensaje
    
            
