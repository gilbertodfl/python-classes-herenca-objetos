# 
# Dentro da classe, você vai criar a "função" (método) __init__
# Esse método é quem define o que acontece quando você cria uma instância da Classe
#
# Todos terão a cor preta:
# Use quando o valor é igual para todos os objetos e faz sentido ser compartilhado:

# Um padrão de fábrica → cor = 'preta' (todas as TVs saem pretas de fábrica)
# Um contador de instâncias criadas
# Uma configuração global da classe

#classes
class TV:
    cor = 'preta'  # atributo de classe

    def __init__(self, tamanho):
        self.tamanho = tamanho  # atributo de instância

tv_sala = TV(55)
tv_quarto = TV(70)

# Alterando o atributo de CLASSE muda para todas as TVs
TV.cor = 'branca'
print(tv_sala.cor)    # branca
print(tv_quarto.cor)  # branca

# Alterando o atributo de INSTÂNCIA muda só aquela TV
tv_sala.tamanho = 100
print(tv_sala.tamanho)    # 100
print(tv_quarto.tamanho)  # 70  ← não foi afetada
