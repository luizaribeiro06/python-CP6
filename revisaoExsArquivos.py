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
linhas = arquivo.readlines() #para ler a linha e retorna uma lista
arquivo.close()

for linha in linhas:
    contador_espacos = 0
    for caractere in linha:
        if caractere == ' ':
            contador_espacos += 1
    # se tem mais de 6 espaços, então tem mais de 6 notas (nome + 6 = 7 palavras)
    if contador_espacos > 6:
        nome = ""
        for caractere in linha:
            if caractere == ' ':
                break
            nome += caractere
        print(nome)

#print a media e o nome de cada aluno
arquivo = open("notas.txt", "r")
linhas = arquivo.readlines()
arquivo.close()

for linha in linhas:
    nome = ""
    numero = ""
    notas = []
    lendo_nome = True

    for caractere in linha:
        if lendo_nome:
            if caractere == ' ':
                lendo_nome = False
            else:
                nome += caractere
        else:
            if caractere != ' ' and caractere != '\n':
                numero += caractere
            else:
                if numero != "":
                    notas.append(int(numero))
                    numero = ""

    if numero != "":
        notas.append(int(numero))  # última nota

    # Calcula a média manualmente (sem usar sum)
    soma = 0
    for nota in notas:
        soma += nota

    if len(notas) > 0:
        media = soma / len(notas)
        print(nome, "-", round(media, 2))

#mostra o nome, a nota maxima e minima
arquivo = open("notas.txt", "r")
linhas = arquivo.readlines()
arquivo.close()

for linha in linhas:
    nome = ""
    numero = ""
    notas = []
    lendo_nome = True

    for caractere in linha:
        if lendo_nome:
            if caractere == ' ':
                lendo_nome = False
            else:
                nome += caractere
        else:
            if caractere != ' ' and caractere != '\n':
                numero += caractere
            else:
                if numero != "":
                    notas.append(int(numero))
                    numero = ""

    if numero != "":
        notas.append(int(numero))  # adiciona a última nota

    # Calcula mínimo e máximo manualmente
    if len(notas) > 0:
        minimo = notas[0]
        maximo = notas[0]
        for nota in notas:
            if nota < minimo:
                minimo = nota
            if nota > maximo:
                maximo = nota
        print(nome, "- Mínima:", minimo, "| Máxima:", maximo)

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

saldo = 0

for linha in linhas:
    valor_texto = ""
    i = 0
    # Lê o valor (antes do primeiro espaço)
    while i < len(linha) and linha[i] != ' ':
        valor_texto += linha[i]
        i += 1

    if valor_texto != "":
        valor = int(valor_texto)
        saldo += valor

print("Saldo atual da empresa:", saldo)

"""2) Escreva um programa que leia um valor e uma descrição, e inclua uma nova
linha no arquivo financeiro.log, conforme o formato ilustrado acima"""

# Lê um valor e uma descrição digitados pelo usuário
valor = input("Digite o valor (ex: 300 ou -150): ")
descricao = input("Digite a descrição: ")

# Abre o arquivo no modo append para adicionar no final
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