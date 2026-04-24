from ContasBancos import ContaCorrente, CartaoCredito
from Agencia import AgenciaPremium, AgenciaComum, AgenciaVirtual

# programa
# conta_Gilberto = ContaCorrente("Gilberto", "111.222.333-45", 1234, 34062)
#
# cartao_Gilberto = CartaoCredito('Gilberto', conta_Gilberto)
#
#
# conta_Gilberto.nome = "João Gilberto"
# print(conta_Gilberto.nome)
#
#
# cartao_Gilberto.senha = '2345'
# print(cartao_Gilberto.senha)
#
# print(conta_Gilberto.__dict__)
# print(cartao_Gilberto.__dict__)
print('Agências : agencia_premium_especial')

agencia_premium_especial = AgenciaPremium(22221111, 15888888888888)
print(agencia_premium_especial.caixa)


