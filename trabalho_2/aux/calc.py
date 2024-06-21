from aux.format import criar_lista_mes_ano, format_mes_ano, converter_mes_legivel


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
