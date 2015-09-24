import matplotlib.pyplot as plt
# n representa o numero total de elementos a serem ordenados 
n = 20 
# lista contendo os elementos
lista = [11,18,3,1,16,12,6,19,5,0,14,4,17,9,13,7,10,15,2,8]
#imprime a lista original 
print("lista original", lista)
#gerar um arquivo de figura em branco
plt.figure()
#plotar as variáveis; (coordenadas x, coordenadas y, cor e simbolo)
plt.plot(range(0,n), lista, "ok")
#título do gráfico
plt.title("Lista Original")
#legenda do eixo x
plt.xlabel("Índices")
#legenda do eixo y
plt.ylabel("Números")
#salvar figura; local,nome e formato da figura a ser salva
plt.savefig("fig/bubble-inicio.png")
#fechar operação
plt.close()
#nova variável para contagem das trocas 
trocas = 0
#nova variável para todas as posições havendo troca ou não
posicao = 0
# i é o elemeto a ser fixado. 0 é o inicio, n-1 é ultimo elemento a ser analisado e 1 é o intervalo
for i in range(0,n-1,1):
# j é o elemento que será comparado com i de modo que sempre será diferente do mesmo. i+1 é o início.
    for j in range(i+1,n,1):
#cada vez que o programa passar por essa linha o valor da variável será acrescido de uma unidade para controle de todas as posições possíveis	
        posicao = posicao + 1
        plt.figure()	
        plt.plot(range(0,n), lista, "ok")
#coordenadas nas quais o símbolo será vermelho		
        plt.plot(i, lista[i], "or")
#coordenadas nas quais o símbolo será azul		
        plt.plot(j, lista[j], "ob")
        plt.title("Iteração-{}".format(posicao))
        plt.xlabel("Índices")
        plt.ylabel("Números")
        plt.savefig("fig/bubble-it-{}.png".format(posicao))
        plt.close()
# indica que caso o valor de i seja maior que o do j, temp irá assumir o valor de i, depois i o valor de j e por fim j o de temp. Representa uma troca de valores.
# temp é uma variável temporaria, para que os valores de i e j, com o intuito de serem trocados de lugar, não sejam perdidos.
        if lista[i] > lista[j]:
            temp = lista[i]
            lista[i] = lista[j]	
            lista[j] = temp
            trocas = trocas + 1			
            plt.figure()	
            plt.plot(range(0,n), lista, "ok")
            plt.title("Troca-{}".format(trocas))
            plt.xlabel("Índices")
            plt.ylabel("Números")
            plt.savefig("fig/bubble-troca-{}.png".format(trocas))
            plt.close()			
plt.figure()	
plt.plot(range(0,n), lista, "ok")
plt.title("Lista com ordem crescente")
plt.xlabel("Índices")
plt.ylabel("Números")
plt.savefig("fig/bubble-final.png")
plt.close()

#comando para imprimir na tela a lista em ordem crescente; 
print("lista em ordem crescente", lista)
#comando para imprimir na tela os cincos menores valores da lista; 0:5 significa o intervalo entre 0 e 5, com 5 aberto
print("Cinco menores valores", lista[0:5])
#comando para imprimir os cinco maiores valores; n-5:n representa o intervalo dos 5 ultimos elementos
print("Cinco maiores valores", lista[n-5:n])



