from classe_dog import Dog
# Para criar o objeto, utilizamos a vriável doberman e realizamos o
# processo de instanciação da classe Dog.
# foi passado o nome e a idade.
doberman = Dog("Zeus",1)
#acessamos o método data_dog que mostra
# os dados do cachorros
doberman.data_dog()
doberman.sit()
doberman.roll_over()
print(doberman.__class__)
print(doberman.__dict__)