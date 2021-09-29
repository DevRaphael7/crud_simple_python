import random

def opcoesDoPrograma():
    print('1) Cadastrar estudante')
    print('2) Buscar estudante')
    print('3) Ver todos os estudantes')
    print('4) Atualizar estudante')
    print("5) Notas AV1 e AV2")
    print('6) Deletar estudante')
    print("7) Sair")

def mostrarDados(indice : int, dicionario : dict):
    print("\n=================================================")
    print(f"Nome: {dicionario['nome'][indice]}")
    print(f"RA: {dicionario['ra'][indice]}")
    print(f"Idade: {dicionario['idade'][indice]}")
    print(f"Periodo: {dicionario['periodo'][indice]}")
    print(f"Sala: {dicionario['sala'][indice]}")
    print(f"Sexo: {dicionario['sexo'][indice]}")
    print(f"Data de Nascimento: {dicionario['nascimento'][indice]}")
    # print(f"Nome: {dicionario['nome'][indice]}")
    # print(f"Nome: {dicionario['nome'][indice]}")
    # print(f"Nome: {dicionario['nome'][indice]}")
    print("=================================================")

def adicionarNovoEstudante(dicionario : dict, nome : str, ra : int, idade : int, periodo : str, sala : str, sexo : str, nascimento : str):
    
    ind = 0
    lista_dados = [ra, nome, idade, periodo, sala, sexo, nascimento]
    for i in dicionario:
        lista_add = dicionario[i]
        lista_add.append(lista_dados[ind])
        dicionario[i] = lista_add
        ind += 1
     

def sortearRA(ras : list):
    ra = random.randint(11111, 99999)
    while ra in ras:
        ra = random.randint(11111, 99999)

    return ra

def updateDados(ra : int, dicionario : dict, periodo : str, chave:str):
    
    index = dicionario['ra'].index(ra)

    lista_up = dicionario[chave]
    lista_up.insert(index, periodo)
    dicionario[chave] = lista_up

def verNotas(dicionario : dict):

    aux = 0
    for i in dicionario['nome']:
        aux += 1
    
    for i in range(0, aux):
        print(f"Nome: {dicionario['nome'][i]}")
        print(f"AV1: {dicionario['AV1'][i]}")
        print(f"AV2: {dicionario['AV2'][i]}")
        media = (dicionario['AV1'][i] + dicionario['AV2'][i]) / 2
        print(f"Média do aluno: {media}")

def updateNotas(dicionario : dict, ra : int, nota_av1 : int, nota_av2 : int):

    ind = dicionario['ra'].index(ra)

    lista_av1 = dicionario['AV1']
    lista_av2 = dicionario['AV2']

    lista_av1.insert(ind, nota_av1)
    lista_av2.insert(ind, nota_av2)

    print(f"Novas notas AV1 e AV2: {lista_av1[ind]} {lista_av2[ind]}")

    dicionario['AV1'] = lista_av1
    dicionario['AV2'] = lista_av2