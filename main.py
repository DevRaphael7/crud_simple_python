from classes.Classes import Estudante
from components.Funcoes import *
from Dados import *
import random
import os

clear = lambda: os.system("cls")

if __name__ == '__main__':

    opcoesDoPrograma()
    escolha = int(input("Opção: "))

    clear()

    est = Estudante("", 0, 0, "", "", "", "", 0, 0)

    # Variáveis do programa
    nome  = ""
    idade = ""
    ra = 0
    periodo = ""
    sala = ""
    sexo = ""
    dataDeAniversario = ""
    chave = ""

    while(escolha != 7):
        if escolha == 1:

            ra = est.sortearRA(estudantes['ra'], random)
            nome = input("Digite o seu nome: ")
            idade = int(input("Digite a sua idade: "))


            print("(1)Manhã\t(2)Tarde\t(3)Noite")
            escolha_periodo = int(input("Escolha um período: "))

            dataDeAniversario = input("Data de aniversário no formato dd/mm/yyyy: ")
            est.setDataDeAniversario(dataDeAniversario)

            sexo = input("Seu sexo(M) ou (F): ")

            if escolha_periodo == 1:
                periodo = "Manhã"
            elif periodo == 2:
                periodo = "Tarde"
            elif periodo == 3:
                periodo = "Noite"
            else:
                print("Valor inválido!")
            

            print("(1)Sala 01\t(2)Sala 02\t(3)Sala 03")
            escolha_sala = int(input("Escolha uma das salas: "))

            if escolha_sala == 1:
                sala = "Sala 01"
            elif escolha_sala == 2:
                sala = "Sala 02"
            elif escolha_sala == 3:
                sala = "Sala 03"
            
            av1 = float(input("AV1 do aluno: "))
            av2 = float(input("AV2 do aluno: "))

            if (len(str(ra)) == 5 and nome != "" and sala != "" and sexo in ['M', 'F'] and est.validarDataDeNascimento()):
                est.setName(nome)
                est.setIdade(idade)
                est.setRa(ra)
                est.setPeriodo(periodo)
                est.setSala(sala)
                est.setSexo(sexo)
                est.setAv1(av1)
                est.setAv2(av2)

                adicionarNovoEstudante(estudantes, est)
            
            clear()
            opcoesDoPrograma()
            escolha = int(input("Opção: "))

        elif escolha == 2:

            est.setRa(input("Insira o ra para buscar: "))
            
            
            if int(est.getRa()) in estudantes['ra']:
                ind = int(estudantes['ra'].index(int(est.getRa())))
                clear()
                mostrarDados(ind, estudantes)
            
            
            opcoesDoPrograma()
            escolha = int(input("Opção: "))

        elif escolha == 3:

            for ra in estudantes['ra']:
                ind = estudantes['ra'].index(ra)
                mostrarDados(ind, estudantes)
            
            print("\n")
            opcoesDoPrograma()
            escolha = int(input("Opção: "))
        
        elif escolha == 4:
            clear()
            escolhaUpdate = int(input("O que deseja atualizar? (1) Periodo | (2) Sala:\n"))
            escolhaAluno = int(input("Insira o ra do aluno: "))
            index = estudantes['ra'].index(escolhaAluno)

            if escolhaUpdate == 1:

                est.setPeriodo(input(f"Insira o update para {estudantes['nome'][index]}: "))
                updatePeriodoOuSala(est, escolhaAluno, estudantes, est.getPeriodo(), "periodo")

            elif escolhaUpdate == 2:

                est.setSala(input(f"Insira o update para {estudantes['nome'][index]}: "))
                updatePeriodoOuSala(est, escolhaAluno, estudantes, est.getSala(), "sala")

            opcoesDoPrograma()
            escolha = int(input("Opção: "))

        elif escolha == 5:

            escolha_opcao = int(input("Escolha uma opção sobre as notas: (1) Ver notas || (2) Alterar notas || (3) Ver média de alunos\n"))

            if escolha_opcao == 1:

                aux = 0
                for i in estudantes['nome']:
                    aux += 1
        
                for i in range(0, aux):
                    est.verNotas(estudantes, i)
            
            elif escolha_opcao == 2:

                escolha_ra = int(input("Insira o RA do aluno que deseja alterar a nota: "))

                # Função para atualizar nota AV1 e AV2
                est.updateNotas(estudantes, escolha_ra)
            
            elif escolha_opcao == 3:

                escolha_ra = int(input("Insira o RA do aluno que deseja ver a média: "))
                print("\n")

                if escolha_ra in estudantes['ra']:
                    ind = estudantes['ra'].index(escolha_ra)
                    est.verNotas(estudantes, ind)

                opcoesDoPrograma()
                escolha = int(input("Opção: "))

        elif escolha == 6:

            clear()
            ra = int(input("Digite o RA do estudante que você quer deletar: "))
            if ra in estudantes['ra']:
                est.deletarEstudante(estudantes, ra)
                print("Operação realizada com sucesso!")
            else:
                print("RA não encontrado!")
            print("\n")
            opcoesDoPrograma()
            escolha = int(input("Opção: "))

        elif escolha == 7:
            break