from random import randint

def formatar_brl(valor):
    """Formata um valor numérico para o padrão monetário brasileiro. Ex: 1.000.000,00"""
    return f'R$ {valor:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')

## Veja que agencia não herda nada de ninguém.
class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        ## uma agência tem uma lista de clientes 
        self.clientes = []
        self.caixa = 0
        ## uma agência tem uma lista de empréstimos, onde cada empréstimo é representado por uma tupla com o valor do empréstimo,
        # o cpf do cliente que fez o empréstimo, e a taxa de juros do empréstimo.
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print(f'Caixa abaixo do nível recomendado. Caixa Atual: {formatar_brl(self.caixa)}')
        else:
            print(f'O Valor de Caixa está ok. Caixa Atual: {formatar_brl(self.caixa)}')

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
            print(f'Empréstimo de {formatar_brl(valor)} realizado para o CPF {cpf} com juros de {juros:.2f}%.')
        else:
            print('Empréstimo não é possível. Dinheiro não disponível em caixa.')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))

# Veja que as outras classes herdam da classe Agencia, ou seja, elas são subclasses da classe Agencia, 
# e a classe Agencia é a superclasse das classes AgenciaVirtual, AgenciaComum e AgenciaPremium. 
# Ou seja, as classes AgenciaVirtual, AgenciaComum e AgenciaPremium são especializações da classe Agencia, 
# ou seja, elas são tipos específicos de Agência, com características e comportamentos específicos.
class AgenciaVirtual(Agencia):

    # A agencia virtual tem a propriedade site, e tem os métodos depositar_paypal e sacar_paypal, que são específicos da agência virtual, 
    # ou seja, eles não fazem sentido para as outras agências, então eles são definidos apenas na classe AgenciaVirtual.
    def __init__(self, site, telefone, cnpj):
        self.site = site
        ## Quando usamos o __init__ da superclasse, estamos dizendo que queremos usar o método __init__ da classe Agencia para inicializar 
        # os atributos telefone, cnpj e numero, e depois disso, podemos adicionar os atributos específicos da classe AgenciaVirtual, que são caixa e caixa_paypal.
        ## Dessa forma temos tudo do pai e mais o peculiar da Virtual neste caso.
        super().__init__(telefone, cnpj, 1000)
        self.caixa = 1000000
        self.caixa_paypal = 0

    ## Uma agência comum não tem os métodos depositar_paypal e sacar_paypal, pois eles são específicos da agência virtual,
    #  ou seja, eles não fazem sentido para as outras agências, então eles são definidos apenas na classe AgenciaVirtual.
    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor
        print(f'Depósito PayPal de {formatar_brl(valor)} realizado.')

    def sacar_paypal(self, valor):
        self.caixa_paypal -= valor
        self.caixa += valor
        print(f'Saque PayPal de {formatar_brl(valor)} realizado.')


class AgenciaComum(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 1000000


class AgenciaPremium(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 10000000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            ## Observe que adiciono patrimonio, embora não seja um parâmetro da classe pai.
            ## é possível porque é uma lista de tuplas.
            super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print('O Cliente não tem o patrimônio mínimo necessário para entrar na Agência Premium')


## esse main permite testar o código individualmente como se fosse um script, sem precisar importar a classe Agencia em outro arquivo, 
# ou seja, ele permite testar o código da classe Agencia sem precisar criar um arquivo separado para isso.
## É bom que fica documentado o uso. 
## Basta rodar no terminal ou executar run se for seu caso: python3 Agencia.py
if __name__ == '__main__':
    agencia1 = Agencia(22223333, 2000000000, 4568)

    agencia_virtual = AgenciaVirtual('www.agenciavirtual.com.br', 22224444, 15200000000)
    agencia_virtual.verificar_caixa()

    agencia_comum = AgenciaComum(22225555, 25500000000)
    agencia_premium = AgenciaPremium(22226666, 55500000000)

    agencia_virtual.depositar_paypal(20000)
    print(f'Caixa: {formatar_brl(agencia_virtual.caixa)}')
    print(f'Caixa PayPal: {formatar_brl(agencia_virtual.caixa_paypal)}')

    agencia_premium.adicionar_cliente('Gilberto', 15000000000, 50000000)
    print('\nClientes Agência Premium:')
    for nome, cpf, patrimonio in agencia_premium.clientes:
        print(f'  Cliente: {nome} | CPF: {cpf} | Patrimônio: {formatar_brl(patrimonio)}')

    agencia_comum.adicionar_cliente('Filho do Gilberto', 10200000000, 10)
    print('\nClientes Agência Comum:')
    for nome, cpf, patrimonio in agencia_comum.clientes:
        print(f'  Cliente: {nome} | CPF: {cpf} | Patrimônio: {formatar_brl(patrimonio)}')