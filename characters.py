import random as rd


class Character:
    """
    모든 캐릭터의 모체가 되는 클래스
    """

    def __init__(self, name, hp, power, speed):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power
        self.speed = speed

    def attack(self, other):
        if self.hp == 0:
            print(f"{self.name}은 전투불능. 공격하지 못했습니다.")
            return
        damage = rd.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")


class Player(Character):
    def __init__(self, name, hp, power, speed, mag):
        super().__init__(name, hp, power, speed)
        self.mag = mag
        self.sp = 5
        self.max_sp = 5

    def mag_attack(self, other):
        if self.hp == 0:
            print(f"{self.name}은 전투불능. 공격하지 못했습니다.")
            return
        if self.sp == 0:
            print("공격실패: SP가 부족합니다")
            return
        self.sp -= 1
        damage = rd.randint(self.mag - 2, self.mag + 2)
        damage = max(0, damage-other.mag_d)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")


class Archer(Player):
    def __init__(self, name, hp, power, speed, mag):
        super().__init__(name, hp, power, speed, mag)

    def mag_attack(self, other):
        if self.sp == 0:
            print("공격실패: SP가 부족합니다")
            return
        super().mag_attack(other)
        dice = rd.randint(1, 20)
        if dice == 20:
            print('바람의 화신이 직접 행차하십니다')
            print('적은 거의 움직일 수 없습니다! 당신의 속도가 증가합니다!')
            other.speed = 0
            self.speed = min(self.speed+1, 5)
        elif dice > 17:
            print('바람의 화신이 축복하십니다')
            print('적이 움직이기 힘들어지고 당신은 발이 빨라집니다!')
            other.speed = max(other.speed-1, 0)
            self.speed = min(self.speed+1, 5)
        elif dice > 14:
            print('바람의 화신이 화살을 인도합니다')
            print('적의 다리가 느려집니다!')
            other.speed = max(other.speed-1, 0)
        elif dice > 11:
            print('바람의 화신이 주목하십니다! 당신의 속도가 빨라집니다!')
            self.speed = min(self.speed+1, 5)
        else:
            False


class Babarian(Player):
    def __init__(self, name, hp, power, speed, mag):
        super().__init__(name, hp, power, speed, mag)

    def mag_attack(self, other):
        if self.hp == 0:
            print(f"{self.name}은 전투불능. 공격하지 못했습니다.")
            return
        if self.sp == 0:
            print("공격실패: SP가 부족합니다")
            return

        self.sp -= 1
        damage = rd.randint(self.mag - 2, self.mag + 2)
        damage = max(0, damage-other.mag_d)
        damage += rd.randint(self.power - 1, self.power + 4)
        self.hp = max(self.hp-self.mag, 0)
        print(f"피의신께 피를!{self.name}가 피를 제물로 사악한 공격을 한다!")
        print(f"{self.name}는 {self.mag}의 자해 데미지를 받는다.")
        if not self.hp:
            print(f"{self.name}의 마지막 일격입니다!")
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")
        if self.hp == 0:
            print(f'{self.name}이(가) 쓰러졌습니다.')


class Cleric(Player):
    def __init__(self, name, hp, power, speed, mag):
        super().__init__(name, hp, power, speed, mag)

    def mag_attack(self, other):
        if self.sp == 0:
            print("공격실패: SP가 부족합니다")
            return
        dice = rd.randint(1, 100)
        if dice == 100:
            print('신벌! 적이 쓰러졌습니다')
            self.sp -= 1
            other.hp = 0
            return
        if dice > 80:
            print('은총! 체력이 회복되고 적이 피해를 입습니다.')
            self.hp = min(self.max_hp, self.hp+self.mag+rd.randint(-2, 2))
            return super().mag_attack(other)
        if dice > 60:
            print('축복! SP가 회복되고 적이 피해를 입습니다.')
            self.sp = min(self.sp+1, 5)
            return super().mag_attack(other)
        print('믿음의 힘이 적을 덮칩니다.')
        return super().mag_attack(other)


class Monster(Character):
    def __init__(self, type_, name, hp, power, speed, mag_d):
        super().__init__(name, hp, power, speed)
        self.type_ = type_
        self.mag_d = mag_d
        self.random_name()

    def random_name(self):
        vowel = 'aeiou'
        non_vowel = 'bcdfghjklmnpqrstvwxyz'
        name = ''
        name = name+chr(rd.randint(65, 90))
        for i in range(rd.randint(1, 2)):
            name = name + vowel[rd.randint(0, 4)]
        for i in range(rd.randint(1, 3)):
            name = name + non_vowel[rd.randint(0, 10)]
        name = name+vowel[rd.randint(0, 4)]
        name = name + non_vowel[rd.randint(0, 10)]
        self.name = name
