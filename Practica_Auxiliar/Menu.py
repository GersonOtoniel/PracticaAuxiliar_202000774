from tkinter.filedialog import askopenfilename
from xml.dom import minidom
from ListaSimple import ListaSimple
from Item import Item
from os import system

class Menu:
    def __init__(self):
        self.lista1 = ListaSimple()
        self.lista2 = ListaSimple()
        self.opciones = 'Abrir Archivo', 'Mostrar Top 10 Productos con Mayor Margen de Ganancia', 'Mostrar Top 10 productos con Mayor Valor de Inventario','Top 10 para Margen 1','Top 10 para Margen 2','Top 10 para Margen 3', 'Salir'
    
    def mostrar(self, on:bool):
        while on:
            print('----------------------------------')
            print('|                                |')
            print('|       Practica Auxiliar        |')
            print('|                                |')
            print('|       Gerson David Otoniel     |')
            print('|       González Morales         |')
            print('|                                |')
            print('----------------------------------')
            print()


            j = 0
            for i in self.opciones:
                j+=1
                print('\t', j, ' - ' + i)
            
            print()
            opcion = input('Escribe tu opción: ')


            if opcion == '1':
                try:
                    self.file = askopenfilename(title="Cargar un archivo")
                    self.xml = minidom.parse(self.file)
                    self.item = Item(self.xml)
                except:
                    print('Error, no se ha seleccionado ningún archivo')
            if opcion == '2':
                system('cls')
                self.resultados('margen')
            if opcion =='3':
                system("cls")
                self.resultados('valor')
            if opcion == '4':
                system('cls')
                self.resultados('margen1')
            if opcion == '5':
                system('cls')
                self.resultados('margen2')
            if opcion == '6':
                system('cls')
                self.resultados('margen3')
            if opcion == '7':
                system('cls')
                break
                
                

    def resultados(self, llave):
        opcion = llave
         
        while True:
            print('----------------------------------')
            print('|                                |')
            print('|       Practica Auxiliar        |')
            print('|                                |')
            print('|       Gerson David Otoniel     |')
            print('|       González Morales         |')
            print('|                                |')
            print('----------------------------------')
            print()
            print('1. Salir')
            print('---------------------------------------------------------------------------------')
            print(f'Top 10 {llave.upper()}')
            print('---------------------------------------------------------------------------------')
            lista = self.item.lista1
            lista.Ordenar(opcion)
            lista.Imprimir()
            print('----------------------------------------------------------------------------------')
            entrada = input('Escriba opcion: ')


            if entrada =='1':
                system('cls')
                break


j = Menu()
j.mostrar(True)
