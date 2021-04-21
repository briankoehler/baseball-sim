from dataclasses import dataclass


@dataclass
class Scoreboard:
    balls: int
    strikes: int
    outs: int
    home_runs: int
    away_runs: int