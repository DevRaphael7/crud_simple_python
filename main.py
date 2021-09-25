from classes.Classes import Estudante
from components.Funcoes import *

def opcoesDoPrograma():
    print('1) Cadastrar estudante')
    print('2) Buscar estudante')
    print('3) Atualizar estudante')
    print('4) Deletar estudante')

if __name__ == '__main__':

    opcoesDoPrograma()
    escolha = int(input("Opção: "))

    est = Estudante("", 0, 0, "", "")

    # Variáveis do programa
    nome  = ""
    idade = ""
    ra = 0
    periodo = ""
    sala = ""
    sexo = ""
    dataDeAniversario = ""

    if escolha == 1:

        nome = input("Digite o seu nome: ")
        idade = int(input("Digite a sua idade: "))

        print("(1)Manhã\t(2)Tarde\t(3)Noite")
        escolha_periodo = int(input("Escolha um período: "))

        if escolha_periodo == 1:
            periodo = "Manhã"
        elif periodo == 2:
            periodo = "Tarde"
        elif periodo == 3:
            periodo = "Noite"
        else:
            print("Valor inválido!")
        
        ra = sortearRA()

        print("(1)Sala 01\t(2)Sala 02\t(3)Sala 03")
        sala = input("Escolha uma das salas: ")


    
        if (len(str(ra)) == 5 and nome != "" and sala != ""):
            est.setName(nome)
            est.setIdade(idade)
            est.setRa(ra)
            est.setPeriodo(periodo)
            est.setSala(sala)

            mostrarInformacoes(est.getName(), est.getIdade(), est.getRa(), est.getPeriodo(), est.getSala())