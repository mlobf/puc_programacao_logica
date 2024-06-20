from datetime import *
from dateutil.relativedelta import relativedelta

""" 
(X) c) Média da temperatura mínima de um determinado mês (auge do inverno) nos últimos 11 anos (2006 a 2016): 
    Meus comentarios.
    sic - Qual a temperatura media de 'agosto' dos ultimos 11 anos.....por exemplo.
"""


def filtrar_base_temp_minima(base):
    # criar uma lista contendo a temp_media
    lista = []
    for x in base:
        dia = {
            "data": x.get("data"),
            "minima": x.get("minima"),
        }
        lista.append(dia)

    return lista


def filtrar_ultimos_onze_ano(base_minima):
    """Estou alterando pois a base de dados nao possui registros atuais \n
    desta forma, nao posso realizar o calculo de forma dinamica.
    2006 a 2016.
    """
    lista = []
    data_atual = datetime.now()
    data_anterior = data_atual - relativedelta(years=11)
    for x in base_minima:
        # if x.get("data").year >= data_anterior.year:
        if int(x.get("data").year) >= 2006 and int(x.get("data").year) <= 2016:
            lista.append(x)
    return lista


def filtrar_ultimos_onze_anos_mes(base_filtrada: list, mes_informado: int) -> list:
    """Pega a base convertida contendo os ultimos 11 anos e separa somente\n
    o mes informado pelo usuario por todo periodo abrangido
    """
    import pdb

    # pdb.set_trace()
    lista = []
    for x in base_filtrada:
        if int(x.get("data").month) == int(mes_informado):
            lista.append(x)
    return lista
