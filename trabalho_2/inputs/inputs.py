from datetime import datetime
from validacoes.vaidacoes import validar_inteiro_no_intervalo


def apresentacao_dados() -> int:
    apresentacao_dados = input(
        """ \n
    Informe o que você gostaria de ver em relação aos dados carregados:\n
    Digite o numero 1 para ver todos os dados, \n
    Digite o numero 2 para ver a precipitação, \n
    Digite o numero 3 para ver a temperatura, ou \n
    Digite o numero 4 para ver a umidade e vento para o período informado. \n"""
    )
    if validar_inteiro_no_intervalo(apresentacao_dados, 1, 4):
        return apresentacao_dados


def procurar_data_final():
    mes = input("Informe o mês da data final ")
    ano = input("Informe o ano da data final ")
    """
    mes = 12
    ano = 2020
    """
    if validar_inteiro_no_intervalo(mes, 1, 12) and validar_inteiro_no_intervalo(
        ano, 1500, 2024
    ):
        data = datetime(int(ano), int(mes), 1)
        data_final = data
        return data_final


def procurar_data_inicial():
    """
    mes = 12
    ano = 1997
    """
    mes = input("Informe o mês da data inicial ")
    ano = input("Informe o ano da data inicial")
    if validar_inteiro_no_intervalo(mes, 1, 12) and validar_inteiro_no_intervalo(
        ano, 1500, 2024
    ):
        data = datetime(int(ano), int(mes), 1)
        data_inicial = data
        return data_inicial
