# Apartheid Digital? Uma Análise da Desigualdade no Uso Funcional da Internet no Brasil (2023-2025)

Projeto Integrador de Ciência de Dados, Fatec Rubens Lara

## Pergunta de pesquisa

> Existe diferença na capacidade de resolver, pela internet, serviços essenciais (documentos, saúde, educação, trabalho, impostos, segurança, transporte e finanças) entre diferentes grupos de renda, raça, escolaridade e região no Brasil — e em quais dessas dimensões a diferença é maior ou menor?

## Fonte de dados

Pesquisa TIC Domicílios (CETIC.br/NIC.br), módulos Domicílios e Indivíduos, anos 2023, 2024 e 2025.

## Estrutura do repositório

```
apartheid-digital/
├── data/
│   ├── raw/          → microdados originais, fora do Git (ver data/raw/README.md)
│   │   ├── individuos/
│   │   └── domicilios/
│   └── processed/    → dados harmonizados, gerados pelo notebook 01 (fora do Git)
├── notebooks/        → 01 harmonização, 02 análise exploratória, 03 testes estatísticos
├── src/              → funções Python reutilizáveis (harmonizacao.py)
├── docs/             → documentação, caderno de bordo, lista de variáveis e fontes da CETIC
├── outputs/          → tabelas e gráficos finais, que alimentam o Power BI
├── requirements.txt  → bibliotecas Python usadas
└── .gitignore
```

## Como rodar

1. Clonar o repositório
2. Baixar os microdados em https://www.cetic.br/microdados/ e colocar nas subpastas de `data/raw/`, com os nomes que o `data/raw/README.md` indica
3. Criar o ambiente virtual com Python 3.11 ou mais novo (o `svy` não roda em versões anteriores):
   - `python -m venv .venv`
   - Windows: `.venv\Scripts\activate` / Linux e Mac: `source .venv/bin/activate`
4. Instalar as dependências: `pip install -r requirements.txt`
5. Rodar os notebooks de `notebooks/` na ordem (01, 02, 03), sempre com Restart + Run All. O 01 gera os arquivos de `data/processed/` que os outros usam
