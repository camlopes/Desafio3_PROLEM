
import sys
import csv


class CalculadoraCR(object):
    def __init__(self, nome_arquivo):
        self.leituraArquivo(nome_arquivo)

    def CalculoMediaCr(self, disciplinas, Crs, Cursos, indice):
        Cursos.sort()
        SomaCr = 0
        QuantidadeCr = 0
        Matricula = 0
        Curso = Cursos[indice]
        for item in range(len(disciplinas)):
            if Curso == int(disciplinas[item]["COD_CURSO"]) and Matricula != disciplinas[item]["MATRICULA"]:
                SomaCr += Crs[disciplinas[item]["MATRICULA"]]
                QuantidadeCr += 1
                Matricula = disciplinas[item]["MATRICULA"]  # Recebe a proxima matricula
        indice += 1
        # Print Cod_curso - media de cada curso:
        print(Curso, " - ", int(SomaCr/QuantidadeCr))
        if indice < len(Cursos):
            self.CalculoMediaCr(disciplinas, Crs, Cursos, indice)

    def CalculoCr(self, disciplinas):  # Média ponderada de Nota(i)*CargaHoraria(i) + ... /TotalCargaHoraria
        print("\n", "------- O CR dos alunos é: --------")
        Cursos = []  # Lista com os cursos sem repeticoes
        Crs = {}
        NotaXcargaHoraria = 0
        TotalcargaHoraria = 0
        Matricula = disciplinas[0]["MATRICULA"]
        for item in range(len(disciplinas)):
            if int(disciplinas[item]["COD_CURSO"]) not in Cursos:
                Cursos.append(int(disciplinas[item]["COD_CURSO"]))
            if Matricula == disciplinas[item]["MATRICULA"]:
                #  Somatório das multiplicações entre valores e pesos da média ponderada:
                NotaXcargaHoraria += int(disciplinas[item]["NOTA"]) * int(disciplinas[item]["CARGA_HORARIA"])
                #  Somatório dos pesos da média ponderada:
                TotalcargaHoraria += int(disciplinas[item]["CARGA_HORARIA"])
            else:
                # Print Matricula - cr dessa matricula:
                print(Matricula, " - ", int(NotaXcargaHoraria / TotalcargaHoraria))
                Crs[Matricula] = int(NotaXcargaHoraria / TotalcargaHoraria)
                Matricula = disciplinas[item]["MATRICULA"]
                NotaXcargaHoraria = 0
                TotalcargaHoraria = 0
        # Print a ultima Matricula - cr dessa matricula:
        print(Matricula, " - ", int(NotaXcargaHoraria / TotalcargaHoraria))
        Crs[Matricula] = int(NotaXcargaHoraria / TotalcargaHoraria)
        print("-----------------------------------")
        print("----- Média de CR dos cursos ------")
        self.CalculoMediaCr(disciplinas, Crs, Cursos, 0)

    def leituraArquivo(self, arquivo):  # Le um arquivo e guarda em uma lista seu conteudo
        with open(arquivo, "r") as arquivo_csv:
            CouteudoArquivo = []
            disciplinas = csv.DictReader(arquivo_csv, delimiter=",")
            for disciplina in disciplinas:
                CouteudoArquivo.append(disciplina)
        self.CalculoCr(CouteudoArquivo)


def main():
    print("Digite o local do arquivo: ")
    nome_arquivo = input() 
    CalculadoraCR(nome_arquivo)
    print("-----------------------------------")


if __name__ == '__main__':
    sys.exit(main())
