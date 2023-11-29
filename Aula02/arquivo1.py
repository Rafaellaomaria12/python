# importar a biblioteca os(sistema operacional)
import os

#limpar a tela
os.system("clear")

arqui = open("./texto.txt","w")
arqui.write("Hoje é quarta-feira\nultima semana de novembro")
arqui.close()