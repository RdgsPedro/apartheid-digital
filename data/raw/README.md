# data/raw/

Aqui ficam os microdados originais da TIC Domicílios, do jeito que a CETIC disponibiliza. Os CSVs são grandes, então ficam fora do Git (regra no `.gitignore`) e cada pessoa do grupo baixa na própria máquina.

## Onde baixar

Em https://www.cetic.br/microdados/, pesquisa TIC Domicílios, anos 2023, 2024 e 2025. São 6 arquivos: um de domicílios e um de indivíduos por ano.

## Onde colocar e com que nome

O notebook 01 procura os arquivos exatamente com estes nomes, então vale renomear depois de baixar:

```
data/raw/
├── individuos/
│   ├── 2023_individuos.csv
│   ├── 2024_individuos.csv
│   └── 2025_individuos.csv
└── domicilios/
    ├── 2023_domicilios.csv
    ├── 2024_domicilios.csv
    └── 2025_domicilios.csv
```

## Cuidados

- Os arquivos usam separador `;` e decimal `,`, então a leitura é `pd.read_csv(caminho, sep=';', decimal=',')`. Sem o `decimal=','`, o `PESO` vira texto.
- Nada aqui é editado à mão. Toda limpeza e recodificação acontece no notebook 01.
- Os dicionários, questionários e relatórios metodológicos de cada ano estão em `docs/fontes_cetic/`.
