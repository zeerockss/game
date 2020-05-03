class Object():
    def __init__(self, room, name):
        self.room = room
        self.name = name

    def __str__(self):
        return self.name
