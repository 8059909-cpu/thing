# Office Entrance System

class OfficeEntrance:
    def __init__(self, entrance_name, defense_system):
        self.entrance_name = entrance_name
        self.defense_system = defense_system

entrances = [
    OfficeEntrance('left vent', 'motion sensor'),
    OfficeEntrance('right vent', 'camera system'),
    OfficeEntrance('hallway', 'armed guard')
]

for entrance in entrances:
    print(f'Entrance: {entrance.entrance_name}, Defense System: {entrance.defense_system}')
