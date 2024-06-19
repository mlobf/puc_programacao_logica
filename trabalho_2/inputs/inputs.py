from datetime import datetime

# from validacoes.validacoes import validar_inteiro_no_intervalo

"""
    Adicionar a validacao de forma, caso o usuario digite um valor incorreto,
    que seja identificado o erro e que ele seja direcionado a redigitar o valor
    novamente
"""


def apresentacao_dados() -> int:
    while True:
        try:
            apresentacao_dados = input(
                """ \n
            Informe o que você gostaria de ver em relação aos dados carregados:\n
            Digite o numero 1 para ver todos os dados, \n
            Digite o numero 2 para ver a precipitação, \n
            Digite o numero 3 para ver a temperatura, ou \n
            Digite o numero 4 para ver a umidade e vento para o período informado. \n"""
            )
            print("")
            if int(apresentacao_dados) > 0 and int(apresentacao_dados) < 5:
                return apresentacao_dados
            else:
                print("\n O numero escolhido deve ser entre 1 e 4.")

        except Exception as e:
            print("")
            print(f"Houve um erro do tipo => {e} , \n escolha uma NUMERO valido.")
            print("")


def informar_mes() -> int:
    while True:
        try:
            mes = input("Informe o repectivo mês do periodo desejado. ")
            if int(mes) > 0 and int(mes) <= 12:
                return mes
        except Exception as e:
            print(
                "O valor informado deve ser entre 1 e 12, correspondente aos meses do ano"
            )


def informar_ano() -> int:
    while True:
        try:
            ano = input("Informe o respectivo ano do periodo desejado. ")
            if int(ano) > 1499 and int(ano) <= 2024:
                return ano
        except Exception as e:
            print(
                "O valor informado deve ser entre o ano de 1500 e o ano corrente 2024"
            )


def procurar_data_inicial() -> datetime:
    """
    mes = 12
    ano = 1999
    """
    print("")
    print("Informe a data incial da sua procura")
    print("")
    mes = informar_mes()
    ano = informar_ano()
    data = datetime(int(ano), int(mes), 1)
    data_inicial = data
    return data_inicial


def procurar_data_final(data_inicial: datetime) -> datetime:
    while True:
        try:
            """
            mes = 12
            ano = 2024
            """
            print("")
            print("Informe a data final da sua procura")
            print("")
            mes = informar_mes()
            ano = informar_ano()
            data = datetime(int(ano), int(mes), 1)
            data_final = data
            if data_final > data_inicial:
                return data_final
            else:
                print("A data final deve ser maior que a data inicial")
        except Exception as e:
            print(f"Infelizmente ocorreu um erro do tipo => {e} . Tente novamente")
