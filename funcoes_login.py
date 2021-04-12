"""

Arquivo destinado a funções de Login e acesso ao sistema

"""


def recuperar_chave(arquivo):
    """
    Essa função recupera a chave do arquivo(publico ou privada)
    """
    arq = open(arquivo, 'r')
    linha = arq.readline()
    info = linha.split(' ')
    arq.close()
    return int(info[0]), int(info[1])


def criptografar_string(string):
    """
    Essa função criptografa uma unica string
    """
    e, n = recuperar_chave("chavePublica.txt")
    codigo = ''
    for char in string:
        codigo += str((ord(char)**e)%n)+'@'
    return codigo


def decifrar_string(string):
    """
    Essa função descriptografa uma unica string
    """
    d, n = recuperar_chave("chavePrivada.txt")
    char = string.split('@')
    frase = ''
    for num in char:
        if not(num == '' or num == '\n'):
            frase += chr((int(num) ** d)%n)
    return frase


def criptografar_dicionario(dic, arq):
    """
    Essa função criptografa um dicionário e salva em um arquivo
    """
    e, n = recuperar_chave("chavePublica.txt")
    arquivo = open(arq, 'w')
    for chave in dic:
        arquivo.write(criptografar_string(chave))
        arquivo.write(' ')
        for item in dic[chave]:
            arquivo.write(criptografar_string(item))
            arquivo.write(' ')
        arquivo.write('\n')
    arquivo.close()

def descriptografar_arquivo(caminho):
    """
    Descriptografa um arquivo
    """
    texto = ler_arquivo(caminho)
    return descriptografar_dicionario(texto)

def ler_arquivo(caminho):
    with open(caminho, encoding='utf-8') as arquivo:
        return arquivo.read()

def descriptografar_dicionario(string):
    """
    Essa função recebe o arquivo como string e transforma a string num dicionário
    """
    dic = {}
    d, n = recuperar_chave("chavePrivada.txt")
    entradas = string.split('\n')
    for entrada in entradas:
        valores = entrada.split()
        valores_descriptografados = []
        for valor in valores:
            criptografados = valor.split('@')
            descriptografado = ''
            for criptografado in criptografados:
                if criptografado:
                    descriptografado += chr((int(criptografado) ** d)%n)
            valores_descriptografados.append(descriptografado)
        if valores_descriptografados:
            chave = valores_descriptografados.pop(0)
            dic[chave] = tuple(valores_descriptografados)
    return dic
            

def login(login, senha, dicionario):
    """
    Essa função permite o login, se o usuario estiver no dicionário
    """
    permissao = False
    contas = dicionario
    conta =  login
    if conta in contas:
        if (conta == login and contas[conta][1] == senha):
            permissao = True
            return permissao, dicionario[login][3]
        else:
            print("Senha inválida!")
            return permissao, "1"
    else:
        print("Login inválido!")
        return permissao, "1"

    

def cadastrar(dicionario):
    """
    Essa função cadastra o usuário no sistema
    """
    login = "admin"
    while(login in dicionario):
        login = input("Digite um login de sua preferência: ")
        senha = input("Digite sua senha: ")
        email = input("Digite seu Email: ")
        nivel = "1"
        if login in dicionario:
            print("Login já existente!")
            print("Digite novamente.")

    dicionario[login] = (login, senha, email, nivel)

    return dicionario
