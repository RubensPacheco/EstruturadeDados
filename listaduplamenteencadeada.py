class No:
    def __init__ (self,valor):
        self.valor=valor
        self.ant=None
        self.prox=None
class Lista:
    def __init__ (self,maxtam):
        self.prim=None
        self.ultimo=None
        self.tammax=maxtam
        self.nelems=0
    def inserir(self,x):
        if self.nelems==self.tammax:
            return
        self.nelems+=1
        p=No(x)
        if self.prim==None:
            self.prim=p
            self.ultimo=p
            return
        segundo=self.prim
        p.prox=self.prim
        segundo.ant=p
        self.prim=p
        return
    def listariniciopfim(self):
        if self.prim==None:
            print("lista vazia")
            return
        print("Listar do inicio ao fim")
        print(f"Lista com {self.nelems} elementos => ",end="")
        ponteiro=self.prim
        print(ponteiro.valor,end=" ")
        while ponteiro.prox:
            ponteiro=ponteiro.prox
            print(ponteiro.valor,end=" ")
        print("")
        return
    def listardofimparaoinicio(self):
        if self.prim==None:
            print("Lista vazia")
            return
        print("imprimindo do final ao início")
        ponteiro=self.ultimo
        print("Lista :",end=" ")
        if self.ultimo==self.prim:
            print(self.valor)
        while ponteiro.ant!=None:
            print(ponteiro.valor,end=" ")
            ponteiro=ponteiro.ant
        if ponteiro==self.prim:
            print(ponteiro.valor)
        return
    def consultar(self,x):
        if self.prim==None:
            return False,-1
        ponteiro=self.prim
        if self.prim.prox==None and self.prim.valor==x:
            return True, self.prim
        while ponteiro.prox!=None and ponteiro.valor!=x:
            ponteiro=ponteiro.prox
        if ponteiro.valor==x:
            return True, ponteiro
        return False,-1
    def remover(self,x):
         
        localizou,ponteiro=self.consultar(x)
        if not localizou:
            return
        self.nelems-=1
        if ponteiro==self.prim:
            self.prim=self.prim.prox
            self.prim.ant=None
            return
        if ponteiro==self.ultimo:
            self.ultimo=self.ultimo.ant
            self.ultimo.prox=None
            return
        anterior=ponteiro.ant
        posterior=ponteiro.prox
        anterior.prox=posterior
        posterior.ant=anterior
        return
         
             
        
            
l=Lista(10)
for i in range(1,10):
    l.inserir(i)

l.listariniciopfim()
print("***********")
l.listardofimparaoinicio()
localizou,ponteiro=l.consultar(1)
if localizou:
    print(f"localizou; > {ponteiro.valor} <")
aapagar=8
l.remover(aapagar)
print(f"verificar se apagou o {aapagar}")
l.listariniciopfim()
