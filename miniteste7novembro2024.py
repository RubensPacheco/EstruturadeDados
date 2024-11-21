class No:
    def __init__ (self,valor):
        self.dado=valor
        self.prox=None
class Lista:
    def __init__ (self):
        self.prim=None
    def inserir(self,x):        
        p=No(x)
        p.prox=self.prim
        self.prim=p
        return
    def listar(self):
        if self.prim==None:
            print("lista vazia")
            return       
        ponteiro=self.prim
        print(ponteiro.dado,end=" ")
        while ponteiro.prox!=None:
            ponteiro=ponteiro.prox
            print(ponteiro.dado,end=" ")
        print("")
        return
    def retirarSegundoElemento(self):
        if self.prim!=None and self.prim.prox!=None:            
            p=self.prim.prox
            p.dado=self.prim.dado
            self.prim=self.prim.prox
        return
    def retirarUltimoElemento(self):
        if self.prim==None:
            return
        if self.prim.prox==None:
            self.prim=None
            return
        ponteiro=self.prim
        while ponteiro.prox!=None:
            anterior=ponteiro
            ponteiro=ponteiro.prox
        anterior.prox=None
        

   
import os
os.system('cls')
l=Lista()
for i in range(5,0,-1):
    l.inserir(i)
l.listar()
print("funcao para rodar")
l.retirarSegundoElemento()
l.retirarUltimoElemento()
l.listar()
