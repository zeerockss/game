from classes.Player import Player


class Monster(Player):
    def __init__(self, name, room, hp, dmg):
        super().__init__(name, room, dmg=1, hp=5)
