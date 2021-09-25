import random

def opcoesDoPrograma():
    print('1) Cadastrar estudante')
    print('2) Buscar estudante')
    print('3) Atualizar estudante')
    print("4) Notas AV1 e AV2")
    print('4) Deletar estudante')


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

def sortearRA():
    ra = random.randint(11111, 99999)
    return ra
