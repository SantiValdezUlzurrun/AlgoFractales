from algoturtle import *
import sys
import csv
_a = sys.argv
_prueba = ['arbol1.sl', '3', 'abc.svg']
PEDIDO = _prueba
x_max = 0
x_min = 0
y_max = 0
y_min = 0
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
    if arreglar_pedido():
        return
    escribir_svg()
    
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
    with open(PEDIDO[0],'r',encoding = 'utf8') as archivo:
        lector = csv.reader(archivo, delimiter=delimitador)
        tabla_conversion["angulo"] = next(lector)[0]
        tabla_conversion["axiomas"] = next(lector)[0]
        for linea in lector:
            tabla_conversion[linea[0]] = linea[1]
def crear_cola_comandos(cadena):
    ''' '''
    cola_comandos = Cola()
    pila_tortugas = Pila()
    letra_0 = cadena[0]
    tortuga_anterior = Tortuga()  
    tortuga_anterior,pila_tortugas = aplicar_cambios(letra_0,tortuga_anterior,pila_tortugas)
    if not tortuga_anterior:
        print('error cadena')
        return None
    x_max = tortuga_anterior.posicion[0]
    x_min = tortuga_anterior.posicion[0]
    y_max = tortuga_anterior.posicion[1]
    y_min = tortuga_anterior.posicion[1]
    cola_comandos.encolar(tortuga_anterior.pasar_linea_svg())
    for letra in cadena[1::]:
        posicion_in = tortuga_anterior.posicion[:]
        posicion_p = tortuga_anterior.posicion[:]
        orientacion_p = str(tortuga_anterior.orientacion)
        orientacion_p = int(orientacion_p)
        tortuga_actual = Tortuga(orientacion_p,posicion_p,tortuga_anterior.pluma,posicion_in)
        
        if letra == ']':
            tortuga_anterior = pila_tortugas.ver_tope()
        
        else:
            tortuga_anterior = tortuga_actual
            
        tortuga_actual,pila_tortugas = aplicar_cambios(letra,tortuga_actual,pila_tortugas)
        
        if not tortuga_actual:
            print('error cadena')
            return None
        
        if tortuga_actual.posicion[0] > x_max:
            x_max = tortuga_actual.posicion[0]
        
        if tortuga_actual.posicion[0] < x_min:
            x_min = tortuga_actual.posicion[0]
        
        if tortuga_actual.posicion[1] > y_max:
            y_max = tortuga_actual.posicion[1]
        
        if tortuga_actual.posicion[1] < y_min:
            y_min = tortuga_actual.posicion[1]
        cola_comandos.encolar(tortuga_actual.pasar_linea_svg())
        

    primera_linea = f'<svg viewBox="{x_min } {y_min } {x_max } {y_max }" xmlns="http://www.w3.org/2000/svg">'
    return cola_comandos,primera_linea

def aplicar_cambios(letra,tortuga,pila_tortugas):
    if letra == 'F' or letra == 'G' or letra == 'X':
        tortuga.avanzar()
    elif letra == 'f' or letra == 'g':
        tortuga.mover_pluma()
        tortuga.avanzar()
        tortuga.mover_pluma
    elif letra == '+':
        tortuga.girar_derecha(int(tabla_conversion['angulo']))
    elif letra == '-':
        tortuga.girar_izquierda(int(tabla_conversion['angulo']))
    elif letra == '|':
        tortuga.orientar_costado()
    elif letra == '[':
        pila_tortugas.apilar(tortuga)
    elif letra == ']':
        pila_tortugas.desapilar()
    else:
        return None
    return tortuga,pila_tortugas


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
main()
