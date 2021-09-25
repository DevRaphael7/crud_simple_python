import random

def opcoesDoPrograma():
    print('1) Cadastrar estudante')
    print('2) Buscar estudante')
    print('3) Atualizar estudante')
    print('4) Deletar estudante')


def mostrarInformacoes(name : str, idade : int, ra : int, periodo : str, sala :str, sexo : str, date : str):
    print("\n")
    print(f'Nome: {name}\nIdade: {idade}\nRA: {ra}\nPeríodo: {periodo}\nSala: {sala}\nSexo: {sexo}\nData de nascimento: {date}')
    print("\n")


def sortearRA():
    ra = random.randint(11111, 99999)
    return ra
