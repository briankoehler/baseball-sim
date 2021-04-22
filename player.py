import simpy
from dataclasses import dataclass


@dataclass
class Player:
    first_name: str
    last_name: str
    age: int
    env: simpy.rt.RealtimeEnvironment


@dataclass
class Batter(Player):

    def bat(self):
        yield self.env.live_pitch
        yield self.env.timeout(0.5)
        print(f'{self.first_name} {self.last_name} swings and misses.')


@dataclass
class Pitcher(Player):

    def pitch(self):
        self.env.live_pitch.succeed()
        print(f'{self.first_name} {self.last_name} pitches a fastball.')
