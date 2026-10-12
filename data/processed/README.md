# data/processed/

Aqui ficam os dados depois da harmonização: nomes de colunas iguais nos 3 anos, variáveis recodificadas e os anos empilhados. Tudo é gerado pelo `notebooks/01_harmonizacao.ipynb`, então nada aqui é editado à mão.

## Os 4 arquivos

| Arquivo | Linhas × colunas | Uma linha é | Peso | Para que serve |
| --- | --- | --- | --- | --- |
| `dados_harmonizados.csv` | 66.976 × 33 | uma pessoa, com os dados da casa dela | `peso_amostral_individuo` | arquivo principal da EDA e dos testes |
| `individuos_harmonizado.csv` | 66.976 × 27 | uma pessoa entrevistada | `peso_amostral_individuo` | módulo indivíduos sozinho, com G1 e G2 completos |
| `domicilios_harmonizado.csv` | 75.008 × 9 | um domicílio | `peso_amostral_domicilio` | análises sobre casas (ex: % de domicílios com internet) |
| `individuos_pesos_replica.csv` | 66.976 × 204 | uma pessoa | o mesmo peso + `rep1` a `rep200` | erro padrão e Rao-Scott no notebook 03 (cerca de 170 MB) |

- `dados_harmonizados` junta indivíduos com domicílios por `chave_domicilio` + `ano`. Ele leva só o peso do indivíduo, de propósito, pra ninguém misturar os dois sistemas de peso.
- As réplicas ficam num arquivo separado porque deixavam os outros CSVs com mais de 90 MB. No notebook 03, o join com `dados_harmonizados` é por `chave_domicilio` + `ID_MORADOR` + `ano`.
- Qualquer análise com G1 ou G2 usa o peso do indivíduo e as réplicas do indivíduo, mesmo cruzando com renda ou região, porque a unidade de análise é a pessoa.

## O universo da análise: `usuario_internet`

- `usuario_internet` = 1 para quem tem 16 anos ou mais e usou a internet nos últimos 3 meses (pergunta C3). É a `F_C3_IDADE` da CETIC, o universo das tabelas oficiais do módulo G.
- Os arquivos guardam **todo mundo** (66.976 pessoas). Os notebooks 02 e 03 filtram `usuario_internet == 1` (45.436 pessoas: 13.859 em 2023, 14.686 em 2024 e 16.891 em 2025).
- Sem o filtro, o G1 e o G2 incluem umas mil pessoas por ano que disseram "não" na C3 e "sim" na J3 (internet no celular). Elas responderam o módulo G, mas ficam fora das tabelas oficiais, e com elas os nossos % não batem com os da CETIC.

## As réplicas de 2023

- No arquivo bruto de 2023, `rep1` a `rep200` não são pesos: são **contagens** do sorteio do bootstrap (inteiros de 0 a 5). O notebook 01 multiplica cada uma pelo `PESO` da pessoa, então em `individuos_pesos_replica.csv` as réplicas dos 3 anos já estão como peso.
- Em 2024 e 2025 a soma de cada réplica é igual à soma do peso do ano. Em 2023 fica entre 0,93 e 1,10 vezes a soma do peso, porque essas réplicas não foram calibradas como as de 2024 e 2025.

## Versionamento

Os 4 arquivos ficam fora do Git (regra `data/processed/**/*.csv` no `.gitignore`). Pra gerar de novo: colocar os 6 CSVs brutos em `data/raw/individuos/` e `data/raw/domicilios/` (ver `data/raw/README.md`) e rodar o notebook 01 inteiro.
