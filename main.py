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
    chave = ""

    while(escolha != 7):
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
            
            ra = sortearRA(estudantes['ra'])

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

                adicionarNovoEstudante(estudantes, est.getName(), est.getRa(), est.getIdade(), est.getPeriodo(), est.getSala(), est.mostrarSexo(), est.getDataDeAniversario())
            
            clear()

            opcoesDoPrograma()
            escolha = int(input("Opção: "))

        elif escolha == 2:

            ra_select = input("Insira o ra para buscar: ")

            for i in estudantes['ra']:
                if int(ra_select) == i:
                    ind = int(estudantes['ra'].index(i))
                    clear()
                    mostrarDados(ind, estudantes)
                    break
            
            opcoesDoPrograma()
            escolha = int(input("Opção: "))

        elif escolha == 3:

            for ra in estudantes['ra']:
                ind = estudantes['ra'].index(ra)
                print(f"{ra}\t{estudantes['nome'][ind]}")
            
            print("\n")
            opcoesDoPrograma()
            escolha = int(input("Opção: "))
        
        elif escolha == 4:

            update_periodo = ''
            update_sala = ''

            clear()
            escolhaUpdate = int(input("O que deseja atualizar? (1) Periodo | (2) Sala:\n"))
            escolhaAluno = int(input("Insira o ra do aluno: "))

            if escolhaUpdate == 1:
                index = estudantes['ra'].index(escolhaAluno)
                update_periodo = input(f"Insira o update para {estudantes['nome'][index]}: ")
                chave = "periodo"
            elif escolhaUpdate == 2:
                index = estudantes['ra'].index(escolhaAluno)
                update_sala = input(f"Insira o update para {estudantes['nome'][index]}: ")
                chave = "sala"

            if update_periodo in ['Manhã', 'Tarde', 'Noite']:
                updateDados(escolhaAluno, estudantes, update_periodo, chave)
            elif update_sala in ['Sala 01', 'Sala 02', 'Sala 03']:
                updateDados(escolhaAluno, estudantes, update_sala, chave)

            print("\n")
            opcoesDoPrograma()
            escolha = int(input("Opção: "))
        elif escolha == 5:

            escolha_opcao = int(input("Escolha uma opção sobre as notas: (1) Ver notas || (2) Alterar notas || (3) Ver média de alunos\n"))

            if escolha_opcao == 1:

                verNotas(estudantes)
            
            elif escolha_opcao == 2:

                escolha_ra = int(input("Insira o RA do aluno que deseja alterar a nota: "))

                if escolha_ra in estudantes['ra']:
                    new_nota_av1 = int(input("Nota AV1: "))
                    new_nota_av2 = int(input("Nota AV2: "))

                    if new_nota_av1 >= 10.0 and new_nota_av2 >= 10.0:
                        updateNotas(estudantes, escolha_ra, new_nota_av1, new_nota_av2)
                    else:
                        print("Notas inválida")

                else:
                    print("RA não encontrado!")
            
            elif escolha_opcao == 3:

                escolha_ra = int(input("Insira o RA do aluno que deseja ver a média: "))
                
                if escolha_ra in estudantes['ra']:

                    ind = estudantes['ra'].index(escolha_ra)

                    av1_nota = estudantes['AV1'][ind]
                    av2_nota = estudantes['AV2'][ind]

                    media = ( av1_nota + av2_nota ) / 2

                    print(f"RA: {estudantes['ra'][ind]}")
                    print(f"Nome: {estudantes['nome'][ind]}")
                    print(f"Média: {media}")
                
                print("\n")
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