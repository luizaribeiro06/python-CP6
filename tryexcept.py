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

"""except IndexError: #(pode colocar aqui exatamente para o tipo de erro: NameError, etc OU NAO eai vai pegar todos os erros)
    print("Erro de Index!")"""

try:
    a=[1,2,3]

except: #(pode colocar aqui exatamente para o tipo de erro: NameError, etc)
    print("Erro de Nome!")
else:
    print("Continuação do programa")
    
finally:
    print("executa de toda forma") #mesmo que tenha erro no programa, fecha o arquivo
    
#raise: vou tratar mas ainda nao tratei
#pode fazer em while true até o usuário fazer oq ele quer
while True:
    try:
        a = int(input("Digite um numero inteiro: "))
    
    except Exception as i:  
        print("Por favor, é inteiro!")
    else:
        print("else")
        break
    
    finally:
        print("executa de toda forma") 
