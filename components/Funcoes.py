import random

def mostrarInformacoes(name : str, idade : int, ra : int, periodo : str, sala :str):
    print("\n")
    print(f'Nome: {name}\nIdade: {idade}\nRA: {ra}\nPeríodo: {periodo}\nSala: {sala}')
    print("\n")

def sortearRA():
    ra = random.randint(11111, 99999)
    return ra
