#try except
#ele mostra o arquivo, linha e tipo de erro

"""
syntax error: se não conseguir ler oq foi escrito
precisa verificar:
- linha
se fechou tudo (aspas,etc)
dois pontos
letras minusculas/maiusculas
dgitou corretamente"""

#identation error

#key error
#se tiver um dicionario e tentar acessar uma chave q não existe

#name error
#se tiver usando uma variavel antes de iniciar, vai dar erro

#value error
#type erorr (se chamar uma função, usando mais parametros do q ela recebe)

#index error

#tab error

#tratamento de exceções - para debugar o codigo
#é um evento que vai interromper o fluxo da execução do programa
#se tem uma suspeita de dar erro coloca o bloco try
"""try:
    bloco de comando
except:
    se ocorrer essa essa exceção, executa esse bloco
    
except:
    se ocorrer essa essa exceção, executa esse bloco //pode ter varias exceções
    
else:
    se não tiver nenhuma exceção, executa esse bloco"""

try:
    a=[1,2,3]
    b = a[4]
except IndexError: #(pode colocar aqui exatamente para o tipo de erro: NameError, etc OU NAO eai vai pegar todos os erros)
    print("Erro de Index!")
except NameError: #(pode colocar aqui exatamente para o tipo de erro: NameError, etc)
    print("Erro de Nome!")
