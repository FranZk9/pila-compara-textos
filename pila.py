#----------pila-----------------------
class pila(object):
    def __init__(self):
        self.items=[]
    def is_empty(self):
        if len(self.items)==0:
            return True
        else:
            return False
    def apilar(self, texto):
        self.items.append(texto)
    def desapilar(self):
        if self.is_empty():
            return None
        else:
            return self.items.pop()
    def ver(self):
        print(self.items)
    def verTexto(self,i):
        return self.items[i]
    def obtenerLargo(self):
        return len(self.items[-1])
#------------------------------------        
pilita=pila()
elementos=0
largos=[]
while True:    
    opcion=int(input("1 - almacenar texto\n2 - ver texto más largo y más corto\n3 - imprimir un texto de la pila\n4 - comparar tamaños\n5 - salir\n"))
    if opcion==1:
        texto=str(input("texto a apilar: "))
        pilita.apilar(texto)
        elementos+=1
        largos.append([pilita.obtenerLargo(),elementos])
        pilita.ver()
        #print(largos)
    elif opcion==2:
        masLargo=max(largos)
        masCorto=min(largos)
        #print(masLargo)
        queElementoL=masLargo[1]-1
        queElementoC=masCorto[1]-1
        print("El texto más largo es:",pilita.verTexto(queElementoL))    
        print("El texto más corto es: ",pilita.verTexto(queElementoC))
    elif opcion==3:
        textoImprimir=int(input("número del elemento que desea ver: "))-1
        print(pilita.verTexto(textoImprimir))
    else:
        break