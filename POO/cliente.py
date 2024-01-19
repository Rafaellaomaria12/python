 #Declaração da clse Cliente. Esta classe permite
 #que sejam criados novos objetos do tipo cliente
class Cliente:
    #A implementação do método __init__ representa a construção
    # do método construtor da classe, reponsavel por inicializar
    #o objeto que será criado. Este método possui um argumento
    #self que faz referênciar a propria estrutura de classe a qual
    # ele pertence.
    # Note que no método __init__(contrutor) foram iniciados os
    #atributos classe, representando as caracteristicas do cliente
    #todos eles foram criados usando o comando self. que indica
    #que eles pertencem a classe Cliente. Os atributos foram
    #declarados como privados. Para isso utilizamos 2 undescores.
    ''''
    A classe Cliente gera novos clientes e pede  alguns
    dados pessoais e é capaz de salvar o cliente.
    '''
    def _init_(self):
     self.__nome = ""
     self.__idade = "0"
     self.__genero = ""
     self.__email = ""
   
    # O método dados é utilizado para realizar a passagem dos dados
    # do cliente para dentro da classe Cliente
    def dados(self,nome="",idade=0,genero="",email=""):
       """
    O método dados pede algumas informações do cliente para ele
    seja salvo no sistema.
       """
       self.__nome = nome
       self.idade = idade
       self.genero = genero
       self.email = email
    # O método gravar exibir uma mensagem com o do cliente
       # dizendo que foi salgo com sucesso
    def gravar(self):
     """
     O método gravar e exibir uma mensagem com o do cliente
     gravação realizada com sucesso.

     """
     
     print("O cliente "+self.__nome+" Foi gravado com sucesso")