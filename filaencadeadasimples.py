class No:
    def __init__ (self,valor):
        self.dado=valor
        self.prox=None
class Fila:
    def __init__ (self,maxtam):
        self.prim=None
        self.ultimo=None
        self.maxtam=maxtam
        self.nelems=0

    def enfileirar(self,x):  
        if self.maxtam==self.nelems:
            return      
        p=No(x)
        self.nelems+=1
        if self.prim==None:
            self.prim=p
            self.ultimo=p            
            return
        self.ultimo.prox=p
        self.ultimo=self.ultimo.prox        
        return
    def mostrarfila(self):
        if self.prim==None:
            print("Fila vazia")
            return       
        ponteiro=self.prim
        print(f"Fila - primeiro elemento {self.prim.dado} - ultimo elemento {self.ultimo.dado}")
        print("Fila: ",end="")
        print(ponteiro.dado,end=" ")
        while ponteiro.prox!=None:
            ponteiro=ponteiro.prox
            print(ponteiro.dado,end=" ")
        print("")
        return
    def desenfileirar(self):
        if self.prim==None:
            return False, -1
        x=self.prim.dado
        self.nelems-=1
        if self.prim.prox!=None:
            self.prim=self.prim.prox
        else:
            self.prim=None
            self.ultimo=None
        return True, x

    
        

   
import os
os.system('cls')
l=Fila(3)
for i in range(1,6):
    l.enfileirar(i)
l.mostrarfila()

situacao, valor=l.desenfileirar()
if situacao:
    print(f"O valor {valor} foi retirado com sucesso")
else:
    print("A pilha já esta vazia")
l.mostrarfila()

situacao, valor=l.desenfileirar()
if situacao:
    print(f"O valor {valor} foi retirado com sucesso")
else:
    print("A pilha já esta vazia")
l.mostrarfila()
situacao, valor=l.desenfileirar()
if situacao:
    print(f"O valor {valor} foi retirado com sucesso")
else:
    print("A pilha já esta vazia")
l.mostrarfila()