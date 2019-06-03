from algoturtle import *
import sys
import csv



ENTRADA = sys.argv[1::]
DELIMITADOR_ARCHIVO_SISTEMA_L = ' '
tabla_conversion = {}
MENSAJE_ERROR = 'Error de parametros'
OPERACIONES = "FGXYfg+-|[]"
ERROR_ARCH_SISTEMA_L = 'El archivo ingresado a leer no existe'
ERROR_ANGULO = 'el angulo del archivo no es un numero'
ERROR_ARCHIVO_LETRA = 'hay una linea que falla en el archivo'

def algo_fractales():
    '''funcion main del archivo que conecta las distintas funciones, en caso de que alguna encuentre un error, lo imprime y devuelve un Exception
    en ese caso el programa se termina
    pre: la Entrada tiene que ser valida
    post: llama a las funciones necesarias para poder escribir el archivo svg deseado'''
    try:
        if validar_entrada(ENTRADA):
            ruta_archivo_sistema_l, iteraciones, ruta_archivo_svg = leer_entrada(ENTRADA)
            comandos = generar_comandos(ruta_archivo_sistema_l, DELIMITADOR_ARCHIVO_SISTEMA_L, tabla_conversion, iteraciones)
            primera_linea, cola_comandos = interpretar_comandos(comandos, OPERACIONES, tabla_conversion["angulo"])
            escribir_archivo_svg(ruta_archivo_svg, primera_linea, cola_comandos)
        else:
            print(MENSAJE_ERROR)
    except Exception:
        return

def validar_entrada(entrada):
    '''Pre: recibe una lista de 3 elementos los cuales debe tener al elemento [1] como una cadena de entero
    Post: devuelve True'''
    if len(entrada) < 3:
        return False
    elif len(entrada) == 3 and entrada[1].isdigit():
        return True
    return False


def leer_entrada(entrada_valida):
    '''Pre:recibe una entrada valida
    post: devuelve la primer componente y (1), la segunda componente con (2), y la tercera componente y (3)
         (1) si la componente del archivo le falta el .ls se lo agrega
         (2) la transforma en entero
         (3) si la componente del archivo le falta el .svg se lo agrega'''
    
    if not entrada_valida[2][::-1][:4:] == 'gvs.':
        entrada_valida[2] = entrada_valida[2] + '.svg'
    if not entrada_valida[0][::-1][:3:] == 'ls.':
        entrada_valida[0] = entrada_valida[0] + '.sl' 
    return entrada_valida[0], int(entrada_valida[1]), entrada_valida[2]


def generar_comandos(ruta, delimitador, tabla_conversion, iteraciones):
    '''Pre : Recibe la ruta del archivo donde se encuentra el sistema l, su separador, una tabla de conversion y la cantidad de iteraciones
    Post: devuelve una cadena de letras que se corresponden con los movimientos que debe realizar la tortuga
    '''
    leer_archivo_sistema_l(ruta, delimitador, tabla_conversion)
    movimientos = formar_movimientos(tabla_conversion, iteraciones)
    return movimientos

def formar_movimientos(tabla_conversion, iteraciones):
    '''Pre: recibe un diccionario con un formato de conversion y un entero 
    Post: devuelve una cadena de la conversion recursiva hecha tantas veces como las recibidas'''
    movimientos = tabla_conversion["axiomas"]
    movimientos_nuevo = ""
    for i in range(iteraciones):
        for letra in movimientos:
            if letra in tabla_conversion.keys():
                movimientos_nuevo += tabla_conversion[letra]
            else:
                movimientos_nuevo += letra
        movimientos = movimientos_nuevo
        movimientos_nuevo = ""
    return movimientos

def leer_archivo_sistema_l(ruta, delimitador, tabla_conversion):
    '''Pre: recibe un nombre de un archivo en formato cadena (si el archivo no existe imprime un mensaje y devuelve Exception),
    una cadena que va a servir como delimitador, y un diccionario vacio
    Post: si el archivo se encontro de la forma:
    -angulo
    -axiomas
    -reglas
    Entonces devuelve un diccionario con keys angulo,axioma, y las letras del archivo; y como valor lo que diga el archivo
    '''
    try:
        with open(ruta, 'r', encoding = 'utf8') as archivo:
            lector = csv.reader(archivo, delimiter=delimitador)
            numero_angulo = next(lector)[0].split('.')
            
            if numero_angulo[0].isdigit():
                if len(numero_angulo) == 1:
                    tabla_conversion["angulo"] = int(numero_angulo[0])
                elif len(numero_angulo) ==2:
                    tabla_conversion["angulo"] = int(numero_angulo[0]) + int(numero_angulo[1])/(10*len(numero_angulo[1]))
                else:
                    print(ERROR_ANGULO)
                    return Exception
            
            else:
                print(ERROR_ANGULO)
                return Exception
            
            tabla_conversion["axiomas"] = next(lector)[0]
            for linea in lector:
                if len(linea) == 2:
                    tabla_conversion[linea[0]] = linea[1]
                else:
                    print(ERROR_ARCHIVO_LETRA)
                    return Exception
    except FileNotFoundError:
        print(ERROR_ARCH_SISTEMA_L)
        return Exception


def interpretar_comandos(cadena_comandos, operaciones, angulo):
    '''Pre: Recibe una cadena de comandos a hacer, una cadena con las operaciones validas y un entero que va a servir de angulo
    Post: genera una cola de cadenas con formato svg'''
    if len(cadena_comandos) == 0:
        print('ERROR_C_A')
        return Exception
    pila_tortugas = Pila()
    cola_comandos = Cola()
    pila_tortugas.apilar(Tortuga())
    tortuga = pila_tortugas.ver_tope()
    cordenada_minima = tortuga.posicion[:]
    cordenada_maxima = tortuga.posicion[:]
    for letra in cadena_comandos:
        if letra not in operaciones:
            continue
        tortuga = pila_tortugas.ver_tope()
        linea_comando_svg, posicion_anterior, posicion_nueva = ejecutar_comando(letra, angulo, tortuga, pila_tortugas)
        cola_comandos.encolar(linea_comando_svg)
        cordenada_minima, ancho, alto = actualizar_canvas(posicion_anterior, posicion_nueva, cordenada_minima, cordenada_maxima)
    primera_linea = f'<svg viewBox="{cordenada_minima[0] - 5} {cordenada_minima[1] - 5} {ancho + 5} {alto + 5}" xmlns="http://www.w3.org/2000/svg">'
    return primera_linea, cola_comandos



def ejecutar_comando(letra, angulo, tortuga, pila_tortugas):
    '''Pre: Recibe una letra que va a significar la accion a la tortuga recibida ( tambien se recibe una pila de tortugas si es un corchete la accion
    y un angulo en caso de que la accion requerida lo pida
    Post: devuelve la linea_comando_svg de la tortuga luego de aplicarle los cambios, su posicion inicial y final'''
    posicion_inicial = tortuga.posicion_inicial[:]
    if letra in 'FGXY':
        tortuga.avanzar()
    elif letra == 'fg':
        tortuga.pluma_arriba()
        tortuga.avanzar()
        tortuga.pluma_abajo()
    elif letra == '+':
        tortuga.girar_derecha(angulo)
    elif letra == '-':
        tortuga.girar_izquierda(angulo)
    elif letra == '|':
        tortuga.orientar_costado()
    if letra == '[':
        tortuga_nueva = Tortuga()
        tortuga.copiar_tortuga(tortuga_nueva)
        pila_tortugas.apilar(tortuga_nueva)
    elif letra == ']':
        pila_tortugas.desapilar()
    posicion_final = tortuga.posicion[:]
    linea_comando_svg = tortuga.pasar_linea_svg()
    tortuga.posicion_inicial = posicion_final
    return linea_comando_svg, posicion_inicial, posicion_final


def actualizar_canvas(posicion_anterior, posicion_nueva, cordenada_minima, cordenada_maxima):
    '''pre: recibe 4 listas de largo 2 con enteros 
    post: compara las posiciones y devuelve la minimas la suma de la minima y la maxima en cada eje'''
    eje_x = [posicion_anterior[0], posicion_nueva[0]]
    eje_y = [posicion_anterior[1], posicion_nueva[1]]
    if max(eje_x) > cordenada_maxima[0]:
        cordenada_maxima[0] = max(eje_x)
    if max(eje_y) > cordenada_maxima[1]:
        cordenada_maxima[1] = max(eje_y)
    if min(eje_x) < cordenada_minima[0]:
        cordenada_minima[0] = min(eje_x)
    if min(eje_y) < cordenada_minima[1]:
        cordenada_minima[1] = min(eje_y)
    ancho = abs(cordenada_minima[0]) + abs(cordenada_maxima[0])
    alto = abs(cordenada_minima[1]) + abs(cordenada_maxima[1])
    return cordenada_minima, ancho, alto




def escribir_archivo_svg(ruta, primera_linea, sucesion_comandos):
    '''Pre: recibe el nombre de una ruta a escribir, la primera linea a escribir y una cola de cadenas las cuales se escribiran en el orden el cual se vayan desencolando
    Post: se escribio el archivo''' 
    if sucesion_comandos == None:
        print(MENSAJE_ERROR)
        return
    with open(ruta, 'w', encoding = 'utf8') as archivo:
        archivo.write(f'{primera_linea}\n')
        while not sucesion_comandos.esta_vacia():
            archivo.write(f'{sucesion_comandos.desencolar()}\n')
        archivo.write('</svg>')





algo_fractales()
