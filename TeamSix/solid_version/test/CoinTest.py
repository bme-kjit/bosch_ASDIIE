from field import Field
from coin import Coin
from pacman import Pacman

def pacman_gets_points_on_coin_hit():
    coin_field = Field(0,0)
    coin = Coin(coin_field)
    coin_field.things.append(coin)
    pacman = Pacman(Field(0,1))

    coin.hit_by(pacman)

    assert pacman.points is 1

def coin_is_removed_on_eat():
    coin_field = Field(0,0)
    coin = Coin(coin_field)
    coin_field.things.append(coin)
    pacman = Pacman(Field(0,1))

    coin.hit_by(pacman)

    assert len(coin_field.things) is 0