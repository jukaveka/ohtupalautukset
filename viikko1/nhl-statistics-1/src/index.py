from statistics_service import StatisticsService, SortBy
from player_reader import PlayerReader


def main():
    stats = StatisticsService(
        PlayerReader("https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt")
    )
    philadelphia_flyers_players = stats.team("PHI")
    top_scorers_without_enum = stats.top(10)
    top_scorers = stats.top(10, SortBy.POINTS)
    top_goals = stats.top(10, SortBy.GOALS)
    top_assists = stats.top(10, SortBy.ASSISTS)

    print("Philadelphia Flyers:")
    for player in philadelphia_flyers_players:
        print(player)

    print("Top point getters:")
    for player in top_scorers_without_enum:
        print(player)

    print("Top point getters:")
    for player in top_scorers:
        print(player)

    print("Top goal scorers:")
    for player in top_goals:
        print(player)

    print("Top assist getters:")
    for player in top_assists:
        print(player)


if __name__ == "__main__":
    main()
