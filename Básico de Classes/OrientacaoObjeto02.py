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

    def __init__(self):
        self.cor = 'preta'
        self.ligada = False
        self.tamanho = 55
        self.canal = "Netflix"
        self.volume = 10

    def mudar_canal(self, novo_canal):
        self.canal = novo_canal


#programa
tv_sala = TV()
tv_quarto = TV()

## vamos mudar de canal.
tv_sala.mudar_canal("Globo")
tv_quarto.mudar_canal('Youtube')
print('O canal da tv_sala é:', tv_sala.canal)
print('O canal da tv_quarto é:', tv_quarto.canal)


