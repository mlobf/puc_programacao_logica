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

class LargeFileProcessor:
    """Load big files"""
    def __init__(self, file_path):
        self.file_path = file_path

    def __iter__(self):
        with open(self.file_path, 'r') as file:
            for line in file:
                yield line.strip()

# Uso
"""
processor = LargeFileProcessor('large_file.txt')
for line in processor:
    print(line)
"""
