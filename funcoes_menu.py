from funcoes_login import *
from funcoes_sistema import *
import os
from datetime import *

def visitante():
    """
    Essa função printa o menu e retorna a opção escolhida
    """
    print("|------------------------------| \n"
          "|------------ Menu ------------| \n"
          "      Buscar Nota(1)         \n"
          "      Sair da conta(2)       \n"
          "      Sair(3)                \n")

    opcao = 0
    lista = [1, 2, 3]
    while not(opcao in lista  ):
        opcao = int(input("Digite a opção desejada: "))

    return opcao

def moderador():
        """
        Essa função printa o menu e retorna a opção escolhida
        """
        print("|------------------------------| \n"
              "|------------ Menu ------------| \n"
              "      Cadastrar Nota(1)      \n"
              "      Buscar Nota(2)         \n"
              "      Alterar Nota(3)        \n"
              "      Remover Nota(4)        \n"
              "      Relatório de notas(5)  \n"
              "      Sair da conta(6)    \n"
              "      Sair(7)             \n")

        opcao = 0
        lista = [1, 2, 3, 4, 5, 6, 7]
        while opcao not in lista:
            opcao = int(input("Digite a opção desejada: "))

        return opcao

def administrador():
    """
    Essa função printa o menu e retorna a opção escolhida
    """
    print("|------------------------------|         \n"
          "|------------ Menu ------------|         \n"
          "      Cadastrar Nota(1)              \n"
          "      Cadastrar Empresa(2)           \n"
          "      Buscar Nota(3)                 \n"
          "      Alterar Nota(4)                \n"
          "      Remover Nota(5)                \n"
          "      Alterar nível de usuário(7)    \n"
          "      Relatório de notas(8)          \n"
          "      Sair da conta(9)               \n"
          "      Sair(10)                       \n"
          "      Ler log do sistema(11)         \n")

    opcao = 0
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    while not(opcao in lista  ):
        opcao = int(input("Digite a opção desejada: "))

    return opcao
