
#carregar vetor que sera ordenado
a=[40,6,2,9,1,4]
#quantidade de elementos do vetor
n=len(a)
#mostrar os elementos antes da ordenacao
print(a)
#mostrar a quantidade de elementos do vetor
print(n)


for j in range(1,n):
    print("j= ",j,end="   ")
    chave=a[j]
    i=j-1
    print ("i=",i)
    while (i>=0) and (a[i]>chave):
        a[i+1]=a[i]
        i-=1
    a[i+1]=chave
    print (a)
print ("ordenado ",a)
