# 
# Dentro da classe, você vai criar a "função" (método) __init__
# Esse método é quem define o que acontece quando você cria uma instância da Classe
#
# Todos terão a cor preta:
# Use quando o valor é igual para todos os objetos e faz sentido ser compartilhado:

# Um padrão de fábrica → cor = 'preta' (todas as TVs saem pretas de fábrica)
# Um contador de instâncias criadas
# Uma configuração global da classe

class TV:
    total_tvs = 0  # conta quantas TVs foram criadas

    def __init__(self, tamanho):
        self.tamanho = tamanho
        TV.total_tvs += 1
print(' Exemplo de atributo de classe para contar quantas TVs foram criadas:')
TV(55)
TV(70)
TV(32)
print(TV.total_tvs)  # 3