from rich.console import Console
from rich.table import Table

console = Console()

# Dados para o gráfico de barras
data = {
    "Janeiro": 10,
    "Fevereiro": 15,
    "Março": 7,
    "Abril": 22,
    "Maio": 5,
    "Junho": 18,
}


def grafico_barra(dict_mes_temp: dict) -> Table:
    # Cria uma tabela para exibir o gráfico de barras
    table = Table(title="Gráfico de Barras")

    # Adiciona colunas para a tabela
    table.add_column("Mês", justify="right", style="cyan", no_wrap=True)
    table.add_column("Valor", justify="right", style="magenta")
    table.add_column("Gráfico", style="green")

    # Adiciona linhas com os dados e barras
    for month, value in data.items():
        bar = "█" * value
        table.add_row(month, str(value), bar)

    # Exibe a tabela com o gráfico de barras no terminal
    console.print(table)


grafico_barra(data)
