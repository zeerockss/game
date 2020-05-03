from classes.Object import Object


class Humanoid(Object):
    def __init__(self, name, room, dmg, hp):
        super().__init__(name)
        self.room = room
        self.dmg = dmg
        self.hp = hp
        self.max_hp = hp
        self.inventory = list()
        self.blocking = False

    def __str__(self):
        return f'{self.name}: ', '{\n', f'\t[\n\t\thp: {self.hp}/{self.max_hp},\n\t\tdmg: {self.dmg}]'

    def move(self, room):
        self.room = room

    def add_item(self, item):
        item.take(self, self.room)

    def take_damage(self, attacker):
        if not self.blocking:
            self.hp -= attacker.dmg
            print(f'{self.name} took {attacker.dmg} damage! {self.hp}/{self.max_hp}')
        else:
            self.blocking = False
            print(f'{self.name} blocked your attack!')

    def block(self):
        self.blocking = True

    def print_health(self):
        print(f'{self.name}\'s hp: {self.hp}/{self.max_hp}')
