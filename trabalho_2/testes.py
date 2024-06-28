from rich.console import Console
from rich.table import Table

console = Console()

# Dados para o gráfico de barras
""" 
data = {
    "Janeiro": 10,
    "Fevereiro": 15,
    "Março": 7,
    "Abril": 22,
    "Maio": 5,
    "Junho": 18,
}
"""


def grafico_barra(
    dict_mes_temp: dict,
    nome_do_grafico: str,
    nome_primeira_coluna: str,
    nome_segunda_coluna: str,
) -> Table:
    # Cria uma tabela para exibir o gráfico de barras
    table = Table(title=nome_do_grafico)
    # Adiciona colunas para a tabela
    table.add_column(nome_primeira_coluna, justify="right", style="cyan", no_wrap=True)
    table.add_column(nome_segunda_coluna, justify="right", style="magenta")
    table.add_column("Gráfico", style="green")

    # Adiciona linhas com os dados e barras
    import pdb

    # pdb.set_trace()
    for month, value in dict_mes_temp.items():
        bar = "█" * int(value)
        table.add_row(month, str(value), bar)

    # Exibe a tabela com o gráfico de barras no terminal
    console.print(table)


# grafico_barra(data)
