# Refatorar um código para usar POO e Classes

O projeto é que temos um programa que já funciona com pyautogui. A ideia é migrar tudo para POO.


Vamos precisar de :

pip install pyautogui

OBSERVAÇÃO 1: Este projeto foi feito no Windows, então tem coisas que não funciona no linux. Ele vai tentar acessar com botão direito para copiar o link,  não tem isto no linux no browser. Sugiro que rode no windows mesmo. 

OBSERVAÇÃO 2: as posições de search( pesquisa mudaram, então atualize)

https://www.hashtagtreinamentos.com/classes-no-python

# Instalação do JupyterLab no Linux Mint

Há duas formas principais de instalar:

---

## Opção 1: Via `pip` (mais leve, só o Jupyter)

```bash
# Atualizar o pip
pip install --upgrade pip

# Instalar o JupyterLab
pip install jupyterlab

# Rodar
jupyter lab
```

---

## Opção 2: Via Anaconda (recomendado para ciência de dados)

```bash
# 1. Baixar o instalador
wget https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-x86_64.sh

# 2. Rodar o instalador
bash Anaconda3-2024.10-1-Linux-x86_64.sh

# 3. Recarregar o terminal
source ~/.bashrc

# 4. Ativar o ambiente base
conda activate base

# 5. Rodar o JupyterLab
jupyter lab
```

---

## Opção 3: Via `apt` + `pip` (mais integrado ao sistema)

```bash
# Instalar Python e pip pelo apt
sudo apt update
sudo apt install python3 python3-pip -y

# Instalar o JupyterLab
pip3 install jupyterlab

# Rodar
jupyter lab
```

---

## Recomendação

| Objetivo | Opção recomendada |
|---|---|
| Ciência de dados (pandas, numpy, matplotlib) | **Anaconda** (Opção 2) |
| Instalação leve e rápida | **pip** (Opção 1) |
| Integração com o sistema Linux | **apt + pip** (Opção 3) |
# Instalação do JupyterLab no Linux Mint

Há duas formas principais de instalar:

---

## Opção 1: Via `pip` (mais leve, só o Jupyter)

```bash
# Atualizar o pip
pip install --upgrade pip

# Instalar o JupyterLab
pip install jupyterlab

# Rodar
jupyter lab
```

---

## Opção 2: Via Anaconda (recomendado para ciência de dados)

```bash
# 1. Baixar o instalador
wget https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-x86_64.sh

# 2. Rodar o instalador
bash Anaconda3-2024.10-1-Linux-x86_64.sh

# 3. Recarregar o terminal
source ~/.bashrc

# 4. Ativar o ambiente base
conda activate base

# 5. Rodar o JupyterLab
jupyter lab
```

---

## Opção 3: Via `apt` + `pip` (mais integrado ao sistema)

```bash
# Instalar Python e pip pelo apt
sudo apt update
sudo apt install python3 python3-pip -y

# Instalar o JupyterLab
pip3 install jupyterlab

# Rodar
jupyter lab
```

---

## Recomendação

| Objetivo | Opção recomendada |
|---|---|
| Ciência de dados (pandas, numpy, matplotlib) | **Anaconda** (Opção 2) |
| Instalação leve e rápida | **pip** (Opção 1) |
| Integração com o sistema Linux | **apt + pip** (Opção 3) |