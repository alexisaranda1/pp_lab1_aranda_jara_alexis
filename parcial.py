from funciones_parcial import *


def app(lista_jugadores: list) -> None:

    texto_generado = ""
    jugador_segun_indice = None

    while True:

        imprimir_menu()
        opcion = input("Ingrese una opción: ")
        opcion = validar_opcion_expresion(r'^([0-9]|1[0-9]|2[0-3])$', opcion)

        match opcion:

            case 0:
                print("¡Salió!")
                break
            case 1:
                buscar_nombre_posicion(lista_jugadores)
            case 2:
                buscar_nombre_posicion(lista_jugadores)
                jugador_segun_indice = obtener_nombre_estadisticas(lista_jugadores)
            case 3:
                if jugador_segun_indice:
                    nombre_archivo = "nombre_estadisticas_jugador.csv"
                    texto_generado = genera_texto(jugador_segun_indice)
                    guardar_archivo_csv(nombre_archivo, texto_generado)
                else:
                    print("No se puede guardar el archivo. Primero debe ingresar a la opción 2.")
            case 4:
                buscar_nombre_posicion(lista_jugadores)
                jugadores_encontrados = buscar_jugador_por_nombre(lista_jugadores)
                imprimir_datos_jugadores(jugadores_encontrados)
            case 5:
                lista_jugadores_alfabeticamente(lista_jugadores)
            case 6:
                buscar_nombre_posicion(lista_jugadores)
                jugadores_encontrados = buscar_jugador_por_nombre(lista_jugadores)
                imprimir_datos_jugadores_salon(jugadores_encontrados)
            case 7:
                max_rebotes = encontrar_maximo(lista_jugadores, "estadisticas", "rebotes_totales")
                imprimir_dato(max_rebotes)
            case 8:
                max_porcentaje_tiros_campo = encontrar_maximo(lista_jugadores, "estadisticas", "porcentaje_tiros_de_campo")
                imprimir_dato(max_porcentaje_tiros_campo)
            case 9:
                max_asistencias = encontrar_maximo(lista_jugadores, "estadisticas", "asistencias_totales")
                imprimir_dato(max_asistencias)
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
                imprimir_dato(jugadores_max_robos)
            case 14:
                jugadores_max_bloqueos = encontrar_maximo(lista_jugadores, "estadisticas", "bloqueos_totales")
                imprimir_dato(jugadores_max_bloqueos)
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
            case 23:

                #imprimir_tabla_jugadores(lista_jugadores)

                lista_ordenada_puntos_totales = ordenar_por_estaditica(lista_jugadores,"puntos_totales",False)
                lista_ordenada_rebotes_totales = ordenar_por_estaditica(lista_jugadores,"rebotes_totales",False)
                lista_ordenada_asistencias_totales = ordenar_por_estaditica(lista_jugadores,"asistencias_totales",False)
                lista_ordenada_bloqueos_totales = ordenar_por_estaditica(lista_jugadores,"bloqueos_totales",False)

                print ("----------------puntos-------------------")
                for i in range(len(lista_ordenada_puntos_totales)):
                    jugador = lista_ordenada_puntos_totales[i]
                    jugador["estadisticas"]["puntos_totales"] = i + 1
                    print(jugador["nombre"], jugador["estadisticas"]["puntos_totales"])
                print("-----------------rebotes-----------------------------")

                for i in range(len(lista_ordenada_rebotes_totales)):
                    jugador = lista_ordenada_puntos_totales[i]
                    jugador["estadisticas"]["puntos_totales"] = i + 1
                    print(jugador["nombre"], jugador["estadisticas"]["puntos_totales"])
                print("----------------asitencias-------------")

                for i in range(len(lista_ordenada_asistencias_totales)):
                    jugador = lista_ordenada_puntos_totales[i]
                    jugador["estadisticas"]["puntos_totales"] = i + 1
                    print(jugador["nombre"], jugador["estadisticas"]["puntos_totales"])
                print("----------------bloqueos-------------")
                for i in range(len(lista_ordenada_bloqueos_totales)):
                    jugador = lista_ordenada_puntos_totales[i]
                    jugador["estadisticas"]["puntos_totales"] = i + 1
                    print(jugador["nombre"], jugador["estadisticas"]["puntos_totales"])
            case _:
                print("¡Opción incorrecta!")

        clear_console()




archivo = "dt.json"
lista_jugadores = leer_archivo_json(archivo)
app(lista_jugadores)









