from classes.Object import Object


class Item(Object):
    def __init__(self, name, description):
        super().__init__(name)
        self.description = description
        self.droppable = True
        self.equippable = False

    def take(self, player, room):
        player.inventory.append(self)
        room.items.remove(self)
        print(f'You have picked up {self.name}.')

    def drop(self, player, room):
        player.inventory.remove(self)
        room.items.append(self)
        print(f'You have dropped {self.name}.')

    def use(self, player):
        print(f'You cannot use {self.name}.')


class Food(Item):
    def __init__(self, name, description, amount):
        super().__init__(name, description)
        self.amount = amount

    def use(self, player):
        s_if = 's' if self.amount > 1 else ''
        hp = player.hp + self.amount
        player.hp = hp if hp <= player.max_hp else player.max_hp
        player.inventory.remove(self)
        print(
            f'You have been healed for {self.amount} point{s_if}. ({player.hp}/{player.max_hp})')


class Weapon(Item):
    def __init__(self, name, description, dmg):
        super().__init__(name, description)
        self.dmg = dmg
        self.equippable = True

    def use(self, player):
        player.equip(self)
        print(f'You have equipped {self.name}. ')
