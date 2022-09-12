import logging
logging.basicConfig(filename='logfile.log',
level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')
logging.info("Inicia ejecución")
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
    print("------------------------")
    print("- Elija una operación -")
    try:    
        opcion=int(input("1 - almacenar texto en pila\n2 - ver texto más largo y más corto\n3 - imprimir un texto de la pila\n4 - comparar tamaños\n5 - desapilar texto\n6 - salir\n"))
        if opcion==1:
            texto=str(input("Ingrese texto a apilar: "))
            if texto == '':
                print("Entrada vacía")
                logging.info('Opción 1. Se ingresó una entrada vacía')
            else:
                pilita.apilar(texto)
                elementos+=1
                largos.append([pilita.obtenerLargo(),elementos])
                pilita.ver()
            #print(largos)
        elif opcion==2:
            if pilita.is_empty()==True:
                print("Pila vacía")
                logging.info("Opción 2. Pila vacía")
            else:
                masLargo=max(largos)
                masCorto=min(largos)
                #print(masLargo)
                queElementoL=masLargo[1]-1
                queElementoC=masCorto[1]-1
                print("El texto más largo es:",pilita.verTexto(queElementoL))    
                print("El texto más corto es: ",pilita.verTexto(queElementoC))
                logging.info("Opción 2. Éxito")
        elif opcion==3:
            if pilita.is_empty()==True:
                print("Pila vacía")
                logging.info("Opción 3. Pila vacía")
            else:
                try:
                    textoImprimir=int(input("Número del elemento que desea ver: "))-1
                    if (textoImprimir+1)>len(largos):
                        print("No existe")
                        logging.info('Opción 3. El texto solicitado no existe')
                    else:
                        print(pilita.verTexto(textoImprimir))
                        logging.info("Opción 3. Éxito")
                except:
                    print("Formato inválido")
                    logging.info("Opción 3. Se ingresó un formato inválido")
        elif opcion==4:
            if pilita.is_empty()==True:
                print("Pila vacía")
                logging.info("Opción 4. Pila vacía")
            else:
                try:
                    primer=int(input("# Primer elemento a comparar: "))
                    seg=int(input("# Segundo elemento a comparar: "))
                    pos1=0
                    pos2=0
                    #print(len(largos))
                    if primer>len(largos):
                        print("Esta posición no existe")
                        logging.info('Posición {} no existe'.format(primer))
                    elif seg>len(largos):
                        print("Esta posición no existe")
                        logging.info('Posición {} no existe'.format(seg))
                    
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
                except:
                    print("Formato inválido")
                    logging.info("Opción 3. Se ingresó un formato inválido")
        elif opcion==5:
            pilita.desapilar()
            if pilita.is_empty()==True:
                print("Pila ya está vacía")
                logging.info("Opción 5. Pila ya vacía")
            else:
                pilita.ver()
        elif opcion==6:
            logging.info('Terminar')
            break
        else:
            print("Opción no válida")
            logging.info('Operacion inválida')
    except:
        print("Formato inválido")
        logging("Opción inválida")
