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
    lista = []
    data_atual = datetime.now()
    data_anterior = data_atual - relativedelta(years=11)
    for x in base_minima:
        import pdb

        # pdb.set_trace()
        if x.get("data").year >= data_anterior.year:
            lista.append(x)
    return lista


def filtar_ultimos_onze_anos_mes(base_filtrada, mes_informado):
    """Pega a base convertida contendo os ultimos 11 anos e separa somente\n
    o mes informado pelo usuario por todo periodo abrangido
    """
    lista = []
    for x in base_filtrada:
        if x.get("data").month == mes_informado:
            lista.append(x)
    return lista
