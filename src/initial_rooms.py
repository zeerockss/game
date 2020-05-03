from classes.Item import Item, Food, Weapon
from classes.Room import Room

rooms = {
    'intro': Room('Vehicle', '''A spacious SUV. The interior is perfect; no stains, new car smell. The works.'''),
    'scrapyard1': Room('Scrapyard', '''A dirty scrapyard, filled with stacked andscattered cars. There is a
    surprisingly short, dingy fence that surrounds the facility and a  rusted
    shack that lies in the West.'''),
    'scrapyard2': Room('Scrapyard Shack', '''Rusted metal on the inside and out, honestly disgusting.''')
}

items = {
    'bread': Food('Bread', 'A slice of bread. It\'s not molded yet.', 1),
    'bread': Food('Bread', 'A slice of bread. It\'s not molded yet.', 1),
    'sword': ('Sword', 'One of the skeletons dropped this.', 1)
}
