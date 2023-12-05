n1 = [7,17,27,37,47,57,67,77]
n2 = [52,63,7,25,17,69,27,31,29,41]
n3 = []

for i in n1:
    for j in n2:
        if i == j:
            # print(i)
            n3.append(i)
print(n3)

# aqui estamos usando o comando que estava incorreto no cod passado:
# for i in n1:
    # for j in n2:
        # if i == j:
# for no J vai listar tds os numeros da n2 e SE i = j ele será mosrado na tela