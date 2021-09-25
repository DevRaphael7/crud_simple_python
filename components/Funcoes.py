import random

def opcoesDoPrograma():
    print('1) Cadastrar estudante')
    print('2) Buscar estudante')
    print('3) Ver todos os estudantes')
    print('3) Atualizar estudante')
    print("4) Notas AV1 e AV2")
    print('4) Deletar estudante')
    print("6) Sair")


# def mostrarInformacoes(name : str, idade : int, ra : int, periodo : str, sala :str, sexo : str, date : str):
#     print("\n")
#     print(f'Nome: {name}\nIdade: {idade}\nRA: {ra}\nPeríodo: {periodo}\nSala: {sala}\nSexo: {sexo}\nData de nascimento: {date}')
#     print("\n")

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
    lista_ra = dicionario['ra']
    lista_nome = dicionario['nome']
    lista_idade = dicionario['idade']
    lista_periodo = dicionario['periodo']
    lista_sala = dicionario['sala']
    lista_sexo = dicionario['sexo']
    lista_nascimento = dicionario['nascimento']

    lista_nome.append(nome)
    lista_ra.append(ra)
    lista_idade.append(idade)
    lista_periodo.append(periodo)
    lista_sala.append(sala)
    lista_sexo.append(sexo)
    lista_nascimento.append(nascimento)

    dicionario['ra'] = lista_ra
    dicionario['nome'] = lista_nome
    dicionario['idade'] = lista_idade
    dicionario['nascimento'] = lista_nascimento
    dicionario['sexo'] = lista_sexo
    dicionario['periodo'] = lista_periodo
    dicionario['sala'] = lista_sala
     

def sortearRA():
    ra = random.randint(11111, 99999)
    return ra
