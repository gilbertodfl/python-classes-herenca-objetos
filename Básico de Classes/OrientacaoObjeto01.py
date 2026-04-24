# Criando nossa 1ª Classe em Python
# Sempre que você quiser criar uma classe, você vai fazer:
#
# class Nome_Classe:
#
# Dentro da classe, você vai criar a "função" (método) __init__
# Esse método é quem define o que acontece quando você cria uma instância da Classe
#
# Vamos ver um exemplo para ficar mais claro, com o caso da Televisão que a gente vinha comentando

#classes
class TV:

    ## Toda classe tem um método chamado __init__, que é o método construtor da classe, ou seja, ele é o método que é chamado quando você cria uma instância da classe.
    # Ele é responsável por inicializar os atributos da classe, ou seja, definir os valores iniciais dos atributos da classe.
    def __init__(self):
        self.cor = 'preta'
        self.ligada = False
        self.tamanho = 55
        self.canal = "Netflix"
        self.volume = 10

    def mudar_canal(self):
        self.canal = "Disney+"



#programa
tv_sala = TV()
tv_quarto = TV()

## Observe que quando criamos a instância da classe TV, o método __init__ é chamado automaticamente, e os atributos da classe são inicializados com os valores definidos no método __init__
## veja que mudar o canal da tv_sala não muda o canal da tv_quarto, isso porque cada instância da classe TV tem seus próprios atributos, 
# ou seja, cada instância da classe TV tem seu próprio canal, volume, etc.
print('Antes de mudar o canal da tv_sala: assume o default do método __init__')
print(tv_sala.canal)
tv_sala.mudar_canal()
print('Depois de mudar o canal da tv_sala:')
print(tv_sala.canal)
print('\n\nO canal da tv_quarto continua o mesmo, pois cada instância da classe TV tem seus próprios atributos:')
print(tv_quarto.canal)

