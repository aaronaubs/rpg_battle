import main
import random as r
from time import sleep

class Hero:
    """Base Hero class"""
    gold = 0

    def __init__(self, hp, mp, attack_power, magic_power):
        self.name = None
        self.exp = 0
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_mp = mp
        self.attack_power = attack_power
        self.magic_power = magic_power

    def set_name(self, name):
        self.name = name
    
    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.name} takes {damage} damage!")
        sleep(1)
        if self.hp > 0:
            print(f"HP is now {self.hp}.")
        else: 
            print(f"{self.name} has been defeated!")   

    def attack(self, target):
        damage = round(self.attack_power * r.uniform(1.0, 1.2))
        print(f"{self.name} attacks {target.name}!")
        target.take_damage(damage)
    
    def receive_healing(self, heal_amount):
        print(f"{self.name} heals for {heal_amount} HP!") 
        if self.hp + heal_amount > self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp += heal_amount
        print(f"HP is now {self.hp}")



        
        