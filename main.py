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

            if (len(str(ra)) == 5 and nome != "" and sala != "" and sexo in ['M', 'F']):
                est.setName(nome)
                est.setIdade(idade)
                est.setRa(ra)
                est.setPeriodo(periodo)
                est.setSala(sala)
                est.setSexo(sexo)
                est.setAv1(av1)
                est.setAv2(av2)
                est.setDataDeAniversario(dataDeAniversario)

                est.adicionarNovoEstudante(estudantes, est.getName(), est.getRa(), est.getIdade(), est.getPeriodo(), est.getSala(), est.mostrarSexo(), est.getDataDeAniversario(), est.getAv1(), est.getAv2())
            
            clear()
            opcoesDoPrograma()
            escolha = int(input("Opção: "))

        elif escolha == 2:

            ra_select = input("Insira o ra para buscar: ")
            
            for i in estudantes['ra']:
                if int(ra_select) == i:
                    ind = int(estudantes['ra'].index(i))
                    clear()
                    est.mostrarDados(ind, estudantes)
                    break
            else:
                print("Estudante não encontrado!\n")
            
            opcoesDoPrograma()
            escolha = int(input("Opção: "))

        elif escolha == 3:

            for ra in estudantes['ra']:
                ind = estudantes['ra'].index(ra)
                est.mostrarDados(ind, estudantes)
            
            print("\n")
            opcoesDoPrograma()
            escolha = int(input("Opção: "))
        
        elif escolha == 4:
            update_periodo = ''
            update_sala = ''

            clear()
            escolhaUpdate = int(input("O que deseja atualizar? (1) Periodo | (2) Sala:\n"))
            escolhaAluno = int(input("Insira o ra do aluno: "))
            index = estudantes['ra'].index(escolhaAluno)

            if escolhaUpdate == 1 and (escolhaAluno in estudantes['ra']):
                update_periodo = input(f"Insira o update para {estudantes['nome'][index]}: ")
                chave = "periodo"
            elif escolhaUpdate == 2 and (escolhaAluno in estudantes['ra']):
                update_sala = input(f"Insira o update para {estudantes['nome'][index]}: ")
                chave = "sala"

            if update_periodo in ['Manhã', 'Tarde', 'Noite']:
                est.updateDados(escolhaAluno, estudantes, update_periodo, chave)
            elif update_sala in ['Sala 01', 'Sala 02', 'Sala 03']:
                est.updateDados(escolhaAluno, estudantes, update_sala, chave)
            else:
                print("Ocorreu um erro na inserção dos dados\n---")

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