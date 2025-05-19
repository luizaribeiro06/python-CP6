def potencia(m,n):
    if n == 0:
        return 1
    elif n == 1:
        return m
    else:
        pot = m * potencia(m, n - 1) #diminuindo o valor até que seja o caso base
        return pot
print(potencia(5,3))

def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n-1)
print(fatorial(5))

#soma dos números naturais até n
def soma(n):
    if n == 0:
        return 0
    else:
        return n + soma(n - 1)

a = [1,3,5,7,9]
#a[0] + a[1:]
def somaLista(a):
    if len(a) == 1:
        return a[0]
    else:
        return a[0] + somaLista(a[1:]) #sempre vai chamar, a partir do primeiro

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        soma = fibo(n - 1) + fibo(n - 2)
        return soma

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

def exponencial(x, n):
    if n == 0:
        return 1
    else:
        """calcula-se o n-ésimo termo da série: f(x) = x^n / n! usando a função potencia(x, n) e fatorial(n) e depois soma com o resultado da função exponencial(x, n - 1) que representa a soma de todos os termos anteriores da série."""
        funcao = (potencia(x,n) / fatorial(n) + exponencial(x, n-1))
        return funcao

def palindromo(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return palindromo(s[1:-1])

def derivada(f, a, dx=1e-5): #notação para um numero muito pequeno
    return (f(a + dx) - f(a)) / dx

def f(x):
    return x**2

ponto = 3
resultado = derivada(f, ponto)

"""
Escreva uma função recursiva que, dada uma lista l de n
números inteiros ordenados (n ≥ 1) e um inteiro x, retorne, usando
uma busca binária, o índice de x na lista ou o valor −1, caso x não
pertença à lista.
"""
#binaria sempre precisa de inicio, meio e fim, mas o meio e declarado dentro da função
#usar lista[meio] para as condições
def busca_binaria(lista, x, inicio, fim):
    if inicio > fim:
        return -1  # x não está na lista

    meio = (inicio + fim) // 2

    if lista[meio] == x:
        return meio #já achou de primeira
    elif x < lista[meio]:
        return busca_binaria(lista, x, inicio, meio - 1) #significa que o x está antes
    else:
        return busca_binaria(lista, x, meio + 1, fim) #significa q o x está depois


#crie um marketplace......................
produtos = []
#criar uma função para funcionário cadastrar os produtos, para o cliente comprar e de compra

def cadastrar_produto():
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: R$ "))
    estoque = int(input("Quantidade em estoque: "))
    produto = [nome, preco, estoque]
    produtos.append(produto)
    print("Produto cadastrado com sucesso.")

def listar_produtos():
    print("\nProdutos disponíveis:")
    for i in range(len(produtos)):
        nome = produtos[i][0]
        preco = produtos[i][1]
        estoque = produtos[i][2]
        print(i, "-", nome, "- R$", preco, "-", estoque, "em estoque")

def comprar_produtos():
    if len(produtos) == 0:
        print("Nenhum produto disponível.")
        return

    listar_produtos()
    total = 0
    continuar = "s"

    while continuar == "s":
        print("\nDigite o número do produto que deseja comprar:")
        indice = int(input())
        print("Digite a quantidade que deseja comprar:")
        quantidade = int(input())

        if indice >= 0 and indice < len(produtos):
            if quantidade <= produtos[indice][2]:
                subtotal = produtos[indice][1] * quantidade
                total = total + subtotal
                produtos[indice][2] = produtos[indice][2] - quantidade
                print("Produto adicionado. Subtotal: R$", subtotal)
            else:
                print("Quantidade maior que o estoque.")
        else:
            print("Produto inválido.")

        print("Deseja continuar comprando? (s para sim / qualquer outra tecla para não)")
        continuar = input()

    print("\nTotal da compra: R$", total)

def menu():
    sair = 0
    while sair == 0:
        print("\n--- MENU ---")
        print("1 - Cadastrar produto (funcionário)")
        print("2 - Comprar produto (cliente)")
        print("3 - Sair")

        opcao = int(input("Escolha a opção: "))

        if opcao == 1:
            cadastrar_produto()
        elif opcao == 2:
            comprar_produtos()
        elif opcao == 3:
            sair = 1
            print("Saindo do sistema...")
        else:
            print("Opção inválida.")

menu()
