from algoturtle import *
import sys
import csv


ENTRADA = ['arbol1.sl', '3', 'abc.svg']#sys.argv[1::]
DELIMITADOR_ARCHIVO_SISTEMA_L = ' '
tabla_conversion = {}
MENSAJE_ERROR = 'Error de parametros'
OPERACIONES = "FGXfg+-|[]"



def algo_fractales():
    '''funcion main del archivo '''
    if validar_entrada(ENTRADA):
        ruta_archivo_sistema_l, iteraciones, ruta_archivo_svg = leer_entrada(ENTRADA)
        comandos = generar_comandos(ruta_archivo_sistema_l, DELIMITADOR_ARCHIVO_SISTEMA_L, tabla_conversion, iteraciones)
        primera_linea, cola_comandos = interpretar_comandos(comandos, OPERACIONES, tabla_conversion["angulo"])
        escribir_archivo_svg(ruta_archivo_svg, primera_linea, cola_comandos)
    else:
        print(MENSAJE_ERROR)


def validar_entrada(entrada):
    '''Se fija que lo que pasaron no rompa todo (Falta arreglar) '''
    if len(entrada) < 3:
        return False
    elif len(entrada) == 3 and entrada[1].isdigit():
        return True
    return False


def leer_entrada(entrada_valida):
    '''devuelve la entrada valida '''
    return entrada_valida[0], int(entrada_valida[1]), entrada_valida[2]


def generar_comandos(ruta, delimitador, tabla_conversion, iteraciones):
    '''Recibe la ruta del archivo donde se encuentra el sistema l, su separador, una tabla de conversion y la cantidad de iteraciones
    y devuelve una cadena de letras que se corresponden con los movimientos que debe realizar la tortuga
    '''
    leer_archivo_sistema_l(ruta, delimitador, tabla_conversion)
    movimientos = formar_movimientos(tabla_conversion, iteraciones)
    return movimientos

def formar_movimientos(tabla_conversion, iteraciones):
    ''' Itera el diccionario de axiomas y reglas hasta llegar a la deseada '''
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
    ''' Lee el archivo y genera un diccionario con las reglas necesarias '''
    with open(ruta, 'r', encoding = 'utf8') as archivo:
        lector = csv.reader(archivo, delimiter=delimitador)
        tabla_conversion["angulo"] = int(next(lector)[0])
        tabla_conversion["axiomas"] = next(lector)[0]
        for linea in lector:
            tabla_conversion[linea[0]] = linea[1]



#def interpretar_comandos(cadena_comandos, operaciones, angulo):
#    ''' '''
#    pila_tortugas = Pila()
#    cola_comandos = Cola()
#    pila_tortugas.apilar(Tortuga())
#    tortuga = [pila_tortugas.ver_tope()][:][0]
#    cordenada_minima = tortuga.posicion_inicial[:]
#    cordenada_maxima = tortuga.posicion[:]
#    for letra in cadena_comandos:
#        if letra not in operaciones:
#            continue
#        linea_comando_svg, posicion_anterior, posicion_nueva = ejecutar_comando(letra, angulo, tortuga, pila_tortugas)
#        cola_comandos.encolar(linea_comando_svg)
#        cordenada_minima, cordenada_maxima = actualizar_canvas(posicion_anterior, posicion_nueva, cordenada_minima, cordenada_maxima)
#    primera_linea = f'<svg viewBox="{cordenada_minima[0]} {cordenada_minima[1]} {cordenada_maxima[0]} {cordenada_maxima[1]}" xmlns="http://www.w3.org/2000/svg">'
#    return primera_linea, cola_comandos

def interpretar_comandos(cadena_operaciones,operaciones, angulo):
    '''Recibe una cadena de operaciones y genera una cola de cada operacion en formato svg '''
    cola_comandos = Cola()
    pila_tortugas = Pila()
    letra_0 = cadena_operaciones[0]
    tortuga_anterior = Tortuga()  
    ejecutar_comando(letra_0,angulo,tortuga_anterior,pila_tortugas)

    a = tortuga_anterior.posicion[:]
    x_max = a[0]
    x_min = a[0]
    y_max = a[1]
    y_min = a[1]
    cola_comandos.encolar(tortuga_anterior.pasar_linea_svg())
    
    for letra in cadena_operaciones[1::]:
        
        posicion_in = tortuga_anterior.posicion[:]
        posicion_p = tortuga_anterior.posicion[:]
        orientacion_p = [tortuga_anterior.orientacion][:]

        tortuga_actual = Tortuga(orientacion_p[0],posicion_p,tortuga_anterior.pluma,posicion_in)
        
        if letra == ']':
            tortuga_anterior = [pila_tortugas.ver_tope()][:][0]
        
        else:
            tortuga_anterior = [tortuga_actual][:][0]
            
        ejecutar_comando(letra,angulo,tortuga_actual,pila_tortugas)
        
        if tortuga_actual.posicion[0] > x_max:
            a = tortuga_actual.posicion[:]
            x_max = a[0] 
        
        if tortuga_actual.posicion[0] < x_min:
            a = tortuga_actual.posicion[:]
            x_min = a[0]
        
        if tortuga_actual.posicion[1] > y_max:
            a = tortuga_actual.posicion[:]
            y_max = a[1] 
        
        if tortuga_actual.posicion[1] < y_min:
            a = tortuga_actual.posicion[:]
            y_min = a[1] 
#        cordenada_minima, cordenada_maxima = actualizar_canvas(tortuga_actual.posicion_inicial[:], tortuga_actual.posicion[:], [x_min,y_min], [x_max,y_max])
        cola_comandos.encolar(tortuga_actual.pasar_linea_svg())
        
    primera_linea = f'<svg viewBox="{x_min } {y_min } {x_max } {y_max }" xmlns="http://www.w3.org/2000/svg">'
#    primera_linea = f'<svg viewBox="{cordenada_minima[0]} {cordenada_minima[1]} {cordenada_maxima[0]} {cordenada_maxima[1]}" xmlns="http://www.w3.org/2000/svg"'
    return primera_linea,cola_comandos

def ejecutar_comando(letra, angulo, tortuga, pila_tortugas):
    '''recibe una tortuga y aplica una operacion que se le de '''

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
    elif letra == '[':
        tortuga_nueva = Tortuga()
        tortuga.copiar_tortuga(tortuga_nueva)
        pila_tortugas.apilar(tortuga_nueva)
        tortuga = pila_tortugas.ver_tope()
    elif letra == ']':
        pila_tortugas.desapilar()
    


#def actualizar_canvas(posicion_anterior, posicion_nueva, cordenada_minima, cordenada_maxima):
#    eje_x = [posicion_anterior[0], posicion_nueva[0]]
#    eje_y = [posicion_anterior[1], posicion_nueva[1]]
#    cordenada_maxima = [max(eje_x), max(eje_y)]
#    cordenada_minima = [min(eje_x), min(eje_y)]
#    return cordenada_minima, cordenada_maxima
#
#


def escribir_archivo_svg(ruta, primera_linea, sucesion_comandos):
    ''' escribe un archivo segun lo devuelto en la funcion interpretar_comandos '''
    if sucesion_comandos == None:
        print(MENSAJE_ERROR)
        return
    with open(ruta, 'w', encoding = 'utf8') as archivo:
        archivo.write(f'{primera_linea} \n')
        while not sucesion_comandos.esta_vacia():
            archivo.write(f' {sucesion_comandos.desencolar()} \n')
        archivo.write('</svg>')






algo_fractales()