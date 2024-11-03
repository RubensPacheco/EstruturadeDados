a=[0,4,6,2,9,1,4]
n=len(a)
print(a)
print(n)
#o loop for no python funciona apartir do 0 a n-1
#obtei em seguir o proximo possivel 
# o n praticamente e desnecessario porem preferi declarar para
#
contadorj=[2,3,4,5,6]
for j in contadorj:

    chave=a[j]
    i=j-1
    while (i>0) and (a[i]>chave):
        a[i+1]=a[i]
        i-=1
    a[i+1]=chave
print ("ordenado ",a)
