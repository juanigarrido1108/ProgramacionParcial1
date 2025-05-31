#GENERAL


#Crea una matriz con dimensiones específicas e inicializada con un valor determinado. 
def crear_matriz(cantidad_filas:int,cantidad_columnas:int,valor_inicial:any) -> list:
    """
    Args:
        cantidad_filas (int): Número de filas que tendrá la matriz. 
                              Debe ser un entero positivo
        cantidad_columnas (int): Número de columnas que tendrá la matriz.
                                 Debe ser un entero positivo.
        valor_inicial (any): Valor con el que se inicializarán todos los 
                             elementos de la matriz. Puede ser de cualquier tipo
                             (int, str, float, bool, None, etc.).

    Returns:
        list: matriz creada con la cantidad de filas, columnas, y el valor inicial designado.
    """
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        #matriz.append(fila)
        matriz += [fila]
   
    return matriz

#Crea una lista (array) unidimensional con un número específico de elementos, todos inicializados con el mismo valor.
def crear_array(cantidad_elementos:int,valor_inicial:any) -> list:
    """
    Args:
        cantidad_elementos (int): Número de elementos que tendrá el array.
                                  Debe ser un entero no negativo.
        valor_inicial (any): Valor con el que se inicializarán todos los 
                             elementos del array. Puede ser de cualquier tipo
                             (int, str, float, bool, None, etc.).

    Returns:
        list: Una lista con la cantidad de elemenots indicada, donde cada elemento toma el valor inicial mencionado.
    """
    array = [valor_inicial] * cantidad_elementos
    return array

#Solicita al usuario que ingrese el nombre de los participantes y los almacena en un array previamente creado, modificando el array correspondiente al parametro indicado.
def cargar_nombres_participantes_valido(array_nombres: list) -> bool:
    """
    Esta función valida que el parámetro sea una lista no vacía, se posiciona sobre cada posición solicitando input del usuario para llenar cada espacio del array con los nombres del participante.

    Args:
        array_nombres (list): Lista de nombres creada en principio.

    Returns:
        bool: True si la lista fue validada.
              False si el parámetro no es una lista o la lista no está validada.
    """    
    if type(array_nombres) == list and len(array_nombres) > 0:
        for i in range(len(array_nombres)):
            while True:  # Esto repite hasta que el nombre sea válido
                nombre = input(f"Ingrese el nombre del participante (Solo se permiten letras y espacios) {i + 1}: ")
                
                # funcion que valida el nombre
                if es_nombre_valido(nombre) and es_solo_espacio(nombre):
                    array_nombres[i] = nombre
                    break  # Salir del while, nombre válido obtenido
                else:
                    print("Solo se permiten letras, espacios y un minimo de 3 letras.")
        
        return True
    else:
        return False

def es_nombre_valido(nombre: str) -> bool:
    """
    Se encarga de validar que el nombre ingresado del participante no contenga menos de 3 caracteres, y que lo ingresado sean unicamente letras mayusculas, minusculas y espacios.
    Esta funcion se utiliza dentro de la funcion cargar_nombres_participantes_valido2().

    Args:
        nombre: str: Nombre proporcionado en la funcion cargar_nombres_participantes_valido2()
    Returns:
        bool: True si cumple con las validaciones.
              False si no cumple con las validaciones.
    """    
    
    if len(nombre) < 3:  # Si no quiero que sean menos de 3 caracteres.
        return False
    
    # Verifica cada carácter y compara si son o no mayusculas, minusculas y espacios.
    else:
        for i in range(len(nombre)):
            caracter = nombre[i]
            codigo = ord(caracter)
            
            # Verificar si es letra (A-Z, a-z) o espacio (32)
            es_letra_mayuscula = 65 <= codigo <= 90
            es_letra_minuscula = 97 <= codigo <= 122
            es_espacio = codigo == 32
            if not (es_letra_mayuscula or es_letra_minuscula or es_espacio):
                return False
    
    return True

from Funciones import *


#Esta funcion está en el modulo de funciones, por alguna razon cuando quiero importarla desde funciones, no me permite invocarla dentro de otra funcion que estoy definiendo. Me da error de definición de la variable al ejecutar el código. Por eso la copie y pegué en este modulo de inputs para poder ejecutar el codigo sin problemas.


def obtener_opcion_menu() -> int:
    """Obtiene la opción ingresada y la valida en la funcion correspondiente"""
    # ingreso la opcion
    entrada = input("Su opcion: ")
    # valido, si no es valido entre en bucle hasta que sea valida la opcion.
    while not es_opcion_valida2(entrada):
        print("Debe ingresar una opción válida (1-16)")
        entrada = input("Su opcion: ")
    # una vez validado, paso el valor de la entrada a un entero para poder validar a que opcion corresponde dentro del menu de opciones.
    return int(entrada)
    


def es_opcion_valida2(entrada: str) -> bool:
    """
        Valida que la entrada de la opcion elegida sea un número válido para las opciones del menu.

    Args:
        entrada: str: string proveniente de la variable "opcion" proporcionada por el input en la funcion obtener_opcion_menu()
    Returns:
        bool: True si cumple con las validaciones.
              False si no cumple con las validaciones.
   
    """
    if entrada == "":  # Sí es un enter, no es valido
        return False
    
    if len(entrada) > 2:  # Si supera los 2 digitos, no es valido
        return False
    
    # Verifica que todos los caracteres sean digitos
    for i in range(len(entrada)):
        caracter = entrada[i]
        codigo = ord(caracter)
        
        # Verificar si es un numero del 0 al 9 mediante ascii
        es_digito = 48 <= codigo <= 57
        
        if not es_digito:
            return False  # Si encuentra una letra o símbolo, no es valido
    
    # si llega aca es porque cumple las validaciones.
    # convierto la entrada en un entero para verificar que esté dentro del rango que deseo de opciones.
    numero = int(entrada)
    # Devuelvo un booleano para validar en la siguiente funcion
    return 1 <= numero <= 16

#Se encarga de validar si el nombre tiene espacios al momento de ingresar los nombres de los participantes.
def es_solo_espacio(nombre: str) -> bool:
    """
    Valida que el nombre solo contenga espacios

    Args:
        nombre: str: Nombre proporcionado en la funcion cargar_nombres_participantes_valido2()

    returns:
        bool: false si valida que hay un espacio.
                true si valida que no hay un espacio.
    """
    
    # Verificar cada carácter
    for i in range(len(nombre)):
        caracter = nombre[i]
        codigo = ord(caracter)
        
        # Verificar si es espacio (32)
        es_espacio = codigo == 32
        
        if es_espacio:
            return False
    
    return True


#GENERAL
def mostrar_array(array:list) -> None:

    for i in range(len(array)):
        print(f"{array[i]}")

#GENERAL  
def mostrar_matriz(matriz:list) -> None:
    for fil in range(len(matriz)):
        for col in range(len(matriz[fil])):
            print(f"{matriz[fil][col]}",end=" ")
        print("")
        

#Cargar puntaje validado: Se encarga de validar el puntaje cargado de los jurados dentro de la matriz, en un rango del puntaje del 1 al 10.
def cargar_puntaje_valido(matriz_puntaje:list) -> bool:
    """
    Valida el puntaje cargado de los jurados dentro de la matriz, en un rango del puntaje del 1 al 10.

    Args:
        matriz_puntaje: list: Matriz inicializada en el Main.

    returns:
        bool: true si la validacion de rangos es correcta, la matriz es una lista y es mayor a 0, y si es un numero.
                false si la matriz no es una lista ni es mayor a 0 ni es un numero.
    """
    if type(matriz_puntaje) == list and len(matriz_puntaje) > 0:
        retorno = True
    
        for fil in range(len(matriz_puntaje)):
            for col in range(len(matriz_puntaje[fil])):
                #Pedir el dato
                while True:  #Bucle para validar entrada
                    entrada = input(f"Ingrese un puntaje del 1 al 10 del participante {fil + 1} para el turno {col + 1}: ")
                    
                    #Validar que sea un número 
                    if es_opcion_valida2(entrada):
                        votos = int(entrada)  # Ahora sí convertir a entero
                        #Validar rango específico (1-10) 
                        if 1 <= votos <= 10:
                            matriz_puntaje[fil][col] = votos
                            break  # Salir del while, puntaje válido
                        else:
                            print("El puntaje debe estar entre 1 y 10.")
                    else:
                        print("Debe ingresar un número válido.")
    else:
        retorno = False
        
    return retorno
#ESPECIFICA
def mostrar_puntaje(array_nombres:list,matriz_puntaje:list,indice:int) -> bool:
    """
    Muestra los puntajes de los participantes, discriminado por cada jurado, mostrando la suma de los 3 puntajes y el promedio del puntaje de cada participante.

    Args:
        array_nombre: list (lista de nombres) matriz_puntaje: list (matriz con puntajes ya cargados.) indice: int (opcional, no hace falta ponerlo para que esta funcion se ejecute ya que toma el valor por si misma dentro de la funcion)

    returns:
        bool: true si la validacion de rangos es correcta y la matriz es una lista y es mayor a 0.
                false si la matriz no es una lista ni es mayor a 0.
    """
    if type(matriz_puntaje) == list and type(array_nombres) == list and len(matriz_puntaje) > 0 and len(array_nombres) > 0 and (indice < len(array_nombres) and indice >= 0):
        puntaje_participantes = sumar_columnas_por_fila3(matriz_puntaje)
        promedio_puntaje_participantes = promedio_puntaje(matriz_puntaje)
        retorno = True
        print(f"NOMBRE: {array_nombres[indice]}")
        print(f"PUNTAJE JURADO 1: {matriz_puntaje[indice][0]}")
        print(f"PUNTAJE JURADO 2: {matriz_puntaje[indice][1]}")
        print(f"PUNTAJE JURADO 3: {matriz_puntaje[indice][2]}")
        print(f"SUMA DE LOS 3 PUNTAJES {puntaje_participantes[indice]}")
        print(f"PROMEDIO DE LOS 3 PUNTAJES {round(promedio_puntaje_participantes[indice],2)}")
    else:
        retorno = False
        
    return retorno

#Funcion que muestra los puntajes con lo solicitado.
def mostrar_puntajes(array_nombres:list,matriz_puntaje:list) -> bool:
    '''
    Muestra los puntajes detallados de todos los participantes, incluyendo 
    las calificaciones de cada jurado, la suma total y el promedio.
    
    Args:
        array_nombres (list): Lista con los nombres de los participantes
        matriz_puntaje (list): Matriz con los puntajes otorgados por cada jurado
        
    Returns:
        bool: True si se pudieron mostrar los puntajes correctamente,
                False si los parámetros no son válidos
    '''

    if type(matriz_puntaje) == list and type(array_nombres) == list and len(matriz_puntaje) > 0 and len(array_nombres) > 0:
        retorno = True
        for i in range(len(array_nombres)):
            mostrar_puntaje(array_nombres,matriz_puntaje,i)
            print("")
    else:
        retorno = False
        
    return retorno

def sumar_columnas_por_fila(matriz_puntaje:list) -> list:
    
    puntaje_participantes = crear_array(5,0)
    primera_suma = True

    for fil in range(len(matriz_puntaje)):
        for col in range(len(matriz_puntaje)):
            if primera_suma == True:
                puntaje_participantes[0] += matriz_puntaje[fil][col]
                primera_suma = False
            else:
                for i in range(len(puntaje_participantes)):
                    puntaje_participantes[i+1] += matriz_puntaje[fil][col]
    
    return puntaje_participantes

# def mostrar_suma_nota_participantes(puntaje_participantes) -> bool:

def sumar_columnas_por_fila2(matriz_puntaje:list) -> list:
    
    cantidad_filas = len(matriz_puntaje)
    puntaje_participantes = crear_array(cantidad_filas,0)
    primera_suma = True

    for fil in range(len(matriz_puntaje)):
        for col in range(len(matriz_puntaje[fil])):
            if primera_suma == True:
                puntaje_participantes[0] += matriz_puntaje[fil][col]
                primera_suma = False
            else:
                for i in range(len(puntaje_participantes)):
                    puntaje_participantes[fil] += matriz_puntaje[fil][col]
    
    return puntaje_participantes

def sumar_columnas_por_fila3(matriz_puntaje: list) -> list:
    """
    Suma todos los elementos de cada fila y devuelve un array con los totales.
    """
    cantidad_filas = len(matriz_puntaje)
    puntaje_participantes = crear_array(cantidad_filas, 0)

    for fil in range(len(matriz_puntaje)):
        for col in range(len(matriz_puntaje[fil])):
            # Simplemente suma cada elemento a SU fila correspondiente
            puntaje_participantes[fil] += matriz_puntaje[fil][col]
    
    return puntaje_participantes


#promedio de los puntajes de cada participante
def promedio_puntaje(matriz_puntaje: list) -> list:
    '''
   Calcula el promedio de puntaje de cada participante basado en las 
   calificaciones de todos los jurados.
   
   Args:
       matriz_puntaje (list): Matriz con los puntajes de cada participante por jurado
       
   Returns:
       list: Array con el promedio de puntaje de cada participante
   '''
    
    cantidad_filas = len(matriz_puntaje)
    promedio_puntaje_participantes = crear_array(cantidad_filas,0)

    for fil in range(len(matriz_puntaje)):
        contador = 0
        for col in range(len(matriz_puntaje[fil])):
            contador += matriz_puntaje[fil][col]
            promedio_puntaje_participantes[fil] = contador/len(matriz_puntaje[fil])
    
    return promedio_puntaje_participantes

#calcula promedio menor a 4 del puntaje de los participantes.
def mostrar_participantes_promedio_4(promedio_puntaje_participantes: list, array_nombres: list) -> bool:
    '''
   Muestra los participantes que tienen un promedio de puntaje menor a 4.
   
   Args:
       promedio_puntaje_participantes (list): Array con los promedios de cada participante
       array_nombres (list): Lista con los nombres de los participantes
       
   Returns:
       bool: True si hay al menos un participante con promedio menor a 4
             False si no hay ninguno
   '''
    retorno = False

    for i in range(len(promedio_puntaje_participantes)):
        if promedio_puntaje_participantes[i] < 4:
            print(f"El participante {array_nombres[i]} tiene un promedio menor a 4. ")
            retorno = True
        else: 
            None

    return retorno

#Misma funcion que promedio 4 pero con 8
def mostrar_participantes_promedio_8(promedio_puntaje_participantes: list, array_nombres: list) -> bool:
    '''
    Muestra los participantes que tienen un promedio de puntaje menor a 8.
    
    Args:
        promedio_puntaje_participantes (list): Array con los promedios de cada participante
        array_nombres (list): Lista con los nombres de los participantes
        
    Returns:
        bool: True si hay al menos un participante con promedio menor a 8
                False si no hay ninguno
    '''
    retorno = False

    for i in range(len(promedio_puntaje_participantes)):
        if promedio_puntaje_participantes[i] < 8:
            print(f"El participante {array_nombres[i]} tiene un promedio menor a 8. ")
            retorno = True
        else: 
            None

    return retorno

def suma_puntaje_jurado(matriz_puntaje: list) -> list:
    cantidad_jurados = len(matriz_puntaje[0])  # Número de columnas se indica asi dentro de la matriz -> [0]
    suma_puntaje_jurados = crear_array(cantidad_jurados, 0)

    for fil in range(len(matriz_puntaje)):
        for col in range(len(matriz_puntaje[fil])):
            suma_puntaje_jurados[col] += matriz_puntaje[fil][col]

    return suma_puntaje_jurados # <-- Esta lista se entrega como parametro o para contenerla en una variable en otra
                                    # función que la precise.

#Mostrar puntaje promedio de jurados
#Este si va, aunque depende de que le pasemos la posición del array de suma_puntaje_jurados para cada print.
def mostrar_suma_puntaje_de_jurados(array_nombres:list,matriz_puntaje:list,indice:int) -> bool:

    '''
   Muestra la suma total de puntajes otorgados por cada jurado a todos los participantes.
   
   Args:
       array_nombres (list): Lista con los nombres de los participantes
       matriz_puntaje (list): Matriz con los puntajes de cada participante por jurado
       indice (int): Índice de referencia para validaciones (no se usa en la lógica principal)
       
   Returns:
       bool: True si se pudieron mostrar los puntajes de los jurados correctamente,
             False si los parámetros no son válidos
   '''
    suma_puntaje_jurados = suma_puntaje_jurado(matriz_puntaje)
    if type(suma_puntaje_jurados) == list and type(array_nombres) == list and len(suma_puntaje_jurados) > 0 and len(array_nombres) > 0 and (indice < len(array_nombres) and indice >= 0):
        retorno = True
        print(f"PUNTAJE JURADO 1: {suma_puntaje_jurados[0]}")
        print(f"PUNTAJE jURADO 2: {suma_puntaje_jurados[1]}")
        print(f"PUNTAJE jURADO 3: {suma_puntaje_jurados[2]}")
    else:
        retorno = False
        
    return retorno

#mostrar puntaje promedio de jurados
# No funciona, repite la puntuacion 3 veces por igual. 
def mostrar_puntaje_promedio_de_jurados2(array_nombres:list,matriz_puntaje:list,indice:int) -> bool:
    
    
    suma_puntaje_jurados = suma_puntaje_jurado(matriz_puntaje)
    if type(suma_puntaje_jurados) == list and type(array_nombres) == list and len(suma_puntaje_jurados) > 0 and len(array_nombres) > 0 and (indice < len(array_nombres) and indice >= 0):
        retorno = True
        for i in range(len(suma_puntaje_jurados)):
            print(f"PUNTAJE JURADO 1: {suma_puntaje_jurados[i]}")
            print(f"PUNTAJE jURADO 2: {suma_puntaje_jurados[i]}")
            print(f"PUNTAJE jURADO 3: {suma_puntaje_jurados[i]}")
    else:
        retorno = False
        
    return retorno

#Promedio del puntaje por cada uno de los jurados. Toma la suma de las 3 notas de cada jurado y las divide entre 3.
def mostrar_puntaje_promedio_de_jurados3(array_nombres:list,matriz_puntaje:list,indice:int) -> bool:
    '''
    Muestra el puntaje promedio otorgado por cada uno de los 3 jurados a todos los participantes.

    Args:
    array_nombres (list): Lista con los nombres de los participantes
    matriz_puntaje (list): Matriz con los puntajes de cada participante por jurado
    indice (int): Índice de referencia para validaciones (debe estar dentro del rango de participantes)
    
    Returns:
    bool: True si se pudieron mostrar los puntajes promedio de los jurados correctamente,
            False si los parámetros no son válidos o están fuera de rango
    '''
    promedio_puntaje_por_jurado = promedio_puntaje_jurado(matriz_puntaje)
    if type(promedio_puntaje_por_jurado) == list and type(array_nombres) == list and len(promedio_puntaje_por_jurado) > 0 and len(array_nombres) > 0 and (indice < len(array_nombres) and indice >= 0):
        retorno = True
        print(f"PUNTAJE JURADO 1: {round(promedio_puntaje_por_jurado[0],2)}")
        print(f"PUNTAJE jURADO 2: {round(promedio_puntaje_por_jurado[1],2)}")
        print(f"PUNTAJE jURADO 3: {round(promedio_puntaje_por_jurado[2],2)}")
    else:
        retorno = False
        
    return retorno

#Calcula el puntaje promedio del jurado
def promedio_puntaje_jurado(matriz_puntaje: list) -> list:
    '''
Calcula el puntaje promedio otorgado por cada jurado a todos los participantes.

Args:
   matriz_puntaje (list): Matriz bidimensional donde cada fila representa un participante
                         y cada columna representa los puntajes de cada jurado
   
Returns:
   list: Lista con el promedio de puntajes por jurado, donde cada índice corresponde
         al promedio del jurado de esa columna
'''
    cantidad_jurados = len(matriz_puntaje[0])  # Número de columnas se indica asi dentro de la matriz -> [0]
    promedio_puntaje_por_jurado = crear_array(cantidad_jurados, 0)

    for fil in range(len(matriz_puntaje)):
        for col in range(len(matriz_puntaje[fil])):
            promedio_puntaje_por_jurado[col] += matriz_puntaje[fil][col] / len(matriz_puntaje)

    return promedio_puntaje_por_jurado  # <-- Esta lista se entrega como parametro o para contenerla en una variable en otra
                                    # función que la precise.

#Calcula cual es el jurado mas estricto
def encontrar_jurado_mas_estricto(matriz_puntaje: list) -> list:
    """
    Encuentra el o los jurados que otorgaron los puntajes promedio más bajos.
    
    Args:
        matriz_puntaje (list): Matriz con los puntajes de cada participante por jurado
        
    Returns:
        list: Lista con los índices de los jurados más estrictos
    """
    promedio_por_jurado = promedio_puntaje_jurado(matriz_puntaje)
    
    # Encontrar el promedio más bajo
    promedio_minimo = promedio_por_jurado[0]
    for i in range(len(promedio_por_jurado)):
        if promedio_por_jurado[i] < promedio_minimo:
            promedio_minimo = promedio_por_jurado[i]
    
    # Encontrar todos los jurados con ese promedio mínimo
    jurados_estrictos = crear_array(len(promedio_por_jurado), -1)
    contador = 0
    
    for i in range(len(promedio_por_jurado)):
        if promedio_por_jurado[i] == promedio_minimo:
            jurados_estrictos[contador] = i
            contador += 1
    
    # Crear array del tamaño correcto solo con los jurados encontrados
    resultado = crear_array(contador, -1)
    for i in range(contador):
        resultado[i] = jurados_estrictos[i]
    
    return resultado

#Calcula cual es el jurado mas generoso
def encontrar_jurado_mas_generoso(matriz_puntaje: list) -> list:
    """
    Encuentra el o los jurados que otorgaron los puntajes promedio más altos.
    
    Args:
        matriz_puntaje (list): Matriz con los puntajes de cada participante por jurado
        
    Returns:
        list: Lista con los índices de los jurados más generosos
    """
    promedio_por_jurado = promedio_puntaje_jurado(matriz_puntaje)
    
    # Encontrar el promedio más alto
    promedio_maximo = promedio_por_jurado[0]
    for i in range(len(promedio_por_jurado)):
        if promedio_por_jurado[i] > promedio_maximo:
            promedio_maximo = promedio_por_jurado[i]
    
    # Encontrar todos los jurados con ese promedio máximo
    jurados_generosos = crear_array(len(promedio_por_jurado), -1)
    contador = 0
    
    for i in range(len(promedio_por_jurado)):
        if promedio_por_jurado[i] == promedio_maximo:
            jurados_generosos[contador] = i
            contador += 1
    
    # Crear array del tamaño correcto solo con los jurados encontrados
    resultado = crear_array(contador, -1)
    for i in range(contador):
        resultado[i] = jurados_generosos[i]
    
    return resultado

#muestra los jurados mas estrictos
def mostrar_jurado_mas_estricto(matriz_puntaje: list) -> bool:
    """
    Muestra el/los jurado o jurados más estrictos con sus promedios.
    
    Args:
        matriz_puntaje (list): Matriz con los puntajes de cada participante por jurado
        
    Returns:
        bool: True si se pudo mostrar la información, False en caso contrario
    """
    if type(matriz_puntaje) == list and len(matriz_puntaje) > 0:
        jurados_estrictos = encontrar_jurado_mas_estricto(matriz_puntaje)
        promedio_por_jurado = promedio_puntaje_jurado(matriz_puntaje)
        
        print("JURADO O JURADOS MAS ESTRICTOS:")
        
        if len(jurados_estrictos) == 1:
            indice = jurados_estrictos[0]
            print(f"Jurado {indice + 1} con promedio: {round(promedio_por_jurado[indice], 2)}")
        else:
            print("Empate entre los siguientes jurados:")
            for i in range(len(jurados_estrictos)):
                indice = jurados_estrictos[i]
                print(f"Jurado {indice + 1} con promedio: {round(promedio_por_jurado[indice], 2)}")
        
        return True
    else:
        return False

#muestra los jurados mas generosos
def mostrar_jurado_mas_generoso(matriz_puntaje: list) -> bool:
    """
    Muestra el/los jurado(s) más generoso(s) con sus promedios.
    
    Args:
        matriz_puntaje (list): Matriz con los puntajes de cada participante por jurado
        
    Returns:
        bool: True si se pudo mostrar la información, False en caso contrario
    """
    if type(matriz_puntaje) == list and len(matriz_puntaje) > 0:
        jurados_generosos = encontrar_jurado_mas_generoso(matriz_puntaje)
        promedio_por_jurado = promedio_puntaje_jurado(matriz_puntaje)
        
        print("JURADO O JURADOS MAS GENEROSOS:")
        
        if len(jurados_generosos) == 1:
            indice = jurados_generosos[0]
            print(f"Jurado {indice + 1} con promedio: {round(promedio_por_jurado[indice], 2)}")
        else:
            print("Empate entre los siguientes jurados:")
            for i in range(len(jurados_generosos)):
                indice = jurados_generosos[i]
                print(f"Jurado {indice + 1} con promedio: {round(promedio_por_jurado[indice], 2)}")
        
        return True
    else:
        return False

def encontrar_participantes_puntuaciones_iguales(matriz_puntaje: list, array_nombres: list) -> bool:
    """
    Encuentra y muestra participantes que tienen puntuaciones totales iguales.
    
    Args:
        matriz_puntaje (list): Matriz con los puntajes de cada participante
        array_nombres (list): Array con los nombres de los participantes
        
    Returns:
        bool: True si encontró participantes con puntuaciones iguales, False si no hay ninguno
    """
    if type(matriz_puntaje) == list and type(array_nombres) == list and len(matriz_puntaje) > 0 and len(array_nombres) > 0:
        puntajes_totales = sumar_columnas_por_fila3(matriz_puntaje)
        hay_iguales = False
        
        print("PARTICIPANTES CON PUNTUACIONES TOTALES IGUALES:")
        
        # Comparar cada participante con todos los demás
        for i in range(len(puntajes_totales)):
            for j in range(i + 1, len(puntajes_totales)):  # Solo comparar hacia adelante para evitar duplicados
                if puntajes_totales[i] == puntajes_totales[j]:
                    if hay_iguales == False:  # Primera vez que encuentra iguales
                        hay_iguales = True
                    print(f"{array_nombres[i]} y {array_nombres[j]} tienen el mismo puntaje total: {puntajes_totales[i]}")
        
        if hay_iguales == False:
            print("Error: No hay participantes con puntuaciones totales iguales.")
        
        return hay_iguales
    else:
        return False

def encontrar_participantes_promedios_iguales(matriz_puntaje: list, array_nombres: list) -> bool:
    """
    Encuentra y muestra participantes que tienen promedios iguales.
    
    Args:
        matriz_puntaje (list): Matriz con los puntajes de cada participante
        array_nombres (list): Array con los nombres de los participantes
        
    Returns:
        bool: True si encontró participantes con promedios iguales, False si no hay ninguno
    """
    if type(matriz_puntaje) == list and type(array_nombres) == list and len(matriz_puntaje) > 0 and len(array_nombres) > 0:
        promedios = promedio_puntaje(matriz_puntaje)
        hay_iguales = False
        
        print("PARTICIPANTES CON PROMEDIOS IGUALES:")
        
        # Comparar cada participante con todos los demás
        for i in range(len(promedios)):
            for j in range(i + 1, len(promedios)):  # Solo comparar hacia adelante para evitar duplicados
                # Redondear a 2 decimales para comparar (evitar problemas de precisión)
                promedio_i = round(promedios[i], 2)
                promedio_j = round(promedios[j], 2)
                
                if promedio_i == promedio_j:
                    if hay_iguales == False:  # Primera vez que encuentra iguales
                        hay_iguales = True
                    print(f"{array_nombres[i]} y {array_nombres[j]} tienen el mismo promedio: {promedio_i}")
        
        if hay_iguales == False:
            print("Error: No hay participantes con promedios iguales.")
        
        return hay_iguales
    else:
        return False

def mostrar_participantes_puntuaciones_iguales(matriz_puntaje: list, array_nombres: list) -> bool:
    """
    Muestra participantes con puntuaciones totales y promedios iguales.
    
    Args:
        matriz_puntaje (list): Matriz con los puntajes de cada participante
        array_nombres (list): Array con los nombres de los participantes
        
    Returns:
        bool: True si la operación fue exitosa, False en caso contrario
    """
    if type(matriz_puntaje) == list and type(array_nombres) == list and len(matriz_puntaje) > 0 and len(array_nombres) > 0:
        print("="*50)
        encontro_totales = encontrar_participantes_puntuaciones_iguales(matriz_puntaje, array_nombres)
        print("")
        encontro_promedios = encontrar_participantes_promedios_iguales(matriz_puntaje, array_nombres)
        print("="*50)
        
        return True
    else:
        return False

def buscar_participante_por_nombre(array_nombres: list, matriz_puntaje: list, nombre_buscado: str) -> bool:
    """
    Busca un participante por nombre y muestra sus datos si existe.
    
    Args:
        array_nombres (list): Array con los nombres de los participantes
        matriz_puntaje (list): Matriz con los puntajes de cada participante
        nombre_buscado (str): Nombre del participante a buscar
        
    Returns:
        bool: True si encontró el participante, False si no existe
    """
    if type(array_nombres) == list and type(matriz_puntaje) == list and len(array_nombres) > 0 and len(matriz_puntaje) > 0:
        
        # Buscar el nombre en el array
        indice_encontrado = -1
        for i in range(len(array_nombres)):
            # Comparar ignorando mayúsculas/minúsculas y espacios extra
            nombre_array = ""
            nombre_buscar = ""
            
            
            for j in range(len(array_nombres[i])):
                caracter = array_nombres[i][j]
                codigo = ord(caracter)
                if 65 <= codigo <= 90:  # Si es mayúscula, convertir a minúscula
                    nombre_array += chr(codigo + 32)
                elif caracter != ' ' or (j > 0 and array_nombres[i][j-1] != ' '):  # Evitar espacios dobles
                    nombre_array += caracter
            
            for j in range(len(nombre_buscado)):
                caracter = nombre_buscado[j]
                codigo = ord(caracter)
                if 65 <= codigo <= 90:  # Si es mayúscula, convertir a minúscula
                    nombre_buscar += chr(codigo + 32)
                elif caracter != ' ' or (j > 0 and nombre_buscado[j-1] != ' '):  
                    nombre_buscar += caracter
           
            while len(nombre_array) > 0 and nombre_array[0] == ' ':
                nombre_array = nombre_array[1:]
            while len(nombre_array) > 0 and nombre_array[len(nombre_array)-1] == ' ':
                nombre_array = nombre_array[:-1]
                
            while len(nombre_buscar) > 0 and nombre_buscar[0] == ' ':
                nombre_buscar = nombre_buscar[1:]
            while len(nombre_buscar) > 0 and nombre_buscar[len(nombre_buscar)-1] == ' ':
                nombre_buscar = nombre_buscar[:-1]
            
            if nombre_array == nombre_buscar:
                indice_encontrado = i
                break
        
        if indice_encontrado != -1:
            print("="*50)
            print("PARTICIPANTE ENCONTRADO:")
            mostrar_puntaje(array_nombres, matriz_puntaje, indice_encontrado)
            print("="*50)
            return True
        else:
            print("Error: No se encontró ningún participante con ese nombre.")
            return False
    else:
        return False

def solicitar_busqueda_participante(array_nombres: list, matriz_puntaje: list) -> bool:
    """
    Solicita el nombre del participante a buscar y ejecuta la búsqueda.
    
    Args:
        array_nombres (list): Array con los nombres de los participantes
        matriz_puntaje (list): Matriz con los puntajes de cada participante
        
    Returns:
        bool: True si la operación fue exitosa, False en caso contrario
    """
    if type(array_nombres) == list and type(matriz_puntaje) == list and len(array_nombres) > 0 and len(matriz_puntaje) > 0:
        nombre_buscado = input("Ingrese el nombre del participante a buscar: ")
        
        # Validar que no esté vacío
        while len(nombre_buscado) == 0 or es_solo_espacio(nombre_buscado) == False:
            print("Debe ingresar un nombre válido.")
            nombre_buscado = input("Ingrese el nombre del participante a buscar: ")
        
        return buscar_participante_por_nombre(array_nombres, matriz_puntaje, nombre_buscado)
    else:
        return False
