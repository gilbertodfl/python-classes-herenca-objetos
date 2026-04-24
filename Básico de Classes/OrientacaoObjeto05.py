# Criando nossa 1ª Classe em Python
# Sempre que você quiser criar uma classe, você vai fazer:
#
# class Nome_Classe:
#
## Quando vamos ler da instância e da classe, a ordem de busca é:
## 1. Atributo de INSTÂNCIA (se existir, é o que vai ser lido)
## 2. Atributo de CLASSE (se não existir o atributo de instância, ele vai ler o atributo de classe)
## 3. Se não existir o atributo de classe, vai dar erro 

#classes
class TV:

    cor = 'preta'

    def __init__(self, tamanho):
        self.ligada = False
        self.tamanho = tamanho
        self.canal = "Netflix"
        self.volume = 10
    def mudar_canal(self, novo_canal):
        self.canal = novo_canal


#programa
tv_sala = TV(55)
tv_quarto = TV(70)
print('Aqui vai mostrar a cor das TVs:')
print( 'tv_sala',tv_sala.cor)
print( 'tv_quarto',tv_quarto.cor)

print(tv_sala.tamanho)
print(tv_quarto.tamanho)

print(' Exemplo de atributo de classe para contar quantas TVs foram criadas:')
print( 'veja que a cor é um atributo de classe, ou seja, é compartilhado por todas as instâncias da classe TV, enquanto o tamanho é um atributo de instância, ou seja, cada instância da classe TV tem seu próprio tamanho.')
tv_quarto.cor = 'azul'  # cria um atributo de INSTÂNCIA em tv_quarto

print( 'tv_sala',tv_sala.cor) # 'preta' → ainda lê o atributo de CLASSE
print( 'tv_quarto',tv_quarto.cor) # 'azul'  → lê o atributo de INSTÂNCIA, que é criado só para tv_quarto, e não afeta as outras TVs


