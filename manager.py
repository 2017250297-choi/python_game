import os
from time import sleep
from characters import *
import csv


class WindowManager:
    def __init__(self) -> None:
        self.player_name = ''
        self.player_class = ''

    def clear_all(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def name_input(self):
        while True:
            self.clear_all()
            self.player_name = input('Please enter your name: ')
            if len(self.player_name) == 0:
                print('\r')
                continue
            if len(self.player_name) > 8:
                print('\rRejected: Too Long Name. Enter 1~8 Characters')
                sleep(1.3)
                print('\r')
                continue
            while True:
                print(f'Your name is {self.player_name}. OK?')
                check = input('[Y]es or [N]o: ')
                if check == 'N':
                    print('\r')
                    break
                elif check == 'Y':
                    print(f'Now You are {self.player_name}')
                    sleep(1.3)

                    return self.player_name
                else:
                    print('Invalid Input')
                    sleep(1.3)
                    self.clear_all()

    def choose_class(self):
        self.clear_all()
        while True:
            print("-------- Choose your Mastery --------")
            print("| A: Archer, B: Babarian, C: Cleric |")
            print("-------------------------------------")
            class_choice = input('enter: ')
            if class_choice not in ('A', 'B', 'C'):
                print("Invalid Input. Choose class among A, B, C")
                sleep(1.3)
                self.clear_all()
                continue
            if class_choice == 'A':
                class_name = 'Archer'
            elif class_choice == 'B':
                class_name = 'Babarian'
            else:
                class_name = 'Cleric'
            self.player_class = class_name
            print(f"{self.player_name}, You are now {self.player_class}")
            return class_name

    def battle_window(self, player_entity: Player, enemy: Monster):
        self.clear_all()
        while True:
            print('Battle Status:')
            print(f'\tPlayer \t\t {enemy.type_}')
            print(f'Name\t{player_entity.name} \t\t {enemy.name}')
            print(
                f'HP\t{player_entity.hp}/{player_entity.max_hp} \t\t {enemy.hp}/{enemy.max_hp}')
            print(f'SP\t{player_entity.sp} \t\t -')
            print(f'POW\t{player_entity.power} \t\t {enemy.power}')
            print(f'MAG(D)\t{player_entity.mag} \t\t {enemy.mag_d}')
            print(f'SPEED\t{player_entity.speed} \t\t {enemy.speed}')
            print('\n')
            print('A: Attack, W: Magic Attack, Q: Run(Game Over)')
            while True:
                move = input('Your Move: ')
                if move not in ('A', 'W', 'Q'):
                    print('\r\r', end="")
                    continue
                if move == 'A':
                    p_move = player_entity.attack
                    break
                if move == 'W':
                    p_move = player_entity.mag_attack
                    break
                if move == 'Q':
                    print('You are hopeless CHICKEN. Game Over.')
                    return
            p_s = player_entity.speed
            e_s = enemy.speed
            if p_s == e_s:
                movelist = [enemy.attack, p_move]
                targets = [player_entity, enemy]
                index = rd.randint(0, 1)
                movelist[index](targets[index])
                movelist[(index+1) % 2](targets[(index+1) % 2])
            elif p_s-e_s > 0:
                p_move(enemy)
                if (p_s-e_s)**2 <= rd.randint(1, 25):
                    enemy.attack(player_entity)
                else:
                    print(f"{enemy.name}는 움직이지 못했다.")
            else:
                enemy.attack(player_entity)
                if (e_s-p_s)**2 <= rd.randint(1, 25):
                    p_move(enemy)
                else:
                    print((f"{player_entity.name}는 움직이지 못했다."))

            if player_entity.hp == 0:
                print('You Dead! Game Over.')
                break
            if enemy.hp == 0:
                print('You Slayed it! Happy end.')
                break

            sleep(2.5)
            self.clear_all()


def make_monster():
    csv_file = open('monster_classes.csv', "r", encoding="utf-8")
    csv_data = csv.DictReader(csv_file)
    csv_data = list(csv_data)
    dice = rd.randint(0, 2000) % len(csv_data)
    row = csv_data[dice]
    monster_entity = Monster(row['class_name'], '', int(row['hp']), int(
        row['power']), int(row['speed']), int(row['mag_d']))
    csv_file.close()
    return monster_entity


def make_player(player_name, class_name):
    csv_file = open('player_classes.csv', "r", encoding="utf-8")
    csv_data = csv.DictReader(csv_file)
    csv_data = list(csv_data)
    for i in csv_data:
        if i['class_name'] == class_name:
            break
    hp_ = int(i['hp'])
    power_ = int(i['power'])
    speed_ = int(i['speed'])
    mag_ = int(i['mag'])
    if class_name == 'Archer':
        player_entity = Archer(player_name, hp_, power_, speed_, mag_)
    elif class_name == 'Babarian':
        player_entity = Babarian(player_name, hp_, power_, speed_, mag_)
    elif class_name == 'Cleric':
        player_entity = Cleric(player_name, hp_, power_, speed_, mag_)
    else:
        False
    csv_file.close()
    return player_entity
