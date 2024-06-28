import pprint
from testes import grafico_barra
from datetime import datetime
from aux.load import carregar_csv
from aux.filters import (
    filtrar_range_data,
    filtrar_range_tipo,
    filtrar_base_chuvoso,
    filtrar_base_temp_minima,
    filtrar_ultimos_onze_ano,
    filtrar_ultimos_onze_anos_mes,
)
from aux.format import (
    formatar_data_pre_apresentacao,
    apresentacar_data_filtrados_data_tipo,
    criar_lista_mes_ano,
    converter_mes_legivel,
    converter,
    popular_dict_apresentacao,
)
from aux.calc import (
    somar_chuva_mes_ano,
    achar_media_temp_minima_ano,
    media_das_medias_minimas,
)
from inputs.inputs import (
    procurar_data_inicial,
    procurar_data_final,
    apresentacao_dados,
    escolher_mes,
    enviar_resposta_mes_mais_chuvoso,
    apresentacao_dados_media_minima,
)

path = "Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores.csv"

if __name__ == "__main__":

    base = carregar_csv(path=path)
    di = procurar_data_inicial()
    df = procurar_data_final(di)
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
    resposta = max(somar_chuva_mes_ano(cmc), key=lambda x: x[1])
    mes_ano_legivel = converter_mes_legivel(resposta=resposta)
    enviar_resposta = enviar_resposta_mes_mais_chuvoso(mes_ano_legivel)

    base_minima = filtrar_base_temp_minima(base)

    base_minima_onze = filtrar_ultimos_onze_ano(base_minima)
    mes_informado = escolher_mes()

    ultimos_onze = filtrar_ultimos_onze_anos_mes(
        base_minima_onze, mes_informado=mes_informado
    )
    lista_com_mes_ano = criar_lista_mes_ano(ultimos_onze)

    dict_apresentacao = apresentacao_dados_media_minima(lista_com_mes_ano, ultimos_onze)

    grafico_barra(
        dict_apresentacao,
        "temp media minima por mes e ano",
        "mes_ano",
        "Valor em Graus Celsus",
    )
    print(
        "A media das temperaturas minimas medias dos ultimos 11 anos, para o mes escolhido pelo usuario, foi ->",
        media_das_medias_minimas(dict_apresentacao),
    )
