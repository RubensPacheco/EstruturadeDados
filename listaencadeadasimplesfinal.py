class No:
    def __init__ (self,valor):
        self.valor=valor
        self.prox=None
class Lista:
    def __init__ (self,maxtam):
        self.prim=None
        self.tammax=maxtam
        self.nelems=0
    def inserir(self,x):
        if self.nelems==self.tammax:
            return
        self.nelems+=1
        p=No(x)
        p.prox=self.prim
        self.prim=p
        return
    def listar(self):
        if self.prim==None:
            print("lista vazia")
            return
        print(f"Lista com {self.nelems} elementos => ",end="")
        ponteiro=self.prim
        print(ponteiro.valor,end=" ")
        while ponteiro.prox!=None:
            ponteiro=ponteiro.prox
            print(ponteiro.valor,end=" ")
        print("")
        return
    def consultar(self,x):
        if self.prim==None:
            return
        ponteiro=self.prim
        if ponteiro.valor==x:
            return ponteiro
        while ponteiro.prox!=None:
            ponteiro=ponteiro.prox
            if ponteiro.valor==x:
                return ponteiro
        return
    def remover(self,x):
        p=self.consultar(x)
        if p==None:
            return
        self.nelems-=1
        if p!=self.prim:
            p.valor=self.prim.valor
        self.prim=self.prim.prox
l=Lista(15)
l.inserir(1)
l.inserir(2)
l.inserir(3)
l.inserir(4)
l.inserir(5)
l.inserir(6)
l.listar()
l.remover(2)
l.listar()