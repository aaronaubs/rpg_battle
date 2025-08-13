import locations as loc
from characters import hero_party
from time import sleep

def show_hero_party():
    print("\nYour party:")
    print("-" * 40)
    for hero in hero_party:
        print(hero)
        sleep(0.5)
    print("-" * 40)    


if __name__ == "__main__":
    show_hero_party()
    loc.traverse_map()
