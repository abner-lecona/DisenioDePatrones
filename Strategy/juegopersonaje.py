class IAttackBehavior:
    def attack(self):
        pass

class IDefenceBehavior:
    def defence(self):
        pass

class AttackWithSword(IAttackBehavior):
    danio = 20
    def attack(self):
        print("I'm attacking with my sword!!")

class AttackWithBow(IAttackBehavior):
    danio = 10
    def attack(self):
        print("I'm attacking with my bow!!")

class AttackWithMagicAttack(IAttackBehavior):
    danio = 15
    def attack(self):
        print("I'm attacking with my magic attack!!")

class DefenceWithShield(IDefenceBehavior):
    endurance = 40
    def defence(self):
        print("I'm defending with my shield!!")

class DefenceWithDodge(IDefenceBehavior):
    endurance = 15
    def defence(self):
        print("I'm defending with Dodge!!")

class DefenceWithMagic(IDefenceBehavior):
    endurance = 50
    def defence(self):
        print("I'm defencing with Magic")

class Character:
    def __init__(self, attack_behavior, defence_behavior, life, name):
        self.attack_behavior = attack_behavior
        self.defence_behavior = defence_behavior
        self.life = life
        self.name = name
    
    def display(self):
        pass

    def perform_attack(self):
        self.attack_behavior.attack()

    def perform_defence(self):
        self.defence_behavior.defence()

    def attacks_enemy(self, enemy):
        if enemy.defence_behavior.endurance > 0:
            enemy.defence_behavior.endurance -= self.attack_behavior.danio
            enemy.defence_behavior.defence()
            print(f"{enemy.name} was attacked, but didn't take damage")
            print(f"{enemy.name} tiene {enemy.defence_behavior.endurance} puntos de defensa")
        else:
            enemy.life -= self.attack_behavior.danio
            print(f"{enemy.name} was attacked and take damage")
            print(f"{enemy.name} ahora tiene {enemy.life} puntos de vida")
        

    def is_alive(self):
        if self.life > 0:
            return True
        else:
            return False

class Warrior(Character):
    def display(self):
        print("Warrior")

class Magician(Character):
    def display(self):
        print("Magician")

class Combat:
    def __init__(self, char1, char2):
        self.char1 = char1
        self.char2 = char2

    def fight(self):
        print(f"{self.char1.name} se enfrenta a {self.char2.name}")
        while self.char1.is_alive() == self.char2.is_alive():
            print()
            self.char1.attacks_enemy(self.char2)
            if not self.char1.is_alive():
                print()
                print(f"Ganador: {self.char2.name}")
            self.char2.attacks_enemy(self.char1)
            if not self.char2.is_alive():
                print()
                print(f"Ganador: {self.char1.name}")
            
warrior = Warrior(AttackWithSword(),DefenceWithShield(),100, "Joahan")
magician = Magician(AttackWithMagicAttack(), DefenceWithMagic(), 10, "Kary")

combate = Combat(warrior, magician)
combate.fight()