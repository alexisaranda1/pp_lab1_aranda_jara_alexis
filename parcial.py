from funciones_parcial import *
from biblioteca_imprimir import*

def app(lista_jugadores: list) -> None:
    
    """
    Esta es una función que contiene un menú con varias opciones para manipular una lista de jugadores
    de baloncesto y sus estadísticas.
    
    :param lista_jugadores: El parámetro "lista_jugadores" es una lista de diccionarios, donde cada
    diccionario representa a un jugador de baloncesto y sus estadísticas
    :type lista_jugadores: list
    """

    jugador_segun_indice = None

    while True:

        imprimir_menu()
        opcion = input("Ingrese una opción: ")
        opcion = validar_opcion_expresion(r'^([0-9]|1[0-9]|2[0-3])$', opcion)

        match opcion:
            case 1:
                imprimir_lista_jugadores(lista_jugadores)
            case 2:
                imprimir_lista_jugadores(lista_jugadores)
                jugador_segun_indice = obtener_nombre_estadisticas(lista_jugadores)
            case 3:
                if jugador_segun_indice:
                    nombre = jugador_segun_indice["nombre"]
                    nombre = nombre.replace(" ", "_")
                    nombre = nombre.lower()
                    nombre_archivo = "estadisticas_{}.csv".format(nombre)
                    texto_generado = generar_texto(jugador_segun_indice)
                    guardar_archivo_csv(nombre_archivo, texto_generado)
                    jugador_segun_indice = None
                else:
                    print("No se puede guardar el archivo. Primero debe ingresar a la opción 2.")
            case 4:
                imprimir_lista_jugadores(lista_jugadores)
                jugadores_encontrados = buscar_jugador_por_nombre(lista_jugadores)
                imprimir_datos_jugadores(jugadores_encontrados)
            case 5:
                lista_jugadores_alfabeticamente(lista_jugadores)
            case 6:
                imprimir_lista_jugadores(lista_jugadores)
                jugadores_encontrados = buscar_jugador_por_nombre(lista_jugadores)
                imprimir_datos_jugadores_salon(jugadores_encontrados)
            case 7:
                max_rebotes = encontrar_maximo(lista_jugadores, "estadisticas", "rebotes_totales")
                imprimir_jugador_maximo(max_rebotes, "estadisticas","rebotes_totales")
            case 8:
                max_porcentaje_tiros_campo = encontrar_maximo(lista_jugadores, "estadisticas", "porcentaje_tiros_de_campo")
                imprimir_jugador_maximo(max_porcentaje_tiros_campo, "estadisticas", "porcentaje_tiros_de_campo")
            case 9:
                    max_asistencias = encontrar_maximo (lista_jugadores, "estadisticas",  "asistencias_totales")
                    imprimir_jugador_maximo(max_asistencias,"estadisticas", "asistencias_totales" )
        
            case 10:
                jugadores_promedio_puntos = filtrar_jugadores_por_estadistica(lista_jugadores, "promedio_puntos_por_partido")
                imprimir_jugadores(jugadores_promedio_puntos, "promedio_puntos_por_partido")
            case 11:
                jugadores_promedio_rebotes = filtrar_jugadores_por_estadistica(lista_jugadores, "promedio_rebotes_por_partido")
                imprimir_jugadores(jugadores_promedio_rebotes, "promedio_rebotes_por_partido")
            case 12:
                jugadores_promedio_asistencias = filtrar_jugadores_por_estadistica(lista_jugadores, "promedio_asistencias_por_partido")
                imprimir_jugadores(jugadores_promedio_asistencias, "promedio_asistencias_por_partido")
            case 13:
                jugadores_max_robos = encontrar_maximo(lista_jugadores, "estadisticas", "robos_totales")
                imprimir_jugador_maximo(jugadores_max_robos, "estadisticas","robos_totales")
            case 14:
                jugadores_max_bloqueos = encontrar_maximo(lista_jugadores, "estadisticas", "bloqueos_totales")
                imprimir_jugador_maximo(jugadores_max_bloqueos, "estadisticas","bloqueos_totales")
            case 15:
                jugadores_porcentaje_tiros_libres = filtrar_jugadores_por_estadistica(lista_jugadores, "porcentaje_tiros_libres")
                imprimir_jugadores(jugadores_porcentaje_tiros_libres, "porcentaje_tiros_libres")
            case 16:
                procesar_jugadores(lista_jugadores)
            case 17:
                jugador_con_mayor_logros = obtener_jugador_mayor_logros(lista_jugadores)
                print("El jugador con la mayor cantidad de logros obtenidos es:", jugador_con_mayor_logros)
            case 18:
                jugadores_porcentaje_tiros_triples = filtrar_jugadores_por_estadistica(lista_jugadores, "porcentaje_tiros_triples")
                imprimir_jugadores(jugadores_porcentaje_tiros_triples, "porcentaje_tiros_triples")
            case 19:
                jugador_con_mas_temporadas(lista_jugadores)
            case 20:
                ordenados_posicion_cancha(lista_jugadores)
            case 21:
                print("¡Salió!")
                break
            case 23:
                jugadores_con_estadisticas = obtener_jugadores_con_estadisticas_ordenadas(lista_jugadores)
                nombre_archivo = "informe_jugadores.csv"
                texto_generado = generar_texto(jugadores_con_estadisticas)
                guardar_archivo_csv(nombre_archivo, texto_generado)
                imprimir_guarda_tabla_jugadores(jugadores_con_estadisticas)

            case _:
                print("¡Opción incorrecta!")
        clear_console()


archivo = "dt.json"
lista_jugadores = leer_archivo_json(archivo)
app(lista_jugadores)

