# Decoradores e Convenções em Python

Guia prático sobre `@staticmethod`, `@property` e o uso de `_` em atributos e métodos, ilustrado com a classe `CartaoCredito`.

---

## 1. `@staticmethod`

### Para que serve

Marca um método que **não depende da instância (`self`) nem da classe (`cls`)**. É uma função comum que mora dentro da classe apenas por organização e coesão semântica.

```python
class CartaoCredito:

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR
```

No exemplo acima, `_data_hora()` só consulta o horário do sistema — não precisa de nenhum dado do cartão. Por isso faz sentido ser `@staticmethod`.

### Como chamar

```python
# Pela classe (sem criar objeto)
CartaoCredito._data_hora()

# Pela instância (também funciona)
meu_cartao._data_hora()
```

### Cuidados

| ⚠️ Cuidado | Explicação |
|---|---|
| Não use `self` nem `cls` | O método não recebe nenhum dos dois. Tentar usá-los causará erro. |
| Não acesse atributos de instância | Se precisar de dados do objeto, use um método normal com `self`. |
| Não acesse atributos de classe | Se precisar de dados da classe, use `@classmethod` com `cls`. |
| Não abuse | Se a função não tem relação nenhuma com a classe, considere tirá-la de lá e torná-la uma função simples no módulo. |

---

## 2. `_` — Atributos e Métodos "Privados"

### Para que serve

O underscore `_` no início do nome é uma **convenção** que sinaliza: *"isto é de uso interno — não mexa diretamente por fora da classe"*.

```python
self._senha = '1234'    # atributo "privado"

@staticmethod
def _data_hora():       # método "privado"
    ...
```

### Python não impede o acesso

Diferente de outras linguagens como Java, Python **não bloqueia** o acesso a atributos com `_`. A convenção é apenas um aviso para outros desenvolvedores (e para você mesmo no futuro):

```python
# Funciona, mas vai contra a convenção — evite fazer isso:
print(meu_cartao._senha)
meu_cartao._senha = '9999'
```

### Variações

| Prefixo | Significado | Exemplo |
|---|---|---|
| `_nome` | Privado por convenção | `self._senha` |
| `__nome` | Privado de verdade (name mangling) — Python renomeia internamente | `self.__senha` |
| `nome_` | Use _ para evitar conflito com palavra reservada do Python | `type_`, `id_` |

```
## Exemplos de palavras reservadas: type, id, list, input, filter, class, for, if...
class Produto:
    def __init__(self, type_, id_):   # ✅ underscore no final evita o conflito
        self.type_ = type_
        self.id_ = id_
```
### Cuidados

| ⚠️ Cuidado | Explicação |
|---|---|
| `_` é só um aviso, não uma proteção | Qualquer código pode acessar — confie na convenção, não na restrição. |
| Não altere diretamente de fora da classe | Crie getters e setters com `@property` para controlar o acesso (veja seção 3). |
| `__` (dois underscores) é diferente | Ativa o *name mangling*: `self.__senha` vira `_CartaoCredito__senha` internamente, dificultando o acesso externo. Use com moderação. |

---

## 3. `@property` — Getter e Setter controlados

### Para que serve

Permite **controlar a leitura e escrita** de um atributo, adicionando validações ou lógica, mas mantendo a sintaxe simples de acesso (`objeto.atributo`).

```python
@property
def senha(self):          # GETTER — chamado ao ler  meu_cartao.senha
    return self._senha

@senha.setter
def senha(self, valor):   # SETTER — chamado ao fazer meu_cartao.senha = '...'
    if len(valor) == 4 and valor.isnumeric():
        self._senha = valor
    else:
        print("Nova Senha Inválida")
```

### Como usar

```python
meu_cartao = CartaoCredito(titular, conta)

# Leitura — chama o @property (getter)
print(meu_cartao.senha)       # '1234'

# Escrita — chama o @senha.setter
meu_cartao.senha = '4321'     # válido: 4 dígitos numéricos
meu_cartao.senha = 'abcd'     # inválido: imprime "Nova Senha Inválida"
meu_cartao.senha = '12'       # inválido: imprime "Nova Senha Inválida"
```

> Note que a chamada **não usa parênteses** — parece acesso a atributo normal, mas por baixo executa o método.

### Cuidados

| ⚠️ Cuidado | Explicação |
|---|---|
| O atributo interno deve ter `_` | Use `self._senha` internamente e exponha como `self.senha` via `@property`. Sem o `_`, ocorre recursão infinita. |
| `@setter` precisa do `@property` primeiro | O `@senha.setter` só funciona se `senha` já foi definida com `@property`. |
| Getter sem setter = somente leitura | Se você definir só o `@property` sem o `.setter`, qualquer tentativa de atribuição gerará `AttributeError`. Use isso intencionalmente quando quiser proteger o valor. |
| Não coloque lógica pesada no getter | O getter é chamado toda vez que o atributo é lido. Lógica custosa ali pode prejudicar a performance. |

---

## Resumo Visual

```
_senha          → atributo interno (convenção: não acesse diretamente de fora)
@staticmethod   → método que não usa self nem cls (utilitário da classe)
@property       → getter: leitura controlada do atributo
@senha.setter   → setter: escrita controlada com validação
```

---

