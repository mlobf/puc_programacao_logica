def apresentacar_data_filtrados_data_tipo(dados_prontos_para_apresentacao):
    import pdb

    # pdb.set_trace()
    """ 
    "Precipitação (mm)"- 17
    "Máxima (°C)" - 11
    "Mínima (°C)" - 11
    Horas de Insolação" - 18
    "Temperatura Média (°C) - 22
    Umidade Relativa (%) - 20
    "Velocidade do Vento (km/h)" - 26



    """
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
    print(" | ".join(cabecalho))
    print("-" * 80)
    for dado in lista:
        linha = [
            dado["data"],
            str(dado["nome"]),
            str(dado["age"]),
        ]
        print(" | ".join(linha))
    print(" | ".join(cabecalho))
    print("-" * 80)


def preenchimento(campo, valor):
    n_campo = len(campo)
    n_valor = len(valor)
    return n_campo - n_valor


if __name__ == "__main__":
    lista = [{"nome": "Marcos", "age": 43}]

    cabecalho = [
        "nome               ",
        "age (mm)",
    ]

    print(" | ".join(cabecalho))
    for x in lista:
        linha = [
            x["nome"] + " " * preenchimento(cabecalho[0], x["nome"]),
            str(x["age"]) + " " * preenchimento(cabecalho[1], str(x["age"])),
        ]
        print(" | ".join(linha))

    print(" | ".join(cabecalho))
    print("-" * 80)
