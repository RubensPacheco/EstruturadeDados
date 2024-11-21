class No:
    def __init__ (self,x):
        self.dado=x
        self.prox=None
        self.ant=None
        
class Lista:
    def __init__ (self):
        self.prim=None
        self.ultimo=None
        
    def inserir(self,x):
        p=No(x)
        if not self.prim:
            self.prim=p
            self.ultimo=p
            return
        p.prox=self.prim
        self.prim.ant=p
        self.prim=p
    def listarinicioparafim(self):
        if not self.prim:
            print("Lista vazia")
            return
        p=self.prim
        print(f"Lista: {self.prim.dado}",end=" ")
        while p.prox:
            p=p.prox
            print(p.dado,end=" ")
        print("")
    def listardofinalparaoinicio(self):
        if not self.prim:
            print("Lista vazia")
            return
        p=self.ultimo
        print(f"Lista: {self.ultimo.dado}",end=" ")
        while p.ant:
            p=p.ant
            print(p.dado,end=" ")
        print("")
    def consulta(self,x):
        if not self.prim:            
            return False,-1 
        if self.prim.dado==x:
            return True, self.prim
        p=self.prim        
        while p.prox and p.dado!=x:
            p=p.prox
        if p.dado==x:
            return True, p
        return False,-1
    def colocardepois(self,ponteiro,y):
        p=No(y)
        p.prox=ponteiro.prox
        p.ant=ponteiro
        if ponteiro.prox!=None:            
            ponteiro.prox.ant=p
        ponteiro.prox=p
    def apagaroultimo(self):
        print("")
        if self.prim==None:
            return
        if self.prim.prox==None:
            self.prim=None
            self.ultimo=None
            return
        p=self.prim
        while p.prox:
            p=p.prox
        p.ant.prox=None
        self.ultimo=p.ant
        

        
        


            


    
        
        
        
        
        

import os
os.system("cls")
l=Lista()
for i in range(1,6):
    l.inserir(i)
l.listarinicioparafim()
print("******")

valor=1

situacao,ponteiro=l.consulta(valor)

print(f"** {ponteiro.dado}")
if situacao:
    print("colocando depois")
    l.colocardepois(ponteiro,90)
    l.listarinicioparafim()
print("testnado questao 2 do miniteste")
l.apagaroultimo()
l.apagaroultimo()
print("verificar se apagou")
l.listarinicioparafim()
l.listardofinalparaoinicio()




        
