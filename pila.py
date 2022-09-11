import logging
logging.basicConfig(filename='logfile.log',
level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')
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
        logging.info('{} agregado a la pila'.format(texto))
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
    print("- Elija una operación -")    
    opcion=int(input("1 - almacenar texto\n2 - ver texto más largo y más corto\n3 - imprimir un texto de la pila\n4 - comparar tamaños\n5 - salir\n"))
    if opcion==1:
        texto=str(input("texto a apilar: "))
        if texto == '':
            print("Entrada vacía")
        else:
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
    elif opcion==4:
        primer=int(input("# Primer elemento a comparar: "))
        seg=int(input("# Segundo elemento a comparar: "))
        pos1=0
        pos2=0
        #print(len(largos))
        if primer>len(largos) or seg>len(largos):
            print("Esta posición no existe")
            logging.info('Posición {} no existe'.format(primer))
        else:
            for largo in largos:
                if primer in largo:
                    primer=largo[0]
                    pos1=largo[1]-1
            for largo in largos:
                if seg in largo:
                    seg=largo[0]
                    pos2=largo[1]-1
                #else:
                #    print("Esta posición no existe")
                #    logging.info('Posición {} no existe'.format(primer))
            if primer<seg:
                print(pilita.verTexto(pos2),"es más largo que",pilita.verTexto(pos1))
                logging.info('texto de {} es más largo que el de {}'.format(pos2+1,pos1+1))
            elif primer>seg:
                print(pilita.verTexto(pos1),"es más largo que",pilita.verTexto(pos2))
                logging.info('texto de {} es más largo que el de {}'.format(pos1+1,pos2+1))
            else:
                print("Ambos textos miden lo mismo")
    elif opcion==5:
        logging.info('Terminar')
        break
    else:
        print("Opción no válida")
        logging.info('Operacion inválida')
