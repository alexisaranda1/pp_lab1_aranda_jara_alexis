from funciones_parcial import *

def app(lista_jugadores: list)-> None:

    while True:      

        imprimir_menu_Desafio()
        opcion = input("Ingrese una opcion: ")
        opcion = validar_opcion_expresion(r'^[0-9]{1,2}$', opcion )


        match opcion:
            case 1:

                buscar_nombre_posicion(lista_jugadores)
            case 2:

                buscar_nombre_posicion(lista_jugadores)
                indice = input("selecciona un jugador por su índice para ver sus estadísticas: ")
                indice = validar_opcion_expresion(r'^[0-9]{1,2}$', indice )

                if indice >= 0 and indice <len(lista_jugadores):
                    nombre_archivo = "nombre_estiditicas_jugador.csv"
                    jugador_segun_indice = obtener_nombre_estadisticas(lista_jugadores, indice)
                else:
                    print("indice invalido".format(indice))
            case 3:
                if nombre_archivo: 
                    guardar_archivo_csv(nombre_archivo, jugador_segun_indice)
                else:

                    print("No puede guardar el archivo, primero tiene que ingresar a la opcion 2")
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
                resultado = encontrar_maximo(lista_jugadores, "estadisticas", "rebotes_totales")
                imprimir_dato(resultado)
            case 8:
                resultado = encontrar_maximo(lista_jugadores, "estadisticas", "porcentaje_tiros_de_campo")
                imprimir_dato(resultado)
            case 9:
                resultado = encontrar_maximo(lista_jugadores, "estadisticas", "asistencias_totales")
                imprimir_dato(resultado)
            case 10:
                filtrar_jugadores_por_estadistica(lista_jugadores, "promedio_puntos_por_partido")
            case 11:
                filtrar_jugadores_por_estadistica(lista_jugadores, "promedio_rebotes_por_partido")
            case 12:
                  filtrar_jugadores_por_estadistica(lista_jugadores, "promedio_asistencias_por_partido")           
            case 13:
                resultado = encontrar_maximo(lista_jugadores, "estadisticas", "robos_totales")
                imprimir_dato(resultado)
            case 14:
                resultado = encontrar_maximo(lista_jugadores, "estadisticas", "bloqueos_totales")
                imprimir_dato(resultado)
            case 15:
                filtrar_jugadores_por_estadistica(lista_jugadores, "porcentaje_tiros_libres")
            case 16:
                procesar_jugadores(lista_jugadores)
            case 17:
                jugador_con_mayor_logros = obtener_jugador_mayor_logros(lista_jugadores)
                print("El jugador con la mayor cantidad de logros obtenidos es:", jugador_con_mayor_logros)
            case 18:
                filtrar_jugadores_por_estadistica(lista_jugadores, "porcentaje_tiros_triples")
            case 19:
                jugador_con_mas_temporadas(lista_jugadores)
            case 20:
                ordenados_posicion_cancha(lista_jugadores)
            case 21:
                print("salio!")
                break
            case 23:

                print("---------------------------------------------------------------------------")
                print("|     Jugador          |    Puntos  |   Rebotes |  Asistencias  |  Robos  |")
                print("---------------------------------------------------------------------------")
                for jugador in lista_jugadores:
                    print("|  {:19s} | {:^10d} | {:^9d} | {:^13d} | {:^7d} |".format(jugador["nombre"], jugador["estadisticas"]["puntos_totales"], jugador["estadisticas"]["rebotes_totales"], jugador["estadisticas"]["asistencias_totales"], jugador["estadisticas"]["robos_totales"]))
                print("---------------------------------------------------------------------------")

            case _:
                print("¡opción incorrecta!.")
                
        clear_console()

archivo = "dt.json"
lista_jugadores = leer_archivo_sjon(archivo)
app(lista_jugadores)