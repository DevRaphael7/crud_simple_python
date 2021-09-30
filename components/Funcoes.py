import random

def opcoesDoPrograma():
    print('1) Cadastrar estudante')
    print('2) Buscar estudante')
    print('3) Ver todos os estudantes')
    print('4) Atualizar estudante')
    print("5) Notas AV1 e AV2")
    print('6) Deletar estudante')
    print("7) Sair")

def adicionarNovoEstudante(dicionario : dict, object):
    ind = 0
    lista_dados = [object.getRa(), object.getName(), object.getIdade(), object.getPeriodo(), object.getSala(), object.getSexo(), object.getDataDeAniversario(), object.getAv1(), object.getAv2()]
    for i in dicionario:
        lista_add = dicionario[i]
        lista_add.append(lista_dados[ind])
        dicionario[i] = lista_add
        ind += 1

def mostrarDados(indice : int, dicionario : dict):
    print("=================================================")
    print(f"Nome: {dicionario['nome'][indice]}")
    print(f"RA: {dicionario['ra'][indice]}")
    print(f"Idade: {dicionario['idade'][indice]}")
    print(f"Periodo: {dicionario['periodo'][indice]}")
    print(f"Sala: {dicionario['sala'][indice]}")
    print(f"Sexo: {dicionario['sexo'][indice]}")
    print(f"Data de Nascimento: {dicionario['nascimento'][indice]}")
    print("=================================================")

def updatePeriodoOuSala(object , ra : int, dicionario : dict, update : str, chave : str):

    if object.getPeriodo() in ['Manhã', 'Tarde', 'Noite']:
        object.updateDados(ra, dicionario, update, chave)
    elif object.getSala() in ['Sala 01', 'Sala 02', 'Sala 03']:
        object.updateDados(ra, dicionario, update, chave)
    else:
        print("Opção inválida!\n---")