#Lista encadeada simples
#Aluno Rubens Gigante Pacheco
#
#elemento No da lista
class No:
    def __init__ (self,x):
        self.valor=x
        self.proximo=None
#
#lista propriamente dita com ponto inicial e tamanho
#
class Lista:
    def __init__ (self):
        self.inicio=None
        self.tamanho=0
#
# a função consultar retorna True se o valor já existe e False se não existe
#
    def consulta(self,x): 
        if self.inicio==None:
            return False            
        ponteiro=self.inicio
        if ponteiro.valor==x:
            return True
        while ponteiro.valor!=x:
            if ponteiro.proximo==None:
                return False
            ponteiro=ponteiro.proximo
        return True
            
            
#
# a função inserir                
#
    def inserir(self,x):       
#verifica se a lista é vazia
        if self.inicio==None:
            self.inicio=No(x)
            self.tamanho=1
            return
#se o valor já existe pare
        if self.consulta(x):
            return
        ponteiro= self.inicio     
        while ponteiro.proximo!=None:
            ponteiro=ponteiro.proximo
        ponteiro.proximo=No(x)
        self.tamanho+=1
#
#função para mostrar todos elementos da lista
#
    def mostrar(self):
        print("Tamanho da cadeia ",self.tamanho)
        if self.inicio==None:
            print("Lista vazia")
            return
            
        ponteiro=self.inicio
        print(ponteiro.valor,end=" ")
        while ponteiro.proximo!=None:
            ponteiro=ponteiro.proximo
            print(ponteiro.valor,end=" ")
            
        print("")
#
#função para remover elemento
#
    def remover(self,x):
#verifica se o elemento não existe ou se a lista está vazia
        if not self.consulta(x):
            return False
        ponteiro= self.inicio
#verifica se o elemento a ser retirado é o primeiro da lista porque será mais fácil de retirar
        if ponteiro.valor==x:
            self.inicio=ponteiro.proximo
            self.tamanho-=1
            return True
# O elemento existe, não é o primeiro e ou está no meio ou é o último
        anterior=ponteiro
        while ponteiro.valor!=x:
            anterior=ponteiro            
            ponteiro=ponteiro.proximo
#aqui o ponteiro anterior fará um bypass no nó e este pelo gerenciador do python será removido
        anterior.proximo=ponteiro.proximo
        self.tamanho-=1


        


        
        

l=Lista()
l.inserir(1)
l.inserir(1)
l.inserir(2)
l.inserir(3)
l.inserir(3)
l.inserir(4)
l.inserir(4)
l.remover(2)
l.mostrar()