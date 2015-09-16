# n representa o numero total de elementos a serem ordenados 
n = 20 
# lista contendo os elementos
lista = [11,18,3,1,16,12,6,19,5,0,14,4,17,9,13,7,10,15,2,8] 
# i é o elemeto a ser fixado. 0 é o inicio, n-1 é ultimo elemento a ser analisado e 1 é o intervalo
for i in range(0,n-1,1):
# j é o elemento que será comparado com i de modo que sempre será diferente do mesmo. i+1 é o início.
    for j in range(i+1,n,1):
# indica que caso o valor de i seja maior que o do j, temp irá assumir o valor de i, depois i o valor de j e por fim j o de temp. Representa uma troca de valores.
# temp é uma variável temporaria, para que os valores de i e j, com o intuito de serem trocados de lugar, não sejam perdidos.
        if lista[i] > lista[j]:
            temp = lista[i]
            lista[i] = lista[j]	
            lista[j] = temp			
    print [lista]