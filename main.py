from characters import Party, Warrior, Forest_Wolf
from time import sleep

hero_party = [Warrior("Nate", mp=0), Warrior("Tasha"), Warrior("Stacy")]
party = Party(hero_party)

enemy_party = [Forest_Wolf("Forest Wolf Leader"), Forest_Wolf(), Forest_Wolf()]

def battle(group, party, enemies):
    round_num = 1

    while any(hero.is_alive() for hero in party) and any(enemy.is_alive() for enemy in enemies):
        print(f"\n========== Round {round_num} ==========")
        sleep(0.3)
        print("\n----Your party's turn----")
        sleep(0.5)
        for hero in party:
            if hero.is_alive():
                hero.choose_action(enemies)

        if any(enemy.is_alive() for enemy in enemies):
            print("\n----Enemy party's turn----")
            sleep(0.5)
            for enemy in enemies:
                if enemy.is_alive():
                    enemy.attack_at_random(party)
        # if no enemies are alive, break out of the loop
        else:
            break
        
        round_num += 1

    if any(hero.is_alive() for hero in party):
        print("*" * 30)
        print("Victory!")
        print("*" * 30)
        sleep(0.5)
        group.gold_bag += group.gain_gold(enemies)
        for hero in party:
            if hero.is_alive():
                hero.gain_exp(enemies)
                hero.check_level_up()
        print("*" * 30)        
    else:
        print("*" * 30)
        print("Your party has been defeated...")
        print("*" * 30)
#if __name__ == "__main__":
battle(party, hero_party, enemy_party)