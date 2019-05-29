from algoturtle import *
import sys
import csv
_a = sys.argv
PEDIDO = _a
#PRIMERA_LINEA = f'<svg viewBox="{pila_x_min.ver_tope()} {pila_y_min.ver_tope()} {pila_x_max.ver_tope()} {pila_y_max.ver_tope()}" xmlns="http://www.w3.org/2000/svg">'
COLOR = None
ANCHO = None
ER_BV = '''Bienvenido, abriste el archivo sin ningun comando o con menos de los necesarios, sus comandos son:
1. nombre del archivo .sl (obligatorio)
2. numero de veces a iterar (obligatorio tiene que ser entero)
3. nombre del archivo svg a escribir (obligatorio)
4. color del archivo (opcional y en ingles)
5. ancho del lapiz a escribir (opcionar y un entero)'''
ER_PED_1 = 'No ingresaste un entero para iterar el archivo'
ER_PED_0 = 'El archivo el cual pasaste para leer esta vacio o no responde a las normas acordadas para trabajar'
DELIMITADOR_ARCHIVO_SISTEMAL = " "
tabla_conversion = {}
def main():
    if not arreglar_pedido():
        return
    generar_comandos(DELIMITADOR_ARCHIVO_SISTEMAL, tabla_conversion)
    
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
    
def generar_comandos(delimitador, tabla_conversion):
    '''Recibe la ruta del archivo donde se encuentra el sistema l, su separador, una tabla de conversion y la cantidad de iteraciones
    y devuelve una cadena de letras que se corresponden con los movimientos que debe realizar la tortuga
    '''
    leer_archivo_sistemal(delimitador, tabla_conversion)
    movimientos = formar_movimientos(tabla_conversion)
    return movimientos

def formar_movimientos(tabla_conversion):
    ''' - '''
    movimientos = tabla_conversion["axiomas"]
    movimientos_nuevo = ""
    for i in range(PEDIDO[1]):
        for letra in movimientos:
            if letra in tabla_conversion.keys():
                movimientos_nuevo += tabla_conversion[letra]
            else:
                movimientos_nuevo += letra
        movimientos = movimientos_nuevo
    return movimientos

def leer_archivo_sistemal(delimitador, tabla_conversion):
    ''' - '''
    with open(PEDIDO[0]) as archivo:
        lector = csv.reader(archivo, delimiter=delimitador)
        tabla_conversion["angulo"] = next(lector)[0]
        tabla_conversion["axiomas"] = next(lector)[0]
        for linea in lector:
            tabla_conversion[linea[0]] = linea[1]

def crear_cola_comandos(cadena):
    ''' '''
    
def escribir_svg():
    ''' '''
    cola_comandos = crear_cola_comandos(f)
    with open (PEDIDO[2],'w',encoding = 'utf8') as archivo:
        archivo.write(f'PRIMERA_LINEA /n')
        while not cola_comandos.esta_vacia():
            archivo.write(cola_comandos.desencolar() + '/n')