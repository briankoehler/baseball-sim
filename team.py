from dataclasses import dataclass
from player import Player
from typing import Set, List


@dataclass
class Team:
    location: str
    name: str
    players: Set[Player]
    lineup: List[Player]
    pitcher: Player
