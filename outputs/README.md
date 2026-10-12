# outputs/

Aqui ficam os resultados que saem dos notebooks 02 e 03: tabelas e gráficos prontos. O Power BI só lê esses arquivos; nenhuma estatística é recalculada lá.

## Saídas do notebook 03 (resultados, com margem de erro)

As três tabelas usam só os usuários de Internet de 16 anos ou mais (o universo das tabelas da CETIC), as faixas da análise (renda em 5 e escolaridade em 3) e o fator das margens de 2024 e 2025 (decisão nº 9 do caderno).

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

## Saídas do notebook 02 (exploratórias)

- `tabelao_eda.csv`: uma linha por ano × área × dimensão × categoria (462 linhas), com n, resolveram, % sem peso, % com peso e n efetivo. Desde 12/10, só com os usuários de Internet de 16 anos ou mais (`usuario_internet == 1`), o mesmo universo das tabelas oficiais da CETIC. Não tem margem de erro: serve pra explorar os dados, não como resultado final.
- `gap_renda_pct_com_peso.png` e `gap_renda_pct_sem_peso.png`: o gap da renda (mais de 10 SM menos até 1 SM) por área e ano, com e sem peso, na mesma escala.

## O que ainda vai aparecer aqui

- Gráficos de pontos com IC por grupo e heatmap área × dimensão com o V de Cramér, em `.png`, para o artigo.

## Observações

- Justiça (H) só existe em 2025, então fica fora do ranking principal e entra como análise à parte.
- Finanças vem da C8_H, que é outra pergunta (uso nos últimos 3 meses, outro universo), então também não entra no ranking do G2.
- O tamanho (`v_cramer`) e a certeza (`real_holm`) são coisas diferentes: uma área pode ter o maior V e não passar no Holm (exemplo: polícia, por região, em 2024). Os gráficos e o texto mostram sempre os dois.
- Os CSVs saem com `sep=';'` e `decimal=','` pra o Power BI em português ler os números certo, e com `encoding='utf-8-sig'` pra o Excel abrir os acentos certo.
