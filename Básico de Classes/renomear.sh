#!/bin/bash
# O conteúdo da imagem mostra nomes de arquivos .py numa lista. 
# Você quer um script bash que renomeie esses arquivos removendo o prefixo "Gabarito - " dos nomes.
for arquivo in "Gabarito - "*.py; do
    novo_nome="${arquivo/Gabarito - /}"
    mv "$arquivo" "$novo_nome"
    echo "Renomeado: '$arquivo' → '$novo_nome'"
done
