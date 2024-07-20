"""Main aux calculation"""

from app.aux.format import (
    criar_lista_mes_ano,
    format_mes_ano,
    converter,
)


def soma_mes(mes_ano, cmc, key: str):
    """Realiza a soma de um periodo especifico"""

    acumulado = []
    for x in cmc:
        if mes_ano == format_mes_ano(x["data"]):
            acumulado.append(float(x.get(key)))
    return (mes_ano, sum(acumulado))


def somar_chuva_mes_ano(cmc):
    """retorna uma lista com todos os mes/ano
    e sua respectiva somatoria de chuva acumulada"""

    lista_mes_ano = criar_lista_mes_ano(cmc)
    lista_acumulado = []
    for x in lista_mes_ano:
        sm = soma_mes(x, cmc, "precip")
        lista_acumulado.append(sm)

    return lista_acumulado


def achar_media_temp_minima_ano(lista_com_mes_ano, ultimos_onze):
    """Encontra a temperatura media minima do ano"""

    lista = []
    for x in lista_com_mes_ano:
        lista_valores = []
        for y in ultimos_onze:
            valor = converter(y)
            if x == valor:
                lista_valores.append(float(y.get("minima")))
        mes_ano = {"data": x, "valores": lista_valores}
        lista.append(mes_ano)

    return lista


def media_das_medias_minimas(apresentacao_dados_media_minima):
    """Calcula a medias das temperaturas minimas"""

    soma_temp = []
    for x, y in apresentacao_dados_media_minima.items():
        soma_temp.append(y)
    return sum(soma_temp) / len(soma_temp)
