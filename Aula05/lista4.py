n1 = [20,15,3,48,21]
n2 = [2,51,17,6,20]
p = 0
n3 = []
# a lista vai ser vazia pq o conteudo vai ser gerado aqui dentro

'''for i in n1:
    for j in n2 - 
    esta forma ta incorreta pq o for vai ir até o final de n2 para
    reutilizar novamnete a segunda posição do n2'''

# aqui o for esta pegando o valor que esta na posição 0 do n1 e jogando no i
for i in n1:
    el = i + n2[p]
    n3.append(el)
    p+=1

print(n1)
print(n2)
print(n3)


# p = n2 ta indicando no el

'''Explicando o cods
    n1 = [20,15,3,48,21]
    n2 = [2,51,17,6,20]
    p = 0
    n3 = [] - vazia posi 
    for i in n1:
      (20) 
              0        
    el  = i + n2[p] = 2
    n3.append(el)
'''