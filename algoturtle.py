class _Nodo:

    def __init__(self, dato=None, prox=None):
        self.dato = dato
        self.prox = prox
class Cola:

    def __init__(self):
        self.prim = None
        self.ultimo = None

    def __len__(self):
        actual = self.prim
        contador = 0
        while actual:
            contador += 1
            actual = actual.prox
        return contador

    def ver_primero(self):
        return self.prim

    def encolar(self, dato):
        nuevo_nodo = _Nodo(dato)
        if self.ultimo is not None:
            self.ultimo.prox = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            self.prim = nuevo_nodo
            self.ultimo = nuevo_nodo

    def desencolar(self):
        if len(self) == 0:
            raise IndexError
        dato = self.prim.dato
        self.prim = self.prim.prox
        if not self.prim:
            self.ultimo = None
        return dato

    def esta_vacia(self):
        if self.ultimo == None:
            return True
        return False

class _Pila:
    def __init__(self):
        self.ult = None
    def apilar (self,dato):
        if self.ult == None:
            self.ult = _Nodo(dato)
        else:
            dato_a_agregar = _Nodo(dato,self.ult)
            self.ult = dato_a_agregar
    def desapilar(self):
        dato = self.ult.dato
        self.ult = self.ult.prox
        return dato
    def esta_vacia(self):
        if self.ult == None:
            return True
        return False
    def ver_tope(self):
        return self.ult.dato


class Tortuga:
    '''clase tortuga la cual tiene como atributos posicion ( lista de 2 numeros), orientacion (entero), pluma(true si esta abajo y false en caso contrario)
    como metodos:
    avanzar_x (avanza 10 unidades en la 1ra componente)
    avanzar_y (avanza 10 unidades en la 2da componente)
    orientar_arriba (suma 90 grados a orientacion)
    girar (gira una cantidad pasada por parametro)
    '''
    def __init__(self,posicion = [0,0],orientacion = 0,pluma = True,color ='black',ancho = 1):
        self.pluma = pluma
        self.posicion = posicion
        self.posicion_inicial = posicion
        self.orientacion = orientacion
        self.orientacion_inicial = orientacion
        self.color = color
        self.ancho = ancho
    def avanzar_x(self):
        self.posicion[0] += 10
    def avanzar_y(self):
        self.posicion[1] += 10
    def orientar_costado(self):
        self.orientacion += 90
    def girar(self,cantidad):
        self.orientacion += cantidad
    def avanzar(self,cantidad):
        self.posicion[0] += cantidad[0]
        self.posicion[1] += cantidad[1]
    def circulo_svg(self):
       return '<circle cx="15" cy="10" r="8" fill="white" />'
    def pasar_linea_svg(self):
       return f' <line x1="{self.posicion_inicial[0]}" y1="{self.posicion_inicial[1]}" x2="{self.posicion[0]}" y2="{self.posicion[1]}" stroke-width="{self.ancho}" stroke="{self.color}" />'
    def __repr__(self):
        return f'[{self.pluma},{self.posicion},{self.orientacion}]'

PRIMERA_LINEA = f'<svg viewBox="{pila_x_min.ver_tope()} {pila_y_min.ver_tope()} {pila_x_max.ver_tope()} {pila_y_max.ver_tope()}" xmlns="http://www.w3.org/2000/svg">'
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

def escribir_svg(cola_comandos):
    ''' '''
    with open (PEDIDO[2],'w',encoding = 'utf8') as archivo:
        archivo.write(f'PRIMERA_LINEA /n')
        while not cola_comandos.esta_vacia():
            archivo.write(cola_comandos.desencolar())
def arreglar_pedido():
    if len(PEDIDO) < 3:
        print(ER_BV)
        return None
    if not PEDIDO[1].isdigit():
        print(ER_PED_1)
        return None
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
