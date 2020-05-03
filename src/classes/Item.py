from classes.Object import Object


class Item(Object):
    def __init__(self, room, name, description, droppable=True):
        super().__init__(room, name)
        self.description = description
        self.droppable = droppable
        self.equippable = False
        if self.room:
            self.add_to_room(room)

    def add_to_room(self, room):
        room.add_item(self)

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
    def __init__(self, room, name, description, amount):
        super().__init__(room, name, description)
        self.amount = amount

    def use(self, player):
        s_if = 's' if self.amount > 1 else ''
        hp = player.hp + self.amount
        player.hp = hp if hp <= player.max_hp else player.max_hp
        player.inventory.remove(self)
        print(
            f'You have been healed for {self.amount} point{s_if}. ({player.hp}/{player.max_hp})')


class Weapon(Item):
    def __init__(self, room, name, description, dmg):
        super().__init__(room, name, description)
        self.dmg = dmg
        self.equippable = True

    def use(self, player):
        player.equip(self)
        print(f'You have equipped {self.name}. ')
