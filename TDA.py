# TDAs

class _Nodo:

    def __init__(self, dato=None, prox=None):
        self.dato = dato
        self.prox = prox


class ListaEnlazada:

    def __init__(self):
        self.prim = None

    def __repr__(self):
        actual = self.prim
        if self.prim == None:
            cadena = "ListaEnlazada("
        else:
            cadena = f"ListaEnlazada({self.prim.dato}"
            while actual.prox:
                actual = actual.prox
                cadena = cadena + f", {actual.dato}"
        return cadena + ")"

    def __str__(self):
        actual = self.prim
        if self.prim == None:
            cadena = "ListaEnlazada("
        else:
            cadena = f"ListaEnlazada({self.prim.dato}"
            while actual.prox:
                actual = actual.prox
                cadena = cadena + f", {actual.dato}"
        return cadena + ")"

    def __len__(self):
        actual = self.prim
        contador = 0
        while actual:
            contador += 1
            actual = actual.prox
        return contador


    def append(self, dato):
        nuevo_nodo = _Nodo(dato)
        if self.prim == None:
            self.prim = nuevo_nodo
        else:
            actual = self.prim
            while actual.prox:
                actual = actual.prox
            actual.prox = nuevo_nodo


    def insert(self, indice, dato):
        actual = self.prim
        contador = 1
        if indice == 0:
            self.prim = _Nodo(dato, actual)
        if (actual == None and indice != 0) or (actual.prox == None and indice > contador):
            raise IndexError
        while contador < indice:
            contador += 1
            actual = actual.prox
        if indice != 0:
            actual.prox = _Nodo(dato, actual.prox)


    def get(self, indice):
        actual = self.prim
        if actual == None:
            raise IndexError
        contador = 0
        while contador < indice and actual.prox:
            actual = actual.prox
            contador += 1
        if contador == indice:
            return actual.dato
        raise IndexError

    def pop(self, indice=None):
        actual = self.prim
        anterior = None
        if actual == None:
            raise IndexError
        elif indice == 0 or len(self) == 1 and indice == None:
            dato = actual.dato
            self.prim = actual.prox
            return dato
        elif indice == None or indice <= len(self)-1:
            contador = 0
            while actual.prox:
                if contador == indice:
                    dato = self.get(contador)
                    anterior.prox = actual.prox
                    return dato
                anterior = actual
                actual = actual.prox
                contador += 1
            if contador == len(self)-1 and indice == None:
                dato = self.get(contador)
                anterior.prox = actual.prox
                return dato
        raise IndexError

    def set(self, indice, dato):
        self.insert(indice, dato)
        self.pop(indice+1)

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

    def __str__(self):
        actual = self.prim
        if self.prim == None:
            cadena = "Cola("
        else:
            cadena = f"Cola({self.prim.dato}"
            while actual.prox:
                actual = actual.prox
                cadena = cadena + f", {actual.dato}"
        return cadena + ")"

    def __repr__(self):
        actual = self.prim
        if self.prim == None:
            cadena = "Cola("
        else:
            cadena = f"Cola({self.prim.dato}"
            while actual.prox:
                actual = actual.prox
                cadena = cadena + f", {actual.dato}"
        return cadena + ")"

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
        self.prim = None

    def __repr__(self):
        actual = self.prim
        if self.prim == None:
            cadena = "Pila("
        else:
            cadena = f"Pila({self.prim.dato}"
            while actual.prox:
                actual = actual.prox
                cadena = cadena + f", {actual.dato}"
        return cadena + ")"

    def __str__(self):
        actual = self.prim
        if self.prim == None:
            cadena = "Pila("
        else:
            cadena = f"Pila({self.prim.dato}"
            while actual.prox:
                actual = actual.prox
                cadena = cadena + f", {actual.dato}"
        return cadena + ")"

    def apilar(self, dato):
        if self.prim == None:
            self.prim = _Nodo(dato)
        else:
            self.prim = _Nodo(dato, self.prim)

    def desapilar(self):
        if self.prim == None:
            raise IndexError
        dato = self.prim.dato
        if self.prim.prox:
            self.prim = self.prim.prox
        else:
            self.prim = None
        return dato


    def ver_tope(self):
        if self.prim == None:
            raise IndexError
        return self.prim.dato

    def esta_vacia(self):
        if self.prim == None:
            return True
        return False
