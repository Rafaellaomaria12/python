nota = input("Digite a nota do aluno: ")

nota = float(nota)

if nota >= 6:
    print("Aprovado")
elif nota <= 4:
    print("Reprovado")
else:
    print("Recuperação ")
 
    nt = input("Digite a nota do trabalho de recuperação: ")
    nt = float(nt)
    if nt > 6:
        print("Aprovado")
    else:
        print("Recuperação")