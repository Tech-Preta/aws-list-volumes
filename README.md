# AWS Volume and Snapshot List

Este projeto lista todos os volumes e snapshots da AWS usando a biblioteca boto3 do Python.

## Pré-requisitos

- Python 3.6 ou superior
- Biblioteca boto3, pandas e openpyxl
- Credenciais da AWS configuradas (você pode configurá-las usando o comando `aws configure` do AWS CLI) ou exportando variáveis de ambiente `AWS_ACCESS_KEY_ID` e `AWS_SECRET_ACCESS_KEY`

## Como usar

1. Clone este repositório.
2. Instale as dependências com o comando `pip3 install -r requirements.txt`.
3. Execute o script com o comando `python3 main.py` para obter o resultado em um arquivo JSON e TXT. E  `python3 list.py` para obter o resultado em lista no terminal.

O script irá listar todos os volumes e snapshots da AWS, e armazenará a saída em um arquivo chamado `output.json`. Ele também criará um arquivo `output.txt`.

A saída inclui o ID, tamanho, tipo, zona de disponibilidade e estado de cada volume, e o ID, ID do volume, tamanho, estado e data de início de cada snapshot. Além disso, a saída inclui o total de volumes, o total de snapshots e o tamanho total em GB.
