# data/processed/

Aqui ficam os dados depois da harmonização: nomes de colunas iguais nos 3 anos, variáveis recodificadas e os anos empilhados. Tudo é gerado pelo `notebooks/01_harmonizacao.ipynb`, então nada aqui é editado à mão.

## Os 4 arquivos

| Arquivo | Linhas × colunas | Uma linha é | Peso | Para que serve |
| --- | --- | --- | --- | --- |
| `dados_harmonizados.csv` | 66.976 × 32 | uma pessoa, com os dados da casa dela | `peso_amostral_individuo` | arquivo principal da EDA e dos testes |
| `individuos_harmonizado.csv` | 66.976 × 26 | uma pessoa entrevistada | `peso_amostral_individuo` | módulo indivíduos sozinho, com G1 e G2 completos |
| `domicilios_harmonizado.csv` | 75.008 × 9 | um domicílio | `peso_amostral_domicilio` | análises sobre casas (ex: % de domicílios com internet) |
| `individuos_pesos_replica.csv` | 66.976 × 204 | uma pessoa | o mesmo peso + `rep1` a `rep200` | erro padrão e Rao-Scott no notebook 03 (cerca de 133 MB) |

- `dados_harmonizados` junta indivíduos com domicílios por `chave_domicilio` + `ano`. Ele leva só o peso do indivíduo, de propósito, pra ninguém misturar os dois sistemas de peso.
- As réplicas ficam num arquivo separado porque deixavam os outros CSVs com mais de 90 MB. No notebook 03, o join com `dados_harmonizados` é por `chave_domicilio` + `ID_MORADOR` + `ano`.
- Qualquer análise com G1 ou G2 usa o peso do indivíduo e as réplicas do indivíduo, mesmo cruzando com renda ou região, porque a unidade de análise é a pessoa.

## Versionamento

Os 4 arquivos ficam fora do Git (regra `data/processed/**/*.csv` no `.gitignore`). Pra gerar de novo: colocar os 6 CSVs brutos em `data/raw/individuos/` e `data/raw/domicilios/` (ver `data/raw/README.md`) e rodar o notebook 01 inteiro.
