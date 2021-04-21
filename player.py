import simpy
from dataclasses import dataclass


@dataclass
class Player:
    first_name: str
    last_name: str
    age: int


@dataclass
class Fielder(Player):
    pass


@dataclass
class Pitcher(Player):
    pass
