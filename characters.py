import questionary
from settings import exp_table
import random
from time import sleep


# Character parent
class Character:
    """Character class: Hero and Enemy subclasses"""
    def __init__(self, name, hp, mp, attack_power, magic_power):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_mp = mp
        self.attack_power = attack_power
        self.magic_power = magic_power

    def is_alive(self) -> bool:
        """Monitors whether the character has HP"""
        return self.hp > 0

    def attack(self, target):
        """Attack the target"""
        damage = round(self.attack_power * random.uniform(1.0, 1.2))
        print(f"\n{self.name} attacks {target.name}!")
        target.take_damage(damage)

    def set_name(self, name):
        self.name = name

# Heroes
class Hero(Character):
    """Hero class: Warrior, Thief, White Mage and Black Mage subclasses"""
    gold_bag = 0 # Gold in party's possession

    def __init__(self, name, hp, mp, attack_power, magic_power):
        """Create an instance of the hero class"""
        super().__init__(name, hp, mp, attack_power, magic_power)
        self.exp = 0
        self.level = 1
        self.max_level = 99        

    def set_name(self, name):
        """Sets character's name"""
        self.name = name

    def take_damage(self, damage):
        """Receive damage"""
        self.hp -= damage
        sleep(0.7)
        print(f"{self.name} takes {damage} damage!")
        sleep(0.7)
        if self.hp > 0:
            print(f"HP is now {self.hp}.")
        else: 
            print(f"{self.name} has been defeated!") 
        sleep(0.7)     

    def recover_hp(self, amount):
        """Restores hp"""
        sleep(0.7)
        print(f"{self.name} recovers {amount} HP!") 
        if self.hp + amount > self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp += amount
        sleep(0.7)
        print(f"HP is now {self.hp}")
        sleep(0.7)

    def recover_mp(self, amount):
        """Restores mp"""
        print(f"{self.name} recovers {amount} MP!") 
        if self.mp + amount > self.max_mp:
            self.mp = self.max_mp
        else:
            self.mp += amount
        print(f"HP is now {self.mp}")

    def gain_exp(self, enemies): 
        """Gives exp to living party members at end of battle"""
        # Only executes if hero is alive at end of battle
        if self.is_alive():
            battle_exp = 0
            for enemy in enemies:
                battle_exp += enemy.exp
            print(f"{self.name} gained {battle_exp} exp!")
            self.exp += battle_exp        
    
    def check_level_up(self):
        """Checks party member's exp and executes level up if exp threshold reached"""
        if self.exp >= exp_table[self.level]:
            self.level += 1
            print(f"{self.name} has leveled up! Lvl: {self.level - 1} >> {self.level}")
            hp_up = random.randint(20, 40)
            self.hp += hp_up
            mp_up = random.randint(7, 13)
            self.mp += mp_up
            attack_up = random.randint(3, 7)
            self.attack_power += attack_up
            magic_up = random.randint(3, 7)
            self.magic_power += magic_up
            print(f"HP +{hp_up}. HP: {self.hp}")
            print(f"MP +{mp_up}. MP: {self.mp}")
            print(f"Attack +{attack_up}. Attack Power: {self.attack_up}")
            print(f"Magic +{magic_up}. Magic Power: {self.magic_power}")


# Warrior class
class Warrior(Hero):
    """Warrior class
    
    Skills: Bash
    """
    def __init__(self, name="Warrior", hp=160, mp=18, attack_power=14, magic_power=7):
        super().__init__(name, hp, mp, attack_power, magic_power)
        self.role = "Warrior"
        self.skills = {
            "Bash": {"func": self.bash, "mp_cost": 5}
        }

    def __str__(self):
        return f"{self.name} ({self.role}: {self.hp} HP | {self.mp} MP)"

    def bash(self, target):
        """Warrior starting skill: Bash"""
        self.mp -= self.skills["Bash"]["mp_cost"]
        damage = round(self.attack_power * random.uniform(1.3, 1.65))
        print(f"\n{self.name} uses Bash on {target.name}!")
        target.take_damage(damage)

    def choose_action(self, enemies):
        """Choose action and target to receive action"""
        if any(enemy.is_alive() for enemy in enemies):
            living_enemies = [{"name": f"{enemy.name}", "value": enemy} for enemy in enemies if enemy.is_alive()]
            print(f"\n{self.name}'s turn!")
            print(f"HP: {self.hp}, MP: {self.mp}")
            sleep(0.5)

            while True:
                print("-" * 20)
                action = questionary.select("--Choose an action--\n", choices=["Attack", f"Bash ({self.skills['Bash']['mp_cost']} MP)", "Pass"]).ask()

                if action == "Attack":
                    target = questionary.select("\n--Choose a target--\n", choices=living_enemies).ask()
                    self.attack(target)
                    return
                
                elif action == f"Bash ({self.skills['Bash']['mp_cost']} MP)":
                    if self.mp >= self.skills["Bash"]["mp_cost"]:
                        target = questionary.select("\n--Choose a target--\n", 
                        choices=living_enemies).ask()
                        self.bash(target)
                        return
                    else:
                        print(f"{self.name} doesn't have enough MP to use that skill!")
                        continue
            
                elif action == "Pass":
                    print(f"\n{self.name} passes their turn!")
                    sleep(0.7)
                    return


# Thief class
class Thief(Hero):
    """Thief class
    
    Skills: Quick Strike
    """
    def __init__(self, name="Thief", hp=120, mp=20, attack_power=11, magic_power=7):
        super().__init__(name, hp, mp, attack_power, magic_power)
        self.role = "Thief"
        self.skills = {
            "Quick Strike": {"func": self.quick_strike, "mp_cost": 4}
        }
    def __str__(self):
        return f"{self.name} ({self.role}: {self.hp} HP | {self.mp} MP)"


    def quick_strike(self, target):
        """Thief starting skill: Quick Strike"""
        self.mp -= self.skills["Quick Strike"]["mp_cost"]
        damage = round(self.attack_power * random.uniform(1.3, 1.6))
        print(f"\n{self.name} uses Quick Strike on {target.name}!")
        target.take_damage(damage)

    def choose_action(self, enemies):
        """Choose action and target to receive action"""
        if any(enemy.is_alive() for enemy in enemies):
            living_enemies = [{"name": f"{enemy.name}", "value": enemy} for enemy in enemies if enemy.is_alive()]
            print(f"\n{self.name}'s turn!")
            print(f"HP: {self.hp}, MP: {self.mp}")
            sleep(0.5)

            while True:
                print("-" * 20)
                action = questionary.select("--Choose an action--\n", choices=["Attack", f"Quick Strike ({self.skills['Quick Strike']['mp_cost']} MP)", "Pass"]).ask()

                if action == "Attack":
                    target = questionary.select("\n--Choose a target--\n", choices=living_enemies).ask()
                    self.attack(target)
                    return
                
                elif action == f"Quick Strike ({self.skills['Quick Strike']['mp_cost']} MP)":
                    if self.mp >= self.skills["Quick Strike"]["mp_cost"]:
                        target = questionary.select("\n--Choose a target--\n", 
                        choices=living_enemies).ask()
                        self.quick_strike(target)
                        return
                    else:
                        print(f"{self.name} doesn't have enough MP to use that skill!")
                        continue
            
                elif action == "Pass":
                    print(f"\n{self.name} passes their turn!")
                    sleep(0.7)
                    return


# White Mage class
class White_Mage(Hero):
    """White Mage class
    
    Skills: Heal
    """
    def __init__(self, name="White Mage", hp=85, mp=35, attack_power=7, magic_power=14):
        super().__init__(name, hp, mp, attack_power, magic_power)
        self.role = "White Mage"
        self.skills = {
            "Heal": {"func": self.heal, "mp_cost": 7}
        }
    def __str__(self):
        return f"{self.name} ({self.role}: {self.hp} HP | {self.mp} MP)"


    def heal(self, target):
        """White Mage starting skill: Heal"""
        self.mp -= self.skills["Heal"]["mp_cost"]
        amount = round(self.magic_power * random.uniform(1.3, 1.6))
        print(f"\n{self.name} uses Heal on {target.name}!")
        target.recover_hp(amount)

    def choose_action(self, party, enemies):
        """Choose action and target to receive action"""
        if any(enemy.is_alive() for enemy in enemies):
            living_enemies = [{"name": f"{enemy.name}", "value": enemy} for enemy in enemies if enemy.is_alive()]
            living_heroes = [{"name": f"{hero.name}", "value": hero} for hero in party if hero.is_alive()]
            print(f"\n{self.name}'s turn!")
            print(f"HP: {self.hp}, MP: {self.mp}")
            sleep(0.5)

            while True:
                heal_mp_cost = self.skills["Heal"]["mp_cost"]
                print("-" * 20)
                action = questionary.select("--Choose an action--\n", choices=["Attack", f"Heal ({heal_mp_cost} MP)", "Pass"]).ask()

                if action == "Attack":
                    target = questionary.select("\n--Choose a target--\n", choices=living_enemies).ask()
                    self.attack(target)
                    return
                
                elif action == f"Heal ({heal_mp_cost} MP)":
                    if self.mp >= heal_mp_cost:
                        target = questionary.select("\n--Choose a party member--\n", 
                        choices=living_heroes).ask()
                        self.heal(target)
                        return
                    else:
                        print(f"{self.name} doesn't have enough MP to use that skill!")
                        continue
            
                elif action == "Pass":
                    print(f"\n{self.name} passes their turn!")
                    sleep(0.7)
                    return


# Black Mage class
class Black_Mage(Hero):
    """Black Mage class
    
    Skills: Fire, Blizzard, Thunder
    """
    def __init__(self, name="Black Mage", hp=75, mp=45, attack_power=7, magic_power=13):
        super().__init__(name, hp, mp, attack_power, magic_power)
        self.role = "Black Mage"
        self.skills = {
            "Fire": {"func": self.fire, "mp_cost": 9},
            "Blizzard": {"func": self.blizzard, "mp_cost": 9},
            "Thunder": {"func": self.thunder, "mp_cost": 8}
        }
    def __str__(self):
        return f"{self.name} ({self.role}: {self.hp} HP | {self.mp} MP)"


    def fire(self, target):
        """Black Mage starting skill #1: Fire"""
        self.mp -= self.skills["Fire"]["mp_cost"]
        damage = round(self.magic_power * random.uniform(1.3, 1.6))
        print(f"\n{self.name} uses Fire on {target.name}!")
        target.take_damage(damage)

    def blizzard(self, target):
        """Black Mage starting skill #2: Blizzard"""
        self.mp -= self.skills["Blizzard"]["mp_cost"]
        damage = round(self.magic_power * random.uniform(1.3, 1.7))
        print(f"\n{self.name} uses Blizzard on {target.name}!")
        target.take_damage(damage)

    def thunder(self, target):
        """Black Mage starting skill #3: Thunder"""
        self.mp -= self.skills["Thunder"]["mp_cost"]
        damage = round(self.magic_power * random.uniform(1.3, 1.6))
        print(f"\n{self.name} uses Thunder on {target.name}!")
        target.take_damage(damage)    

    def choose_action(self, enemies):
        """Choose action and target to receive action"""
        if any(enemy.is_alive() for enemy in enemies):
            living_enemies = [{"name": f"{enemy.name}", "value": enemy} for enemy in enemies if enemy.is_alive()]
            print(f"\n{self.name}'s turn!")
            print(f"HP: {self.hp}, MP: {self.mp}")
            sleep(0.5)

# Remember to update choices to reflect class skills
            while True:
                print("-" * 20)
                action = questionary.select("--Choose an action--\n", choices=["Attack", "Cast Spell", "Pass"]).ask()

                if action == "Attack":
                    target = questionary.select("\n--Choose a target--\n", choices=living_enemies).ask()
                    self.attack(target)
                    return
                
                elif action == "Cast Spell":
                    fire_mp_cost = self.skills["Fire"]["mp_cost"]
                    blizzard_mp_cost = self.skills["Blizzard"]["mp_cost"]
                    thunder_mp_cost = self.skills["Thunder"]["mp_cost"]

                    if self.mp < thunder_mp_cost:
                        print(f"{self.name} doesn't have enough MP to use any spells!\n")
                        continue
                        
                    else:
                        choice = questionary.select("\n--Choose a spell--\n", 
                        choices=[
                            f"Fire ({fire_mp_cost} MP)",
                            f"Blizzard ({blizzard_mp_cost} MP)",
                            f"Thunder ({thunder_mp_cost} MP)"
                        ]).ask()
                        if choice == f"Fire ({fire_mp_cost} MP)" and self.mp >= fire_mp_cost:
                            target = questionary.select("\n--Choose a target--\n", choices=living_enemies).ask()
                            self.fire(target)
                            return
                            
                        elif choice == f"Blizzard ({blizzard_mp_cost} MP)" and self.mp >= blizzard_mp_cost:
                            target = questionary.select("\n--Choose a target--\n", choices=living_enemies).ask()
                            self.blizzard(target)
                            return
                            
                        elif choice == f"Thunder ({thunder_mp_cost} MP)" and self.mp >= thunder_mp_cost:
                            target = questionary.select("\n--Choose a target--\n", choices=living_enemies).ask()
                            self.thunder(target)
                            return
                        
                        else:
                            print("You don't have enough MP to use that skill!")
                            continue
            
                elif action == "Pass":
                    print(f"\n{self.name} passes their turn!")
                    sleep(0.7)
                    return


class Party:
    """Class to keep track of party gold and shared inventory
    
    A list of game inventory items can be found in the items.py file.
    """
    gold_bag = 0
    inventory = {}

    def __init__(self, members):
        self.members = members

    @staticmethod
    def gain_gold(enemies):
        """Adds battle gold to party gold bag. Called at the end of battle"""
        battle_gold = 0
        for enemy in enemies:
            battle_gold += enemy.gold
        print(f"Your party gained {battle_gold} gold!\n")
        Party.gold_bag += battle_gold

    
# Enemies
class Enemy(Character):
    """Enemy class with Forest Wolf subclass"""
    def __init__(self, name, level, exp, gold, hp, mp, attack_power, magic_power): 
        super().__init__(name, hp, mp, attack_power, magic_power) 
        self.level = level     
        self.exp = exp
        self.gold = gold  
        self.magic_power = magic_power

    def __str__(self):
        return f"{self.name}"

    def take_damage(self, damage):
        self.hp -= damage
        sleep(0.7)
        print(f"{self.name} takes {damage} damage!")
        sleep(0.7)
        if self.hp < 0:
            print(f"{self.name} has been defeated!") 
            sleep(0.7)     

    def recover_hp(self, amount):
        """Recovers hp"""
        print(f"{self.name} recovers {amount} HP!") 
        if self.hp + amount > self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp += amount

    def recover_mp(self, amount):
        """Recovers mp"""
        print(f"{self.name} recovers {amount} MP!") 
        if self.mp + amount > self.max_mp:
            self.mp = self.max_mp
        else:
            self.mp += amount

# Forest Wolf
class Forest_Wolf(Enemy):
    def __init__(self, name="Forest Wolf", level=1, exp=9, gold=7, hp=32, mp=6, attack_power=7, magic_power=1):
        super().__init__(name, level, exp, gold, hp, mp, attack_power, magic_power)
        self.skills = {
            "Bite": {"func": self.bite, "mp_cost": 2}
        }              

    def bite(self, target):
        mp_cost = self.skills["Bite"]["mp_cost"]
        self.mp -= mp_cost
        print(f"{self.name} uses Bite on {target.name}!")
        damage = round(self.attack_power * random.uniform(1.2, 1.5))
        target.take_damage(damage)

    def attack_at_random(self, party):
        """Attacks random target in hero party"""
        targets = [hero for hero in party if hero.is_alive()]
        target = random.choice(targets)
        if self.mp < self.skills["Bite"]["mp_cost"]:
            self.attack(target)
        else:    
            # 33% chance of using skill "Bite"
            attack = random.choice([self.attack, self.attack, self.bite])
            attack(target)
    
# Forest Goblin class
class Forest_Goblin(Enemy):
    def __init__(self, name="Forest Goblin", level=2, exp=17, gold=20, hp=47, mp=13, attack_power=10, magic_power=9):
        super().__init__(name, level, exp, gold, hp, mp, attack_power, magic_power)
        self.skills = {
            "Slash": {"func": self.slash, "mp_cost": 2},
            "Fire": {"func": self.fire, "mp_cost": 4}
        }              

    def slash(self, target):
        mp_cost = self.skills["Slash"]["mp_cost"]
        self.mp -= mp_cost
        print(f"\n{self.name} uses Slash on {target.name}!")
        damage = round(self.attack_power * random.uniform(1.2, 1.5))
        target.take_damage(damage)

    def fire(self, target):
        mp_cost = self.skills["Fire"]["mp_cost"]
        self.mp -= mp_cost
        print(f"{self.name} uses Fire on {target.name}!")
        damage = round(self.magic_power * random.uniform(1.4, 1.7))
        target.take_damage(damage)

    def attack_at_random(self, party):
        """Attacks random target in hero party"""
        targets = [hero for hero in party if hero.is_alive()]
        target = random.choice(targets)
        if self.mp < self.skills["Slash"]["mp_cost"]:
            self.attack(target)
        # If remaining mp is between the cost of slash and fire
        elif self.skills["Slash"]["mp_cost"] < self.mp < self.skills["Fire"]["mp_cost"]:
            #33% chance of using "Slash"
            attack = random.choice([self.attack, self.attack, self.slash])
        else:    
            # 25% chance of using skills "Slash" and "Fire"
            attack = random.choice([self.attack, self.attack, self.slash, self.fire])
            attack(target)    

        
        