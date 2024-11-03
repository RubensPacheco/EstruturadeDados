#Aluno: Rubens Gigante Pacheco
#Programa de lista simples estática sem ordenacao
#programa adequado as sugestões de aula
#materia Estrutura de dados

class lista:
    def __init__ (self,tamanho):
        self.dados = [0]*tamanho
        self.tamatual=0
    def posicao(self,x):
        i=0
        while (i<self.tamatual) and (self.dados[i]!=x):
            i+=1
        if i==self.tamatual:
            return -1
        return i
        
    def consulta(self,x):
        if self.posicao(x)==-1:
            return False
        return True
    def inserir(self,x):
        #caso o numero ja exista ou   a lista esta cheia retornar falso
        if self.consulta(x)or(self.tamatual==len(self.dados)):
            return False
        self.dados[self.tamatual]=x
        self.tamatual+=1
        return True
    def mostrar(self):
        i=0
        while (i<self.tamatual):
            print(self.dados[i],end=" ")
            i+=1
        print(" quantidade na lista =",self.tamatual)
    def remover(self,x):
        i=self.posicao(x)
        if i==-1:
            return False
        else:
            self.dados[i]= self.dados[self.tamatual-1]
            self.tamatual-=1
            return True
        
l=lista(6)
l.inserir(0)
l.inserir(1)
l.inserir(2)
l.inserir(3)
l.inserir(4)
l.inserir(5)
l.mostrar()
numero=6
print("Posicao do numero ",numero," na lista    situacao = ",l.posicao(numero))
if not l.inserir(numero):
    print("nao foi possivel inserir o numero ",numero)
else:
    print("numero inserido")
l.mostrar()
numero=5
if l.remover(numero):
    print("O item ",numero," foi apagado")
else:
    print("O item ",numero," nao foi apagado")      
l.mostrar()  
numero=0
if l.remover(numero):
    print("O item ",numero," foi apagado")
else:
    print("O item ",numero," nao foi apagado")      
l.mostrar()  
    
        