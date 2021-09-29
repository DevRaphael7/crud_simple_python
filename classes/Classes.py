from random import randint

class Pessoa:
    def __init__(self, name : str, idade : int, sexo : str, dataDeAniversario : str):
        self.name = name 
        self.idade = idade
        self.sexo = sexo
        self.dataDeAniversario = dataDeAniversario

    def getName(self):
        return self.name
    
    def setName(self, nome : str):
        if not(nome == ""):
            self.name = nome
    
    def getIdade(self):
        return self.idade

    def setIdade(self, idade : int):
        if idade > 0:
            self.idade = idade
    
    def getSexo(self):
        return self.sexo
    
    def setSexo(self, sexo : str):
        if sexo in ['M', 'F']:
            self.sexo = sexo

    def getDataDeAniversario(self):
        return self.dataDeAniversario
    
    def setDataDeAniversario(self, dataDeAniversario : str):
        self.dataDeAniversario = dataDeAniversario
    
    def mostrarSexo(self):
        sex = 'Masculino' if self.sexo == 'M' else 'Feminino'
        return sex

class Estudante(Pessoa):

    def __init__(self, name : str, idade : int, ra : int, periodo : str, sala : str, sexo : str , dataDeAniversario : str, av1 : float, av2 : float):
        super().__init__(name, idade, sexo, dataDeAniversario)
        self.ra = ra
        self.periodo = periodo
        self.sala = sala
        self.av1 = av1
        self.av2 = av2
    
    def getRa(self):
        return self.ra
    
    def setRa(self, ra : int):
        a = str(ra)
        if len(a) >= 5:
            self.ra = ra
        else:
            self.ra = 0
    
    def getPeriodo(self):
        return self.periodo
    
    def setPeriodo(self, periodo : str):
        if periodo in ['Manhã', 'Tarde', 'Noite']:
            self.periodo = periodo
    
    def getSala(self):
        return self.sala 
    
    def setSala(self, sala : str):
        if sala in ['Sala 01', 'Sala 02', 'Sala 03']:
            self.sala = sala
    
    def setAv1(self, av1 : float):
        self.av1 = av1
    
    def getAv1(self):
        return self.av1

    def setAv2(self, av2 : float):
        self.av2 = av2
    
    def getAv2(self):
        return self.av2

    def adicionarNovoEstudante(self, dicionario : dict, nome : str, ra : int, idade : int, periodo : str, sala : str, sexo : str, nascimento : str, av1 : int, av2 : int):
        ind = 0
        lista_dados = [ra, nome, idade, periodo, sala, sexo, nascimento, av1, av2]
        for i in dicionario:
            lista_add = dicionario[i]
            lista_add.append(lista_dados[ind])
            dicionario[i] = lista_add
            ind += 1

    def sortearRA(self, ras : list, random : randint):
        ra = random.randint(11111, 99999)
        while ra in ras:
            ra = random.randint(11111, 99999)

        return ra

    def mostrarDados(self, indice : int, dicionario : dict):
        print("=================================================")
        print(f"Nome: {dicionario['nome'][indice]}")
        print(f"RA: {dicionario['ra'][indice]}")
        print(f"Idade: {dicionario['idade'][indice]}")
        print(f"Periodo: {dicionario['periodo'][indice]}")
        print(f"Sala: {dicionario['sala'][indice]}")
        print(f"Sexo: {dicionario['sexo'][indice]}")
        print(f"Data de Nascimento: {dicionario['nascimento'][indice]}")
        print("=================================================")
    
    def updateDados(self, ra : int, dicionario : dict, periodo : str, chave:str):
    
        index = dicionario['ra'].index(ra)

        lista_up = dicionario[chave]
        lista_up.insert(index, periodo)
        dicionario[chave] = lista_up
    
    def updatePeriodo(self, escolhaAluno : int, dicionario : dict, update_periodo : str, chave : str):

        if self.getPeriodo() in ['Manhã', 'Tarde', 'Noite']:
            self.updateDados(escolhaAluno, dicionario, update_periodo, chave)
        elif self.getSala() in ['Sala 01', 'Sala 02', 'Sala 03']:
            self.updateDados(escolhaAluno, dicionario, update_periodo, chave)
        else:
            print("Opção inválida!\n---")
    
    def verNotas(self, dicionario : dict, i : int):

        print(f"Nome: {dicionario['nome'][i]}")
        print(f"AV1: {dicionario['AV1'][i]}")
        print(f"AV2: {dicionario['AV2'][i]}")
        media = (dicionario['AV1'][i] + dicionario['AV2'][i]) / 2
        print(f"Média do aluno: {media}")
        print("-------------\n")
    
    def updateNotas(self, dicionario : dict, ra : int):

        if ra in dicionario['ra']:

                new_nota_av1 = float(input("Nota AV1: "))
                new_nota_av2 = float(input("Nota AV2: "))

                if new_nota_av1 >= 10.0 and new_nota_av2 >= 10.0:
                    ind = dicionario['ra'].index(ra)

                    lista_av1 = dicionario['AV1']
                    lista_av2 = dicionario['AV2']

                    lista_av1.insert(ind, new_nota_av1)
                    lista_av2.insert(ind, new_nota_av2)

                    print(f"Novas notas AV1 e AV2: {lista_av1[ind]} {lista_av2[ind]}")

                    dicionario['AV1'] = lista_av1
                    dicionario['AV2'] = lista_av2

                else:
                    print("Notas inválida")
        else:
            print("RA não encontrado!")

        

    def deletarEstudante(self, dicionario : dict, ra : int):

        ind = dicionario['ra'].index(ra)

        for i in dicionario.keys():
            lista_deletar = dicionario[i]
            lista_deletar.pop(ind)
            dicionario[i] = lista_deletar
