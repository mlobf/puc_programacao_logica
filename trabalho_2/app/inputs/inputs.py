"""
Classes relacionadas com a interacao do usuario.
"""

from datetime import datetime
from app.aux.calc import achar_media_temp_minima_ano
from app.aux.format import converter_mes_legivel

# from aux.calc import apresentacao_dados_media_minima

# from validacoes.validacoes import validar_inteiro_no_intervalo


class Perguntas:
    """Classe que contempla as perguntas a serem feitas para o usuario"""

    def escolher_mes(self) -> str:
        """Pergunta para o usuario qual mes sera selecionado"""

        while True:
            try:
                resposta = input(
                    """ \n
                        Informe o numero correspondente ao mes em que vc \n
                        gostaria de ver as temperatura minimas.\n
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
            except Exception as error:
                print(
                    """f"Infelizmente ocorreu um erro do tipo => {error}, /n
                    a sua resposta deve ser um numero de 1 a 12, /n
                    tendo por correspondencia, os meses do ano"""
                )

    def apresentacao_dados(self) -> int:
        """Pergunta para o usuario qual é a forma de apresentacao dos dados"""

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

    @property
    def informar_mes(self) -> int:
        """Pergunta ao usuario qual sera o mes escolhido"""

        while True:
            try:
                mes = input("Informe o repectivo mês do periodo desejado. ")
                if int(mes) > 0 and int(mes) <= 12:
                    return mes
            except Exception as error:
                print(
                    """Ocorreu um erro do tipo {error}. n/
                    O valor informado deve ser entre 1 e 12, correspondente aos meses do ano"""
                )

    @property
    def informar_ano(self) -> int:
        """Pergunta ao usuario qual sera o ano escolhido"""
        while True:
            try:
                ano = input("Informe o respectivo ano do periodo desejado. ")
                if int(ano) > 1499 and int(ano) <= 2024:
                    return ano
            except Exception as e:
                print(
                    "O valor informado deve ser entre o ano de 1500 e o ano corrente 2024"
                )

    @property
    def procurar_data_inicial(self) -> datetime:
        """Pergunta ao usuario qual sera a data inicial"""
        # mes = 12
        # ano = 1999
        print("")
        print("Informe a data inicial da sua procura")
        print("")
        mes = self.informar_mes
        ano = self.informar_ano
        data = datetime(int(ano), int(mes), 1)
        data_inicial = data

        return data_inicial

    def procurar_data_final(self, data_inicial: datetime) -> datetime:
        """Pergunta ao usuario qual sera a data final"""

        while True:
            try:
                print("")
                print("Informe a data final da sua procura")
                print("")
                mes = self.informar_mes
                ano = self.informar_ano
                data = datetime(int(ano), int(mes), 1)
                data_final = data
                if data_final > data_inicial:
                    return data_final
                else:
                    print("A data final deve ser maior que a data inicial")
            except Exception as e:
                print(f"Infelizmente ocorreu um erro do tipo => {e} . Tente novamente")

    def enviar_resposta_mes_mais_chuvoso(self, mes_ano_legivel):
        """Envia a resposta ao usuario informando qual sera o mes mais chuvoso"""

        return print(
            f"O mes mais chuvoso  de todos os tempos for o mes {mes_ano_legivel["mes"]} do ano de {mes_ano_legivel["ano"]}"
        )

    def apresentacao_dados_media_minima(self, lista_com_mes_ano, ultimos_onze) -> list:
        """Apresenta ao usuario a media minima"""
        dict_medias = {}
        for x in achar_media_temp_minima_ano(lista_com_mes_ano, ultimos_onze):
            dict_medias.update(
                {
                    str(x.get("data")): float(
                        sum(x.get("valores")) / len(x.get("valores"))
                    ),
                }
            )

        return dict_medias
