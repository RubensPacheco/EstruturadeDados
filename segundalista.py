#Aluno: Rubens Gigante Pacheco
#Programa de lista simples estática sem ordenacao
#programa adequado as sugestões de aula
#materia Estrutura de dados
import os
os.system('cls')
class lista:
    def __init__ (self,tammax):
        self.dados = [0]*tammax
        self.nelems=0
    def posicao(self,x):
        i=0
        while (i<self.nelems) and (self.dados[i]!=x):
            i+=1
        if i==self.nelems:
            return -1
        return i
        
    def consulta(self,x):
        if self.posicao(x)==-1:
            return False
        return True
    def inserir(self,x):
        #caso o numero ja exista ou   a lista esta cheia retornar falso
        if self.consulta(x)or(self.nelems==len(self.dados)):
            return False
        self.dados[self.nelems]=x
        self.nelems+=1
        return True
    def mostrar(self):
        i=0
        while (i<self.nelems):
            print(self.dados[i],end=" ")
            i+=1
        print("")
        print("quantidade na lista =",self.nelems)
    def remover(self,x):
        i=self.posicao(x)
        if i==-1:
            return False
        else:
            self.dados[i]= self.dados[self.nelems-1]
            self.nelems-=1
            return True
    def nmaior(self):
        if self.nelems==0:
            return -1
        maior=self.dados[0]
        x=1
        while x<self.nelems:
            if self.dados[x]>maior:
                maior=self.dados[x]
            x+=1
        return maior
    def apagarindice(self,i):
        if self.nelems==0 or i>=self.nelems:
            return
        self.nelems-=1
        self.dados[i]=self.dados[self.nelems]
       



l=lista(6)
l.inserir(0)
l.inserir(1)
l.inserir(2)
l.inserir(3)
l.inserir(4)
l.inserir(5)
l.mostrar()
print("Maior numero",l.nmaior())
l.apagarindice(5)
l.mostrar()

        