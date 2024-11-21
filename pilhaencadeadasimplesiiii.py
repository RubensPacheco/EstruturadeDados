class No:
    def __init__ (self,valor):
        self.dado=valor
        self.prox=None
class Pilha:
    def __init__ (self):
        self.topo=None
        

    def empilhar(self,x):      
        p=No(x)
        if self.topo==None:
            self.topo=p
            
            return
        p.prox=self.topo
        self.topo=p
        return
    def mostrarpilha(self):
        if self.topo==None:
            #print("Pilha vazia")
            return       
        ponteiro=self.topo
        print("Pilha:  ",end="")
        print(ponteiro.dado,end=" ")
        while ponteiro.prox!=None:
            ponteiro=ponteiro.prox
            print(ponteiro.dado,end=" ")
        print("")
        return
    def desempilha(self):
        if self.topo==None:
            return False, -1
        x=self.topo.dado
        self.topo=self.topo.prox
        
        return True, x
    def nelementos(self):
        if self.topo==None:
            return 0
        p=self.topo
        contador=1
        while p.prox:
            p=p.prox
            contador+=1
        return contador

    
        

import os
os.system('cls')
l=Pilha()
saida=Pilha()
string="4+6*9+7-2*5"

for i in string:
    r=ord(i)
    if r>47 and r<58:
        saida.empilhar(int(i))
    else:
        if l.nelementos()==0:
            l.empilhar(i)
        else:
            sucesso, sinal=l.desempilha()
            ordsinal=ord(sinal)
            if (ordsinal==42 or ordsinal==47) and (r==43 or r==45):
                saida.empilhar(sinal)
                saida.empilhar(i)
            else:
                l.empilhar(sinal)
                l.empilhar(i)
tamanhopilha=l.nelementos()
print(f"pilha de sinais com {tamanhopilha} elementos")
for i in range(tamanhopilha):
    sucesso, sinal=l.desempilha()
    saida.empilhar(sinal)
saida.mostrarpilha()
print("Pilha residual")
l.mostrarpilha()