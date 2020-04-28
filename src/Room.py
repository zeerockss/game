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
        if self.has_items():
            s_if = 's' if len(self.items) > 1 else ''
            print(f'Item{s_if} in {self.name}')
            for item in items:
                print(f'{item.name}: {item.description}')
            print()
        if self.has_monsters():
            for monster in self.monsters:
                print(f'A {monster.name} is in the room!')

    def get_exits(self):
        return [direction for direction in self.directions.keys()]

    def connect(self, direction, connecting_room):
        if direction not in connecting_room.directions:
            print("INVALID ROOM CONNECTION")
            return None
        else:
            connecting_room.direction[direction] = self

    def get_room(self, direction):
        if direction not in self.directions:
            print("INVALID ROOM CONNECTION")
            return None
        else:
            return self.directions[direction]

    def has_items(self):
        return len(self.items) > 0

    def has_monsters(self):
        return len(self.monsters) > 0
