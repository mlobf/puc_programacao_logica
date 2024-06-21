import csv
from datetime import datetime


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
