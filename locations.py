# Locations file
import characters as ch
from time import sleep

class Location:
    def __init__(self, name, description, enemies=False):
        self.name = name
        self.description = description
        self.enemies = enemies
        self.exits = {}
    
    def __str__(self):
        return f"{self.name}"

    def add_exit(self, direction, destination):
        self.exits[direction] = destination

    def get_details(self):
        """Show location details and exits"""
        print(f"Current location: {self.name}")
        print(f"Info: {self.description}")
        sleep(1)
        print("\nExits: ")
        for direction, destination in self.exits.items():
            print(f"-{direction}: {destination}")


# Starting city of Luz 
luz = Location("Luz", "A bright town with a dark past.")
current_location = luz

# Luz town square 
luz_town_square = Location("Luz Town Square", "A humble town square with a few shops beneficial for travelers.")

# Town square destinations 
luz_armory = Location("Luz Armory", "A small armor and weapons shop holding some of the region's finest equipment.")
luz_apothecary = Location("Luz Apothecary", "A local item shop with wares befitting of residents and travelers alike.")
luz_castle_entrance = Location("Luz Castle Entrance", "The entrance to the magnificent Luz Castle, home to Queen Ziphanea.")

# Luz destinations
south_forest = Location("South Forest", "A thick, dense forest filled with fog.", True)
east_meadows = Location("East Meadows", "A vibrant flowery landscape of gently rolling hills.", True)
north_mountains = Location("North Mountains", "A rugged, mountainous terrain full of jagged rocks and steep cliffs. Travelers beware.", True)
west_harbor = Location("West Harbor", "A bustling harbor home to many grand vessels. I wonder what lies beyond the glistening horizon...")

# North mountains destinations
narrow_pass = Location("Narrow Pass", "A narrow mountain pass.", True)
mountain_cave = Location("Mountain Cave", "A cave located at the entrance to the mountains. I wonder what's inside...", True)


# Luz exits 
luz.add_exit("town square", luz_town_square)
luz.add_exit("north mountains", north_mountains)
luz.add_exit("east meadows", east_meadows)
luz.add_exit("south forest", south_forest)
luz.add_exit("west harbor", west_harbor)

# Luz town square exits 
luz_town_square.add_exit("armory", luz_armory)
luz_town_square.add_exit("apothecary", luz_apothecary)
luz_town_square.add_exit("castle entrance", luz_castle_entrance)
luz_town_square.add_exit("luz entrance", luz)

# Luz inner location exits
luz_armory.add_exit("town square", luz_town_square)
luz_apothecary.add_exit("town square", luz_town_square)
luz_castle_entrance.add_exit("town square", luz_town_square)

# North mountains exits  
north_mountains.add_exit("luz entrance", luz)
north_mountains.add_exit("mountain cave", mountain_cave)
north_mountains.add_exit("narrow pass", narrow_pass)

# Mountain cave exit
mountain_cave.add_exit("north mountains", north_mountains)

# Narrow pass exit
narrow_pass.add_exit("north mountains", north_mountains)

# East meadows exits 
east_meadows.add_exit("luz", luz)

# South forest exits 
south_forest.add_exit("luz", luz)

# West harbor exits 
west_harbor.add_exit("luz", luz)


# Map traversal function
def traverse_map():
    global current_location
    while True:
        current_location.get_details()
        print("-" * 30)
        print("Where would you like to go?")
        move = input("> ").strip().lower()
        print("")

        if move in current_location.exits:
            new_location = current_location.exits[move]
            current_location = new_location
            if new_location.enemies:
                enemy_party = ch.create_3_enemy_party()
                ch.show_enemy_party(enemy_party)
                ch.battle(ch.hero_party, enemy_party)
        else:
            print("You can't go that way!")


