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
    avanzar_x (avanza 10 unidades en la 1ra componente)
    avanzar_y (avanza 10 unidades en la 2da componente)
    orientar_arriba (suma 90 grados a orientacion)
    girar (gira una cantidad pasada por parametro)
    '''
    def __init__(self,orientacion = 0, posicion = [0,0],pluma = True,color ='black',ancho = 1):
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
        self.orientacion += 180
    def girar_izquierda(self, cantidad):
        self.orientacion += cantidad
    def girar_derecha(self, cantidad):
        self.orientacion -= cantidad
    def avanzar(self,cantidad = [100,100]):
        self.posicion[0] += cantidad[0]
        self.posicion[1] += cantidad[1]
    def circulo_svg(self):
       return '<circle cx="15" cy="10" r="8" fill="white" />'
    def pasar_linea_svg(self):
        a = self.posicion_inicial[0]* cos(self.orientacion_inicial)
        b = self.posicion_inicial[1] * sin(self.orientacion_inicial)
        c = self.posicion[0] * cos(self.orientacion)
        d = self.posicion[1] * sin(self.orientacion)
        return f''' <line x1="{a}" y1="{b}" x2="{c}" y2="{d}" stroke-width="{self.ancho}" stroke="{self.color}" />'''
    def __repr__(self):
        return f'[{self.pluma},{self.posicion},{self.orientacion}]'
    def mover_pluma(self):
        if self.pluma:
            self.pluma = False
        else:
            self.pluma = True
        self.avanzar()             