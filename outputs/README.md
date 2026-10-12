# outputs/

Aqui ficam os resultados finais que saem dos notebooks 02 e 03: tabelas e gráficos prontos. O Power BI só lê esses arquivos, nenhuma estatística é recalculada lá.

## O que vai aparecer aqui

- Tabela de estimativas, em formato longo (uma linha por ano × área × dimensão × grupo): proporção ponderada com IC 95%, CV e n sem peso
- Tabela de testes, em formato longo (uma linha por ano × área × dimensão): F do Rao-Scott de 2ª ordem com os graus de liberdade, p-valor, p-valor ajustado, gap em p.p. com IC 95% e V de Cramér
- Ranking das 7 áreas do G2 (A a G) dentro de cada dimensão, pelo tamanho do efeito e não pelo p-valor
- Gráficos de pontos com IC por grupo e heatmap área × grupo, em `.png` ou `.svg`

## Saídas do notebook 02 (exploratórias)

- `tabelao_eda.csv`: uma linha por ano × área × dimensão × categoria (462 linhas), com n, resolveram, % sem peso, % com peso e n efetivo. Não tem margem de erro: serve pra explorar os dados, não como resultado final.
- `gap_renda_pct_com_peso.png` e `gap_renda_pct_sem_peso.png`: o gap da renda (mais de 10 SM menos até 1 SM) por área e ano, com e sem peso, na mesma escala.

## Observações

- Justiça (H) só existe em 2025, então fica fora do ranking principal e entra como análise à parte.
- Finanças vem da C8_H, que é outra pergunta (uso nos últimos 3 meses, outro universo), então também não entra no ranking do G2.
- Os CSVs saem com `sep=';'` e `decimal=','` pra o Power BI em português ler os números certo, e com `encoding='utf-8-sig'` pra o Excel abrir os acentos certo.
