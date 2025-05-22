#substitua o "a" por "A"
arq = open("aula.txt", "r")
final = ''
while True:
    txt = arq.read(1)
    if txt == "a":
        txt = "A"
    final += txt
    if txt == '':
        break
print(final)

arq.close()

"""O arquivo notas.txt contém uma linha para cada aluno de
uma turma de estudantes. O nome de cada estudante está no início
da cada linha e é seguido pelas suas notas. Escreva um programa
que imprime o nome dos alunos que têm mais de seis notas.
jose 9 4 6 8 5
pedro 5 8 3 9
suzana 8 8 7 4 3 7 4 10 9
gisela 10 8 10 5 6 10
joao 8 7 5 6 9"""

arquivo = open("notas.txt", "r")
linhas = arquivo.readlines()
arquivo.close()

# percorre cada linha da lista de linhas
for linha in linhas:
    # inicializa o contador de espaços para contar as palavras
    contador_espacos = 0

    # percorre cada caractere da linha
    for caractere in linha:
        # se o caractere for um espaço, aumenta o contador
        if caractere == ' ':
            contador_espacos += 1

    # se houver mais de 6 espaços, significa que há mais de 6 notas
    if contador_espacos > 6:
        # extrai o nome do aluno (antes do primeiro espaço)
        nome = ""
        for caractere in linha:
            if caractere == ' ':
                break
            nome += caractere

        # imprime o nome do aluno com mais de 6 notas
        print(nome)

# printa a média de notas
arquivo = open("notas.txt", "r")
linhas = arquivo.readlines()
arquivo.close()

# percorre cada linha da lista
for linha in linhas:
    nome = ""
    numero = ""
    notas = []
    lendo_nome = True

    for caractere in linha:
        if lendo_nome:
            if caractere == ' ':
                lendo_nome = False  # terminou de ler o nome
            else:
                nome += caractere
        else:
            if caractere != ' ' and caractere != '\n':
                numero += caractere  # constrói o número
            else:
                if numero != "":
                    notas.append(int(numero))  # adiciona a nota à lista
                    numero = ""

    # adiciona a última nota (caso não tenha espaço depois dela)
    if numero != "":
        notas.append(int(numero))

    # calcula a média manualmente
    soma = 0
    contador = 0
    for nota in notas:
        soma += nota
        contador += 1

    media = soma / contador  # resultado exato com decimais

    # imprime o nome e a média com todas as casas decimais padrão
    print(nome, "-> média:", media)

#ex: mostra o nome, a nota maxima e minima
arquivo = open("notas.txt", "r")
linhas = arquivo.readlines()
arquivo.close()

# percorre cada linha da lista
for linha in linhas:
    nome = ""          # variável que vai guardar o nome do aluno
    numero = ""        # variável para montar cada número lido da linha
    notas = []         # lista que vai armazenar as notas do aluno
    lendo_nome = True  # indica se ainda está lendo o nome

    # percorre cada caractere da linha
    for caractere in linha:
        if lendo_nome:
            if caractere == ' ':
                lendo_nome = False  # ao encontrar o primeiro espaço, para de ler o nome
            else:
                nome += caractere  # adiciona o caractere ao nome
        else:
            if caractere != ' ' and caractere != '\n':
                numero += caractere  # monta o número da nota caractere por caractere
            else:
                if numero != "":
                    notas.append(int(numero))  # converte o número em inteiro e adiciona à lista
                    numero = ""  # limpa a variável para a próxima nota

    # adiciona a última nota, caso não tenha espaço no final da linha
    if numero != "":
        notas.append(int(numero))

    # se houver pelo menos uma nota, calcula o mínimo e o máximo manualmente
    if len(notas) > 0:
        minimo = notas[0]  # assume que a primeira nota é a menor
        maximo = notas[0]  # assume que a primeira nota é a maior

        # percorre as notas para encontrar o verdadeiro mínimo e máximo
        for nota in notas:
            if nota < minimo:
                minimo = nota
            if nota > maximo:
                maximo = nota

        # imprime o nome do aluno junto com sua menor e maior nota
        print(nome, "- mínima:", minimo, "| máxima:", maximo)


"""
Considere a existência de um arquivo financeiro.log com os registros
financeiros de uma empresa, com o seguinte conteúdo inicial:

1000 capital inicial
-500 compra de matéria -prima
-200 mão de obra
400 venda do primeiro lote
300 venda do segundo lote
-300 aluguel da fábrica
"""
"""1) Escreva um programa que leia o arquivo financeiro.log e imprima o saldo
financeiro da empresa."""

arquivo = open("financeiro.log", "r")
linhas = arquivo.readlines()
arquivo.close()

# inicializa a variável 'saldo' com zero
saldo = 0

# percorre cada linha do arquivo
for linha in linhas:
    valor_texto = ""
    i = 0

    # lê o valor numérico no início da linha (antes do primeiro espaço)
    while i < len(linha) and linha[i] != ' ':
        valor_texto += linha[i]
        i += 1

    # se encontrou um valor, converte para inteiro
    if valor_texto != "":
        valor = int(valor_texto)

        # adiciona o valor ao saldo (pode ser positivo ou negativo)
        saldo += valor

# imprime o saldo final da empresa
print("saldo financeiro:", saldo)


"""2) Escreva um programa que leia um valor e uma descrição, e inclua uma nova
linha no arquivo financeiro.log, conforme o formato ilustrado acima"""

# Lê um valor e uma descrição digitados pelo usuário
valor = input("Digite o valor (ex: 300 ou -150): ")
descricao = input("Digite a descrição: ")

# Abre o arquivo no modo append para adicionar no final e escreve as variaveis que pediu para o usuario
arquivo = open("financeiro.log", "a")
arquivo.write(valor + " " + descricao + "\n")
arquivo.close()

print("Registro adicionado com sucesso.")

#em arquivo binario
"""import pickle: ler e escrever objetos no arquivos
após fizer isso, utiliza o método pickle.dump(objeto,arquivo) e depois pickle.load"""

#cria o arquivo e escreve o objeto lista
import pickle

lista = [65,66,67,68,69]
arqbin = open('arq1.bin','wb')

pickle.dump(lista,arqbin)
arqbin.close()

#abre no modo leitura e printa a variavel
arqbin = open('arq1.bin', 'rb')
a = pickle.load(arqbin)
print(a)
