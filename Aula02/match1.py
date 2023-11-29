dia = input ("Digite o número entre 1 e 7 e direi qual o dia da semana")

match dia:
    case'1':
        print("Domingo")
    case'2':
        print("Segunda")
    case'3':
        print("Terça-feira")
    case'4':
        print("Quarta-feira")
    case'5':
        print("Quinta-feira")
    case'6':
        print("Sexta-feira")
    case'7':
        print("Sábado")
    case _:
        print("Este dia da semana não existe ♥")