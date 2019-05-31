from algoturtle import *
import sys
import csv


#ENTRADA = sys.argv[1::]
ENTRADA = ["arbol1.sl", "2", "m.svg"]
DELIMITADOR_ARCHIVO_SISTEMA_L = ' '
tabla_conversion = {}
MENSAJE_ERROR = 'Error de parametros'
OPERACIONES = "FGXfg+-|[]"

def algo_fractales():
    ''' '''
    if validar_entrada(ENTRADA):
        ruta_archivo_sistema_l, iteraciones, ruta_archivo_svg = leer_entrada(ENTRADA)
        comandos = generar_comandos(ruta_archivo_sistema_l, DELIMITADOR_ARCHIVO_SISTEMA_L, tabla_conversion, iteraciones)
        primera_linea, cola_comandos = interpretar_comandos(comandos, OPERACIONES, tabla_conversion["angulo"])
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
        tabla_conversion["angulo"] = int(next(lector)[0])
        tabla_conversion["axiomas"] = next(lector)[0]
        for linea in lector:
            tabla_conversion[linea[0]] = linea[1]



def interpretar_comandos(cadena_comandos, operaciones, angulo):
    ''' '''
    pila_tortugas = Pila()
    cola_comandos = Cola()
    pila_tortugas.apilar(Tortuga())
    tortuga = pila_tortugas.ver_tope()
    cordenada_minima = tortuga.posicion
    cordenada_maxima = tortuga.posicion
    for letra in cadena_comandos:
        if letra not in operaciones:
            continue
        if letra in 'FGX':
            linea_comando_svg, posicion_anterior, posicion_nueva = ejecutar_comando(letra, angulo, tortuga, pila_tortugas)
        else:
            continue
        if linea_comando_svg == None:
            continue
        cola_comandos.encolar(linea_comando_svg)
        cordenada_minima, cordenada_maxima = actualizar_canvas(posicion_anterior, posicion_nueva, cordenada_minima, cordenada_maxima)
    primera_linea = f'<svg viewBox="{cordenada_minima[0]} {cordenada_minima[1]} {cordenada_maxima[0]} {cordenada_maxima[1]}" xmlns="http://www.w3.org/2000/svg">'
    return primera_linea, cola_comandos



def ejecutar_comando(letra, angulo, tortuga, pila_tortugas):
    ''' '''
    posicion_inicial = tortuga.posicion_inicial[:]
    if letra in 'FGX':
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
        tortuga = pila_tortugas.ver_tope()
    elif letra == ']':
        pila_tortugas.desapilar()
    linea_comando_svg = tortuga.pasar_linea_svg()
    posicion_final = tortuga.posicion[:]
    tortuga.posicion_inicial = posicion_final
    return linea_comando_svg, posicion_inicial, posicion_final


def actualizar_canvas(posicion_anterior, posicion_nueva, cordenada_minima, cordenada_maxima):
    eje_x = [posicion_anterior[0], posicion_nueva[0]]
    eje_y = [posicion_anterior[1], posicion_nueva[1]]
    cordenada_maxima = [max(eje_x), max(eje_y)]
    cordenada_minima = [min(eje_x), min(eje_y)]
    return cordenada_minima, cordenada_maxima




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
