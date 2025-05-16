"""pode armazenar caracteres que podem ser mostardos na tela, como csv, html
arquivo texto
arquivo binárioo (não legíveis diretamente por um humano)

sempre que quer um dado no programa, pede input, mas a partir de agora pode receber seus dados de entrada de arquivos de texto também)

- o conjunto de dados pode ser muito maior
- os dados podem ser inseridos mais rapidamente
- pode usar os dados em vários programas ao mesmo tempo (uma oisa que o input nao faz)

nome e caminho - único (vai ser definido para poder acessar e alterar)
ler o dado, escrever e appendar

****arquivo texto****
abrir arquivo no programa e associar a uma varievl (tipo file)
variavel_arquivo = open("nome arquivo", "modo")
o nome pode ser absoluto: "/home/fiap/aula.txt" ou relativo (mesma pasta que o arquivo .py está)

existem alguns modos de abrir o arquivo:
- r (leitura)
- r+ (leitura e escrita)
- w (escrita)
- a (append)
- b (binário)

- se abre no modo leitura, ele já tem que estar criado
- se abre no modo escrita, apaga todo o conteudo que já tem
- no modo a de append preserva o q ja existe
- no modo binário é bom para salvar um objeto no arquivo, por exemplo, um dicionario (json) que pegou de uma api

ex leitura: arquivo = open("aula.txt", "r")
- se abrir para leitura e não existir, terá um erro
- se abrir para escrita, será criado


método read
read(qtd de bytes que deseja ler): retorna uma string contendo os próximos num de bytes do arquivo
"""

# = a.read(5) #le 5 carcteres, por exemplo, funciona como um indicador de posição
#se não passar parametro no read lê tudo
#ele leu 5, o 6ºelemento irá se tornar o primeiro se ele chamar dnv
#ler por linha: readline

#armazena cada linha numa lista, cada um como se fosse um eleemnto
"""lista = a.readlines()
print(lista)"""

"""txt = (a.readline())
while True:
    if txt == '':
        print(txt)
    print(txt)"""

#printa até o enter
a = open("aula.txt", "r")
i = 0
while True:
    txt = a.readline()
    i += 1
    print(txt)
    if txt == '':
        print('vazio')
        break

print(txt, end='') #printa um do lado do outro, ou seja, tira o enter

"""***** método close ***** 
toda vez que abre tem que fechar
permite liberar espaço na memória, por exemplo
arquivo.close() - uma forma de voltar para o primeiro indicador de posição"""

#readline() - devolve uma linha do arquivo em formato de string
#quando chega no fim, tem uma string vazia
"""método seek
passa dois parametros, a qtd de bytes"""