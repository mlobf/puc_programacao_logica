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


# Funciona liso
def filtrar_base_chuvoso(base):
    # criar uma lista contendo o total de chuva por mes
    lista = []
    for x in base:
        dia = {
            "data": x.get("data"),
            "precip": x.get("precip"),
        }
        lista.append(dia)

    return lista


# Funciona liso
def filtrar_base_um_relativa_vel_vento(base):
    # criar uma lista contendo o total de chuva por mes
    lista = []
    for x in base:
        dia = {
            "data": x.get("data"),
            "um_relativa": x.get("um_relativa"),
            "vel_vento": x.get("vel_vento"),
        }
        lista.append(dia)

    return lista


def filtrar_base_temp_media(base):
    # criar uma lista contendo a temp_media
    lista = []
    for x in base:
        dia = {
            "data": x.get("data"),
            "precip": x.get("temp_media"),
        }
        lista.append(dia)

    return lista


def filtrar_range_data(data_inicial, data_final, base):
    # criar uma lista contendo a temp_media
    lista = []
    for x in base:
        if x["data"] >= data_inicial and x["data"] <= data_final:
            dia = {
                "data": x.get("data"),
                "precip": x.get("precip"),
                "maxima": x.get("maxima"),
                "minima": x.get("minima"),
                "horas_insol": x.get("horas_insol"),
                "temp_media": x.get("temp_media"),
                "um_relativa": x.get("um_relativa"),
                "vel_vento": x.get("vel_vento"),
            }

            lista.append(dia)

    return lista


def filtrar_range_tipo(tipo_de_busca, base_filtrada_por_data):

    lista = []
    tipo = converter_tipo_de_busca(tipo_de_busca=tipo_de_busca)
    import pdb

    for x in base_filtrada_por_data:
        if tipo_de_busca == "4":
            dia = {
                "data": x.get("data"),
                "um_relativa": x.get("um_relativa"),
                "vel_vento": x.get("vel_vento"),
            }
            lista.append(dia)
        elif tipo_de_busca == "2" or tipo_de_busca == "3":
            dia = {
                "data": x.get("data"),
                f"{tipo}": x.get(f"{tipo}"),
            }
            lista.append(dia)
        elif tipo_de_busca == "1":
            dia = {
                "data": x.get("data"),
                "precip": x.get("precip"),
                "maxima": x.get("maxima"),
                "minima": x.get("minima"),
                "horas_insol": x.get("horas_insol"),
                "temp_media": x.get("temp_media"),
                "um_relativa": x.get("um_relativa"),
                "vel_vento": x.get("vel_vento"),
            }
            lista.append(dia)

    return lista


def converter_tipo_de_busca(tipo_de_busca):
    if tipo_de_busca == "2":
        # precipitaca
        return "precip"
        ...
    elif tipo_de_busca == "3":
        # temperatura
        return "temp_media"
    else:
        return False
