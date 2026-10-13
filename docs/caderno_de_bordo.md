# Caderno de Bordo
### Projeto Integrador: Apartheid Digital? (Ciência de Dados, Fatec Rubens Lara, 2º semestre)

**Grupo:** Pedro Rodrigues Almeida, Vitor Alexandre dos Santos Silva e Eduardo Pedro Nogueira

> Registro das etapas e decisões do projeto, da mais antiga pra mais recente. As datas exatas vêm do histórico do Git. As que aparecem como "até tal data" foram reconstruídas pelas anotações do grupo e só dizem o limite: a etapa aconteceu naquele dia ou antes. Vale o grupo conferir e completar.

---

## Decisões em vigor

A coluna Nº é o número que os notebooks e o `outputs/README.md` usam pra citar as decisões de 12/10 (por exemplo, "decisão nº 9").

| Nº | Tema | Decisão | Desde |
| --- | --- | --- | --- |
|  | Base de dados | Microdados da TIC Domicílios (CETIC.br/NIC.br), módulos domicílios e indivíduos | até 24/08 |
|  | Recorte | 2023, 2024 e 2025 (opção 2 da professora: últimos 3 anos com mais variáveis) | até 24/08 |
|  | Variável central | G2_X (fez o serviço inteiro pela internet), com o G1_X (tentou) como par de cada área | até 24/08 |
| 8 | Universo da análise | G1 e G2 só entre usuários de Internet de 16 anos ou mais (`usuario_internet` = 1, a `F_C3_IDADE` da CETIC), o mesmo universo das tabelas oficiais | 12/10 |
|  | Áreas do ranking | 7 áreas, de A a G. Justiça (H) só existe em 2025 e entra à parte. Finanças vem da C8_H, outra pergunta: fica fora do ranking e entra à parte, como o G1 (com IC e gaps, sem teste e sem ranking) | 21/09 (H), 03/10 (finanças fora do ranking) e 12/10 (finanças à parte) |
|  | Religião | `RELIGIAO` não é usada | até 24/08 |
|  | G2 em 0/1 | 1 = fez tudo online; 2 (precisou ir ao posto) e 3 (só procurou informação) = 0; 97/98/99 = NaN | 07/09 |
|  | Peso | Qualquer conta com G1 ou G2 usa o peso do indivíduo e as réplicas do indivíduo, mesmo cruzando com renda ou região | 21/09 |
|  | Réplicas | 200 réplicas bootstrap do indivíduo, num arquivo separado e fora do Git. No arquivo bruto de 2023 elas vêm como contagens do sorteio, e o notebook 01 multiplica cada uma pelo `PESO` | 21/09 (contagens de 2023: 12/10) |
| 9 | Margem de erro | EP = desvio padrão das 200 réplicas; margem = 1,96 × EP. A margem é multiplicada pelo fator que reproduz as margens oficiais: 1,054 em 2024 e 1,140 em 2025, iguais em todos os grupos, e 1,054 em 2023, em que a CETIC usou outro método e a margem oficial é a nossa × 1,054 em média | 12/10 (2023: 13/10) |
|  | Nível de significância | α = 0,05, fixado antes de qualquer teste | 07/09 |
|  | Teste | Rao-Scott de 2ª ordem, e não um qui-quadrado simples. Feito pelo `svy`, conferido contra a fórmula do `svychisq` do pacote `survey` do R, refeita em Python (resultado idêntico nos 88 testes) | 07/09 (conferência: 12/10) |
|  | Ferramenta | `svy` (Python), fixo na versão 0.31.0; o pacote `survey` do R fica de plano B | até 02/10 (versão fixada em 10/10) |
|  | Códigos 97/98/99 | Viram NaN, com duas exceções: velocidade e valor da conexão (linhas abaixo) | 21/09 e 10/10 |
|  | Renda | 97 e 98 viram NaN; o 7 ("não tem renda") fica como código próprio nos dados (na análise ele entra junto com "até 1 SM", ver "Faixas na análise") | 10/10 |
|  | Velocidade | 5 categorias usando o tipo de conexão (A7): `baixa`, `media`, `alta`, `movel` e `sem internet`; discada e não sabe viram NaN | 10/10 (substitui a regra de 21/09) |
|  | Valor da conexão | 97/98/99 viram NaN; "não paga nada" vira o código 0 nos 3 anos | 10/10 |
|  | Fontes do artigo | Só autores de pós-graduação em diante; estado da arte com textos de 2021 em diante | 02/10 |
| 1 | Medida principal | G2 entre quem tentou (G1 = 1) como medida principal, sempre com o G1 ao lado | 12/10 |
| 2 | Faixas na análise | Renda em 5 faixas: até 1 SM (junto com o 7, "não tem renda"), 1 a 2, 2 a 3, 3 a 5 e mais de 5 SM. Escolaridade em 3: até fundamental (junto com analfabeto/infantil), médio e superior | 12/10 |
| 3 | Grupos do gap | Sempre grupos fixos, nunca "maior − menor". Renda: até 1 SM × mais de 5 SM. Escolaridade: até fundamental × superior. Raça: branca × preta e branca × parda. Região: Sudeste × cada uma das outras quatro | 12/10 |
| 4 | Grupos pequenos | Toda estimativa sai com IC, e com aviso quando o CV passa de 30%. Nos testes, as categorias são as mesmas em todas as áreas e anos; amarela e indígena ficam fora dos testes (aparecem à parte, com IC e aviso) e nunca são juntadas a outro grupo | 12/10 |
| 5 | Correção dos p-valores | Holm, por ano: 28 testes (7 áreas × 4 dimensões); justiça à parte | 12/10 |
| 6 | Ano a ano ou empilhado | Ano a ano como principal; os 3 anos empilhados como complemento | 12/10 |
| 7 | Bases complementares | OuvidoriaSUS e Fala.BR ficam como trabalho futuro: não estão na pergunta de pesquisa e são outro tipo de dado (registros de atendimento, e não uma pesquisa por amostra) | 12/10 |
|  | Camada extra (qualidade do acesso) | Velocidade e valor da conexão ficam como trabalho futuro (muda a ideia de 24/08): cerca de 1 em cada 3 usuários fica sem a velocidade (de 27,6% a 32,7% de vazio), e elas não estão na pergunta de pesquisa. O notebook 01 continua preparando as duas | 12/10 |
|  | Figuras | As figuras do artigo e da apresentação saem do Power BI, a partir das tabelas de `outputs/`. Os gráficos do notebook 03 ficam como conferência | 12/10 |

## Decisões em aberto

Nenhuma. As decisões 1 a 6 que estavam aqui (medida principal, "não tem renda", grupos do gap, grupos pequenos, correção dos p-valores e ano a ano) foram fechadas em 12/10 e estão na tabela acima, junto com as duas de 12/10 à tarde (o universo e a margem de erro, nº 8 e 9). O grupo todo (Pedro, Vitor e Eduardo) confirmou essas decisões em 12/10. A última que sobrava, as bases complementares (OuvidoriaSUS e Fala.BR), virou trabalho futuro em 12/10 (nº 7). Em 13/10, a nº 9 foi revista pra 2023 (ver a entrada de 13/10).

---

## Linha do tempo

### Até 24/08/2026: definição do projeto

- **Base:** o grupo escolheu os microdados da TIC Domicílios e baixou as bases de domicílios e indivíduos de 2016 a 2025, com os dicionários, pensando numa série histórica.
- **Pergunta em aberto:** a professora pediu que a pergunta de pesquisa não supusesse a resposta de antemão.
- **Recorte:** a professora deu duas opções: (1) antes e depois da pandemia, sem 2020, ou (2) os últimos 3 anos com mais variáveis. O grupo ficou com a opção 2 (2023, 2024 e 2025), porque a bateria G2 existe completa nesses 3 anos, sem buracos.
- **Variável central:** o G2 (resolveu o serviço sem ir até um posto). Cada G2_X tem o par G1_X, que mede se a pessoa tentou. A ideia inicial era usar a C8 como "tentativa", mas o par certo é o G1.
- **Camada extra:** entram as variáveis de qualidade de acesso do módulo domicílios (tipo de conexão, velocidade, valor pago, computador, motivo de não ter internet).
- **Religião:** a variável `RELIGIAO` fica de fora, mesmo existindo no dicionário.
- **Bases complementares:** os arquivos da OuvidoriaSUS e do Fala.BR de 2025 foram analisados, mas no máximo vão servir como validação cruzada, agregada por região. Ainda não é uma decisão fechada.
- **Título:** "Apartheid Digital? Uma Análise da Desigualdade no Uso Funcional da Internet no Brasil (2023-2025)".
- **Pergunta:** "Existe diferença na capacidade de resolver, pela internet, serviços essenciais (documentos, saúde, educação, trabalho, impostos, segurança, transporte e finanças) entre diferentes grupos de renda, raça, escolaridade e região no Brasil — e em quais dessas dimensões a diferença é maior ou menor?" (texto oficial da pergunta, igual ao README)

### 07/09/2026: repositório no GitHub e regras estatísticas

- **Repositório criado:** github.com/RdgsPedro/apartheid-digital, com as pastas `data/raw`, `data/processed`, `notebooks`, `src`, `docs` e `outputs`.
- **CSVs no Git por engano:** no primeiro commit, os 6 CSVs brutos subiram junto. No commit seguinte, o `.gitignore` foi corrigido e eles saíram do rastreamento, mas continuam guardados no histórico do Git.
- **Primeiro rascunho do notebook 01**, com a regra do G2: 1 = conseguiu; 2 e 3 = não conseguiu completamente; 97, 98 e 99 viram NaN e nunca contam como sucesso nem como fracasso.
- **Decisões fixadas antes de qualquer teste:** α = 0,05, e Rao-Scott implementado do jeito certo, não como um qui-quadrado simplificado.

### Até 17/09/2026: leitura dos documentos e revisão de literatura

- **Documentos da CETIC:** os 6 CSVs e os documentos de apoio (relatórios metodológicos, questionários e dicionários dos 3 anos) foram analisados e documentados.
- **Primeira entrega:** Introdução + Revisão de literatura, em outubro. A parte de código vem depois.
- **Estratégia de busca:** palavras-chave definidas, em seis blocos temáticos:
    - desigualdade digital no Brasil
    - base teórica internacional (desigualdade digital de 2º e 3º nível)
    - uso funcional e resultados do uso
    - governo eletrônico no Brasil
    - teoria de e-participação
    - precedentes metodológicos com a TIC Domicílios
- **Estado da arte** só com textos de 2021 em diante. Os clássicos (van Dijk, Hargittai, van Deursen e Helsper) ficam à parte, como base teórica.
- **Precedente mais próximo:** Araujo, Reinhard e Cunha (2018), com a mesma base e o mesmo foco, mas fora da janela de 5 anos.

### Entre 07/09 e 21/09/2026: harmonização, achados nos dados

- **G2:** os códigos de não resposta são 97/98/99, e não 8/9 como no questionário impresso.
- **Renda:** a `RENDA_FAMILIAR_2` é a única variável de renda comparável nos 3 anos.
- **Escolaridade:** existe uma versão agregada com 4 categorias iguais nos 3 anos, mas com nomes diferentes: `GRAU_INSTRUCAO_2` em 2023 e `GRAU_INST_1` em 2024/2025.
- **Região:** `COD_REGIAO_2`, presente nos 3 anos.
- **Velocidade:** muda em 2025. A A8 tem 10 faixas em 2023/2024 e a A8A tem 7 em 2025. O grupo agrupou as faixas em baixa (até 10 Mbps), média (11 a 50 Mbps) e alta (51 Mbps ou mais).
- **Valor:** a `A9_FAIXA` já vem com a mesma estrutura nos 3 anos.
- **Réplicas:**
    - As 200 réplicas existem nos 3 anos, inclusive em 2023. Isso corrigiu uma leitura errada do relatório metodológico.
    - Em domicílios, 2023 vem com `rep1` (minúsculo) e 2024/2025 com `REP1` (maiúsculo). Sem padronizar, empilhar os anos criaria 400 colunas.
- **Chave:** `ID_DOMICILIO`, igual nos 3 anos e nos 2 módulos. No projeto ela virou `chave_domicilio`.
- **G1:** já vem em 0/1. Só precisa transformar 97/98/99 em NaN.
- **Dois sistemas de peso:**
    - Cada módulo tem o seu `PESO` e as suas 200 réplicas. Em 2023, 100% das 21.271 pessoas têm um peso diferente do peso da própria casa, e 13.798 já diferem no `rep1`.
    - Faz sentido: a chance de a casa ser sorteada é diferente da chance de uma pessoa dentro dela ser a sorteada.
    - Decisão: qualquer teste com G1 ou G2 usa o peso do indivíduo, porque a unidade de análise é a pessoa.
- **Tamanho dos arquivos:** com as réplicas dentro, os CSVs processados ficavam com 92 a 137 MB. A saída foi um arquivo só com as réplicas do indivíduo, fora do Git.
- **Regra da época para a velocidade:** todo 99 vira "sem conexão". Essa regra foi revista em 10/10.

### 21/09/2026: notebook 01 de harmonização

- **Commit "Harmonização dos dados":** crosswalk (`lista_final_variaveis_projeto.csv`), funções em `src/harmonizacao.py` e o notebook 01 completo.
- **Dicionários oficiais:** os 6 xlsx foram adicionados em `docs/fontes_cetic/dicionarios/`.
- **Raça:** o código 98 aparece em 2.285 pessoas (3,4%). O dicionário confirma que é "Não respondeu", igual nos 3 anos, e ele vira NaN.
- **Erro de importação corrigido:** o `ModuleNotFoundError: No module named 'src'` acontecia quando o VS Code rodava o notebook a partir da raiz do repositório. A função `encontrar_raiz_projeto()` resolveu, e todos os caminhos passaram a partir dela.
- **Testes de integridade:**
    - 75.008 domicílios e 66.976 pessoas, exatamente a soma dos 6 arquivos.
    - Nenhuma casa duplicada e ninguém sem casa no merge.
    - O arquivo de réplicas cobre as mesmas pessoas.
- **Saída:** 4 arquivos em `data/processed/`: `domicilios_harmonizado`, `individuos_harmonizado`, `dados_harmonizados` (o principal, uma linha por pessoa com os dados da casa) e `individuos_pesos_replica`.

### Até 02/10/2026: ferramenta do Rao-Scott

- O plano era usar a biblioteca `samplics`. Ela foi trocada pela `svy`, que é a sucessora, do mesmo autor. O pacote `survey` do R ficou como plano B.

### 02/10/2026: revisão das fontes do artigo

- **Regras do professor:** só autores de pós-graduação em diante, e estado da arte com textos de 2021 em diante.
- **Saíram:**
    - Silva (2022) e Falcão (2022): TCCs de graduação.
    - Santos, Voth e Silva Junior: iniciação científica.
    - Soares (2021): o autor não tem mestrado.
    - Pavesi e Valentim (2021): é só a apresentação de um dossiê.
    - "Mota, Santos e Silva (2025)": essa obra não existe.
    - Ballou (2006) e CLRB (2020): sobraram de outro trabalho.
- **Ficam com cuidado:**
    - Lucas (2002): no lugar dele, citar a OECD (2001).
    - Almeida et al. (2005).
    - Ebbers, Jansen e van Deursen (2016): o estudo não sustenta a preferência por atendimento presencial.
    - Maciel e Lima.
    - Mattos (2003): só como clássico.
    - Santos e Mota (2024).
- **Aprovadas com a página conferida:** van Dijk (2017), OECD (2001), Hargittai (2002), Sorj e Guedes (2005), van Deursen e Helsper (2015), Araujo, Reinhard e Cunha (2018), Vargas et al. (2021), Knop (2020), Raihan et al. (2025), Schiefler, Cristóvam e Sousa (2020), Philippi (2023), Paes e Oliveira (2026), Morte-Nadal e Esteban-Navarro (2025), Barbosa et al. (2022), o relatório metodológico da TIC Domicílios 2025 e a Lei 14.129/2021.
- **Vale citar no artigo:** Vargas et al. (2021) usaram qui-quadrado sem ajuste ao desenho amostral (p. 802). Usar o Rao-Scott é uma melhoria metodológica em relação a eles.

### 03/10/2026: guia de estudo de estatística e conferência do repositório

- **Guia de estudo:** cobre amostragem complexa, peso amostral, réplicas bootstrap, Rao-Scott, tamanho do efeito (gap e V de Cramér), correção de múltiplos testes, o `svy` na prática e o roteiro dos notebooks 02 e 03.
- **Achados que importam pra análise:**
    - **Possível fator de escala nas réplicas:** o relatório não diz qual variante de bootstrap a CETIC usou. Antes dos testes, é preciso comparar os erros padrão com as tabelas oficiais de 2024 e 2025.
    - **Cadastro de 2025:** o de 2025 excluiu 7.805 setores de agrupamentos indígenas e 5.591 de quilombolas. Isso pesa na análise de raça, principalmente pra "indígena".
    - **Texto dos itens em 2025:** alguns mudaram. A ganhou "CNH, título de eleitor", B passou a citar "vacinas ou outros serviços do SUS", C ganhou "Sisu" e G ganhou "consulta sobre linhas e tarifas de ônibus".
- **Pendências achadas no repositório:**
    - `requirements.txt` ainda com `samplics`.
    - Renda, C8_H e A9_FAIXA sem tratar.
    - READMEs desatualizados.
    - `.gitignore` ignorando os dicionários.
    - Comentário "provisório" na célula de raça.

### 09/10/2026: plano do código

- Plano em 5 blocos: arrumação do repositório, limpeza no notebook 01, decisões do grupo, notebook 02 (EDA) e notebook 03 (testes).
- Seis decisões foram propostas pro grupo aprovar (ver "Decisões em aberto").

### 10/10/2026: limpeza, correção da velocidade e conferência com os dados reais

**Repositório**
- **`requirements.txt`:** saiu o `samplics` e entraram o `svy` (fixo na 0.31.0, porque a biblioteca ainda está em beta e muda entre versões), o `polars` e o `pyarrow`. O `svy` precisa de Python 3.11 ou mais novo.
- **READMEs:** o `README.md` principal, `data/processed/` e `outputs/` foram atualizados, e o `data/raw/README.md` foi criado.
- **`.gitignore`:** voltou a versionar os dicionários e passou a ignorar `.venv/`.

**Correção da velocidade (muda a regra de 21/09)**
- Lendo os filtros dos questionários dos 3 anos, deu pra ver que a pergunta de velocidade (A8 e A8A) só é feita a quem tem banda larga fixa (A7 = 2, 3, 4 ou 5).
- Então o 99 da velocidade não quer dizer só "sem conexão". Ele junta as casas sem internet (A7 = 99) com as que só usam internet móvel (A7 = 6) e as que não souberam o tipo de conexão (A7 = 97).
- A regra antiga colocava quem vive só do 4G/5G junto com quem não tem internet nenhuma.
- **Regra nova:** a A7 entrou no crosswalk como `tipo_conexao`, e a velocidade ficou com 5 categorias: `baixa`, `media` e `alta` (banda larga fixa), `movel` (A7 = 6) e `sem internet` (A7 = 99). Discada (A7 = 1), não sabe e não respondeu viram NaN.
- **Ponto pro método:** em 2025 a A7 também é feita pra casas com Wi-Fi ou com morador que acessa a internet em casa (A7A/A7D), então o "sem internet" de 2025 é um pouco mais restrito que o de 2023/2024.

**O que os dados reais mostraram**
- Móvel, não sabe, não respondeu e sem internet sempre têm velocidade 99, como o filtro manda.
- **Discada:** foge do filtro. Em 2023 e 2024 essas casas têm faixa de velocidade (90 e 79 casas), e em 2025 têm 99. Ela vira NaN nos 3 anos, pra regra ficar igual.
- **NaN grande na velocidade:** são de 6 a 8 mil casas por ano. O maior pedaço é o A7 = 97 (casas com internet que não souberam o tipo de conexão, cerca de 2.500 a 3.300 por ano), mais as de banda larga fixa que não souberam a velocidade.
- **Quem não paga a internet:**
    - Em 2023 e 2024, a CETIC colocou essas casas na faixa 1 da A9_FAIXA (até R$ 30): 450 e 373 casas.
    - Em 2025, usou um código 0 que não está no dicionário (351 casas).
    - Decisão: "não paga nada" vira o código 0 nos 3 anos. Em 2023 e 2024 isso usa a pergunta original (A9 = 17).

**Outras mudanças no notebook 01**
- **Renda:** 97 e 98 viram NaN. O 7 fica, porque é uma resposta de verdade.
- **Transações e valor:** na C8_H e na A9_FAIXA, os códigos 97, 98 e 99 viram NaN.
- **`np.nan` no lugar de `None`:** G1, G2 e raça passaram a usar `np.nan`, porque no pandas 3 o `None` deixa a coluna como texto.
- **Merge e testes:** o merge ganhou `validate='many_to_one'` e `indicator=True`, e o notebook ganhou uma seção de conferência dos filtros do questionário e outra de testes de integridade antes de salvar. O teste de valores pegou o código 0 inesperado de 2025.
- **Material de estudo:** o notebook foi reescrito com comentários linha por linha, pra servir de material de estudo do grupo.
- **Rodado com os dados reais:** 75.008 domicílios e 66.976 pessoas, os mesmos totais de 21/09, e todos os testes passaram.

### 11 e 12/10/2026: notebook 02 (análise exploratória)

- **Leitura guiada do notebook 01:** concluída (seções 1 a 13).
- **Notebook 02:** commit de 11/10 ("Notebook 02: tabelas por grupo, n efetivo e tabelao"), junto com a lista de variáveis atualizada. Em 12/10 ele foi reorganizado no formato do 01: 15 seções, comentários linha por linha e testes de integridade.
- **O que o notebook 02 faz:**
    - contagem por área e ano, com % sem peso, % com peso e n efetivo;
    - tabelas por grupo (renda, raça, escolaridade e região), com a função `tabela_por_grupo`;
    - o "tabelão": 462 linhas (22 combinações de ano e área × 21 categorias);
    - o gráfico do gap da renda, com e sem peso.
- **Saídas em `outputs/`:** `tabelao_eda.csv`, `gap_renda_pct_com_peso.png` e `gap_renda_pct_sem_peso.png`. São exploratórias: não têm margem de erro.
- **Filtro do G2 conferido:** nas 22 combinações de ano e área, ninguém responde o G2 sem ter dito que tentou (G1 = 1). Então todo % do G2 é "entre quem tentou".
- **n efetivo (Kish):** (soma dos pesos)² ÷ (soma de cada peso ao quadrado). Diz quantas pessoas um grupo vale de verdade, considerando os pesos. A margem de erro depende dele, e não do n.

**Achados**

*Números de antes do filtro do universo. Os atualizados estão na entrada de 12/10 à tarde.*

1. **O peso muda o %** em até ~11 p.p. (transporte 2023: 31,7 sem peso e 42,5 com peso). Entre as 1.639 pessoas que responderam transporte em 2023, a mais pesada sozinha tem 9,3% do peso.
2. **Grupos frágeis:** "não tem renda" em saúde 2024 tem 53 pessoas, mas n efetivo ≈ 3. Uma pessoa tem 57% do peso do grupo e respondeu 0, e o % cai de 20,8 (sem peso) para 6,3 (com peso). No tabelão, 63 das 462 linhas têm n efetivo menor que 10, quase sempre analfabeto/infantil, indígena, não tem renda e mais de 10 SM.
3. **A regra "n ≥ 50" não basta:** 20 linhas passam nela com n efetivo menor que 10. Ex.: polícia 2024, "até 1 SM": 296 pessoas, n efetivo 6, e o % vai de 30,7 para 60,2 com peso.
4. **A régua muda a resposta:** em impostos 2024, a dimensão com maior diferença (maior − menor % com peso) é a renda com corte n efetivo ≥ 10 e a região com corte ≥ 20. Com o corte 10, as pontas da raça eram justamente os grupos mais frágeis (amarela e preta).
5. **Gap da renda** (mais de 10 SM − até 1 SM): sem peso, positivo em todas as áreas e anos (9 a 42 p.p.); com peso, negativo em educação 2024, polícia 2024 e 2025, trabalho 2025 e transporte 2024, sempre com uma ponta frágil. Impostos é a única área com gap grande e estável nas duas medidas (com peso: 47,0, 43,6 e 31,6 p.p.).
6. **Ideia pra testar no notebook 03:** juntar "5 a 10 SM" e "mais de 10 SM" na ponta de cima. Num teste rápido, o n efetivo dessa ponta em impostos 2024 subiu de 14 para 61, mas os gaps negativos de 2024 não sumiram.

**O que muda nas decisões em aberto**
- **Decisão 2 ("não tem renda"):** o grupo tem n efetivo menor que 10 em 15 das 22 combinações de ano e área. Argumento para juntar com "até 1 SM" ou deixar fora do teste.
- **Decisão 3 (grupos do gap):** comparar grupos fixos, nunca "maior − menor", porque os extremos tendem a ser os grupos frágeis. Atenção às pontas da renda.
- **Decisão 4 (grupos pequenos):** a regra deve olhar o n efetivo ou o CV, e não só o n, e ser fixada antes dos testes, como o α.

### 12/10/2026: decisões para o notebook 03

- As decisões 1 a 6 que estavam em aberto foram fechadas com base no que o notebook 02 mostrou (ver "Decisões em vigor"). Os números desta entrada são de antes do filtro do universo (ver a entrada seguinte).
- **Por que juntar faixas:** o "não tem renda", o "mais de 10 SM" e o "analfabeto/infantil" são frágeis na maioria das áreas e anos. Com as faixas novas (renda em 5, escolaridade em 3), as linhas com n efetivo menor que 10 caem de 63 de 462 (14%) para 26 de 396 (7%), e quase todas as que sobram são de amarela e indígena.
- **Por que a regra dos grupos pequenos não é célula por célula:**
    - Uma regra que tira categorias célula por célula (pelo n, pelo n efetivo ou pelo CV) faz cada área ter categorias diferentes, e aí os testes e o ranking deixam de ser comparáveis entre as áreas.
    - Uma regra pelo CV tira com mais frequência os grupos com % baixo, que são justamente os mais desfavorecidos, e isso distorce a comparação.
    - Por isso as categorias dos testes são fixas. Amarela e indígena ficam fora porque são frágeis em quase tudo: com as faixas novas, a indígena tem n efetivo menor que 20 em 22 das 22 combinações de ano e área, e a amarela em 17.
- **O que ainda balança:** mesmo com as faixas novas, o gap da renda com peso continua negativo em 2024 em educação (−3,0), polícia (−7,5) e transporte (−3,9). A margem de erro do notebook 03 vai dizer se essas diferenças são reais.
- **Situação:** aprovadas pelo Pedro; falta a confirmação do Vitor e do Eduardo.

### 12/10/2026 (tarde): conferência com as tabelas oficiais e correções nos notebooks 01 e 02

**Conferência com as tabelas oficiais da CETIC**
- As 12 planilhas oficiais de indivíduos (proporção, margem de erro, total e margem de erro do total; 2023 v1.1, 2024 v1.1 e 2025 v1.0) foram baixadas do site da CETIC e guardadas em `docs/fontes_cetic/tabelas/`. A aba "G2" das planilhas é o nosso G1 (procurou ou realizou), e a aba "G2A" é o nosso G2 (cinco colunas por área).
- **Os % não batiam.** Exemplo: o G1 de saúde em 2024 dava 30,93%, e o oficial é 31,81%.
- **Motivo: o universo.** As tabelas oficiais do módulo G contam só os usuários de Internet de 16 anos ou mais: quem tem 16+ e disse na C3 que usou a internet nos últimos 3 meses (a variável `F_C3_IDADE`). Já o questionário aplica o módulo G a quem usou a internet nos últimos 3 meses pela C3 **ou** pela J3 (internet no celular). Em 2023, 2024 e 2025, 1.135, 969 e 1.089 pessoas disseram "não" na C3 e "sim" na J3, e 1.133, 967 e 1.088 delas responderam o G1. Com o filtro `F_C3_IDADE = 1`, as nossas estimativas batem exatamente com as oficiais: G1 e G2, Total e grupos (região, raça e renda), nos 3 anos.
- **Réplicas de 2023:** no arquivo bruto de indivíduos de 2023, `rep1` a `rep200` não são pesos, e sim contagens do sorteio do bootstrap (inteiros de 0 a 7, média ≈ 1). O peso de cada réplica é o `PESO` × a contagem. Com isso, as nossas margens de 2023 ficam perto das oficiais: a razão oficial ÷ nossa tem mediana 1,05 em 126 células (Total, região, raça e renda, nas 7 áreas). Não dá pra bater exato porque em 2023 a CETIC calculou as margens por outro método, o do conglomerado primário (relatório metodológico de 2023). A maior diferença é saúde no Total (1,25).
- **Margens de 2024 e 2025:** a margem oficial é a nossa (1,96 × o desvio padrão das 200 réplicas) vezes uma constante, igual em todas as células do ano: 1,054 em 2024 (√(10/9)) e 1,140 em 2025 (√1,3). O relatório metodológico não explica esse fator. Isso confirma o "possível fator de escala nas réplicas" anotado em 03/10.

**Decisões (ver "Decisões em vigor")**
- **Universo da análise:** G1 e G2 só entre usuários de Internet de 16 anos ou mais, como nas tabelas da CETIC.
- **Margem de erro:** em 2024 e 2025, as margens são multiplicadas pelo fator (1,054 e 1,140), pra reproduzir as oficiais. É o lado mais cauteloso: com margem maior, fica mais difícil achar uma diferença que não existe. Em 2023 fica sem fator. A origem do fator entra como limitação no método.
- Falta a confirmação do grupo.

**Correções**
- **Lista de variáveis:** desde o commit de 11/10, a primeira linha de `docs/lista_final_variaveis_projeto.csv` começava com "git status" (o comando foi digitado dentro do arquivo aberto). Isso mudava o nome da coluna `variavel_final` e quebrava o notebook 01 com `KeyError`. Corrigido. A lista ganhou a linha `usuario_internet` (`F_C3_IDADE` nos 3 anos), e as observações das réplicas passaram a avisar das contagens de 2023.
- **Notebook 01:**
    - leva o `usuario_internet` pros arquivos (o `dados_harmonizados` passa a ter 33 colunas, e o `individuos_harmonizado`, 27);
    - multiplica as réplicas de 2023 pelo `PESO` (o arquivo de réplicas foi de 133 pra cerca de 170 MB);
    - ganhou um teste: em cada ano, a soma de cada réplica tem que ficar perto da soma do peso;
    - um `.copy()` antes de criar a coluna `ano` acabou com o aviso `PerformanceWarning`.
- **Notebook 02:** filtra o universo logo depois de carregar os dados (45.436 pessoas: 13.859, 14.686 e 16.891). O % de cada área mudou pouco (no máximo 2,9 p.p., na polícia 2024), e alguns grupos frágeis mudaram bastante. Os achados atualizados:
    1. O peso muda o % em até ~10 p.p. (transporte 2023: 32,8 sem peso e 43,2 com peso; a pessoa mais pesada tem 9,5% do peso).
    2. "Não tem renda" em saúde 2024: 51 pessoas, n efetivo ≈ 3, uma pessoa com 58% do peso; o % cai de 19,6 pra 5,9 com peso. No tabelão, 66 das 462 linhas têm n efetivo menor que 10.
    3. 18 linhas passam na regra "n ≥ 50" com n efetivo menor que 10 (ex.: transporte 2023, "1 a 2 SM": 417 pessoas, n efetivo 9, de 29,3 pra 49,6 com peso).
    4. A régua continua mudando a resposta em impostos 2024 (corte 10: renda; corte 20: região).
    5. Gap da renda: sem peso, positivo em tudo (9,5 a 40,9 p.p.); com peso, negativo em educação 2024, transporte 2024, polícia 2025 e trabalho 2025, sempre com o "mais de 10 SM" frágil. **A polícia 2024 deixou de ser negativa:** no "até 1 SM", uma pessoa de fora do universo carregava 39% do peso do grupo; sem ela, o n efetivo do grupo foi de 6 pra 72, e o gap, de −9,3 pra 14,4 p.p. Impostos continua o único com gap grande e estável (com peso: 46,1, 43,1 e 30,5 p.p.).
    6. Com as faixas novas (renda em 5, escolaridade em 3) e o universo, as linhas com n efetivo menor que 10 são 28 de 396, quase todas de indígena e amarela (a indígena tem n efetivo menor que 20 em 22 das 22 combinações de ano e área, e a amarela em 17). O gap da renda com peso (mais de 5 SM − até 1 SM) só fica negativo em educação 2024 (−3,9).

**Ponto pro artigo**
- As pessoas que ficaram fora do universo disseram, na C3, que não usaram a internet nos últimos 3 meses, mas, na J3, que usaram pelo celular. Isso conversa com o tema do projeto (o que conta como "usar a internet") e vale uma nota no método, explicando por que elas ficam fora da análise.

### 12/10/2026 (noite): notebook 03 (margem de erro e testes)

- **Como foi feito:** o Pedro montou o notebook passo a passo, e depois ele foi organizado no formato do 01 e do 02, com 15 seções, comentários linha por linha e testes de integridade.
- **O que o notebook 03 faz:**
    - margem de erro com as 200 réplicas (EP, IC e CV);
    - conferência com as tabelas oficiais da CETIC (seção 4: o universo, o "não sabe / não respondeu" do G1 e o fator das margens);
    - o tabelão com IC: 418 linhas, com as faixas novas e o Brasil;
    - os gaps com IC: 176 linhas, com os 8 pares da decisão nº 3;
    - o Rao-Scott de 2ª ordem: 88 testes, com a correção de Holm por ano (justiça à parte);
    - o V de Cramér e o ranking das áreas;
    - a exportação das 3 tabelas pro Power BI (ver `outputs/README.md`).
- **O `svy` conferido:** o Rao-Scott do `svy` 0.31.0 deu exatamente o mesmo resultado que a fórmula do `svychisq` do pacote `survey` do R (com `statistic="F"`), nos 88 testes. As réplicas entram no `svy` com `scale` = fator² ÷ 199, o mesmo cálculo de margem do resto do notebook.
- **G1 e o "não sabe / não respondeu":** com o universo certo, a diferença que sobrava pro G1 oficial (até 0,07 ponto) vinha do NS/NR. No nosso arquivo ele é NaN; a CETIC conta como "não". Contando igual, bate exatamente. A medida do projeto (G2 entre quem tentou) não muda.

**Achados**

*Números de antes do fator de 2023: os itens 1, 3 e 4 mudaram. Os atualizados estão na entrada de 13/10.*

1. **A amostra vale bem menos do que o número de entrevistas.** O qui-quadrado comum diria que 83 dos 88 testes têm diferença real; o Rao-Scott, 36; depois do Holm, 10. Em impostos 2024 por renda, o efeito do desenho é de umas 9 vezes. Ponto pro método: é uma melhoria em relação a quem usou o qui-quadrado simples, como Vargas et al. (2021).
2. **As diferenças são pequenas, mas existem.** V de Cramér médio: região 0,175, renda 0,166, escolaridade 0,149 e raça 0,128, todas na faixa "pequena" da régua de Cohen. Escolaridade era a maior em 2023 (0,236) e caiu em 2024 e 2025 (0,096 e 0,116).
3. **Escolaridade e região são as diferenças mais firmes:** dos 10 testes que passam no Holm, 5 são de escolaridade, 4 de região, 1 de renda e nenhum de raça.
4. **Impostos é a área mais desigual e a mais certa:** gap de renda (mais de 5 SM menos até 1 SM) de 39,6, 31,5 e 33,8 pontos em 2023, 2024 e 2025, todos reais, e 6 dos 10 testes que passam no Holm. Polícia e transporte também têm V alto, mas pouca gente respondendo, e quase nunca passam no Holm (ex.: polícia por região em 2024, V = 0,347 e p ajustado de 0,084).
5. **Saúde é a área mais igual:** menor V médio (0,111), e em 2024 a região não faz diferença (p = 0,66).
6. **O Sudeste nem sempre está no topo:** os 8 gaps reais negativos são de região. O Sul resolve mais que o Sudeste em polícia, educação, transporte e saúde (pelos ICs dos gaps, sem Holm).
7. **Raça:** nenhum teste passa no Holm. Isso não prova que não existe desigualdade racial: "preta" tem n efetivo baixo em várias áreas, e amarela e indígena ficaram fora dos testes. Vai como limitação no método.

### 12/10/2026 (noite, parte 2): o G1 ao lado do G2 e os gráficos do artigo

- **O que entrou no notebook 03** (que passou de 15 pra 17 seções):
    - **Seção 13, o G1 ao lado:** o tabelão de quem tentou (418 linhas) e os gaps de quem tentou (176 linhas), com as mesmas contas do G2, mas com todos os usuários do grupo. O "não sabe / não respondeu" do G1 conta como "não", igual à CETIC, e o Brasil de 2024 bate com o número oficial (vira um teste de integridade). Tem também a conta "resolveu entre todos" (tentou × resolveu ÷ 100) e a comparação do V e dos gaps entre tentar e resolver.
    - **Seção 14, os gráficos:** o heatmap do V (área × dimensão e ano, com `*` no que passa no Holm), os gaps de renda e de escolaridade com IC, e tentou × resolveu no Brasil em 2025. As cores seguem o 02 (os anos em 3 tons de azul) e foram conferidas pra daltonismo.
    - **Saídas novas:** `estimativas_g1_ic.csv` e `gaps_g1_ic.csv`, com as mesmas colunas das tabelas do G2, e os 3 `.png` (ver `outputs/README.md`).
- **O G1 é contexto, não teste:** ele mistura quem não conseguiu usar a internet com quem nem precisou do serviço (em impostos, quem ganha pouco muitas vezes nem precisa declarar o imposto de renda). O Rao-Scott, o Holm e o ranking continuam só no G2 (decisão nº 1).

**Achados**

*Com o fator de 2023 (13/10), o 57 do item 5 virou 55.*

1. **Contando todo mundo, pouca gente resolve tudo pela internet.** Em 2025, de cada 100 usuários de Internet, uns 18 resolveram impostos inteiramente online, 12 resolveram documentos e menos de 4, algo com a polícia.
2. **Saúde é a área mais tentada (36,6%) e a menos resolvida (22,6% de quem tentou).** Hipótese pro texto: muita coisa da saúde, como a consulta e o exame, não dá pra terminar pela internet.
3. **A dupla barreira da renda, em impostos 2025:** quem tem até 1 SM tenta menos (12,0% contra 62,6% de quem tem mais de 5 SM) e, quando tenta, resolve menos (39,7% contra 73,5%). Contando todo mundo, 4,8% contra 46,0%: quase 10 vezes menos.
4. **No tentar, pesam escolaridade e renda; no resolver, aparecem também região e raça.** V médio do G1: escolaridade 0,213, renda 0,166, região 0,105 e raça 0,049. No G2: região 0,175, renda 0,166, escolaridade 0,149 e raça 0,128. Brancos, pretos e pardos tentam quase na mesma medida (gaps médios de 1,5 e 1,4 ponto), mas, entre quem tenta, os brancos resolvem uns 10 pontos a mais (sem confirmação no Holm).
5. **O G1 tem mais gaps reais (73 de 176, contra 57 do G2), mas não diferenças maiores:** ele usa todo mundo (de 14 a 17 mil pessoas por ano), e o IC fica mais estreito. Pra comparar o tamanho, vale o gap médio e o V.
6. **Nos gráficos:** a escolaridade era a maior diferença em 2023 (V de 0,26 a 0,35 em 5 das 7 áreas) e caiu em 2024 e 2025; o gap médio da escolaridade foi de 29,8 pontos em 2023 pra 12,8 e 14,0. Os gaps firmes, reais nos 3 anos, são impostos e documentos na renda, e impostos e educação na escolaridade.

### 12/10/2026 (noite, parte 3): decisões finais e finanças à parte

- **O grupo confirmou** todas as decisões de 12/10: o Vitor e o Eduardo deram o ok.
- **Três decisões novas** (na tabela acima):
    - finanças entra à parte, como o G1: com IC e gaps, sem teste e sem ranking;
    - velocidade e valor da conexão ficam como trabalho futuro;
    - as figuras do artigo e da apresentação saem do Power BI, e os gráficos do notebook 03 ficam como conferência.
- **O que mudou no notebook 03** (que passou de 17 pra 18 seções):
    - seção 14 nova, finanças à parte: o tabelão (57 linhas), os gaps (24 linhas), finanças ao lado do G1 e a conferência com a tabela oficial;
    - a seção dos gráficos virou "Gráficos de conferência" (seção 15);
    - 2 tabelas novas em `outputs/`: `estimativas_financas_ic.csv` e `gaps_financas_ic.csv`.
- **Finanças e a CETIC:** o número oficial é menor (57,5% contra 63,1% em 2025) porque a tabela da CETIC (aba C6) conta os usuários de 10 anos ou mais, e o projeto usa os de 16 anos ou mais. No mesmo universo, os dois batem: a diferença é de no máximo 0,17 ponto.

**Achados**
1. **Finanças é o uso mais comum:** 63,1% dos usuários em 2025, contra 36,6% que tentaram saúde, o serviço público mais tentado. A C8_H olha os últimos 3 meses, e o G1, os últimos 12: mesmo numa janela menor, finanças fica bem acima.
2. **A desigualdade em finanças é de escolaridade, renda e região, e não de raça.** Em 2025, são 87,1% no superior contra 32,3% no até fundamental (gap de 54,8 pontos, o maior do projeto), e 86,0% com mais de 5 SM contra 44,3% com até 1 SM. O Sudeste fica 13,1 pontos acima do Nordeste. Os gaps de raça (de 2,1 a 3,8 pontos) não são reais em nenhum ano.
3. **É o mesmo desenho do G1:** no uso, pesam escolaridade e renda, e raça quase não pesa. A diferença no uso da internet aparece também num serviço privado, e não só nos públicos.

### 13/10/2026: revisão final e o fator de 2023

- **Revisão de ponta a ponta:** o projeto foi conferido inteiro, sem mexer no repositório: o último commit rodado do zero em outro computador, os dados brutos, a harmonização contra os dicionários, os % e as margens contra as planilhas oficiais da CETIC, toda a estatística refeita por outro caminho e os textos contra as tabelas.
- **O que passou:**
    - a reprodução: as 8 tabelas de `outputs/` saíram idênticas, byte por byte;
    - os % contra a CETIC: 2.595 comparações, em todos os grupos que as planilhas publicam (G1, G2 entre quem tentou, G2 entre todos, governo eletrônico e finanças), iguais até a terceira casa decimal. Finanças, no universo de 10 anos ou mais, fica a no máximo 0,84 ponto, pelo NS/NR e pela C3 × J3 abaixo dos 16 anos;
    - a soma dos pesos do universo: igual ao total oficial de usuários de 16 anos ou mais, nos 3 anos;
    - a estatística: as estimativas, os gaps, o Rao-Scott (pela fórmula do `svychisq`, refeita em Python), o Holm (pelo `statsmodels`), o V e o ranking, refeitos do zero, deram os mesmos números.
- **As margens de 2024 e 2025:** o fator (1,054 e 1,140) reproduz a margem oficial em todos os 1.079 grupos comparados, e não só no Brasil.
- **O achado: as margens de 2023.** Na linha do Brasil, a razão oficial ÷ nossa ficava perto de 1 (saúde, 1,25). Em todos os grupos, a média é 1,054 (504 comparações; a oficial é maior em 4 de cada 5), o mesmo fator de 2024. 2023 e 2024 têm o mesmo desenho de amostra (88 estratos, conglomerados em 3 estágios), e o guia de estatística de 03/10 já previa que o fator de 2024 valeria pra 2023.
- **Decisão (nº 9 revista):** 2023 também leva o fator 1,054. A mudança veio da conferência com as margens oficiais, e não dos resultados, e só deixa as conclusões mais cautelosas (margem maior).
- **O que mudou nos resultados** (só 2023; 2024, 2025, o V e o ranking não mudam):
    - Rao-Scott com p < 0,05: de 36 pra 33 testes; depois do Holm, de 10 pra 8. Saem trabalho por escolaridade e impostos por região, os dois de 2023. Os 8 que ficam: 4 de escolaridade, 3 de região, 1 de renda e nenhum de raça; 5 são de impostos;
    - gaps reais do G2: de 57 pra 55 (saem documentos e saúde, Sudeste − Nordeste, 2023);
    - linhas com aviso: de 52 pra 56 no G2 e de 23 pra 25 no G1; linhas com IC abaixo de zero: de 15 pra 16;
    - as conclusões continuam: escolaridade e região são as diferenças mais firmes, impostos é a área mais desigual e mais certa, e nenhum teste de raça passa.
- **Correções de texto:** as réplicas brutas de 2023 vão de 0 a 7 (e não de 0 a 5); a ressalva de que finanças olha os últimos 3 meses e o G1, os últimos 12; a coluna Nº na tabela de decisões; OuvidoriaSUS e Fala.BR como trabalho futuro; "fórmula do `svychisq`" na linha do teste; duas frases do notebook 03 (seções 8 e 13.2). O notebook 01 passou a imprimir só o nome da pasta do projeto, e o `requirements.txt` ganhou as versões.
- **Pro artigo:** o G2 é "realizou ao menos um desses serviços sem precisar ir até um posto de atendimento" (questionário), então o texto não pode dizer que a pessoa resolveu todos os serviços da área. Duas limitações novas: em 2025 o texto de 4 itens do G mudou (A, B, C e G ganharam exemplos, como CNH, vacinas, Sisu e tarifas de ônibus), e o cadastro de 2025 tirou 7.805 setores de agrupamentos indígenas e 5.591 de quilombolas. A coleta foi CAPI (tablet, face a face) nos 3 anos.
- **Situação:** aprovada pelo grupo.

---

## Próximos passos

1. Rodar os 3 notebooks na ordem (01, 02 e 03), com Restart + Run All, e commitar as mudanças de 13/10.
2. Montar no Power BI as figuras do artigo e o painel, a partir das 7 tabelas de `outputs/` (se o painel já tiver sido começado, é só usar Página Inicial > Atualizar).
3. Escrever o texto: metodologia, resultados e conclusão, com as limitações (o universo C3 × J3, o fator das margens, a raça e o cadastro de 2025, o texto novo de 4 itens em 2025, o G1 e finanças como medidas de uso, com períodos diferentes, e a camada extra e as bases complementares como trabalho futuro).
4. Fechamento: recriar o `docs/documentacao_projeto.md` (o guia do código pode virar esse arquivo), atualizar o caderno e fazer o último commit.
