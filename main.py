from classes.Classes import Estudante
from components.Funcoes import *
from Dados import *
import os

clear = lambda: os.system("cls")

if __name__ == '__main__':

    opcoesDoPrograma()
    escolha = int(input("Opção: "))

    clear()

    est = Estudante("", 0, 0, "", "", "", "")

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

        dataDeAniversario = input("Data de aniversário no formato dd/mm/yyyy: ")

        sexo = input("Seu sexo(M) ou (F): ")

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
        escolha_sala = int(input("Escolha uma das salas: "))

        if escolha_sala == 1:
            sala = "Sala 01"
        elif escolha_sala == 2:
            sala = "Sala 02"
        elif escolha_sala == 3:
            sala = "Sala 03"

        if (len(str(ra)) == 5 and nome != "" and sala != "" and sexo in ['M', 'F']):
            est.setName(nome)
            est.setIdade(idade)
            est.setRa(ra)
            est.setPeriodo(periodo)
            est.setSala(sala)
            est.setSexo(sexo)
            est.setDataDeAniversario(dataDeAniversario)
        
        clear()

            # mostrarInformacoes(est.getName(), est.getIdade(), est.getRa(), est.getPeriodo(), est.getSala(), est.mostrarSexo(), est.getDataDeAniversario())
    elif escolha == 2:

        ra_select = input("Insira o ra para buscar: ")

        for i in estudantes['ra']:
            if int(ra_select) == i:
                ind = int(estudantes['ra'].index(i))

                clear()
                
                mostrarDados(ind, estudantes)

                break
        

        