from classes.Humanoid import Humanoid
from classes.Item import Weapon, equippable


class Player(Humanoid):
    def __init__(self, room, name, dmg, hp):
        super().__init__(room, name=input('Enter your name: '), dmg=1, hp=10)
        self.equipped = None

    def __str__(self):
        return f'{self.name}: ', '{\n', f'\t[\n\t\thp: {self.hp}/{self.max_hp},\n\t\tdmg: {self.dmg}\n\tequipped: {self.equipped}\n]'

    def use_item(self, item):
        item.use(self)

    def print_inventory(self):
        if len(self.inventory):
            print(f'\n{self.name}\'s Inventory:')
            for inventory_item in self.inventory:
                print(f'\t{inventory_item.name}: {inventory_item.description}')
        else:
            print(
                '\nYou have no items in your inventory.\n\nTry roaming around to find some items.')

    def take_damage(self, attacker):
        if not self.blocking:
            self.hp -= attacker.dmg
            if self.hp <= 0:
                print('You have died. Better luck next time!')
            else:
                print(
                    f'You were hit with {attacker.dmg} damage. ({self.hp}/{self.max_hp})')
        else:
            self.blocking = False
            print('You blocked {attacker.name}\'s attack!')

    def equip(self, item):
        if item.equippable:
            item.use(self)
