from datetime import datetime

# from validacoes.validacoes import validar_inteiro_no_intervalo

"""
    Adicionar a validacao de forma, caso o usuario digite um valor incorreto,
    que seja identificado o erro e que ele seja direcionado a redigitar o valor
    novamente
"""


def escolher_mes():
    while True:
        try:
            resposta = input(
                """ \n
                    Informe o numero correspondente ao mes em que vc gostaria de ver as temperatura minimas.\n
                    Digite o numero 1 para ver os dados, referente a janeiro. \n
                    Digite o numero 2 para ver os dados, referente a fevereiro. \n
                    Digite o numero 3 para ver os dados, referente a marco. \n
                    Digite o numero 4 para ver os dados, referente a abril. \n
                    Digite o numero 5 para ver os dados, referente a maio. \n
                    Digite o numero 6 para ver os dados, referente a junho. \n
                    Digite o numero 7 para ver os dados, referente a julho. \n
                    Digite o numero 8 para ver os dados, referente a agosto. \n
                    Digite o numero 9 para ver os dados, referente a setembro. \n
                    Digite o numero 10 para ver os dados, referente a outubro. \n
                    Digite o numero 11 para ver os dados, referente a novembro. \n
                    Digite o numero 12 para ver os dados, referente a dezembro. \n
                    \n"""
            )
            if int(resposta) > 0 and int(resposta) < 13:
                return resposta
        except Exception as e:
            print(
                f"Infelizmente ocorreu um erro do tipo => {e}, a sua resposta deve ser um numero de 1 a 12, tendo por correspondencia, os meses do ano"
            )


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
    mes = 12
    ano = 1999
    """
    print("")
    print("Informe a data inicial da sua procura")
    print("")
    mes = informar_mes()
    ano = informar_ano()
    """
    data = datetime(int(ano), int(mes), 1)
    data_inicial = data
    return data_inicial


def procurar_data_final(data_inicial: datetime) -> datetime:
    while True:
        try:
            mes = 12
            ano = 2024
            """
            print("")
            print("Informe a data final da sua procura")
            print("")
            mes = informar_mes()
            ano = informar_ano()
            """
            data = datetime(int(ano), int(mes), 1)
            data_final = data
            if data_final > data_inicial:
                return data_final
            else:
                print("A data final deve ser maior que a data inicial")
        except Exception as e:
            print(f"Infelizmente ocorreu um erro do tipo => {e} . Tente novamente")
def enviar_resposta_mes_mais_chuvoso(mes_ano_legivel):
    return print(
        f"O mes mais chuvoso  de todos os tempos for o mes {mes_ano_legivel["mes"]} do ano de {mes_ano_legivel["ano"]}"
    )
