

#bubble sort - ordenar o sistea pelo método de bolhas (bolha de maior tamanho sobe mais rapido para o topo da piscina,
# traduzindo para python: maior elemento "borbulha" para ao fim da lista, será o último)

# quando precisa ordenar (de forma crescente, por ex)
# exemplo - números inteiros
# aplicações diretas: rankings, definição de preferencia em atendimentos por prioridade
# aplicações indiretas: otimização de sistemas de busca, manutenção de estruturas de banco de dados
#cair no cp lista, dicionario, api, ordenacao

l = [12,38,25,31,26]
i=2

#trocar os elementos para deixar a lista ordenada
for iteracao in range(len(l)-1,0,-1): #vai andar -1 unidade até chegar no índice 0
    for i in range(iteracao): #len(l) - 1) vai até o fim da lista - 1, depois via -2 e assim vai
        if l[i] > l[i + 1]:
            aux = l[i]
            l[i] = l[i + 1]
            l[i + 1] = aux
        print(l) #mostra a comparação da lista antiga com aatual ordenada
    print()
print(l)


#selection sort - vai achar o menor elemento e colocar no início da lista

#crie uma função que retorna o índice do menor elemento de uma lista (além disso, declarei o menor elemento por si só)
l= [12,1,95,9,4,25,71]

menor = l[0]
indice= 0
for i in range(1, len(l)):
    if l[i] < menor:
        menor = l[i]
        indice = i
print(menor)
print(indice)


# agora pegue o menor a partir de uma posição inicial dada i, ele tem que retornar o indice desse tal menor de acordo
# com a lista inteira

#como eu estava fazendo
partida =1
indice= 0
menor = l[partida]
for i in range(partida, len(l)):
    if l[i] < menor:
        menor = l[i]
        indice = i
print(menor)
print(indice)

#como o professor fez
inicio = 2
indice = inicio
for i in range(inicio+1, len(l)):
    if l[i] < l[indice]:
        indice = i

print(indice)

#transformando em função
def i_menor(l, indice):

    for i in range(indice + 1, len(l)):
        if l[i] < l[indice]:
            indice = i
    return indice


#transformando em for
for i in range(len(l)):
    aux_i = i_menor(l, i)  # menor elemento da lista no começo qyuando ela estava sem rodem
    aux = l[i] #coloca o elemento menor para a auxiliar
    l[i] = l[aux_i]  # vai assumir ser o menor elemento na primeira posição da lista
    l[aux_i] = aux

print(l)

#insertion
#lista ordenada e o último elemento está sem ordem e precisa inserir o elemento na posição correta
#assume que a lista está ordenada entre as posições 0 e 0

#depois que comparar, o valor maior precisa ir indo para frente
l= [12,41,68,71,95,52]
#vai comparando e joga o numero maior para frente
i = 5
for i in range(len(l)):
    aux = l[i]
    j = i - 1
    while j >= 0 and l[j] > aux:
        l[j+1] = l[j] #jogou uma casa para frente
        j = j - 1 #e subtrai de uma unidade o número desejado
        print(l)
    l[j + 1] = aux
    print(l)
print(l)

#algoritmo com uma lista de varios elementos
#fufncao que recebe lista, a chave de busca e retorne -1 se nao tiver na lista ou o indice do elemento
