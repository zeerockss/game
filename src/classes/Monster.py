from classes.Humanoid import Humanoid


class Monster(Humanoid):
    def __init__(self, name, room, hp, dmg):
        super().__init__(name, room, dmg=1, hp=5)
