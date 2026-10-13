# outputs/

Aqui ficam os resultados que saem dos notebooks 02 e 03: tabelas e gráficos prontos. O Power BI só lê esses arquivos; nenhuma estatística é recalculada lá.

## Saídas do notebook 03 (resultados, com margem de erro)

Todas as tabelas usam só os usuários de Internet de 16 anos ou mais (o universo das tabelas da CETIC), as faixas da análise (renda em 5 e escolaridade em 3) e o fator das margens (decisão nº 9 do caderno: × 1,054 em 2023 e 2024 e × 1,140 em 2025).

### O G2: resolveu tudo pela internet, entre quem tentou (a medida principal)

- `estimativas_ic.csv` (418 linhas): uma linha por ano × área × dimensão × categoria, com o Brasil inteiro na dimensão `total`.
    - `n`: pessoas que responderam o G2 da área
    - `pct`: % que resolveu tudo pela internet, entre quem tentou, com peso
    - `ep`, `ic_inf` e `ic_sup`: erro padrão e intervalo de confiança de 95%
    - `cv` e `aviso`: o `aviso` é True quando o CV passa de 30%, ou seja, número fraco (decisão nº 4)
- `gaps_ic.csv` (176 linhas): uma linha por ano × área × par fixo da decisão nº 3.
    - `gap`: % do grupo A menos % do grupo B, em pontos percentuais
    - `ep`, `ic_inf` e `ic_sup`: erro padrão e IC de 95% do gap, calculados réplica por réplica
    - `diferenca_real`: True quando o IC do gap não passa pelo zero
- `testes_rao_scott.csv` (88 linhas): uma linha por ano × área × dimensão. Na raça, os testes usam só branca, preta e parda.
    - `F`, `gl1` e `gl2`: o teste de Rao-Scott de 2ª ordem e os seus graus de liberdade
    - `p`: o p do Rao-Scott
    - `p_comum`: o p do qui-quadrado comum, sem o desenho da amostra, só pra comparar
    - `grupo_holm` e `p_holm`: o grupo da correção (cada ano, e a justiça à parte) e o p ajustado pelo Holm
    - `real_05` e `real_holm`: True quando o p fica abaixo de 0,05, antes e depois do Holm
    - `v_cramer`: o tamanho da diferença (0 = nenhuma, 1 = a maior possível)
    - `ranking`: o lugar da área naquele ano e dimensão, pelo V (1 = maior diferença). Vazio na justiça
    - Os números saem com 6 casas: um p de 0,000000 quer dizer "menor que 0,000001"

### O G1: tentou usar o serviço pela internet (sempre ao lado do G2, decisão nº 1)

As duas tabelas têm as mesmas colunas das tabelas do G2, então dá pra juntar uma com a outra no Power BI pelo `ano`, `area`, `dimensao` e `categoria` (ou `par`).

- `estimativas_g1_ic.csv` (418 linhas): o mesmo formato do `estimativas_ic.csv`.
    - `n`: todos os usuários de Internet do grupo (tentou ou não)
    - `pct`: % que tentou (G1 = 1), com peso. O "não sabe / não respondeu" conta como "não", igual à CETIC, então a linha do Brasil é o número oficial
- `gaps_g1_ic.csv` (176 linhas): o mesmo formato do `gaps_ic.csv`, com o gap de quem tentou.
- O G1 não tem teste nem ranking: ele é contexto. Ele mistura quem não conseguiu usar a internet com quem nem precisou do serviço.
- Pra comparar o tamanho das diferenças entre o G1 e o G2, use o gap, e não o `diferenca_real`: o G1 usa todo mundo, então o IC dele é mais estreito e mais gaps dão "real".

### Finanças, à parte

Finanças está na pergunta de pesquisa, mas não tem G1 nem G2: vem da C8_H ("fez consultas, pagamentos ou outras transações financeiras" pela internet, nos últimos 3 meses). É uma medida de uso, como o G1 (que olha os últimos 12 meses, e não os últimos 3), então entra à parte, com IC e gaps, sem teste e sem ranking.

- `estimativas_financas_ic.csv` (57 linhas): o mesmo formato do `estimativas_g1_ic.csv`, com `area` = finanças (3 anos × 19 categorias).
    - `pct`: % que fez transações financeiras pela internet, entre todos os usuários de Internet do grupo. O "não sabe / não respondeu" conta como "não"
    - O número do Brasil é maior que o da tabela oficial (63,1% contra 57,5% em 2025) porque a CETIC conta os usuários de 10 anos ou mais, e o projeto usa os de 16 anos ou mais. No mesmo universo, os dois batem (diferença de no máximo 0,17 ponto)
- `gaps_financas_ic.csv` (24 linhas): o mesmo formato do `gaps_g1_ic.csv` (3 anos × 8 pares).

### Gráficos de conferência

As figuras do artigo e da apresentação saem do Power BI, a partir das tabelas acima. Os três gráficos do notebook 03 ficam como conferência: mostram o IC e o Holm, e servem pra checar se o painel mostra os mesmos números.

- `heatmap_v_cramer.png`: o V de Cramér do G2 por área (colunas) e dimensão e ano (linhas). Quanto mais escuro, maior a diferença; o `*` marca o que passou no Holm.
- `gaps_renda_escolaridade_ic.png`: os gaps do G2 de renda (mais de 5 SM menos até 1 SM) e de escolaridade (superior menos até fundamental), com IC, por área e ano. Ponto vazio: o IC passa pelo zero.
- `tentou_resolveu_2025.png`: o G1 e o G2 do Brasil em 2025, por área, com IC.

## Saídas do notebook 02 (exploratórias)

- `tabelao_eda.csv`: uma linha por ano × área × dimensão × categoria (462 linhas), com n, resolveram, % sem peso, % com peso e n efetivo. Desde 12/10, só com os usuários de Internet de 16 anos ou mais (`usuario_internet == 1`), o mesmo universo das tabelas oficiais da CETIC. Não tem margem de erro: serve pra explorar os dados, não como resultado final.
- `gap_renda_pct_com_peso.png` e `gap_renda_pct_sem_peso.png`: o gap da renda (mais de 10 SM menos até 1 SM) por área e ano, com e sem peso, na mesma escala.

## Observações

- Justiça (H) só existe em 2025, então fica fora do ranking principal e entra como análise à parte.
- Finanças vem da C8_H, que é outra pergunta (uso nos últimos 3 meses), então não entra no ranking do G2: fica à parte, nas tabelas de finanças.
- O tamanho (`v_cramer`) e a certeza (`real_holm`) são coisas diferentes: uma área pode ter o maior V e não passar no Holm (exemplo: polícia, por região, em 2024). Os gráficos e o texto mostram sempre os dois.
- Os CSVs saem com `sep=';'` e `decimal=','` pra o Power BI em português ler os números certo, e com `encoding='utf-8-sig'` pra o Excel abrir os acentos certo.
