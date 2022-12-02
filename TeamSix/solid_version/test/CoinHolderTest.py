from coin_holder import Coin_holder
from pacman import Pacman

def pacman_is_accepted():
    coin_holder = Coin_holder(1, 0)
    pacman = Pacman(Coin_holder(0,0))

    coin_holder.accept(pacman)

    assert len(coin_holder.things) == 1
    assert pacman is coin_holder.things
    assert pacman.field == coin_holder

def pacman_is_removed_from_origin_field():
    coin_holder = Coin_holder(1, 0)
    origin = Coin_holder(0,0)
    pacman = Pacman()

    coin_holder.accept(pacman)


    assert len(origin.things) == 0

