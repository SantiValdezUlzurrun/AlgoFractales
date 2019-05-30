from algoturtle import *
from TDA import *
import sys
import csv


ENTRADA = sys.argv[1::]
DELIMITADOR_ARCHIVO_SISTEMA_L = ' '
tabla_conversion = {}
MENSAJE_ERROR = 'Error de parametros'
OPERACIONES_CARACTER = {'F': 'avanzar', 'G': 'avanzar',
'f': ['pluma arriba', 'avanzar', 'pluma abajo'], 'g': 'f': ['pluma arriba', 'avanzar', 'pluma abajo'],
'+': 'girar derecha', '-': 'girar izquierda', '|': 'invertir direccion', '[': 'apilar', ']': 'desapilar'}

def algo_fractales():
    if validar_entrada(ENTRADA):
        ruta_archivo_sistema_l, iteraciones, ruta_archivo_svg = leer_entrada(ENTRADA)
        comandos = generar_comandos(ruta_archivo_sistema_l, DELIMITADOR_ARCHIVO_SISTEMA_L, tabla_conversion, iteraciones)
        primera_linea, cola_comandos = interpretar_comandos(comandos)
        escribir_archivo_svg(ruta_archivo_svg, primera_linea, cola_comandos)
    else:
        print(MENSAJE_ERROR)


def validar_entrada(entrada):
    ''' '''
    if len(entrada) < 3:
        return False
    elif len(entrada) == 3 and entrada[1].isdigit():
        return True
    return False


def leer_entrada(entrada_valida):
    ''' '''
    return entrada_valida[0], int(entrada_valida[1]), entrada_valida[2]


def generar_comandos(ruta, delimitador, tabla_conversion, iteraciones):
    '''Recibe la ruta del archivo donde se encuentra el sistema l, su separador, una tabla de conversion y la cantidad de iteraciones
    y devuelve una cadena de letras que se corresponden con los movimientos que debe realizar la tortuga
    '''
    leer_archivo_sistema_l(ruta, delimitador, tabla_conversion)
    movimientos = formar_movimientos(tabla_conversion, iteraciones)
    return movimientos

def formar_movimientos(tabla_conversion, iteraciones):
    ''' - '''
    movimientos = tabla_conversion["axiomas"]
    movimientos_nuevo = ""
    for i in range(iteraciones):
        for letra in movimientos:
            if letra in tabla_conversion.keys():
                movimientos_nuevo += tabla_conversion[letra]
            else:
                movimientos_nuevo += letra
        movimientos = movimientos_nuevo
    return movimientos

def leer_archivo_sistema_l(ruta, delimitador, tabla_conversion):
    ''' - '''
    with open(ruta, 'r', encoding = 'utf8') as archivo:
        lector = csv.reader(archivo, delimiter=delimitador)
        tabla_conversion["angulo"] = next(lector)[0]
        tabla_conversion["axiomas"] = next(lector)[0]
        for linea in lector:
            tabla_conversion[linea[0]] = linea[1]



def interpretar_comandos(cadena_comandos):
    ''' '''
    cola_comandos = Cola()
    for letra in cadena_comandos:
        linea_comando_svg, posicion_nueva= ejecutar_comando(letra)
        cola_comandos.encolar(linea_comando_svg)
        actualizar_canvas()
    primera_linea = f'<svg viewBox="{cordenada_minima[0]} {cordenada_minima[1]} {cordenada_maxima[0]} {cordenada_maxima[1]}" xmlns="http://www.w3.org/2000/svg">'
    return cola_comandos


















def escribir_archivo_svg(ruta, primera_linea, sucesion_comandos):
    ''' '''
    if sucesion_comandos == None:
        print(MENSAJE_ERROR)
        return
    with open(ruta, 'w', encoding = 'utf8') as archivo:
        archivo.write(f'{primera_linea}')
        while not sucesion_comandos.esta_vacia():
            archivo.write(f'{sucesion_comandos.desencolar()}')
        archivo.write('</svg>')






algo_fractales()

"""

def arreglar_pedido():
    if len(PEDIDO) < 3:
        print(ER_BV)
        return False
    if not PEDIDO[1].isdigit():
        print(ER_PED_1)
        return False
    else:
        PEDIDO[1] = int(PEDIDO[1])
    if not PEDIDO[2][::-1][:4:] == 'gvs.':
        PEDIDO[2] = PEDIDO[2] + '.svg'
    if not PEDIDO[0][::-1][:3:] == 'ls.':
        PEDIDO[0] = PEDIDO[0] + '.sl'
    if len(PEDIDO) > 3:
        COLOR = PEDIDO[4]
    if len(PEDIDO) >4 :
        ANCHO = PEDIDO[5]



def crear_cola_comandos(cadena):
    ''' '''
    cola_comandos = Cola()
    pila_tortugas = Pila()
    letra_0 = cadena[0]
    tortuga_anterior = Tortuga(int(tabla_conversion['angulo']))
    if letra_0 == 'F' or letra_0 == 'G':
        tortuga_anterior.avanzar()
    elif letra_0 == 'f' or letra_0 == 'g':
        tortuga_anterior.mover_pluma()
    elif letra_0 == '+':
        tortuga_anterior.girar_derecha(int(tabla_conversion['angulo']))
    elif letra_0 == '-':
        tortuga_anterior.girar_izquierda(int(tabla_conversion['angulo']))
    elif letra_0 == '|':
        tortuga_anterior.orientar_costado()
    elif letra_0 == '[':
        pila_tortugas.apilar(tortuga_anterior)
    elif letra_0 == ']':
        pila_tortugas.apilar(tortuga_anterior)
    else:
        return None
    x_max = tortuga_anterior.posicion[0]
    x_min = tortuga_anterior.posicion[0]
    y_max = tortuga_anterior.posicion[1]
    y_min = tortuga_anterior.posicion[1]
    cola_comandos.encolar(tortuga_anterior.pasar_linea_svg())
    for letra in cadena[1::]:
        tortuga_actual = Tortuga(tortuga_anterior.orientacion,tortuga_anterior.posicion,tortuga_anterior.pluma)
        if letra == 'F' or letra == 'G':
            tortuga_anterior.avanzar()
        elif letra == 'f' or letra == 'g':
            tortuga_anterior.mover_pluma()
        elif letra == '+':
            tortuga_anterior.girar_derecha(int(tabla_conversion['angulo']))
        elif letra == '-':
            tortuga_anterior.girar_izquierda(int(tabla_conversion['angulo']))
        elif letra == '|':
            tortuga_anterior.orientar_costado()
        elif letra == '[':
            pila_tortugas.apilar(tortuga_anterior)
        elif letra == ']':
            pila_tortugas.apilar(tortuga_anterior)
        else:
            continue
        if tortuga_actual.posicion[0] > x_max:
            x_max = tortuga_actual.posicion[0]
        if tortuga_actual.posicion[0] < x_min:
            x_min = tortuga_actual.posicion[0]
        if tortuga_actual.posicion[1] > y_max:
            y_max = tortuga_actual.posicion[1]
        if tortuga_actual.posicion[1] < y_min:
            y_min = tortuga_actual.posicion[1]
        cola_comandos.encolar(tortuga_actual.pasar_linea_svg())
        if letra == ']':
            tortuga_anterior = pila_tortugas.ver_tope()
        else:
            tortuga_anterior = tortuga_actual
    primera_linea = f'<svg viewBox="{x_min} {y_min} {x_max} {y_max}" xmlns="http://www.w3.org/2000/svg">'
    return cola_comandos,primera_linea


def escribir_svg():
    ''' '''
    cola_comandos,primera_linea = crear_cola_comandos(generar_comandos(DELIMITADOR_ARCHIVO_SISTEMAL, tabla_conversion))
    if cola_comandos == None:
        print('asdad')
        return
    with open (PEDIDO[2],'w',encoding = 'utf8') as archivo:
        archivo.write(f'{primera_linea}')
        while not cola_comandos.esta_vacia():
            archivo.write(f'{cola_comandos.desencolar()}')
        archivo.write('</svg>')


"""
