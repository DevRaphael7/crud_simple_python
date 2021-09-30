from components.Funcoes import *
from classes.Classes import Estudante

estudante1 = Estudante("Raphael Ramalho", 19, 20343, "Norturno", "Sala 02", "M", "30/12/2001", 5.5, 7.0)
estudante2 = Estudante("William Shakespeare", 52, 10355, "Norturno", "Sala 01", "M", "23/04/1564", 10.0, 10.0)
estudante3 = Estudante("J.R.R.Tolkien", 19, 40123, "Matutino", "Sala 03", "M", "03/01/1892", 10.0, 10.0)
estudante4 = Estudante("Nathália", 17, 34212, "Matutino", "Sala 01", "F", "05/03/2004", 9.0, 8.0)

estudantes = {
    'ra' : [],
    'nome': [],
    'idade': [],
    'periodo' : [],
    'sala' : [],
    'sexo' : [],
    'nascimento' : [],
    'AV1': [],
    'AV2': []
}

adicionarNovoEstudante(estudantes, estudante1)
adicionarNovoEstudante(estudantes, estudante2)
adicionarNovoEstudante(estudantes, estudante3)
adicionarNovoEstudante(estudantes, estudante4)