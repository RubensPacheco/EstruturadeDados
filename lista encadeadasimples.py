# lista encadeada simples
#com as sugestoes do Professor
#Aluno Rubens Gigante Pacheco
#
#criando a classe No que sera a parte elementar da lista
class No:
    def __init__(self,x):
        self.valor=x
        self.prox=None
#criando a lista encadeanda simples
#a lista tera três informações referênciais o endereço do primeiro elemento, tamanho máximo e número de elementos atual
class Lista:
    def __init__(self,maxtam):
        self.prim=None
        self.maxtam=maxtam
        self.nelems=0
#
#consultar se o elemento existe on não
# retornará True se ele já existe, e False se o elemento não está na lista ou a lista esta vazia
    def consulta(self,x):
        if self.nelems==0:
            return False
        ponteiro=self.prim
        i=0
        while i<self.nelems and ponteiro.valor!=x:
            i+=1
            ponteiro=ponteiro.prox
        if i==self.nelems:
            return False
        return True
         





#
#função para criar nós e inserir valores
    def inserir(self,x):
#testa pra saber se a lista já está cheia

        if self.nelems==self.maxtam:
            return
#inserir se for o primeiro elemento
        if self.prim==None:

            self.prim=No(x)
            self.nelems=1
            return
        if self.consulta(x):
            return
#já se sabe que não será o primeiro e ainda existe espaço para inseri-lo
#aqui o Nó será colocado sempre no início da lista
        p=No(x)
        p.prox=self.prim
        self.prim=p
        self.nelems+=1
        return
#
#função para listar todos valores contidos na lista encadeada simples
    def listar(self):
        print("Tamanho da lista: ",self.nelems," tamanho máximo: ",self.maxtam)
        if self.nelems==0:
            print("Lista vazia")
            return

        ponteiro=self.prim
        
        for i in range(self.nelems):
            print(ponteiro.valor,end=" ")
            ponteiro=ponteiro.prox
        print("")

       
#
#importa biblioteca e apaga a tela do terminal
import os
os.system('cls')
#criação inserções e listagem
l=Lista(6)
l.inserir(1)
l.inserir(2)
l.inserir(3)
l.inserir(4)
l.inserir(5)
l.listar()



        
