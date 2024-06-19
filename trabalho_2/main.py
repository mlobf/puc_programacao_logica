import csv
import pprint
from datetime import datetime
from validacoes.vaidacoes import valida_int, valida_mes, validar_inteiro_no_intervalo
from inputs.inputs import (
    apresentacao_dados,
    procurar_data_final,
    procurar_data_inicial,
    validar_inteiro_no_intervalo,
)


def carregar_csv(path):
    base = []
    with open(path, mode="r") as arquivo_csv:
        for x in csv.DictReader(arquivo_csv):
            elemento = {
                "data": datetime.strptime(x.get("data"), "%d/%m/%Y"),
                "precip": x.get("precip"),
                "maxima": x.get("maxima"),
                "minima": x.get("minima"),
                "horas_insol": x.get("horas_insol"),
                "temp_media": x.get("temp_media"),
                "um_relativa": x.get("um_relativa"),
                "vel_vento": x.get("vel_vento"),
            }
            base.append(elemento)

    return base


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


def format_mes_ano(x):
    # Funciona liso
    mes = x.month
    ano = x.year
    mes_ano = str(mes) + "_" + str(ano)
    return mes_ano


def criar_lista_mes_ano(lista):
    lista_mes_ano = []
    for x in lista:
        # print(datetime.strptime(str(x.get("data")), "%d/%m/%Y"))
        mes = x.get("data").month
        ano = x.get("data").year
        mes_ano = str(mes) + "_" + str(ano)
        format_mes_ano(x.get("data"))

        lista_mes_ano.append(mes_ano)
    return sorted(list(set(lista_mes_ano)))


def soma_mes(mes_ano, cmc):
    # Funciona liso
    import pdb

    acumulado = []
    for x in cmc:
        if mes_ano == format_mes_ano(x["data"]):
            acumulado.append(float(x.get("precip")))
    return (mes_ano, sum(acumulado))


def somar_chuva_mes_ano(cmc):
    # retorna uma lista com todos os mes_ano e
    # a respectiva somatoria de chuva no mes.
    lista_mes_ano = criar_lista_mes_ano(cmc)
    lista_acumulado = []
    for x in lista_mes_ano:
        sm = soma_mes(x, cmc)
        lista_acumulado.append(sm)

    return lista_acumulado


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


def filtrar_range_tipo(tipo_de_busca, base_filtrada_por_data):

    lista = []
    tipo = converter_tipo_de_busca(tipo_de_busca=tipo_de_busca)
    import pdb

    for x in base:
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


def formatar_data_pre_apresentacao(range_filtrado_por_data_e_tipo):
    import pdb

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

def preenchimento(campo, valor):
    n_campo = len(campo)
    n_valor = len(valor)
    return n_campo - n_valor

def apresentacar_data_filtrados_data_tipo(dados_prontos_para_apresentacao):
    import pdb
    #pdb.set_trace()
    """ 
    "Precipitação (mm)"- 17
    "Máxima (°C)" - 11
    "Mínima (°C)" - 11
    Horas de Insolação" - 18
    "Temperatura Média (°C) - 22
    Umidade Relativa (%) - 20
    "Velocidade do Vento (km/h)" - 26



    """
    cabecalho = ["Data               ", "Precipitação (mm)", "Máxima (°C)", "Mínima (°C)", 
    "Horas de Insolação", "Temperatura Média (°C)", 
    "Umidade Relativa (%)", "Velocidade do Vento (km/h)"]
    print(" | ".join(cabecalho))
    print("-" * 80)
    for dado in dados_prontos_para_apresentacao:
        linha = [
            dado["data"],
            str(dado["precip"]) + " " * preenchimento(cabecalho[1], str(dado["precip"])),
            str(dado["maxima"]) + " " * preenchimento(cabecalho[2], str(dado["maxima"])),
            str(dado["minima"]) + " " * preenchimento(cabecalho[3], str(dado["minima"])),
            str(dado["horas_insol"]) + " " * preenchimento(cabecalho[4], str(dado["horas_insol"])),
            str(dado["temp_media"]) + " " * preenchimento(cabecalho[5], str(dado["temp_media"])),
            str(dado["um_relativa"]) + " " * preenchimento(cabecalho[6], str(dado["um_relativa"])),
            str(dado["vel_vento"]) + " " * preenchimento(cabecalho[7], str(dado["vel_vento"])),
        ]
        print(" | ".join(linha))
    print(" | ".join(cabecalho))
    print("-" * 80)




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


path = "Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores.csv"


base = carregar_csv(path=path)

di = procurar_data_inicial()
df = procurar_data_final()
range_filtrado_por_data = filtrar_range_data(di, df, base)
ad = apresentacao_dados()
range_filtrado_por_data_e_tipo = filtrar_range_tipo(
    tipo_de_busca=ad, base_filtrada_por_data=range_filtrado_por_data
)
dados_prontos_para_apresentacao = formatar_data_pre_apresentacao(
    range_filtrado_por_data_e_tipo
)
apresentacar_data_filtrados_data_tipo(dados_prontos_para_apresentacao)

cmc = filtrar_base_chuvoso(base) 

#print(soma_mes("2_1995", base))

resposta = max(somar_chuva_mes_ano(cmc), key=lambda x: x[1])
mes_ano_legivel = converter_mes_legivel(resposta=resposta)
print('')
print('')
print('')
print(
    f"O mes mais chuvoso  de todos os tempos for o mes {mes_ano_legivel["mes"]} do ano de {mes_ano_legivel["ano"]}"
)
print('')
print('')
print('')

