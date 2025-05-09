#correção cp5
#lista de compras
#ex 1 - lista de compras
def compras(lista, sup):
    tem = []
    ntem = []
    valor = 0
    for i in lista:
        if i in sup:
            valor += sup[i]
            tem.append(i)
        else:
            ntem.append(i)
    return valor, tem, ntem

#ex 2 - ordenação
#faz o buble sort normal e depois pensa em como acessar o segundo indice da tupla (1)
a = [("Equipe A", 85), ("Equipe B", 80)]
def ordem(a):
    for iteracao in range(len(a)-1, 0, -1):
        for i in range(iteracao): #levar o maior numero para o fim
            if a[i][1] > a[i+1][1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp

#ex 3 -  busca sequencial
def busca(lista, chave):
    for i in range(len(lista)):
        if lista[i] == chave:
            return i
    return -1

#ex 4 - estoque

estoque_atual = {"camisa":5, "calça":3, "sapato":2}
novos_itens = {"camisa":2, "calça":1, "boné":2}
def atualiza(estoque, novo):
    for i in novos_itens.items():
        if i[0] in estoque_atual:
            estoque_atual[i[0]] =+ i[1]
        else:
            estoque_atual[i[0]] = i[1]
    return estoque

#ex 5 - medalhas
#dicionario gigantesco chave data

pais = 'China'
def medalhas(pais):
    for i in a['data']:
        if i['name'] == pais:
            return i['name'], i['total_medals'], i['bronze_medals'], i['gold_medals'], i['silver_medals']

#ordenação
#busca sequencial
#dado que temos uma lista e quer buscar um elemento da lista

#busca binária
#requer que a lista esteja ordenada e divide na metade para ver se está acima ou para trás do meio
#mais performática
#verifica se o elemnto via ser igual ao valor da poisção do meio, caso for já encontrou
#caso for maior, repete o processo só que considerar do inicio até o elemento anterior do meio
#caso for menor, repete o processo só que considerar a partir do elemento do meio até o último

#define variavel inicial, final e meio (indice final + inicial / 2), pega o valor inteiro da divisão
#ai valida (exemplo de fazer isso tres vezes:)
"""meio + 1
final + inicial /2

final meio -1
inicial + final /2"""
lista = [1,2,3,4,5]
chave = 15

def buscabinaria(lista, chave):
    ini = 0
    fim = len(lista) - 1
    while ini <= fim:
        meio = (fim + ini) // 2
        if chave == lista[meio]:
            return meio
        elif chave > lista[meio]: #consegue respeitar a ordem alfabética também
            ini = meio + 1
        else:
            fim = meio -1
    return -1

print(buscabinaria(lista, 1))

#recursão: como fazer uma funcao chamar ela mesma
#é um termo para descrever um processo de repetição a um objeto que é similar a ele mesmo
#imagens que aparecem quando tem um espelho voltado para o outro
#quando compartilha a aba do teams varias vezes
#fractal: vai construindo uma coisa a partir dela mesma de forma infinita

#existe um segmento que é quebrado em vários outros segmentos
#ampliacação de uma parte de uma linhas costeira (a costa do brasil por exemplo tem característica fractal),
#depende de quanto zoom você está dando

#se o corpo da FUNÇÃO chamar a própria função, de forma direta ou indireta
#criar um algoritmo para resolver um determinado problema
#solução base e a partir disso faz os casos maiores
#soma de números de uma lista [1,3,5,7,9]
#fazemos com uma função iterativa que calcula soma normalmente, mas supondo que não podemos usar o laço de repetição
#a adição é uma função definida para dois parametros, um par de numeros
#tem um laço interno que vai somando
#como usar em python?
#a soma da lista "numeros" é a soma do primeiro elemento da lista (numeros[0]), com a soma dos números no resto da lista (numeros[1:])


a = [1,3,5,7,9]
a[0] + a[1:]
def somaLista(numeros):
    if len(numeros) == 1:
        return numeros[0]
    else:
        return numeros[0] + somaLista((numeros[1:])) #sempre vai chamar

#fatorial
def fatorial(n):
    if n == 0:
        return 1
    return n * (n-1)
print(fatorial(5))

#pilha na hora de armazenamento de memória

# pilha na hora de armazenamento de memória
# primeiro chama função main, sem nenhum parametro
# cria a pilha com f2, depois f1, faz as contas e vai voltando até o x definido da main
def f1(a, b):
    c = a - b
    return (a + b + c)


def f2(a, b):
    c = f1(b, a)
    return (b + c - a)


def main():
    x = f2(2, 3)
    return 0

    main()


# outro jeito do fatorial, porém com auxiliar
# cada chamada da função fatorial, vai criar varias variaveis locais
# pode fazer várias chamadas da própria função, ter formas indiretas e diretas
def fatorial(n):
    if n == 0:
        return 1
    else:
        aux = fatorial(n - 1)
        return n * aux


# sequência de fibonacci
"""fibo(4) = fibo(3) + fibo(2)
fibo(n) = fibo(n-1) + fibo(n-2)

fibo(1) = 0
fibo(2)=1"""

# em função com a lista
"""n = [0,1,1,2,3,5,8,13,21,34,55]"""


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        soma = fibo(n - 1) + fibo(n - 2)
        return soma


# reusmindo:
# descrever a solução para casos basicos
# assumindo a existencia de soluções para casos menores, mostramos como obter a solução para caso maior

def potencia(a, n):
    if n == 0:
        return 1
    else:
        pot = a * potencia(a, n - 1)
        return pot


print(potencia(5, 3))


# 25 alunos quer saber quais as combinacaoes de grupos 3 a 3 consegue fazer na sala
def combinar(m, n):
    if n == 0:
        return 1
    elif m == n:
        return 1
    elif m <= n:
        return 0
    else:
        comb = combinar(m - 1, n) + combinar(m - 1, n - 1)
        return comb


# f(x) = x ** n / n!

# derivada da exponencial de x é ela mesmo
def fatorial(n):
    if n == 0:
        return 1
    return n * (n - 1)


def exponencial(a, n):
    fatorial(a=n)
    potencia()
