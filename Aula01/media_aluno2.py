# Se a nota for maior ou igual a 6 -> Aprovado
#Se a nota for menor ou igual a 4 -> Reprovado
#Se a nota for maior que 4 e menor que 6 -> Recuperação

bim1 = float (input("Digite a media do 1°bimestre do aluno: "))
bim2 = float (input("Digite a media do 2°bimestre do aluno: "))
bim3 = float (input("Digite a media do 3°bimestre do aluno: "))
bim4 = float (input("Digite a media do 4°bimestre do aluno: "))

media =(bim1 + bim2 + bim3 + bim4)/4

media = float(media)
if media >= 7:
        print("Aluno aprovado")
elif media <= 4:
    print("Aluno reprovado")
else:
    print("Aluno em recuperação")
