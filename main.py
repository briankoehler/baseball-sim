import simpy
import player
from dataclasses import dataclass


@dataclass
class Pitcher:
    name: str
    age: int
    env: simpy.rt.RealtimeEnvironment

    def pitch(self):
        self.env.live_pitch.succeed()
        print(f'{self.name} pitches a fastball.')

@dataclass
class Batter:
    name: str
    age: int
    env: simpy.rt.RealtimeEnvironment

    def run(self):
        yield self.env.live_pitch
        yield self.env.timeout(3)
        print(f'{self.name} swings and misses.')

if __name__ == '__main__':
    env = simpy.rt.RealtimeEnvironment(factor=1)
    # env.live_pitch = env.event()
    # tom = Pitcher('Tom', 24, env)
    # jerry = Batter('Jerry', 22, env)
    # env.process(jerry.run())
    # tom.pitch()
    # env.run()
