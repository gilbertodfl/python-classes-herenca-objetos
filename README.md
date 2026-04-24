
# Estudo didático sobre Orientação à Objetos abordando Class, Inheritance, Polymorphism, Override

## Orientação a Objetos Completo - Classes e Métodos


Aqui é um resumo dos principais pontos da orientação objeto em python. 
Sei que existem mais coisas, mas aqui é um começo bom. 

Comece pela pasta Básico de Classes e à medida que for entendendo, use as demais. 
# Assista o video 
https://www.hashtagtreinamentos.com/classes-no-python


# como rodar no comando de linha

Para rodar no comando de linha execute por exemplo:

python3 OrientacaoObjeto01.py 

-->  saída

Disney+
Netflix

Observação: O Python já deve estar instalado.

# Classes em Python: Atributos e Parâmetros

Resumo dos conceitos aprendidos sobre classes, atributos de classe, atributos de instância e parâmetros com valor padrão.

---

## 1. Parâmetros com Valor Padrão no `__init__`

Quando um atributo precisa ser informado ao criar um objeto, mas nem sempre será fornecido, podemos definir um **valor padrão** diretamente na assinatura do método.

```python
class TV:
    def __init__(self, tamanho=32):  # 👈 valor padrão definido aqui
        self.tamanho = tamanho
```

**Comportamento:**
- Se o argumento **for informado** → usa o valor passado
- Se **não for informado** → usa o valor padrão

```python
tv_sala   = TV(55)  # tamanho = 55
tv_quarto = TV(70)  # tamanho = 70
tv_cozinha = TV()   # tamanho = 32 (padrão)
```

> Essa sintaxe funciona para qualquer método ou função em Python, não só no `__init__`.

---

## 2. Atributo de Classe vs. Atributo de Instância

### Atributo de Instância (dentro do `__init__`)

```python
class TV:
    def __init__(self, tamanho):
        self.tamanho = tamanho  # pertence a CADA objeto individualmente
```

- Definido com `self.atributo`
- Cada objeto tem o **seu próprio valor**
- Alterar em um objeto **não afeta** os outros

### Atributo de Classe (fora do `__init__`)

```python
class TV:
    cor = 'preta'  # pertence à CLASSE, compartilhado por todas as instâncias
```

- Definido diretamente no corpo da classe
- **Compartilhado** entre todas as instâncias
- Alterar via `TV.cor = 'branca'` afeta **todos os objetos**

---

## 3. Tabela Comparativa

| | Atributo de Classe | Atributo de Instância |
|---|---|---|
| Onde fica | Fora do `__init__` | Dentro do `__init__` com `self` |
| Pertence a | À classe toda | A cada objeto |
| Alteração afeta | Todos os objetos | Só aquele objeto |
| Uso ideal | Valores compartilhados / padrões de fábrica | Valores individuais |

---

## 4. Cuidado: Atribuição via Instância não Altera o Atributo de Classe

Este é um ponto de atenção importante. Ao fazer `objeto.atributo = valor`, o Python **não altera o atributo de classe**. Em vez disso, cria um **novo atributo de instância** que "sombreia" o da classe.

```python
class TV:
    cor = 'preta'  # atributo de CLASSE

tv_sala   = TV()
tv_quarto = TV()

tv_quarto.cor = 'azul'  # cria atributo de INSTÂNCIA em tv_quarto

print(tv_sala.cor)   # 'preta' → ainda lê o atributo de CLASSE
print(tv_quarto.cor) # 'azul'  → lê o atributo de INSTÂNCIA (sombreou o de classe)
```

### Como o Python busca um atributo (ordem de prioridade):

```
1º → atributo de INSTÂNCIA  (self.cor)
2º → atributo de CLASSE     (TV.cor)
```

### Para realmente alterar o atributo de classe:

```python
TV.cor = 'branca'  # altera a classe → afeta TODAS as instâncias

print(tv_sala.cor)   # 'branca'
print(tv_quarto.cor) # 'branca'
```

---

## 5. Caso de Uso: Contador de Instâncias

Um uso clássico de atributo de classe é **contar quantos objetos foram criados**:

```python
class TV:
    total_tvs = 0  # atributo de classe — compartilhado

    def __init__(self, tamanho=32):
        self.tamanho = tamanho
        TV.total_tvs += 1  # incrementa o contador da classe

TV(55)
TV(70)
TV(32)

print(TV.total_tvs)  # 3
```

---

## Resumo Rápido

```
objeto.atributo = valor   →  cria atributo de instância (só aquele objeto)
Classe.atributo = valor   →  altera atributo de classe (todos os objetos)
def __init__(self, p=10)  →  parâmetro com valor padrão
```
