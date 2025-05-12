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

"""possiveis exercicios:
- procurando uma palavra em um dicionario
- procurando um livro em uma seção específica
- procurando um elemento em uma lista ordenada
- procurando aunos com mais de 1,50m de altura em uma fila de alunos organizados de acordo com suas alturas
- crie um sistema que permita o registro de nomes. Implemente uma função de busca ness sistema, de forma sequencial e binária.
"""