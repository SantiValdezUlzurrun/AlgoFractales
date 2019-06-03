from math import *

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
        'Devuelve el dato del primer elemento de la cola'
        return self.prim.dato

    def encolar(self, dato):
        'Agrega un elemento a la cola'
        nuevo_nodo = _Nodo(dato)
        if self.ultimo is not None:
            self.ultimo.prox = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            self.prim = nuevo_nodo
            self.ultimo = nuevo_nodo

    def desencolar(self):
        'Saca el primer elemento de la cola'
        if len(self) == 0:
            raise IndexError
        dato = self.prim.dato
        self.prim = self.prim.prox
        if not self.prim:
            self.ultimo = None
        return dato

    def esta_vacia(self):
        'Devuelve True si la cola esta vacia si no False'
        if self.ultimo == None:
            return True
        return False

class Pila:
    def __init__(self):
        self.ult = None
    def apilar (self,dato):
        'agrega un elemento a la pila'
        if self.ult == None:
            self.ult = _Nodo(dato)
        else:
            dato_a_agregar = _Nodo(dato,self.ult)
            self.ult = dato_a_agregar
    def desapilar(self):
        'saca un elemento de la pila'
        dato = self.ult.dato
        self.ult = self.ult.prox
        return dato
    def esta_vacia(self):
        'Devuelve True si el atributo ult es igual a none si no False'
        if self.ult == None:
            return True
        return False
    def ver_tope(self):
        'devuelve el dato del ultimo nodo'
        return self.ult.dato


class Tortuga:
    '''clase tortuga la cual tiene como atributos posicion ( lista de 2 componentes con numeros), orientacion (entero), pluma(true si esta abajo y false en caso contrario),
    posicion_inicial (lista de 2 componentes con numeros), color (color en ingles) y ancho(numero)
    '''
    def __init__(self,orientacion = radians(90), posicion = [0,0],pluma = True,posicion_inicial = [0,0],color ='black',ancho = 1):
        self.pluma = pluma
        self.posicion = posicion
        self.posicion_inicial = posicion_inicial
        self.orientacion = orientacion
        self.color = color
        self.ancho = ancho

    def orientar_costado(self):
        'suma el equivalente a 180 grados al atributo orientacion'
        self.orientacion += radians(180)
        if self.orientacion > radians(360):
            self.orientacion -= radians(360)

    def girar_izquierda(self, cantidad):
        'recibe un numero y le resta el equivalente en radianes al atributo orientacion'
        self.orientacion -= radians(cantidad)
        if self.orientacion > radians(360):
            self.orientacion -= radians(360)

    def girar_derecha(self, cantidad):
        'recibe un numero y le suma su equivalente en radianes al atributo orientacion'
        self.orientacion += radians(cantidad)
        if self.orientacion > radians(360):
            self.orientacion -= radians(360)

    def avanzar(self,cantidad = [12,12]):
        'avanza 10 unidades en la cada componente, o el entero que le pases como parametro'
        self.posicion[0] -= cantidad[0] * cos(self.orientacion)
        self.posicion[1] -= cantidad[1] * sin(self.orientacion)


    def pasar_linea_svg(self):
        'devuelve una cadena en lenguaje svg el movimiento de la tortuga'
        a = self.posicion_inicial[0]
        b = self.posicion_inicial[1]
        c = self.posicion[0]
        d = self.posicion[1]
        return f' <line x1="{a}" y1="{b}" x2="{c}" y2="{d}" stroke-width="{self.ancho}" stroke="{self.color}" />'

    def __repr__(self):
        return f'[{self.pluma},{self.posicion},{self.orientacion}]'

    def pluma_arriba(self):
        'cambia el atributo pluma a False'
        self.pluma = False

    def pluma_abajo(self):
        'cambia el atributo pluma a True'
        self.pluma = True

    def copiar_tortuga(self, tortuga_nueva):
        'Recibe una tortuga y le cambia sus atributos a los mismos que la tortuga self pero con la diferencia de que posicion inicial es igual a posicion'
        tortuga_nueva.pluma = [self.pluma][:][0]
        tortuga_nueva.posicion_inicial = self.posicion[:]
        tortuga_nueva.posicion = self.posicion[:]
        tortuga_nueva.orientacion = [self.orientacion][:][0]
