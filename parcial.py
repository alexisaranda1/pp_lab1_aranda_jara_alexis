from funciones_parcial import *


def app(lista_jugadores: list)-> None:
    nombre_archivo = ""
    jugador_segun_indice = ""

    while True:

        imprimir_menu_Desafio()
        opcion = input("Ingrese una opcion: ")
        opcion = validar_opcion_expresion(r'^[1-9]{1,2}$', opcion )
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

                nombre_buscado = input("Ingresa el nombre del jugador a buscar: ")
                buscar_jugador(lista_jugadores, nombre_buscado)
                
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case 9:
                pass
            case 10:
                pass
            case 10:
                pass
            case 11:
                pass
            
            case 12:
                pass                
            case 13:
                pass
            case 15:
                pass
            case 16:
                pass
            case 17:
                pass
            case 18:
                pass
            case 19:
                pass
            case 20:
                pass
            case 21:
                print("salio!")
                break
            case _:
                print("¡opción incorrecta!.")
        clear_console()




archivo ="dt.json"

lista_jugadores = leer_archivo_sjon(archivo)
app(lista_jugadores)
#print(lista_jugadores)