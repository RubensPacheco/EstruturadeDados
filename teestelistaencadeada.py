class No:
    def __init__ (self,x):
        self.dado=x
        self.prox=None
        self.ant=None
        
class Lista:
    def __init__ (self):
        self.prim=None
        
    def inserir(self,x):
        p=No(x)
        if not self.prim:
            self.prim=p
            self.ant=p
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
        p=self.ant
        print(f"Lista: {self.ant.dado}",end=" ")
        while p.ant:
            p=p.ant
            print(p.dado,end=" ")


l=Lista()
for i in range(1,6):
    l.inserir(i)
l.listarinicioparafim()
print("******")
l.listardofinalparaoinicio()

        
