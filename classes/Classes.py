class Pessoa:
    def __init__(self, name : str, idade : int):
        self.name = name 
        self.idade = idade

    def getName(self):
        return self.name
    
    def setName(self, nome : str):
        if not(self.name == ""):
            self.name = nome
    
    def getIdade(self):
        return self.idade

    def setIdade(self, idade : int):
        if idade > 0:
            self.idade = idade

class Estudante(Pessoa):

    def __init__(self, name : str, idade : int, ra : int, periodo : str, sala : str):
        super().__init__(name, idade)
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