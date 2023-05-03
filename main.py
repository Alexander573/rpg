from random import *
from time import *


class Player:

    def __init__(self, name, hp, damage, prof):
        self.hp = hp
        self.damage = damage
        self.name = name
        self.level = 1
        self.exp = 0
        self.prof = prof
        self.skill = None

    def create_hero(name, rasa, prof):
        hp = 0
        damage = 0
        name = name
        if rasa.lower() == h[0]:
            hp += 70
            damage += 21
        elif rasa.lower() == h[1]:
            hp += 100
            damage += 16
        elif rasa.lower() == h[2]:
            hp += 62
            damage += 27
        elif rasa.lower() == h[3]:
            hp += 90
            damage += 19
        elif rasa.lower() == h[4]:
            hp += 58
            damage += 31
        elif rasa.lower() == h[5]:
            hp += 39
            damage += 42
        elif rasa.lower() == h[6]:
            hp += 82
            damage += 21
        else:
            print('я не знаю кто ты')
        if prof.lower() == i[0]:
            damage += 8
        elif prof.lower() == i[1]:
            hp += 9
            damage += 3
        elif prof.lower() == i[2]:
            hp += 4
            damage += 5
        elif prof.lower() == i[3]:
            hp += 13
        elif prof.lower() == i[4]:
            hp += 6
            damage += 2
        else:
            print('я не знаю такую профессию')
        return Player(name, hp, damage, prof)

    def create_weapon(self):
        wpn_type = weapon_type_list[randint(0, 3)]
        wpn_rare = choice(list(weapon_rare_dict.keys()))
        if wpn_type == weapon_type_list[0]:
            self.damage += 4 * wpn_rare
        elif wpn_type == weapon_type_list[1]:
            self.damage += 5 * wpn_rare
        elif wpn_type == weapon_type_list[2]:
            self.damage += 3 * wpn_rare
        elif wpn_type == weapon_type_list[3]:
            self.damage += 6 * wpn_rare
        return wpn_type, weapon_rare_dict[wpn_rare]

    def create_armor(self):
        armor_type = armor_type_list[randint(0, 4)]
        armor_rare = choice(list(armor_rare_dict.keys()))
        if armor_type == armor_type_list[0]:
            self.hp += 5 * armor_rare
        elif armor_type == armor_type_list[1]:
            self.hp += 3 * armor_rare
        elif armor_type == armor_type_list[2]:
            self.hp += 2 * armor_rare
        elif armor_type == armor_type_list[3]:
            self.hp += 4 * armor_rare
        elif armor_type == armor_type_list[4]:
            self.hp += 4 * armor_rare
        return armor_type, armor_rare_dict[armor_rare]

    def create_food(self):
        heal_size = choice(list(food.keys()))
        self.hp += heal_size
        return food[heal_size]

    def create_potion(self):
        potion_tyre = potion_tyre_list[randint(0, 2)]
        potion_rare = choice(list(potion_rare_dict.keys()))
        if potion_tyre == potion_tyre_list[0]:
            self.exp += 10 * potion_rare
        elif potion_tyre == potion_tyre_list[1]:
            self.hp += 7 * potion_rare
        elif potion_tyre == potion_tyre_list[2]:
            self.damage += 6 * potion_rare
        return potion_tyre, potion_rare_dict[potion_rare]

    def levelup(self, max_exp):
        self.exp -= max_exp
        self.level += 1
        self.damage += self.level * 5
        self.hp += self.level * 5
        print(f'поздровляем с повышением уровня {self.level}')

    def attack(self, victim):
        att = randint(1, 3)
        if att == 1:
            victim.hp -= self.damage % 21
            print('вы нанесли %19 процентов')
        elif att == 2:
            victim.hp -= self.damage
            print('весь урон прошёл')
        elif att == 3:
            victim.hp -= 0
            print('урон не прошёл')
        max_exp = self.level * 100
        n = randint(10, 25)
        if victim.hp <= 0:
            print(f'Поздровляем,{victim.name} Повержен , + {n} опыта')
            self.exp += n
            if self.exp >= max_exp:
                self.levelup(max_exp)
            thing = randint(0, 4)
            if thing == 1:
                wpn = self.create_weapon()
                print(f'вам выпало новое  оружие! {wpn[0]} , {wpn[1]} ')
                sleep(2)
            elif thing == 2:
                armor = self.create_armor()
                print(f'вам выпало новое  броня! {armor[0]} , {armor[1]} ')
                sleep(2)
            elif thing == 3:
                potion = self.create_potion()
                print(f'вам выпало новое  зелье! {potion[0]} , {potion[1]} ')
                sleep(2)
            elif thing == 4:
                food = self.create_food()
                print(f'вам выпало новое  еда! {food[0]} , {food[1]} ')
                sleep(2)
            else:
                print('вам ничего не выпало')
            self.skill = choice(powers)
            print(f'поздровляю вы наделены способностью {self.skill}')
            sleep(2)
            return False
        else:
            if self.skill != None:
                ability()
            print(f'{victim.name}, оставшееся здоровье: {victim.hp}')
            return True


class Enemy:
    def __init__(self, name_monsters, hp_monsters, damage_monsters):
        self.hp = hp_monsters
        self.damage = damage_monsters
        self.name = name_monsters

    def create_enemy():
        name_monsters = choice(monsters)
        hp_monsters = randint(28, 101)
        damage_monsters = randint(6, 20)
        return Enemy(name_monsters, hp_monsters, damage_monsters)

    def attack(self, victim):
        victim.hp -= self.damage
        if victim.hp <= 0:
            print(f'{victim.name} ты повержен , игра окончена')
            sleep(2)
            quit()
        else:
            print(f'{victim.name}, оставшееся здоровье: {victim.hp}')


def fight_choice():
    answer = input(f'хотите ли вы вступить в бой с {enemy.name} ?').lower()
    if answer == 'да':
        rezult = hero.attack(enemy)
        if rezult == True:
            enemy.attack(hero)
            fight_choice()
    elif answer == 'нет':
        t = randint(1, 2)
        if t == 1:
            print('вы убежали')
            sleep(2)
        elif t == 2:
            print('вы не смогли сбежать')
            sleep(2)
            enemy.attack(hero)
            fight_choice()


def ability():
    if hero.skill == 'лечение':
        print('твоё оружие тебя вылечило. + 12 хп')
        hero.hp += 12
        sleep(2)
    elif hero.skill == 'заморозка':
        print('вы заморозили врага')
        enemy.damage = 0
        sleep(2)
    elif hero.skill == 'отравление':
        print('вы отравили врага. - 10 хп')
        enemy.hp -= 10
        sleep(2)
    elif hero.skill == 'метеор':
        print('ты нанёс дополнительный урон. - 19 хп')
        enemy.hp -= 19
        sleep(2)
    elif hero.skill == 'зеркало реальности':
        print('ты нанёс урон и излечил себя')
        enemy.hp -= 9
        hero.hp += 11
        sleep(2)


my_name = input('введите имя вашего персонажа: ')
h = ['гоблин', 'человек', 'эльф', 'гном', 'оборотень', 'фея', 'нежить']
print(f'доступные расы: {h}')
y = input('выбирете расу:')
i = ['лучник', 'воин', 'маг', 'лекарь', 'ассасин']
print(f'доступные профессии: {i}')
k = input('выбирите профессию:')
monsters = ['горд', 'кэрри', 'мартис', 'инь', 'мия', 'сабер', 'циклоп', 'бэйн']
weapon_type_list = ['меч', 'лук', 'посох', 'клинок']
weapon_rare_dict = {1: 'обычный', 2: 'редкий', 3: 'эпический', 4: 'легендарный'}
armor_type_list = ['щит', 'шлем', 'ботинки', 'поножи', 'нагрудник']
armor_rare_dict = {1: 'обычный', 2: 'редкий', 3: 'эпический', 4: 'легендарный'}
potion_tyre_list = ['бодроперовое зелье', 'бедовый ласьён', 'волчье противоядие']
potion_rare_dict = {1: 'обычный', 2: 'редкий', 3: 'эпический', 4: 'легендарный'}
food = {5: 'яблоко', 10: 'мясо', 15: 'аптечка'}
powers = ['лечение', 'заморозка', 'отравление', 'метеор', 'зеркало реальности']
hero = Player.create_hero(my_name, y, k)
print(f' ник нейм: {hero.name} , раса: {y} , урон:  {hero.damage} , хп:  {hero.hp}, профессия: {hero.prof}')

while True:
    event = randint(1, 2)
    if event == 1:
        print('никого нет')
        sleep(3)
    elif event == 2:
        enemy = Enemy.create_enemy()
        print(f'встретился {enemy.name}')
        print(f' ник нейм: {enemy.name} , хп: {enemy.hp} , урон: {enemy.damage}')
        print(f' {hero.name}:\n урон: {hero.damage} \n хп:  {hero.hp} \n  уровень: {hero.level} \n  опыт: {hero.exp}')
        fight_choice()