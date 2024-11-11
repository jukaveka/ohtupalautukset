import requests
from rich import print as rprint
from rich.prompt import Prompt
from rich.table import Table
from rich.console import Console
from player import Player
from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    rprint("[italic]NHL statistics by nationality[/italic]")
    print("")

    season = Prompt.ask("Select season", choices=["2019/20", "2020/21", "2021/22", "2022/23", "2023/24", "2024/25"])
    season = season.strip('"')
    season = season.replace('/', '-')
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"

    nationality = Prompt.ask("Select nationality", choices=["AUT", "AUS", "CZE", "SWE", "GER", "DEN", "SUI", "SVK", "NOR", "RUS", "CAN", "LAT", "BLR", "SLO", "USA", "FIN", "GBR"])
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality)
    
    table = Table(title=f"Top scorers of {nationality} for season {season}")

    table.add_column("name", style="blue")
    table.add_column("team", style="magenta")
    table.add_column("goals", style="green")
    table.add_column("assists", style="green")
    table.add_column("points", style="green")

    for player in players:
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.points))

    console = Console()
    console.print(table)

if __name__ == "__main__":
	main()
