"""recursão: como fazer uma funcao chamar ela mesma
é um termo para descrever um processo de repetição a um objeto que é similar a ele mesmo
exemplos:
- imagens que aparecem quando tem um espelho voltado para o outro
- quando compartilha a aba do teams varias vezes
obs>> fractal: vai construindo uma coisa a partir dela mesma de forma infinita

- existe um segmento que é quebrado em vários outros segmentos
- ampliacação de uma parte de uma linhas costeira (a costa do brasil por exemplo tem característica fractal),
- depende de quanto zoom você está dando
"""

"""se o corpo da FUNÇÃO chamar a própria função, de forma direta ou indireta
- criar um algoritmo para resolver um determinado problema
- solução base e a partir disso faz os casos maiores
- soma de números de uma lista [1,3,5,7,9]
- fazemos com uma função iterativa que calcula soma normalmente, mas supondo que não podemos usar o laço de repetição
- a adição é uma função definida para dois parametros, um par de numeros
- tem um laço interno que vai somando"""

"""como usar em python?
a soma da lista "numeros" é a soma do primeiro elemento da lista (numeros[0]), com a soma dos números no resto da lista (numeros[1:])
"""
# somaLista(numeros) = primeiro(numeros) + somaLista(resto(numeros))
# nesta equação, primeiro(numeros) retorna o primeiro elemento da lista e resto(numeros) retorna a lista com tudo menos o primeiro elemento
a = [1,3,5,7,9]
a[0] + a[1:]
def somaLista(numeros):
    if len(numeros) == 1:
        return numeros[0]
    else:
        return numeros[0] + somaLista((numeros[1:])) #sempre vai chamar, a partir do primeiro

#soma dos números naturais até n
def soma(n):
    if n == 0:
        return 0
    else:
        return n + soma(n - 1)

#fatorial
def fatorial(n):
    if n == 0:
        return 1
    return n * (n-1)
print(fatorial(5))

# outro jeito do fatorial, porém com auxiliar
# cada chamada da função fatorial, vai criar varias variaveis locais
# pode fazer várias chamadas da própria função, ter formas indiretas e diretas
def fatorial(n):
    if n == 0:
        return 1
    else:
        aux = fatorial(n - 1)
        return n * aux

#pilha na hora de armazenamento de memória
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


"""resumindo:
1 - descrever a solução para casos basicos
2 - assumindo a existencia de soluções para casos menores, mostramos como obter a solução para caso maior"""

def potencia(a, n):
    if n == 0: #uma vez que um número elevado a 0 é 1
        return 1
    else:
        pot = a * potencia(a, n - 1) #diminuindo o valor até que seja o caso base
        return pot

print(potencia(5, 3))

# 25 alunos quer saber quais as combinacões de grupos 3 a 3 consegue fazer na sala
def combinar(m, n):
    if n == 0:
        return 1
    elif m == n:
        return 1
    elif m <= n:
        return 0
    else:
        """soma as combinações onde o último elemento não entra com as onde o último elemento entra"""
        comb = combinar(m - 1, n) + combinar(m - 1, n - 1)
        return comb

# f(x) = x ** n / n!
# derivada da exponencial de x é ela mesmo
def fatorial(n):
    if n == 0:
        return 1
    return n * (n - 1)

#calcular a potência de modo recursivo sem usar **
def exponencial(x, n):
    if n == 0:
        return 1
    else:
        """calcula-se o n-ésimo termo da série: f(x) = x^n / n! usando a função potencia(x, n) e fatorial(n) e depois soma com o resultado da função exponencial(x, n - 1) que representa a soma de todos os termos anteriores da série."""
        funcao = (potencia(x,n) / fatorial(n) + exponencial(x, n-1))
        return funcao

"""mais exercicios:
- defina uma função recursiva que calcule o maior divisor comum entre dois números a e b, em que a > b
obs: a - b . a/b pode ser escrito em a%b

- mesma coisa só que para o mínimo múltiplo comum
"""

#contagem regressiva
def contagem_regressiva(n):
    if n == 0:
        print("FIM")
    else:
        print(n)
        contagem_regressiva(n - 1)

#soma dos dígitos de um número
def soma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + soma_digitos(n // 10)

#contar quantos dígitos tem um número
def contar_digitos(n):
    if n < 10:
        return 1
    else:
        return 1 + contar_digitos(n // 10)

#inverter um número
def inverter(n, invertido=0):
    if n == 0:
        return invertido
    else:
        return inverter(n // 10, invertido * 10 + n % 10)

#verificar se uma string é palíndromo
def palindromo(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return palindromo(s[1:-1])

#produto de números inteiros
def produto(a, b):
    if b == 0:
        return 0
    else:
        return a + produto(a, b - 1)

#somar elementos de uma lista
def soma_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + soma_lista(lista[1:])

#contar qnts vezes um numero aparece na lista
def contar_ocorrencias(lista, valor):
    if len(lista) == 0:
        return 0
    else:
        return (1 if lista[0] == valor else 0) + contar_ocorrencias(lista[1:], valor)

#verificar se a lista está ordenada
def esta_ordenada(lista):
    if len(lista) <= 1:
        return True
    else:
        return lista[0] <= lista[1] and esta_ordenada(lista[1:])

#remover todos os elementos iguais a x de uma lista
def remover(lista, x):
    if len(lista) == 0:
        return []
    elif lista[0] == x:
        return remover(lista[1:], x)
    else:
        return [lista[0]] + remover(lista[1:], x)
