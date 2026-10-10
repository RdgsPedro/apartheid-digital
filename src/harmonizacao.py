"""
Funcoes reutilizaveis de harmonizacao dos dados TIC Domicilios.

Este modulo junta as funcoes usadas nos notebooks, pra nao repetir codigo
entre 01_harmonizacao.ipynb, 02_eda.ipynb, 03_testes.ipynb etc.

Ver docs/lista_final_variaveis_projeto.csv para os nomes e codigos de cada
variavel, e docs/caderno_de_bordo.md para o historico de decisoes.
"""

import numpy as np


# ---------------------------------------------------------------------------
# G2: resolveu o servico pela internet?
# ---------------------------------------------------------------------------

def recodificar_g2(serie):
    """Transforma uma coluna G2_X em 0/1.

    Codigos originais (iguais nos 3 anos):
      1 = fez o servico inteiro pela internet       -> 1
      2 = fez parte online, mas precisou ir ao posto -> 0
      3 = so procurou informacao                    -> 0
      97/98/99 = nao sabe / nao respondeu / nao se aplica -> NaN

    O .map troca cada valor pelo que o dicionario manda. Qualquer valor que
    nao estiver no dicionario tambem vira NaN.
    """
    mapa_g2 = {
        1: 1,
        2: 0,
        3: 0,
        97: np.nan,
        98: np.nan,
        99: np.nan,
    }
    return serie.map(mapa_g2)


# ---------------------------------------------------------------------------
# Velocidade da conexao
# ---------------------------------------------------------------------------

# Faixas de velocidade pra quem tem banda larga fixa.
# Criterio do grupo: baixa = ate 10 Mbps, media = 11 a 50 Mbps, alta = 51 Mbps ou mais.

# 2023 e 2024: variavel A8, 10 faixas
MAPA_VELOCIDADE_2023_2024 = {
    1: 'baixa',    # ate 256 Kbps
    2: 'baixa',    # 257 a 999 Kbps
    3: 'baixa',    # 1 Mega
    4: 'baixa',    # 2 Mega
    5: 'baixa',    # 3 a 4 Mega
    6: 'baixa',    # 5 a 8 Mega
    7: 'baixa',    # 9 a 10 Mega
    8: 'media',    # 11 a 20 Mega
    9: 'media',    # 21 a 50 Mega
    10: 'alta',    # 51 Mega ou mais
    97: np.nan,    # nao sabe
    98: np.nan,    # nao respondeu
    99: np.nan,    # nao se aplica: a pergunta nao foi feita (ver tipo de conexao)
}

# 2025: variavel A8A, 7 faixas
MAPA_VELOCIDADE_2025 = {
    1: 'baixa',    # ate 4 Mbps
    2: 'baixa',    # 5 a 10 Mbps
    3: 'media',    # 11 a 50 Mbps
    4: 'alta',     # 51 a 100 Mbps
    5: 'alta',     # 101 a 300 Mbps
    6: 'alta',     # 301 a 500 Mbps
    7: 'alta',     # 501 Mbps ou mais
    97: np.nan,
    98: np.nan,
    99: np.nan,
}


def recodificar_velocidade(velocidade, tipo_conexao, ano):
    """Junta velocidade e tipo de conexao numa coluna so, com 5 categorias.

    A pergunta de velocidade (A8 em 2023/2024, A8A em 2025) so e feita pra
    casas com banda larga fixa (A7 = 2, 3, 4 ou 5). Por isso o 99 da
    velocidade junta casas sem internet e casas que so usam internet movel.
    A A7 (tipo_conexao) separa esses grupos:

      A7 = 2 a 5  (banda larga fixa) -> 'baixa', 'media' ou 'alta'
      A7 = 6      (rede movel 3G/4G/5G) -> 'movel'
      A7 = 99     (casa sem internet)   -> 'sem internet'
      A7 = 1 (discada), 97 ou 98        -> NaN
      (A7 = 97, "nao sabe o tipo de conexao", e o maior grupo dos NaN:
       cerca de 2.500 a 3.300 casas por ano)

    Parametros:
      velocidade   = coluna com o codigo bruto da A8/A8A
      tipo_conexao = coluna com o codigo bruto da A7
      ano          = 2023, 2024 ou 2025 (escolhe qual mapa usar)
    """
    # 1) Escolhe o mapa certo pro ano
    if ano == 2025:
        mapa = MAPA_VELOCIDADE_2025
    else:
        mapa = MAPA_VELOCIDADE_2023_2024

    # 2) Traduz o codigo da velocidade em faixa. Quem nao tem banda larga
    #    fixa tem velocidade 99, entao aqui fica NaN
    resultado = velocidade.map(mapa)

    # 3) Preenche as categorias que vem do tipo de conexao.
    #    tipo_conexao == 6 da uma coluna de True/False; o .loc troca so as
    #    linhas True
    resultado.loc[tipo_conexao == 6] = 'movel'
    resultado.loc[tipo_conexao == 99] = 'sem internet'

    # 4) Discada vira NaN nos 3 anos. Nos dados reais, em 2023 e 2024 algumas
    #    casas com discada responderam a velocidade mesmo fora do filtro (90 e
    #    79 casas); em 2025 todas tem 99. Assim a regra fica igual nos 3 anos
    resultado.loc[tipo_conexao == 1] = np.nan

    return resultado


# ---------------------------------------------------------------------------
# Nomes de colunas
# ---------------------------------------------------------------------------

def renomear_colunas(df, ano, modulo, crosswalk):
    """Renomeia as colunas de um ano/modulo pro nome final do projeto.

    Usa a tabela docs/lista_final_variaveis_projeto.csv (o crosswalk), que diz
    como cada variavel se chama em cada ano.

    Linhas com ".." no nome (ex: "G1_A..G1_G", "rep1..rep200") sao uma
    FAMILIA de colunas, nao uma coluna so. Elas sao puladas aqui e tratadas a
    parte no notebook.
    """
    # Fica so com as linhas do modulo pedido. Precisa disso porque o mesmo
    # PESO vira peso_amostral_domicilio num modulo e peso_amostral_individuo
    # no outro
    filtro = crosswalk['modulo'].str.contains(modulo)
    tabela = crosswalk[filtro]

    # Nome da coluna do crosswalk que tem os nomes daquele ano (ex: 'nome_2024')
    coluna_do_ano = f'nome_{ano}'

    # Monta um dicionario {nome no arquivo: nome final}
    mapa_rename = {}
    for _, linha in tabela.iterrows():
        nome_no_arquivo = linha[coluna_do_ano]
        if '..' in str(nome_no_arquivo):
            continue  # familia de colunas: pula
        mapa_rename[nome_no_arquivo] = linha['variavel_final']

    # rename devolve um DataFrame NOVO; colunas fora do dicionario ficam iguais
    return df.rename(columns=mapa_rename)


def padronizar_pesos_replica(df):
    """Deixa as 200 colunas de peso replica sempre em minusculo (rep1..rep200).

    No modulo domicilios, 2023 vem com rep1..rep200 e 2024/2025 com
    REP1..REP200. Sem padronizar, empilhar os 3 anos criaria 400 colunas em vez
    de 200 (metade vazia em cada ano). No modulo individuos ja vem tudo em
    minusculo, entao a funcao nao muda nada nele.
    """
    mapa_rename = {}
    for i in range(1, 201):
        for variante in (f'rep{i}', f'REP{i}'):
            if variante in df.columns:
                mapa_rename[variante] = f'rep{i}'
    return df.rename(columns=mapa_rename)
