from NodoItem import NodoItem
from ListaSimple import ListaSimple
class Item:
    def __init__(self, texto):
        self.lista1 = ListaSimple()
        self.item = texto.getElementsByTagName('ItemCode')
        self.QuantityOnHand = texto.getElementsByTagName('QuantityOnHand')
        self.PriceLevel1 = texto.getElementsByTagName('PriceLevel1')
        self.PriceLevel2 = texto.getElementsByTagName('PriceLevel2')
        self.PriceLevel3 = texto.getElementsByTagName('PriceLevel3')
        self.LastTotalUnitCost = texto.getElementsByTagName('LastTotalUnitCost')

        self.MarginLevel1 = 0
        self.MarginLevel2 = 0
        self.MarginLevel3 = 0
        self.ValorInventario = 0
        self.codigo=0

        for i in range(len(self.item)):
            codigo = self.item[i].childNodes[0].data
            cantidad = float(self.QuantityOnHand[i].childNodes[0].data)
            precio1 = float(self.PriceLevel1[i].childNodes[0].data)
            precio2 = float(self.PriceLevel2[i].childNodes[0].data)
            precio3 = float(self.PriceLevel3[i].childNodes[0].data)
            costo = float(self.LastTotalUnitCost[i].childNodes[0].data)
           

            self.MarginLevel1= round(((precio1-costo)/costo)*100,2)
            self.MarginLevel2= round(((precio2-costo)/costo)*100,2)
            self.MarginLevel3= round(((precio3-costo)/costo)*100,2)
            Valor = cantidad*costo

            self.ValorInventario = round(Valor,2)


            
            Nuevonodo = NodoItem(codigo,self.MarginLevel1, self.MarginLevel2, self.MarginLevel3, self.ValorInventario)
            
            self.lista1.Agregar(Nuevonodo)
            
        return print('Documento Cargado')
        