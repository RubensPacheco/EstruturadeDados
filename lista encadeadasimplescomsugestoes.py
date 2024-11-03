# lista encadeada simples
#com sugestoes do Professor
#Aluno Rubens Gigante Pacheco
#
#criando a classe No que sera a parte elementar da lista
class No:
    def __init__(self,x):
        self.valor=x
        self.prox=None
#criando a lista encadeada simples
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
#função para criar nós e inserir valores na lista
    def inserir(self,x):
#testa pra saber se a lista já está cheia
        if self.nelems==self.maxtam:
            return False
#inserir se for o primeiro elemento
        if self.prim==None:
            self.prim=No(x)
            self.nelems=1
            return True
#testa para verificar o x já existe na lista
        if self.consulta(x):
            return False
#já se sabe que não será o primeiro e ainda existe espaço para inseri-lo
#aqui o Nó será colocado sempre no início da lista para evitar o loop até o fim da lista
        p=No(x)
        p.prox=self.prim
        self.prim=p
        self.nelems+=1
        return True
#
#função para listar todos valores contidos na lista encadeada simples
    def listar(self):
        print("Tamanho da lista: ",self.nelems)
        if self.nelems==0:
            print("Lista vazia")
            return
        print("Lista:",end="  ")
        ponteiro=self.prim        
        for i in range(self.nelems):
            print(ponteiro.valor,end=" ")
            ponteiro=ponteiro.prox
        print("")
#
#função para remover um nó
    def remover(self,x):
        if self.nelems==0:
            return False  
        if self.prim.valor==x:
            self.prim=self.prim.prox
            self.nelems-=1
            return True
        ponteiro=self.prim   
        i=0
        while i<self.nelems and ponteiro.valor!=x:
            anterior=ponteiro
            ponteiro=ponteiro.prox
            i+=1
        if i==self.nelems:
            return False
        anterior.prox=ponteiro.prox
        self.nelems-=1
        return True
#função fora da classe para imprimir o resultado do comando de inserção se teve sucesso ou não
def imprimirsituacaoinserir(sucesso,valor):
    if sucesso:
        print("valor ",valor," inserido")
    else:
        print("valor ",valor," não inserido")  
#função fora da classe para imprimir o resultado do comando de remoção se teve sucesso ou não      
def imprimirsituacaoremover(sucesso,valor): 
    if sucesso:
        print("valor ",valor," removido")
    else:
        print("valor ",valor," não removido")  
#
#importa biblioteca e apaga a tela do terminal
import os
os.system('cls')
#criação inserções e listagem
l=Lista(6)
valor=1
imprimirsituacaoinserir(l.inserir(valor),valor)
l.listar()
imprimirsituacaoremover(l.remover(valor),valor)
l.listar()
valor=2
imprimirsituacaoinserir(l.inserir(valor),valor)
valor=3
imprimirsituacaoinserir(l.inserir(valor),valor)
valor=4
imprimirsituacaoinserir(l.inserir(valor),valor)
valor=5
imprimirsituacaoinserir(l.inserir(valor),valor)
valor=1
imprimirsituacaoinserir(l.inserir(valor),valor)
l.listar()
valor=1
imprimirsituacaoremover(l.remover(valor),valor)
l.listar()
valor=4
imprimirsituacaoremover(l.remover(valor),valor)
l.listar()
valor=2
imprimirsituacaoremover(l.remover(valor),valor)
l.listar()
valor=5
imprimirsituacaoremover(l.remover(valor),valor)
l.listar()
valor=3
imprimirsituacaoremover(l.remover(valor),valor)
l.listar()    