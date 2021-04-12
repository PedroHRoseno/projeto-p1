from funcoes_login import *
from datetime import *


"""
Aqui estarão as funções do sistema.
"""

def cadastrarNota(x, y):
    """
    Cadastra uma nota fiscal no sistema
    """
    notas = x
    empresas = y
    nota = input("Digite o número da nota: ")
    if not(nota in notas):
        valor = input("Digite o valor da nota(em R$): ")
        data = input("Digite a data da nota(dd/mm/aa): ")
        empresa = input("Digite o nome da empresa contratante: ")
        if not(empresa in empresas):
            print("Empresa não cadastrada no sistema!")
        else:
            notas[nota] = (nota, empresa, valor, data)
            print("Nota cadastrada com sucesso!")
    else:
        print("Nota já existente no sistema!")

    return notas

def buscarNota(dicionario):
    """
    Busca uma nota fiscal no sistema, por empresa e por nota
    """
    print("""
     ------ opções de pesquisa -------

             Por nota(1)
             Por empresa(2)
         """)
    
    busca = 0 
    while not(busca == 1 or busca == 2):
        busca = input("Digite seu método de pesquisa:")
        if busca == "1":
            numeroNota = input("Digite o número da nota: ")
            if numeroNota in dicionario:
                print("As informações presentes na nota são: \n"
                      "Numero  :", numeroNota, "\n"
                      "Empresa :", dicionario[numeroNota][1], "\n"
                      "Valor   :", dicionario[numeroNota][2], "\n"
                      "Data    :", dicionario[numeroNota][3], "\n")
            else:
                print("Número da nota não encontrada no sistema.")
        if busca == "2":
            notas = []
            nomeEmpresa = input("Digite o nome da empresa: ")
            for chave in dicionario:
                if dicionario[chave][1].lower() == nomeEmpresa.lower():
                    notas.append(dicionario[chave])

            if notas:
                print("As notas correspondentes a empresa", nomeEmpresa, "são: \n")
                for elemento in notas:
                    print("N.Nota:", elemento[0], "Empresa:", elemento[1], "Valor(R$):", elemento[2], "Data:", elemento[3])
               
            else:
                print("Nenhuma nota cadastrada!")

        return dicionario 

def alterarNota(dicionario, dicionario2):
    """
    Altera elementos de uma nota cadastrada no sistema
    """
    alterar = input("Digite o número da nota que você quer alterar: ")
    item = input("Digite o item o qual você quer alterar: ")
    if alterar in dicionario:
        if item == "empresa":
            newEnterprise = input("Digite a nova empresa correspondente a nota: ")
            if newEnterprise in dicionario2:
                dicionario[alterar] = (dicionario[alterar][0], newEnterprise, dicionario[alterar][2], dicionario[alterar][3])
            else:
                print("Empresa não cadastrada no sistema!")
        elif item == "valor":
            newValor = input("Digite o novo valor correspondente a nota: ")
            dicionario[alterar] = (dicionario[alterar][0], dicionario[alterar][1], newValor, dicionario[alterar][3])
        elif item == "data":
            newData = input("Digite a nova data correspondente a nota: ")
            dicionario[alterar] = (dicionario[alterar][0], dicionario[alterar][1], dicionario[alterar][2], newData)
    else:
        print("Nota não existente no sistema!")

    return dicionario

    


def removerNota(dicionario):
    """
    Remove uma nota do sistema
    """
    remover = input("Digite o número da nota que você quer remover: ")
    if remover in dicionario:
        dicionario.pop(remover)
        print("Nota removida com sucesso!")
    else:
        print("Esta nota não existe no sistema!")

    return dicionario

def cadastrarEmpresa(dicionario):
    """
    Cadastra uma empresa no sistema
    """
    nome = input("Digite o nome da empresa: ")
    cnpj = input("Digite o CNPJ da empresa: ")
    if nome not in dicionario:
        dicionario[nome] = (nome, cnpj)
    else:
        print("Empresa já existente no sistema!")

    return dicionario


def escreveNoLog(acao, loginUser):
    """
    Descreve a ação realizada no LOG
    """
    with open('log.txt','a',encoding="utf-8") as acoes:
        dataAtual = datetime.now()
        dataFormatada = dataAtual.strftime('%d/%m/%y %H:%M')
        acoes.write("[")
        acoes.write(loginUser)
        acoes.write("]")
        acoes.write(acao)
        acoes.write("[")
        acoes.write(str(dataFormatada))
        acoes.write("]")
        acoes.write("\n")

def alterarUsuario(dicionario):
    """
    Altera o nível do usuário
    """
    alterar = input("Digite o login que você quer alterar: ")
    if alterar in dicionario:
        alt_nivel = input("Digite o novo nível de conta: ")
        dicionario[alterar] = (dicionario[alterar][0], dicionario[alterar][1], dicionario[alterar][2], alt_nivel)
    else:
        print("Usuário não cadastrado!")

    return dicionario

def ordenarNotas(dicionario):
    """
    Ordena as notas pelo número
    """
    lista = []
    for chave in dicionario:
        lista.append(int(chave))
    for passnum in range(len(lista)-1,0,-1):
        for i in range(passnum):
            if lista[i]> lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
    for elemento in lista:
        print("-", elemento)

def lerLog(arquivo):
    with open("log.txt", "r", encoding="utf-8") as arq:
        mostrar = arq.read()
        print(mostrar)


        








            
        
        
        
        
