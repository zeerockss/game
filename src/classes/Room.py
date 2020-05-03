from util import directions, printype


class Room():
    """
    A room class for the rooms in the game.
    Takes a name and a description for the room as parameters.
    """

    def __init__(self, name, description, id=0, x=None, y=None):
        self.id = id
        self.name = name
        self.description = description
        self.directions = {'n': None, 's': None, 'e': None, 'w': None}
        self.items = list()
        self.monsters = list()

    def __str__(self):
        return f'{self.name}'

    def add_item(self, item):
        self.items.append(item)

    def get_exits(self):
        return [f'{direction}: {room}' for direction, room in self.directions.items() if room is not None]

    def connect(self, direction, connecting_room):
        if direction not in connecting_room.directions:
            printype("INVALID ROOM CONNECTION")
            return None
        else:
            self.directions[direction] = connecting_room
            connecting_room.directions[directions[direction]['invert']] = self

    def get_room(self, direction):
        if direction not in self.directions:
            printype("INVALID ROOM CONNECTION")
            return None
        else:
            return self.directions[direction]

    def has_items(self):
        return len(self.items) > 0

    def has_monsters(self):
        return len(self.monsters) > 0

    def print_contents(self):
        if self.has_items():
            s_if = 's' if len(self.items) > 1 else ''
            printype(f'Item{s_if} in {self.name}: ')
            for index, item in enumerate(self.items):
                notLast = index + 1 != len(self.items)
                printype(f'\t{item.name}: {item.description}', notLast)
            print()
        if self.has_monsters():
            for monster in self.monsters:
                printype(f'A {monster.name} is in the room!\n')
            print()
        if not self.has_items() and not self.has_monsters():
            printype('There are no items here.')
