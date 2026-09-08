# Apartheid Digital? Uma Análise da Desigualdade no Uso Funcional da Internet no Brasil (2023-2025)

Projeto Integrador — Ciência de Dados — Fatec Rubens Lara

## Pergunta de pesquisa

> Existe diferença na capacidade de resolver, pela internet, serviços essenciais (documentos, saúde, educação, trabalho, impostos, segurança, transporte e finanças) entre diferentes grupos de renda, raça, escolaridade e região no Brasil — e em quais dessas dimensões a diferença é maior ou menor?

## Fonte de dados

Pesquisa TIC Domicílios (CETIC.br/NIC.br), módulos Domicílios e Indivíduos, anos 2023, 2024 e 2025.

## Estrutura do repositório

```
apartheid-digital/
├── data/
│   ├── raw/          → dados originais (não versionados no Git, ver data/raw/README.md)
│   └── processed/    → dados harmonizados, gerados pelos notebooks
├── notebooks/        → harmonização, análise exploratória, testes estatísticos
├── src/              → funções Python reutilizáveis
├── docs/             → documentação completa do projeto e planejamento
├── outputs/          → gráficos e tabelas finais
├── requirements.txt  → bibliotecas Python usadas
└── .gitignore
```

## Como rodar

1. Clonar o repositório
2. Baixar os microdados originais em https://www.cetic.br/microdados/ e colocar em `data/raw/`
3. Instalar as dependências: `pip install -r requirements.txt`
4. Rodar os notebooks em `notebooks/`, na ordem numerada (01, 02, 03...)

