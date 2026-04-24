# Criando nossa 1ª Classe em Python

#
# Vamos ver de passagem de parâmetros para o método __init__, que é o método construtor da classe, ou seja, ele é o método que é chamado quando você cria uma instância da classe.
# Veja que introduzimos o default do parâmetro tamanho, ou seja, caso a pessoa que esteja criando a instância da classe não queira passar o valor do parâmetro, ela possa assumir um valor default definido no método __init__

#classes
class TV:

    def __init__(self, tamanho=32):  # 👈 valor default definido aqui
        self.cor = 'preta'
        self.ligada = False
        self.tamanho = tamanho
        self.canal = "Netflix"
        self.volume = 10

    def mudar_canal(self, novo_canal):
        self.canal = novo_canal


#programa
tv_sala = TV(55)
tv_quarto = TV(70)
## veja que não estou passando o parâmetro tamanho para a tv_cozinha, então ela vai assumir o valor default definido no método __init__, que é 32.
tv_cozinha = TV()
print('Exemplo de classe recebendo um parâmetro no método __init__ para definir o tamanho da TV:')
print('qual o tamanho da tv_sala?')
print(tv_sala.tamanho)
print('qual o tamanho da tv_quarto?')
print(tv_quarto.tamanho)
print('qual o tamanho da tv_cozinha? Assuma o default do método __init__, que é 32')
print(tv_cozinha.tamanho)
print('RESUMINDO: É boa prática colocar o valor default do parâmetro no método __init__, para que caso a pessoa que esteja criando a instância da classe não queira passar o valor do parâmetro, ela possa assumir um valor default definido no método __init__')
print('Caso não tenha o default, vai dar erro. Dependendo do caso pode ser interessante não ter.')
print('Este é um exemplo de atributo de instância, ou seja, cada instância da classe TV tem seu próprio tamanho, canal, volume, etc. Já o atributo de classe é aquele que é compartilhado por todas as instâncias da classe, ou seja, todas as TVs têm a mesma cor, que é preta.')