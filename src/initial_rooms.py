from Room import Room
from items import items

initial_rooms = {
    'intro': Room('Vehicle', '''A spacious SUV. The interior is perfect; no stains, new car smell. The works.'''),
    'scrapyard1': Room('Scrapyard', '''A dirty scrapyard, filled with stacked andscattered cars. There is a
    surprisingly short, dingy fence that surrounds the facility.''')
}

initial_rooms['scrapyard'].add_item(items['bread'])
