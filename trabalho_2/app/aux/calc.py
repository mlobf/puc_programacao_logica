from app.aux.format import (
    criar_lista_mes_ano,
    format_mes_ano,
    converter_mes_legivel,
    converter,
)


def soma_mes(mes_ano, cmc, key: str):
    # Funciona liso
    import pdb

    acumulado = []
    for x in cmc:
        if mes_ano == format_mes_ano(x["data"]):
            acumulado.append(float(x.get(key)))
    return (mes_ano, sum(acumulado))


def somar_chuva_mes_ano(cmc):
    # retorna uma lista com todos os mes_ano e
    # a respectiva somatoria de chuva no mes.
    lista_mes_ano = criar_lista_mes_ano(cmc)
    lista_acumulado = []
    for x in lista_mes_ano:
        sm = soma_mes(x, cmc, "precip")
        lista_acumulado.append(sm)

    return lista_acumulado


def achar_media_temp_minima_ano(lista_com_mes_ano, ultimos_onze):
    lista = []
    for x in lista_com_mes_ano:
        lista_valores = []
        for y in ultimos_onze:
            valor = converter(y)
            if x == valor:
                lista_valores.append(float(y.get("minima")))
                # lista.append(float(y.get("minima")))
                # dict_mes = {"data": mes_ano, "valor": float(y.get("minima"))}
        mes_ano = {"data": x, "valores": lista_valores}
        lista.append(mes_ano)

    return lista


def media_das_medias_minimas(apresentacao_dados_media_minima):
    import pdb

    # pdb.set_trace()
    soma_temp = []
    for x, y in apresentacao_dados_media_minima.items():
        soma_temp.append(y)
    return sum(soma_temp) / len(soma_temp)
