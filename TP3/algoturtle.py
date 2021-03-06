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

class Pila:
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
    avanzar (avanza 10 unidades en la cada componente, o lo que le pases como segundo parametro)
    orientar_derecha/izquierda (suma/resta x grados a orientacion)
    pasar_linea_svg (escribe en lenguaje svg lo que hizo la tortuga)
    '''
    def __init__(self,orientacion = radians(90), posicion = [0,0],pluma = True,posicion_inicial = [0,0],color ='black',ancho = 1):
        self.pluma = pluma
        self.posicion = posicion
        self.posicion_inicial = posicion_inicial
        self.orientacion = orientacion
        self.color = color
        self.ancho = ancho

    def orientar_costado(self):
        self.orientacion += radians(180)
        if self.orientacion > radians(360):
            self.orientacion -= radians(360)

    def girar_izquierda(self, cantidad):
        self.orientacion -= radians(cantidad)
        if self.orientacion > radians(360):
            self.orientacion -= radians(360)

    def girar_derecha(self, cantidad):
        self.orientacion += radians(cantidad)
        if self.orientacion > radians(360):
            self.orientacion -= radians(360)

    def avanzar(self,cantidad = [10,10]):
        self.posicion[0] -= cantidad[0] * cos(self.orientacion)
        self.posicion[1] -= cantidad[1] * sin(self.orientacion)

    def circulo_svg(self):
       return '<circle cx="15" cy="10" r="8" fill="white" />'

    def pasar_linea_svg(self):
        a = self.posicion_inicial[0]
        b = self.posicion_inicial[1]
        c = self.posicion[0]
        d = self.posicion[1]
        return f' <line x1="{a}" y1="{b}" x2="{c}" y2="{d}" stroke-width="{self.ancho}" stroke="{self.color}" />'

    def __repr__(self):
        return f'[{self.pluma},{self.posicion},{self.orientacion}]'

    def pluma_arriba(self):
        self.pluma = False

    def pluma_abajo(self):
        self.pluma = True

    def copiar_tortuga(self, tortuga_nueva):
        tortuga_nueva.pluma = [self.pluma][:][0]
        tortuga_nueva.posicion_inicial = self.posicion[:]
        tortuga_nueva.posicion = self.posicion[:]
        tortuga_nueva.orientacion = [self.orientacion][:][0]
