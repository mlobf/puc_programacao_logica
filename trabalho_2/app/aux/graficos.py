from rich.console import Console
from rich.table import Table


class Chart:
    """Simple abstration for terminal charts"""

    console = Console()

    def __init__(
        self,
        dict_mes_temp: dict,
        nome_do_grafico: str,
        nome_primeira_coluna: str,
        nome_segunda_coluna: str,
    ) -> Table:

        self.dict_mes_temp = dict_mes_temp
        self.nome_do_grafico = nome_do_grafico
        self.nome_primeira_coluna = nome_primeira_coluna
        self.nome_segunda_coluna = nome_segunda_coluna

    @property
    def show_bar_chart(self):
        """Show bar chart at terminal"""
        # Cria uma tabela para exibir o gráfico de barras
        table = Table(title=self.nome_do_grafico)
        # Adiciona colunas para a tabela
        table.add_column(
            self.nome_primeira_coluna, justify="right", style="cyan", no_wrap=True
        )
        table.add_column(self.nome_segunda_coluna, justify="right", style="magenta")
        table.add_column("Gráfico", style="green")

        for month, value in self.dict_mes_temp.items():
            barra = "█" * int(value)
            table.add_row(month, str(value), barra)

        self.console.print(table)
