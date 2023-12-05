# Criação da classe Dog que dará origem
# a varios dogs(cachorros)
class Dog:
    # Criação da função __init__ que
    # é o responsável por inicializar
    # o objeto que será criado
    # Está sendo pedido o nome e a
    # idade do dog no momento em que ele
    # é criado.
    # Usamos o termo self para fazer uma referencia a propria classe
    # Portanto, quando criar o dog e passar o nome e a idade,
    # elas pertencerão a classe dog      
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def data_dog(self):
        print(self.name)
        print(self.age)
    
    def sit(self):
        print("sentou")

    def roll_over(self):
        print("Rolou")