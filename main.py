from funcoes_login import *
from funcoes_sistema import *
import os
from datetime import *
from funcoes_menu import *
import getpass

acesso = False
sair = False
while(sair == False):
    print("""

          |----------- Bem vindo ao NoteExpress ----------|

                        Logar(1)
                        Cadastrar(2)
                        Sair(3)
         """)
    escolha = input("Qual opção deseja? ")

    os.system('cls' if os.name == 'nt' else 'clear')

    if escolha == "2":

        criptografar_dicionario(cadastrar(descriptografar_arquivo("usuarios.txt")), "usuarios.txt")
        os.system('cls' if os.name == 'nt' else 'clear')

    elif escolha == "1":

        print("""
            |---------- Tela de login -----------|

            """)
        login_usuario = input("Digite seu login: ")
        senha = input("Digite sua senha: ")
        dic_temp = descriptografar_arquivo("usuarios.txt")
        acesso, nivel = login(login_usuario, senha, dic_temp)
        criptografar_dicionario(dic_temp, "usuarios.txt")
        wait = input("Pressione enter para continuar ->")
        os.system('cls' if os.name == 'nt' else 'clear')
        
    elif escolha == "3":
        
        sair == True
        print("#-----------Programa finalizado----------#")
        wait = input("Pressione enter para continuar ->")
        os.system('cls' if os.name == 'nt' else 'clear')

    while(acesso == True):
            
            if nivel == "1":
                
                opcao = visitante()

                if opcao == 1:

                    buscarNota(descriptografar_arquivo("notas.txt"))
                    escreveNoLog("Buscou notas", login_usuario)
                    wait = input("Pressione enter para continuar ->")
                    os.system('cls' if os.name == 'nt' else 'clear')

                elif opcao == 2:

                    acesso = False
                    escreveNoLog("Deslogou do sistema", login_usuario)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    

                elif opcao == 3:

                    acesso = False
                    sair = True
                    escreveNoLog("Encerrou o sistema", login_usuario)
                    os.system('cls' if os.name == 'nt' else 'clear')

            if nivel == "2":

                opcao = moderador()

                if opcao == 1:

                    notasAtu = cadastrarNota(descriptografar_arquivo("notas.txt"), descriptografar_arquivo("empresas.txt"))
                    criptografar_dicionario(notasAtu, "usuarios.txt")
                    escreveNoLog("Cadastrou notas", login_usuario)
                    wait = input("Pressione enter para continuar ->")
                    os.system('cls' if os.name == 'nt' else 'clear')
                       

                elif opcao == 2:

                    buscarNota(descriptografar_arquivo("notas.txt"))
                    escreveNoLog("Buscou notas", login_usuario)
                    wait = input("Pressione enter para continuar ->")
                    os.system('cls' if os.name == 'nt' else 'clear')

                elif opcao == 3:

                    criptografar_dicionario(alterarNota(descriptografar_arquivo("notas.txt")), "notas.txt")
                    escreveNoLog("Acesso a alteração de notas", login_usuario)
                    wait = input("Pressione enter para continuar ->")
                    os.system('cls' if os.name == 'nt' else 'clear')
                
                elif opcao == 4:

                    criptografar_dicionario(removerNota(descriptografar_arquivo("notas.txt")), "usuarios.txt")
                    escreveNoLog("Removeu notas", login_usuario)
                    wait = input("Pressione enter para continuar ->")
                    os.system('cls' if os.name == 'nt' else 'clear')

                elif opcao == 5:

                    ordenarNotas(descriptografar_arquivo("notas.txt"))
                    escreveNoLog("Ordenou otas", login_usuario)
                    wait = input("Pressione enter para continuar ->")
                    os.system('cls' if os.name == 'nt' else 'clear')


                elif opcao == 6:

                    acesso = False
                    escreveNoLog("Deslogou do sistema", login_usuario)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    

                elif opcao == 7:
                    acesso = False
                    sair = True
                    escreveNoLog("Encerrou o sistema", login_usuario)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    


            if nivel == "3":

                opcao = administrador()

                if opcao == 1:

                    notasAtu = cadastrarNota(descriptografar_arquivo("notas.txt"), descriptografar_arquivo("empresas.txt"))
                    criptografar_dicionario(notasAtu, "notas.txt")
                    escreveNoLog("Acesso ao cadastro de notas", login_usuario)
                    wait = input("Pressione enter para continuar ->")
                    os.system('cls' if os.name == 'nt' else 'clear')

                elif opcao == 2:

                    criptografar_dicionario(cadastrarEmpresa(descriptografar_arquivo("empresas.txt")), "empresas.txt")
                    escreveNoLog("Acesso ao cadastro de empresas", login_usuario)
                    wait = input("Pressione enter para continuar ->")
                    os.system('cls' if os.name == 'nt' else 'clear')

                elif opcao == 3:

                    buscarNota(descriptografar_arquivo("notas.txt"))
                    escreveNoLog("Acesso à busca de notas", login_usuario)
                    wait = input("Pressione enter para continuar ->")
                    os.system('cls' if os.name == 'nt' else 'clear')                    

                elif opcao == 4:
                    
                    criptografar_dicionario(
                        alterarNota(
                            descriptografar_arquivo("notas.txt"),
                            descriptografar_arquivo("empresas.txt")
                        ),
                        "notas.txt",
                    )
                    escreveNoLog("Acesso a alteração de notas", login_usuario)
                    wait = input("Pressione enter para continuar ->")
                    os.system('cls' if os.name == 'nt' else 'clear')

                elif opcao == 5:
                    
                    criptografar_dicionario(removerNota(descriptografar_arquivo("notas.txt")), "notas.txt")
                    escreveNoLog("Acesso a remoção de notas", login_usuario)
                    wait = input("Pressione enter para continuar ->")
                    os.system('cls' if os.name == 'nt' else 'clear')

                elif opcao == 7:

                    criptografar_dicionario(alterarUsuario(descriptografar_arquivo("usuarios.txt")), "usuarios.txt")
                    escreveNoLog("Acessou a alteração de nível de usuário", login_usuario)
                    wait = input("Pressione enter para continuar ->")
                    os.system('cls' if os.name == 'nt' else 'clear')

                elif opcao == 8:

                    ordenarNotas(descriptografar_arquivo("notas.txt"))
                    wait = input("Pressione enter para continuar ->")
                    os.system('cls' if os.name == 'nt' else 'clear')


                elif opcao == 9:

                    acesso = False
                    escreveNoLog("Deslogou do sistema", login_usuario)
                    os.system('cls' if os.name == 'nt' else 'clear')

                elif opcao == 10:

                    acesso = False
                    sair = True
                    escreveNoLog("Encerrou o sistema", login_usuario)
                    os.system('cls' if os.name == 'nt' else 'clear')
                elif opcao == 11:
                    lerLog("log.txt")
                    wait = input("Pressione enter para continuar ->")
                    escreveNoLog("Encerrou o sistema", login_usuario)
                    os.system('cls' if os.name == 'nt' else 'clear')

print("---------- Programa finalizado -----------")
wait = input("Pressione enter para continuar ->")
os.system('cls' if os.name == 'nt' else 'clear')
