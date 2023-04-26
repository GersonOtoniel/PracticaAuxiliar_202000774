from NodoItem import NodoItem
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaSimple:
    def __init__(self):
        self.primero = None
        self.tamaño = 0

    def Agregar(self, dato):
        nuevo = Nodo(dato)
        if self.primero==None or self.tamaño==0:
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.siguiente!=None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self.tamaño+=1



    def Imprimir(self):
        count = 0
        actual = self.primero
        while actual!=None:
            if count == 10:
                break
            else:
                print('{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}{:^15}{:^1}'.format('|',actual.dato.codigo,'|', actual.dato.margen1,'|',actual.dato.margen2,'|', actual.dato.margen3,'|',actual.dato.valor,'|'))
                count+=1
            actual = actual.siguiente


    def Ordenar(self,llave):
        llave1 = llave
        for i in range(1,self.tamaño):
            actual = self.primero
            for j in range(0, self.tamaño-1):
                if llave1 == 'codigo':
                    if actual.dato.codigo < actual.siguiente.dato.codigo:
                        temp = actual.dato
                        actual.dato = actual.siguiente.dato
                        actual.siguiente.dato = temp
                elif llave1 == 'margen1':
                    if actual.dato.margen1 < actual.siguiente.dato.margen1:
                        temp = actual.dato
                        actual.dato = actual.siguiente.dato
                        actual.siguiente.dato = temp
                elif llave1=='margen2':
                    if actual.dato.margen2 < actual.siguiente.dato.margen2:
                        temp = actual.dato
                        actual.dato = actual.siguiente.dato
                        actual.siguiente.dato = temp
                elif llave1 == 'margen3':
                    if actual.dato.margen3 < actual.siguiente.dato.margen3:
                        temp = actual.dato
                        actual.dato = actual.siguiente.dato
                        actual.siguiente.dato = temp
                elif llave1=='valor':
                    if actual.dato.valor < actual.siguiente.dato.valor:
                        temp = actual.dato
                        actual.dato = actual.siguiente.dato
                        actual.siguiente.dato = temp
                elif llave1 == 'margen':
                    if actual.dato.margen1<actual.siguiente.dato.margen1 and actual.dato.margen2<actual.siguiente.dato.margen2 and actual.dato.margen3<actual.siguiente.dato.margen3:
                        temp = actual.dato
                        actual.dato = actual.siguiente.dato
                        actual.siguiente.dato = temp
                actual = actual.siguiente 

