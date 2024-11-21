class No:
    def __init__ (self,valor):
        self.dado=valor
        self.prox=None
class Pilha:
    def __init__ (self,maxtam):
        self.topo=None
        self.maxtam=maxtam
        self.nelems=0

    def empilhar(self,x):  
        if self.maxtam==self.nelems:
            return      
        p=No(x)
        if self.topo==None:
            self.topo=p
            self.nelems+=1
            return
        p.prox=self.topo
        self.topo=p
        return
    def mostrarpilha(self):
        if self.topo==None:
            print("Pilha vazia")
            return       
        ponteiro=self.topo
        print("Pilha")
        print(ponteiro.dado)
        while ponteiro.prox!=None:
            ponteiro=ponteiro.prox
            print(ponteiro.dado)
        print("")
        return
    def desempilha(self):
        if self.topo==None:
            return False, -1
        x=self.topo.dado
        self.topo=self.topo.prox
        self.nelems-=1
        return True, x

    
        

   
import os
os.system('cls')
l=Pilha(6)
for i in range(3,0,-1):
    l.empilhar(i)
l.mostrarpilha()

situacao, valor=l.desempilha()
if situacao:
    print(f"O valor {valor} foi retirado com sucesso")
else:
    print("A pilha já esta vazia")
l.mostrarpilha()

situacao, valor=l.desempilha()
if situacao:
    print(f"O valor {valor} foi retirado com sucesso")
else:
    print("A pilha já esta vazia")

situacao, valor=l.desempilha()
if situacao:
    print(f"O valor {valor} foi retirado com sucesso")
else:
    print("A pilha já esta vazia")

situacao, valor=l.desempilha()
if situacao:
    print(f"O valor {valor} foi retirado com sucesso")
else:
    print("A pilha já esta vazia")


