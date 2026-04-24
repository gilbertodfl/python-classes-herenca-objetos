from datetime import datetime
import pytz
from random import randint


class ContaCorrente:
    """
    Cria um objeto ContaCorrente para gerenciar as contas dos clientes.

    Attributos:
        nome (str): Nome do Cliente
        cpf (str): CPF do Cliente. Deve ser inserido com pontos e traços
        agencia: Agencia Responsável pela conta do Cliente
        num_conta: Número da Conta Corrente do Cliente
        saldo: Saldo disponível na conta do Cliente
        limite: Limite de Cheque especial daquele cliente
        transacoes: Histórico de Transações do Cliente
    """

    ## O @staticmethod é um decorador (decorator). Ele modifica o comportamento de uma função ou método.
    ## O @staticmethod especificamente diz ao Python que aquele método não precisa de self (não precisa de uma instância da classe para ser chamado).
    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        ## Quando um atributo tem um _ na frente, isso é uma convenção para dizer que aquele atributo é "protegido", ou seja, ele não deve ser acessado diretamente 
        # fora da classe, e sim através de métodos da classe.
        self._saldo = 0
        self._limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self._transacoes = []
        self.cartoes = []

    def consultar_saldo(self):
        print('Seu saldo atual é de R${:,.2f}'.format(self._saldo))

    def depositar(self, valor):
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))
    # Quando uma função começa com _, isso é uma convenção para dizer que aquela função é "protegida", ou seja, ela não deve ser chamada diretamente fora da classe, 
    # e sim através de métodos da classe. É como se fose uma função "privada" da classe, ou seja, ela é usada apenas dentro da classe, 
    # e não deve ser acessada diretamente fora da classe.
    def _limite_conta(self):
        self._limite = -1000
        return self._limite

    def sacar_dinheiro(self, valor):
        if self._saldo - valor < self._limite_conta():
            print('Você não tem saldo suficiente para sacar esse valor')
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))

    def consultar_limite_chequeespecial(self):
        print('Seu limite de Cheque Especial é de R${:,.2f}'.format(self._limite_conta()))

    def consultar_historico_transacoes(self):
        print('Histórico de Transações:')
        print('Valor, Saldo, Data e Hora')
        for transacao in self._transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((valor, conta_destino._saldo, ContaCorrente._data_hora()))


class CartaoCredito:

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR

    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        ## veja se somamos +4 anos no cartão para validade.
        self.validade = '{}/{}'.format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 4)
        self.cod_seguranca = '{}{}{}'.format(randint(0, 9), randint(0, 9), randint(0, 9))
        self.limite = 1000
        self._senha = '1234'
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)

    ## A forma de definirmos um método getter e setter em Python é usando o @property e o @nome_atributo.setter, 
    #  onde nome_atributo é o nome do atributo que queremos criar o getter e setter.
    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print("Nova Senha Inválida")

## esse main permite testar o código individualmente como se fosse um script, sem precisar importar a classe Agencia em outro arquivo, 
# ou seja, ele permite testar o código da classe Agencia sem precisar criar um arquivo separado para isso.
## É bom que fica documentado o uso. 
## Basta rodar no terminal ou executar run se for seu caso: python3 Agencia.py
if __name__ == '__main__':
    conta_Gilberto = ContaCorrente("Gilberto", "111.222.333-45", 1234, 34062)

    cartao_Gilberto = CartaoCredito('Gilberto', conta_Gilberto)


    conta_Gilberto.nome = "Lins Gilberto"
    print('dados da conta do Gilberto:')
    print(conta_Gilberto.nome)

    cartao_Gilberto.senha = '2345'
    print('senha de acesso do cartão de crédito do Gilberto:')
    print('Usando o get. A senha é :', cartao_Gilberto.senha)
    print('\n\nPode parecer confuso, mas veja que _senha está protegido e podemos usar conta_gilberto.senha para definir como também para recuperar a senha' )
    print('\nSe quiser os detalhes, use o __dict__ para mostrar os atributos do objeto, veja que o atributo _senha é protegido, ou seja, \nele não deve ser acessado diretamente fora da classe, e sim através de métodos da classe, mas usando o __dict__ podemos acessar o atributo protegido e ver seu valor.')
    
    print(cartao_Gilberto.__dict__)