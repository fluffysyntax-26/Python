import random

class Adventurer: 
    '''
    Represents the player in our game,
    The Adventurer moves throughout the Cave system going from Room to Room trying to slay Monsters.
    '''
    def __init__(self, name: str) -> None: 
        self.name: str = name
        self.strength: int = random.randint(3, 18)
        self.constitution: int = random.randint(3,18)
        self.hit_points: int = self.constitution + random.randint(1, 8)
        self.bag: list[Item] = []
        
class Item: 
    '''An item which can be held by an Adventurer.
    Items are weapons in this game, and may have a range of possible damages they can inflict    
    '''
    def __init__(self, name: str, min_damage: int, max_damage: int) -> None: 
        
        # input validation
        if name != None: 
            self.name = name
        else: 
            self.name = "Unknown Item"
            
        self.min_damage: int = min_damage
        self.max_damage: int = max_damage 
    
class Cave: 
    '''
    Represents the cave system
    '''
    def __init__(self, rooms: list[str]):
        self.rooms = [room]
        
class Room: 
    '''
    A Room contains a monster and treasure
    the treasure can be obtained after defeating the monster
    '''
    def __init__(self, monster: Monster, treasure: Item): 
        self.monster = monster
        self.treasure = treasure 
        
class Monster: 
    '''
    An entity which attacks the adventurer
    '''
    def __init__(self, name: str, min_dmg: int, max_dmg: int): 
        self.name = name
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        
        
player = Adventurer("Deepak")