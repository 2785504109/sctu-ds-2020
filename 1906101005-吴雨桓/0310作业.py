import random
import time
class A():
    def __init__(self,name,hp,damage,crit,dodge):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.crit=crit
        self.dodge=dodge

    def attack_B(self,B):
        if random.random() <= self.dodge:
            print('孙悟空攻击被闪避')
            return('攻击被闪避')
            pass
        if random.random() <= self.crit:
            self.attack2_B(B)
        else:
            self.attack1_B(B)


    def attack2_B(self,B):
        B.hp -= (self.damage)*2
        print("%s 攻击%s 暴击伤害值:%d 奥特曼剩余生命值:%d" % (self.name, B.name, (self.damage)*2, B.hp))
    def attack1_B(self,B):
        B.hp -= (self.damage)
        print("%sDay0407 攻击%s 伤害值:%d 奥特曼剩余生命值:%d" % (self.name, B.name, (self.damage), B.hp))


class B():
    def __init__(self, name, hp, damage, crit, dodge):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.crit = crit
        self.dodge = dodge

    def attack_A(self, A):

        if random.random() <= self.dodge:
            print('奥特曼攻击被闪避')
            return('攻击被闪避')
            pass
        if random.random() <= self.crit:
            self.attack2_A(A)
        else:
            self.attack1_A(A)

    def attack2_A(self, A):
        A.hp -= (self.damage) * 2
        print("%s 攻击%s 暴击伤害值:%d 孙悟空剩余生命值:%d" % (self.name, A.name, (self.damage) * 2, A.hp))

    def attack1_A(self, A):
        A.hp -= (self.damage)
        print("%s 攻击%s 伤害值:%d 孙悟空剩余生命值:%d" % (self.name, A.name, (self.damage), A.hp))

count = 1

A1 = A('孙悟空',1000,50,0.2,0.3)

B1 = B('奥特曼',2000,20,0.1,0.2)
while True:
    print("------------------【round%d】-----------------"%count)
    if A1.hp > 0:
        A1.attack_B(B1)
        if B1.hp <= 0:
            print("孙悟空胜")
            break
    if B1.hp > 0:
        B1.attack_A(A1)
        if A1.hp <= 0:
            print("奥特曼胜")
            break
    count += 1
    time.sleep(0.8)
    print('\n'*5)
    