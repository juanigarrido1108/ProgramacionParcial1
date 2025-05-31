import os
from Funciones import *

# array_nombres = crear_array(5,"")
# matriz_votos = crear_matriz(5,3,0)

array_nombres = crear_array(5,"")
matriz_puntaje = crear_matriz(5,3,0)

bandera_carga_nombres = False
bandera_carga_puntaje = False

while True:
    print("¡Competencia de Baile!\n")

    print("1.Cargar Nombres Participantes\n2.Cargar Puntaje\n3.Mostrar Puntaje\n4.Participantes con promedio menor a 4\n5.Participantes con promedio menor a 8\n6.Promedio del puntaje de cada jurado.\n7.Jurado más estricto\n8. Jurado más generoso\n9. Participantes con puntuaciones iguales\n10. Buscar participante por nombre\n 16.Salir")
    
    opcion = obtener_opcion_menu()

    if opcion == 1:
        if cargar_nombres_participantes_valido(array_nombres) == True:
            print("Nombres cargados correctamente...")
            mostrar_array(array_nombres)
            bandera_carga_nombres = True
        else:
            print("Error al realizar la carga")

    elif opcion == 2:
        if bandera_carga_nombres == False:
            print("Error: Primero debe ingresar los nombres de los participantes.")
        elif cargar_puntaje_valido(matriz_puntaje) == True:
            print("Carga exitosa de puntaje!")
            mostrar_matriz(matriz_puntaje)
            bandera_carga_puntaje = True
        else:
            print("Error al realizar la carga")

    elif opcion == 3 and (bandera_carga_puntaje == True and bandera_carga_nombres == True):
        if mostrar_puntajes(array_nombres,matriz_puntaje) == False:
            print("No se pueden mostrar los puntajes")

    elif opcion == 4 and (bandera_carga_puntaje == True and bandera_carga_nombres == True):
        promedio_puntaje_participantes = promedio_puntaje(matriz_puntaje)
        if mostrar_participantes_promedio_4(promedio_puntaje_participantes,array_nombres) == False: 
            print(f"No hay ningun participante con promedio menor a 4")

    elif opcion == 5 and (bandera_carga_puntaje == True and bandera_carga_nombres == True):
        promedio_puntaje_participantes = promedio_puntaje(matriz_puntaje)
        if mostrar_participantes_promedio_8(promedio_puntaje_participantes,array_nombres) == False: 
            print(f"No hay ningun participante con promedio menor a 8")

    elif opcion == 6 and (bandera_carga_puntaje == True and bandera_carga_nombres == True):
        suma_puntaje_jurados = suma_puntaje_jurado(matriz_puntaje)
        if mostrar_puntaje_promedio_de_jurados3(array_nombres,matriz_puntaje,0) == False:
            print(f"error")
    
    elif opcion == 7 and (bandera_carga_puntaje == True and bandera_carga_nombres == True):
        if mostrar_jurado_mas_estricto(matriz_puntaje) == False:
            print("Error al mostrar jurado más estricto")
    
    elif opcion == 8 and (bandera_carga_puntaje == True and bandera_carga_nombres == True):
        if mostrar_jurado_mas_generoso(matriz_puntaje) == False:
            print("Error al mostrar jurado más generoso")

    elif opcion == 9 and (bandera_carga_puntaje == True and bandera_carga_nombres == True):
        if mostrar_participantes_puntuaciones_iguales(matriz_puntaje, array_nombres) == False:
            print("Error al mostrar participantes con puntuaciones iguales")

    elif opcion == 10 and (bandera_carga_puntaje == True and bandera_carga_nombres == True):
        if solicitar_busqueda_participante(array_nombres, matriz_puntaje) == False:
            print("Error en la búsqueda de participante")

    elif opcion == 16:
        print("Saliendo...")

    elif opcion == None:
        print("Debe ingrear una opcion")
        break

    else:
        print("Acceso invalido!")
    input("Toque cualquier boton para continuar...")
    os.system("clear")