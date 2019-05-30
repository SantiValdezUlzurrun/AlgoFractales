class Tortuga:
    '''clase tortuga la cual tiene como atributos posicion ( lista de 2 numeros), orientacion (entero), pluma(true si esta abajo y false en caso contrario)
    como metodos:
    avanzar_x (avanza 10 unidades en la 1ra componente)
    avanzar_y (avanza 10 unidades en la 2da componente)
    orientar_arriba (suma 90 grados a orientacion)
    girar (gira una cantidad pasada por parametro)
    '''

    def __init__(self, orientacion = 0, posicion = [0,0], pluma = True, color ='black', ancho = 1):
        self.pluma = pluma
        self.posicion = posicion
        self.posicion_inicial = posicion
        self.orientacion = orientacion
        self.orientacion_inicial = orientacion
        self.color = color
        self.ancho = ancho

    def avanzar(self,cantidad = [100,100]):
        self.posicion[0] += cantidad[0]
        self.posicion[1] += cantidad[1]

    def dar_vuelta(self):
        self.orientacion += 180
        if self.orientacion > 360:
            self.orientacion -= 360

    def girar_izquierda(self, cantidad):
        self.orientacion += cantidad
        if self.orientacion > 360:
            self.orientacion -= 360

    def girar_derecha(self, cantidad):
        self.orientacion -= cantidad
        if self.orientacion > 360:
            self.orientacion -= 360



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
