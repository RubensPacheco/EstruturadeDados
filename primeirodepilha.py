#Aluno: Rubens Gigante Pacheco
#Programa de pilha simples estática 
#Prof. Flávio
#Disciplina Estrutura de dados
#assunto pilhas

class pilha:
    def __init__ (self,tamanho):
        self.dados = [0]*tamanho
        self.tamatual=0
     
  #pode inserir sem precisar verificar a repetição de valores
    def inserir(self,x):
        # a pilha esta cheia retornar falso
        if self.tamatual==len(self.dados):
            return False
        self.dados[self.tamatual]=x
        self.tamatual+=1
        return True
    def mostrar(self):
        i=0
        while (i<self.tamatual):
            print(self.dados[i],end=" ")
            i+=1
        print(" quantidade na pilha =",self.tamatual)
        #sempre retira o último que foi inserido
    def remover(self):
        if self.tamatual==0:
            return False
        self.tamatual-=1
        return True
        
l=pilha(4)
l.inserir(0)
l.inserir(1)
l.inserir(2)
l.inserir(3)
l.mostrar()
numero=9

if not l.inserir(numero):
    print("nao foi possivel inserir o numero ",numero)
else:
    print("numero inserido")
l.mostrar()

if l.remover():
    print("O item  foi apagado")
else:
    print("O item  nao foi apagado")      
l.mostrar()  

if l.remover():
    print("O item  foi apagado")
else:
    print("O item  nao foi apagado")      
l.mostrar()  

if l.remover():
    print("O item  foi apagado")
else:
    print("O item  nao foi apagado")      
l.mostrar() 

if l.remover():
    print("O item  foi apagado")
else:
    print("O item  nao foi apagado")      
l.mostrar() 

if l.remover():
    print("O item  foi apagado")
else:
    print("O item  nao foi apagado")      
l.mostrar() 