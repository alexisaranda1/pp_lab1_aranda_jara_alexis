from funciones_parcial import *


def app(lista_jugadores: list)-> None:

    while True:

        imprimir_menu_Desafio()
        opcion = input("Ingrese una opcion: ")
        opcion = validar_opcion_expresion(r'^[1-9]{1,2}$', opcion )
        int_opcion = int(opcion)

        match int_opcion:
            case 1:
                datos_jugador = buscar_nombre_posicion(lista_jugadores)
                imprimir_dato(datos_jugador)
            case 2:
                pass
            case 3:
                pass
            case 4:
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