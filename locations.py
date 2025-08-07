# Locations file

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
    
    def __str__(self):
        return f"{self.name}: {self.description}"

    def add_exit(self, direction, destination):
        self.exits[direction] = destination

    def get_details(self):
        """Show location details and """
        print(f"Current location: {self.name}")
        print(f"Info: {self.description}")
        print("\nExits: ")
        for direction, destination in self.exits.items():
            print(f"-{direction}: {destination}")


# Starting city of Luz 
luz = Location("Luz", "A bright town with a dark past.")

# Luz town square 
luz_town_square = Location("Luz Town Square", "A humble town square with a few shops beneficial for travelers.")

# Town square destinations 
luz_armory = Location("Luz Armory", "A small armor and weapons shop holding some of the region's finest equipment.")
luz_apothecary = Location("Luz Apothecary", "A local item shop with wares befitting of residents and travelers alike.")
luz_castle_entrance = Location("Luz Castle Entrance", "The entrance to the magnificent Luz Castle, home to Queen Ziphanea.")

# Luz destinations
south_forest = Location("South Forest", "A thick, dense forest filled with fog.")
east_meadows = Location("East Meadows", "A vibrant flowery landscape of gently rolling hills.")
north_mountains = Location("North Mountains", "A rugged, mountainous terrain full of jagged rocks and steep cliffs. Travelers beware.")
west_harbor = Location("West Harbor", "A bustling harbor home to many grand vessels. I wonder what lies beyond the glistening horizon...")

# North mountains destinations
narrow_pass = Location("Narrow Pass", "A narrow mountain pass.")
mountain_cave = Location("Mountain Cave", "A cave located at the entrance to the mountains. I wonder what's inside...")


# Luz exits 
luz.add_exit("Town Square", luz_town_square)
luz.add_exit("North", north_mountains)
luz.add_exit("East", east_meadows)
luz.add_exit("South", south_forest)
luz.add_exit("West", west_harbor)

# Luz town square exits 
luz_town_square.add_exit("Armory", luz_armory)
luz_town_square.add_exit("Apothecary", luz_apothecary)
luz_town_square.add_exit("Luz Castle Entrance", luz_castle_entrance)

# North mountains exits  
north_mountains.add_exit("Luz", luz)
north_mountains.add_exit("Cave", mountain_cave)
north_mountains.add_exit("Pass", narrow_pass)

# East meadows exits 
east_meadows.add_exit("Luz", luz)

# South forest exits 
south_forest.add_exit("Luz", luz)

# West harbor exits 
west_harbor.add_exit("Luz", luz)

