class Fila:

    def __init__ (self,tammaximo):
        self.dados=[0]*tammaximo
        self.inicio=0
        self.nelems=0
    def enfilerar(self,x):
        if self.nelems==len(self.dados):
            return False
        posicao=(self.nelems+self.inicio)%len(self.dados)
        self.dados[posicao]=x
        
        self.nelems+=1
    def mostrar(self):
        if self.nelems==0:            
            print ("Pilha vazia")
            return False
        print("Inicio = ",self.inicio)
        print("n de elementos",self.nelems)
        for i in range(self.nelems):
            if i<10:
                print(" ",end="")
            print(i,end=" ")
        print("")
        i=self.inicio
        k=1
        while k<=self.nelems:
            print(self.dados[i],end=" ")
            k+=1
            i+=1
            if i==len(self.dados):
                i=0
        print("")
    def desinfileirar(self):
        if self.nelems==0:
            return
        print("elemento ",self.dados[self.inicio]," sera eliminado")
        self.dados[self.inicio]=-1
        self.inicio+=1
        self.nelems-=1
import os
os.system("cls")

l=Fila(6)
l.enfilerar(10)
l.enfilerar(20)
l.enfilerar(30)
l.enfilerar(40)
l.enfilerar(50)
l.enfilerar(60)
l.desinfileirar()
l.mostrar()
l.desinfileirar()
l.mostrar()
l.enfilerar(51)
l.enfilerar(61)
l.desinfileirar()
l.mostrar()
