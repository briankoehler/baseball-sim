# import team
import simpy
import team
import inspect
from dataclasses import dataclass
from typing import List
from time import sleep


@dataclass
class Scoreboard:
    balls = 0
    strikes: int = 0
    outs: int = 0
    inning: int = 1
    half: str = 'top'
    home_runs: int = 0
    away_runs: int = 0


@dataclass
class Game:
    teams: List[team.Team]
    env: simpy.rt.RealtimeEnvironment

    def display(self, message):
        for char in message:
            if char != ' ':
                yield self.env.timeout(0.05)
            print(char, end='', flush=True)
        self.env.display.succeed()

    def opening_announcements(self):
        self.env.display = self.env.event()
        self.env.process(self.display(inspect.cleandoc(f'''Hello, everyone.  Pleasure to have you all tuning in today.
            Today the {self.teams[0].location} {self.teams[0].name} will be taking on the {self.teams[1].location} {self.teams[1].name}.''')
        ))
        yield self.env.display
        self.env.pre_game_finished.succeed()

    def half_inning(self):
        pass

    
    def run_game(self):
        self.scoreboard = Scoreboard()

        self.env.pre_game_finished = self.env.event()
        self.env.process(self.opening_announcements())
        yield self.env.pre_game_finished
        print('test')

        while True:
            self.display(f'On the mound for {self.teams[0].location} is {self.teams[0].pitcher.last_name}.')
        