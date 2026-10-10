# Caderno de Bordo
### Projeto Integrador: Apartheid Digital? (Ciência de Dados, Fatec Rubens Lara, 2º semestre)

**Grupo:** Pedro Rodrigues Almeida, Vitor Alexandre dos Santos Silva e Eduardo Pedro Nogueira

> Registro das etapas e decisões do projeto, da mais antiga pra mais recente. As datas exatas vêm do histórico do Git. As que aparecem como "até tal data" foram reconstruídas pelas anotações do grupo e só dizem o limite: a etapa aconteceu naquele dia ou antes. Vale o grupo conferir e completar.

---

## Decisões em vigor

| Tema | Decisão | Desde |
| --- | --- | --- |
| Base de dados | Microdados da TIC Domicílios (CETIC.br/NIC.br), módulos domicílios e indivíduos | até 24/08 |
| Recorte | 2023, 2024 e 2025 (opção 2 da professora: últimos 3 anos com mais variáveis) | até 24/08 |
| Variável central | G2_X (fez o serviço inteiro pela internet), com o G1_X (tentou) como par de cada área | até 24/08 |
| Áreas do ranking | 7 áreas, de A a G. Justiça (H) só existe em 2025 e entra à parte. Finanças vem da C8_H, outra pergunta, e fica fora do ranking | 21/09 (H) e 03/10 (finanças) |
| Religião | `RELIGIAO` não é usada | até 24/08 |
| G2 em 0/1 | 1 = fez tudo online; 2 (precisou ir ao posto) e 3 (só procurou informação) = 0; 97/98/99 = NaN | 07/09 |
| Peso | Qualquer conta com G1 ou G2 usa o peso do indivíduo e as réplicas do indivíduo, mesmo cruzando com renda ou região | 21/09 |
| Réplicas | 200 réplicas bootstrap do indivíduo, num arquivo separado e fora do Git | 21/09 |
| Nível de significância | α = 0,05, fixado antes de qualquer teste | 07/09 |
| Teste | Rao-Scott de 2ª ordem, e não um qui-quadrado simples | 07/09 |
| Ferramenta | `svy` (Python), fixo na versão 0.31.0; o pacote `survey` do R fica de plano B | até 02/10 (versão fixada em 10/10) |
| Códigos 97/98/99 | Viram NaN, com duas exceções: velocidade e valor da conexão (linhas abaixo) | 21/09 e 10/10 |
| Renda | 97 e 98 viram NaN; o 7 ("não tem renda") fica como código próprio | 10/10 |
| Velocidade | 5 categorias usando o tipo de conexão (A7): `baixa`, `media`, `alta`, `movel` e `sem internet`; discada e não sabe viram NaN | 10/10 (substitui a regra de 21/09) |
| Valor da conexão | 97/98/99 viram NaN; "não paga nada" vira o código 0 nos 3 anos | 10/10 |
| Fontes do artigo | Só autores de pós-graduação em diante; estado da arte com textos de 2021 em diante | 02/10 |

## Decisões em aberto

Têm que ser fechadas antes dos testes do notebook 03. As propostas estão no plano do código e esperam o grupo aprovar.

1. **Medida principal:** G2 entre quem tentou, G1, ou as duas. Proposta: G2 como principal, sempre com o G1 ao lado.
2. **Código 7 da renda ("não tem renda"):** grupo próprio ou junto com "até 1 SM". Proposta: grupo próprio, se tiver pessoas suficientes.
3. **Grupos do gap:** as pontas na renda e na escolaridade; branca e Sudeste como referência em raça e região.
4. **Grupos pequenos (amarela e indígena):** proposta de sempre mostrar a estimativa, com aviso se o CV passar de 30%, e tirar do teste se o n sem peso ficar abaixo de 50. Juntar com outro grupo, nunca.
5. **Correção dos p-valores:** proposta de Holm, por ano (28 testes = 7 áreas × 4 dimensões).
6. **Ano a ano ou empilhado:** proposta de ano a ano como principal e os 3 anos empilhados como complementar.
7. **Bases complementares (OuvidoriaSUS e Fala.BR):** no máximo como validação cruzada por região. Uso ainda não confirmado.

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

---

## Próximos passos

1. Rodar o notebook 01 novo em cada computador do grupo e fazer o commit.
2. Fechar as decisões em aberto e registrar aqui.
3. Notebook 02 (EDA): contagens, valores faltantes, n por grupo e por área, e as primeiras proporções ponderadas.
4. Notebook 03: validação das réplicas contra as tabelas oficiais e depois os testes de Rao-Scott, o gap com IC, o V de Cramér e a correção dos p-valores.
5. Exportar as tabelas pro Power BI e escrever os resultados.
