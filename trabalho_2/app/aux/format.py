from datetime import datetime


def preenchimento(campo, valor):
    n_campo = len(campo)
    n_valor = len(valor)
    return n_campo - n_valor


def apresentacar_data_filtrados_data_tipo(dados_prontos_para_apresentacao):
    cabecalho = [
        "Data               ",
        "Precipitação (mm)",
        "Máxima (°C)",
        "Mínima (°C)",
        "Horas de Insolação",
        "Temperatura Média (°C)",
        "Umidade Relativa (%)",
        "Velocidade do Vento (km/h)",
    ]
    print("-" * 165)
    print(" | ".join(cabecalho))
    print("-" * 165)
    for dado in dados_prontos_para_apresentacao:
        linha = [
            dado["data"],
            str(dado["precip"])
            + " " * preenchimento(cabecalho[1], str(dado["precip"])),
            str(dado["maxima"])
            + " " * preenchimento(cabecalho[2], str(dado["maxima"])),
            str(dado["minima"])
            + " " * preenchimento(cabecalho[3], str(dado["minima"])),
            str(dado["horas_insol"])
            + " " * preenchimento(cabecalho[4], str(dado["horas_insol"])),
            str(dado["temp_media"])
            + " " * preenchimento(cabecalho[5], str(dado["temp_media"])),
            str(dado["um_relativa"])
            + " " * preenchimento(cabecalho[6], str(dado["um_relativa"])),
            str(dado["vel_vento"])
            + " " * preenchimento(cabecalho[7], str(dado["vel_vento"])),
        ]
        print(" | ".join(linha))
    print("-" * 165)
    print(" | ".join(cabecalho))
    print("-" * 165)


def converter_mes_legivel(resposta):
    mes = resposta[0].split("_")
    if str(mes[0]) == "1":
        mes[0] = "janeiro"
    elif str(mes[0]) == "2":
        mes[0] = "fevereiro"
    elif str(mes[0]) == "3":
        mes[0] = "março"
    elif str(mes[0]) == "4":
        mes[0] = "abril"
    elif str(mes[0]) == "5":
        mes[0] = "maio"
    elif str(mes[0]) == "6":
        mes[0] = "junho"
    elif str(mes[0]) == "7":
        mes[0] = "julho"
    elif str(mes[0]) == "8":
        mes[0] = "agosto"
    elif str(mes[0]) == "9":
        mes[0] = "setembro"
    elif str(mes[0]) == "10":
        mes[0] = "outubro"
    elif str(mes[0]) == "11":
        mes[0] = "novembro"
    elif str(mes[0]) == "12":
        mes[0] = "dezembro"
    return {"mes": mes[0], "ano": mes[1]}


def format_mes_ano(x):
    # Funciona liso
    mes = x.month
    ano = x.year
    mes_ano = str(mes) + "_" + str(ano)
    return mes_ano


def criar_lista_mes_ano(lista):
    """ """
    lista_mes_ano = []
    for x in lista:
        mes = x.get("data").month
        ano = x.get("data").year
        mes_ano = str(mes) + "_" + str(ano)
        format_mes_ano(x.get("data"))

        lista_mes_ano.append(mes_ano)
    return sorted(list(set(lista_mes_ano)))


def formatar_data_pre_apresentacao(range_filtrado_por_data_e_tipo):

    # o range esta vindo correto
    lista = []
    for x in range_filtrado_por_data_e_tipo:
        dia = {
            "data": str(x.get("data")),
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


def converter(data: datetime) -> str:
    """Recebe um objeto datatime e devolve um string
    contendo o respectivo padrao mes_ano, por exemplo:
    -->  2_2022
    """

    mes = data.get("data").month
    ano = data.get("data").year

    return str(mes) + "_" + str(ano)


def popular_dict_apresentacao(lista_apresentacao_dados_media_minima: list) -> dict:
    for x in lista_apresentacao_dados_media_minima:
        dict_apresentacao = {str(x.get("data")): x.get("media")}
        dict_apresentacao.update(x)
    return dict_apresentacao
