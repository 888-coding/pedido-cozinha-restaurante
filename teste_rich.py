from rich.console import Console
from rich.table import Table

console = Console()

tabela = Table(title="Exempo de Tabela com Rich")

tabela.add_column("Nome", style="cyan", no_wrap=True)
tabela.add_column("Idade", justify="right", style="magenta")
tabela.add_column("País", justify="right", style="green")

tabela.add_row("João", "25", "Brasil")
tabela.add_row("João", "25", "Brasil")
tabela.add_row("João", "25", "Brasil")

console.print(tabela)

