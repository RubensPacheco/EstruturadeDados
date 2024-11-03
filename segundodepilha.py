#Aluno: Rubens Gigante Pacheco
#Programa de pilha simples estática 
#Prof. Flávio
#Disciplina Estrutura de dados
#assunto pilhas

class pilha:
    def __init__ (self,tamanho):
        self.dados = [0]*tamanho
        self.tamatual=0
     
  #pode empilhar sem precisar verificar a repetição de valores
    def empilhar(self,x):
        # a pilha esta cheia retornar falso
        if self.tamatual==len(self.dados):
            return False
        self.dados[self.tamatual]=x
        self.tamatual+=1
        return True
    def mostrar(self):        

        
        if self.tamatual==0:
            print ("Pilha vazia")
        else:
            print ("Pilha")
            i=self.tamatual-1
            while (i>-1):
                print(self.dados[i])
                i-=1
        print("")
        #sempre retira o último que foi empilhado
    def desempilhar(self):
        if self.tamatual==0:
            return False, -1
        self.tamatual-=1
        y=self.dados[self.tamatual]
        return True, y

def imprimir(situacao,y):
    if situacao:
        print("O item ",y," foi apagado")
    else:
        print("O item  nao foi apagado") 

l=pilha(4)
l.empilhar(0)
l.empilhar(1)
l.empilhar(2)
l.empilhar(3)
l.mostrar()
numero=9

situacao,y = l.desempilhar()
imprimir(situacao,y)
l.mostrar()




situacao,y = l.desempilhar()
imprimir(situacao,y)
l.mostrar()




situacao,y = l.desempilhar()
imprimir(situacao,y)
l.mostrar()




situacao,y = l.desempilhar()
imprimir(situacao,y)
l.mostrar()




situacao,y = l.desempilhar()
imprimir(situacao,y)
l.mostrar()


