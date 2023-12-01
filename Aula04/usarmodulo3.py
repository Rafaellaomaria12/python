# Para importar apenas uma função dentro de
# um módulo, usamos o comando from para indicar
# o nome do módulo e o comando importa para
# usar apenas uma função. Você tambem pode
# aplicar um alias para função importada
from colecao import soma as s

n = [12,0,2,30,5]
print(s(n))
