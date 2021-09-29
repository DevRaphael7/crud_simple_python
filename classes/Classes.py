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

    def __init__(self, name : str, idade : int, ra : int, periodo : str, sala : str, sexo : str , dataDeAniversario : str):
        super().__init__(name, idade, sexo, dataDeAniversario)
        self.ra = ra
        self.periodo = periodo
        self.sala = sala
    
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
        self.sala = sala

    def deletarEstudante(self, dicionario : dict, ra : int):

        ind = dicionario['ra'].index(ra)

        for i in dicionario.keys():
            lista_deletar = dicionario[i]
            lista_deletar.pop(ind)
            dicionario[i] = lista_deletar
