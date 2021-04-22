import simpy
import player
import game
import team
import random


first_names = ['Brian', 'Jacob', 'Jon', 'Zach', 'Adrian', 'Alex', 'Matteen', 'Anthony', 'Nick', 'Trevor', 'Carlos']
last_names = ['Koehler', 'Francisco', 'Becker', 'Holt', 'Kashef', 'Flowers', 'Story', 'Rodon', 'Wilson', 'Schickler', 'Rodriguez', 'Senzel', 'Glasnow', 'Trout']
locations = ['New York', 'Jacksonville', 'Gainesville', 'Orlando', 'Tallahassee', 'Atlanta']
team_names = ['Inters', 'Feeders', 'Ducklings', 'Hammers', 'Gamers', 'Worms']


def generate_batter(env):
    return player.Batter(random.choice(first_names), random.choice(last_names), random.randint(17, 45), env)

def generate_pitcher(env):
    return player.Pitcher(random.choice(first_names), random.choice(last_names), random.randint(17, 45), env)

def generate_team(env):
    players = []
    for _ in range(7):
        new_player = generate_batter(env)
        players.append(new_player)
    pitcher = generate_pitcher(env)
    players.append(pitcher)
    return team.Team(random.choice(locations), random.choice(team_names), players, players, pitcher)


if __name__ == '__main__':
    env = simpy.rt.RealtimeEnvironment(factor=1, strict=False)
    game = game.Game([generate_team(env), generate_team(env)], env)
    env.process(game.run_game())
    env.run()
