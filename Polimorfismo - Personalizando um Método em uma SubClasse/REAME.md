# Polimorfismo em Python — Exemplo com Sistema Bancário

Este documento explica o conceito de **polimorfismo** usando o método `adicionar_cliente` como exemplo prático em um sistema de agências bancárias.

---

## O que é Polimorfismo?

Polimorfismo é um dos pilares da Programação Orientada a Objetos (POO). A palavra vem do grego e significa **"muitas formas"**. Em Python, polimorfismo permite que um mesmo método tenha **comportamentos diferentes** dependendo da classe que o implementa.

> Em termos simples: o mesmo nome de método, comportamentos distintos.

---

## Estrutura das Classes

```
Agencia (classe base)
├── AgenciaVirtual  (herda de Agencia)
├── AgenciaComum    (herda de Agencia)
└── AgenciaPremium  (herda de Agencia — SOBRESCREVE adicionar_cliente)
```

---

## O Método `adicionar_cliente`

### Na classe base — `Agencia`

```python
class Agencia:
    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))
```

Este é o comportamento **padrão**: qualquer cliente pode ser adicionado, sem restrições.

---

### Em `AgenciaComum` e `AgenciaVirtual`

Essas subclasses **não sobrescrevem** o método `adicionar_cliente`. Por isso, herdam diretamente o comportamento da classe base — qualquer cliente é aceito.

```python
agencia_comum.adicionar_cliente('Irmão do Gilberto', 10200000000, 10)
# ✅ Adicionado sem restrições, mesmo com patrimônio de R$ 10
```

---

### Em `AgenciaPremium` — o polimorfismo em ação

```python
class AgenciaPremium(Agencia):
    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            print('O Cliente foi adicionado na Agência Premium', self.cnpj)
            super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print('O Cliente não tem o patrimônio mínimo necessário para entrar na Agência Premium')
```

A `AgenciaPremium` **sobrescreve** o método para adicionar uma regra de negócio: só clientes com patrimônio acima de R$ 1.000.000 são aceitos.

O `super().adicionar_cliente(...)` chama o método da classe pai (`Agencia`) para reaproveitar a lógica de inserção na lista, evitando duplicação de código.

---

## Demonstração do Comportamento

```python
agencia_premium.adicionar_cliente('Gilberto', 15000000000, 50000000)
# ✅ Saída: O Cliente foi adicionado na Agência Premium 55500000000

agencia_premium.adicionar_cliente('Pobre', 15000000000, 1000)
# ❌ Saída: O Cliente não tem o patrimônio mínimo necessário para entrar na Agência Premium

agencia_comum.adicionar_cliente('Irmão do Gilberto', 10200000000, 10)
# ✅ Adicionado normalmente, sem restrição de patrimônio
```

---

## Por que isso é Polimorfismo?

| Classe           | Método `adicionar_cliente` | Comportamento                         |
|------------------|---------------------------|---------------------------------------|
| `Agencia`        | Definição original         | Adiciona qualquer cliente             |
| `AgenciaVirtual` | Herdado da base            | Adiciona qualquer cliente             |
| `AgenciaComum`   | Herdado da base            | Adiciona qualquer cliente             |
| `AgenciaPremium` | **Sobrescrito**            | Exige patrimônio > R$ 1.000.000       |

O mesmo nome de método (`adicionar_cliente`) produz **resultados diferentes** dependendo do tipo de agência. Isso é polimorfismo por **sobrescrita de método** (*method overriding*).

---

## Conceitos-chave utilizados

- **Herança** (`class AgenciaPremium(Agencia)`) — a subclasse herda atributos e métodos da classe pai.
- **Sobrescrita de método** (*override*) — a subclasse redefine um método da classe pai com novo comportamento.
- **`super()`** — permite chamar o método original da classe pai dentro da subclasse, reaproveitando a lógica existente.

---

## Resumo

O polimorfismo torna o código mais **flexível e extensível**. Neste exemplo, foi possível criar um tipo especializado de agência (`AgenciaPremium`) com regras próprias de admissão de clientes, sem alterar o comportamento das demais agências nem duplicar código — apenas sobrescrevendo o método onde necessário.