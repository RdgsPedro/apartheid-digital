"""
Funcoes reutilizaveis de harmonizacao dos dados TIC Domicilios.

Este modulo centraliza as funcoes usadas nos notebooks, para nao repetir
codigo entre 01_harmonizacao.ipynb, 02_eda.ipynb, 03_testes.ipynb etc.

Ver docs/documentacao_projeto.md para o detalhamento de cada regra abaixo,
e docs/caderno_de_bordo.md para o historico de decisoes.
"""


def recodificar_g2(serie):
    """Recodifica uma coluna G2_X em binario: 1=conseguiu, 0=nao conseguiu, NaN=missing."""
    mapa_g2 = {
        1: 1,
        2: 0,
        3: 0,
        97: None,
        98: None,
        99: None
    }
    return serie.map(mapa_g2)


def recodificar_velocidade(serie, ano):
    """Recodifica a coluna de velocidade de internet em baixa, media, alta ou sem conexao.

    2023/2024 usam a variavel A8 (10 categorias, Kbps ate Mega).
    2025 usa a variavel A8A (7 categorias, faixas de Mbps maiores).
    Critério de agrupamento definido pelo grupo: baixa = ate 10 Mbps,
    media = 11-50 Mbps, alta = 51+ Mbps. Codigo 99 (nao se aplica, sem
    internet contratada) vira categoria propria "sem conexão" em vez de NaN,
    por ser informativo pra pesquisa de desigualdade digital.
    """
    mapa_veloc_2023_2024 = {
        1: "baixa",
        2: "baixa",
        3: "baixa",
        4: "baixa",
        5: "baixa",
        6: "baixa",
        7: "baixa",
        8: "media",
        9: "media",
        10: "alta",
        97: None,
        98: None,
        99: "sem conexão"
    }

    mapa_veloc_2025 = {
        1: "baixa",
        2: "baixa",
        3: "media",
        4: "alta",
        5: "alta",
        6: "alta",
        7: "alta",
        97: None,
        98: None,
        99: "sem conexão"
    }
    if ano == 2025:
        return serie.map(mapa_veloc_2025)
    else:
        return serie.map(mapa_veloc_2023_2024)


def renomear_colunas(df, ano, modulo, crosswalk):
    """
    Renomeia as colunas de um DataFrame para o nome final, usando a tabela
    crosswalk (docs/lista_final_variaveis_projeto.csv).

    Linhas do crosswalk cujo nome_no_arquivo contem ".." (ex: "G1_A..G1_G",
    "rep1..rep200") representam uma FAMILIA de colunas, nao uma coluna unica
    -- nao fazem sentido num rename 1-pra-1, entao sao puladas aqui e tratadas
    a parte (ver padronizar_pesos_replica e a selecao de colunas G1_/G2_
    no notebook).
    """
    filtro = crosswalk['modulo'].str.contains(modulo)
    tabela = crosswalk[filtro]

    coluna_do_ano = f'nome_{ano}'

    mapa_rename = {}
    for _, linha in tabela.iterrows():
        nome_no_arquivo = linha[coluna_do_ano]
        if '..' in str(nome_no_arquivo):
            continue
        nome_final = linha['variavel_final']
        mapa_rename[nome_no_arquivo] = nome_final

    return df.rename(columns=mapa_rename)


def padronizar_pesos_replica(df):
    """
    Padroniza os nomes das 200 colunas de peso replica para minusculo
    (rep1..rep200), corrigindo a inconsistencia encontrada nos dados brutos:
    - modulo domicilios: rep1..rep200 (minusculo) em 2023, REP1..REP200
      (maiusculo) em 2024/2025
    - modulo individuos: ja vem sempre minusculo (rep1..rep200) nos 3 anos,
      entao esta funcao nao muda nada quando chamada nele

    Sem essa padronizacao, concatenar os 3 anos criaria 400 colunas em vez
    de 200 (metade ficaria NaN em cada ano), quebrando o calculo de
    Rao-Scott.
    """
    mapa_rename = {}
    for i in range(1, 201):
        for variante in (f'rep{i}', f'REP{i}'):
            if variante in df.columns:
                mapa_rename[variante] = f'rep{i}'
    return df.rename(columns=mapa_rename)
