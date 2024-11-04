class Lista:
    def __init__ (self,tammax):
        self.dados=[0]*tammax
        self.nelems=0
    def posicao(self,x):
        i=0
        while (i<self.nelems) and (self.dados[i]!=x):
            i+=1
        if self.nelems==len(self.dados):
            return -1
        return i            
    def consultar(self,x):
        indice=self.posicao(x)
        if indice==-1:
            return False
        return True
    def inserir(self,x):
        if (self.nelems==len(self.dados)) or (not self.consultar(x)):
            return False   
        self.dados[self.nelems]=x
        self.nelems+=1
    def mostrar(self):
        
        if self.nelems==0:
            print("Lista vazia")
            return
        print("Quantidade de elementos: ",self.nelems)
        for i in range(self.nelems):
            print(self.dados[i],end=" ")
        print("")
        return
    def numerospares(self):
        pares=0
        for i in range(self.nelems):
            if ((self.dados[i]%2)==0):
                pares+=1
        return pares
    def dobraemultiplicar(self):
        if self.nelems==0 or self.nelems*2>len(self.dados):
            return
        for i in range(self.nelems):
            posicao=i+self.nelems
            self.dados[posicao]=2*self.dados[i]
        self.nelems=2*self.nelems

l=Lista(10)
l.inserir(10)
l.inserir(20)
l.inserir(3)
l.inserir(40)
l.inserir(5)
l.mostrar()
print("quantidade de pares; ",l.numerospares())
print("")
l.dobraemultiplicar()
l.mostrar()

        

        