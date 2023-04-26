class NodoItem:
    def __init__(self, codigo, margen1, margen2, margen3, valor):
        self.codigo = codigo
        self.margen1= margen1
        self.margen2 = margen2
        self.margen3 = margen3
        self.valor = valor
        self.siguiente = None
        
    def __str__(self)->str:
        return f'({self.codigo}, {self.margen1}, {self.margen2}, {self.margen3}, {self.valor})'