import random
class Pet:
    def __init__(self, name, happiness, money, hunger):
        self.name = name
        self.happiness = happiness
        self.__money = money
        self.hunger = hunger

    def play(self, activity):
        self.happiness += 10
        print(f"{self.name} is playing {activity}!")
        self.hunger -= 5
        print (f"{self.name} has lost 5 hunger from playing {activity}!")
        if -10 < self.hunger < 0:
            print(f"{self.name} is starving! Feed him before he dies")
        elif self.hunger < -10:
            print(f"{self.name} has died from starvation!")
            exit()
    
    def show_status(self):
        print(f"{self.name} happiness is now {self.happiness}")
        print(f"{self.name} hunger is now {self.hunger}")
    
    def spend(self, item, cost, amount):
        if amount >= 1:
            self.__money -= cost*amount 
    
    def balance(self):
        if self.__money == 0:
            print(f"{self.name} is a broke homeless boy now")
        elif self.__money < 0: 
            self.happiness -= 25
            print(f"{self.name} is in very big debt and lost 25 happiness")
        else: 
            print(f"{self.name} has ${self.__money}")
    
    def feed(self, food):
        self.hunger += 10
        print(f"{self.name} has gained 10 hunger from eating {food}")
        if self.hunger > 110:
            print(f"{self.name} has been overfed and died")
    
    def end(self):
        print("The day has ended.")
        print(f"{self.name} has ended the day with {self.happiness} happiness, {self.hunger} hunger, {self.__money} money.")
        x = input("Start next day?")
        for i in range(1):
            if x == "yes":
                self.hunger -= 20
                self.__money += 10
                self.happiness += 5
                print(f"{self.name} has gain 10 bucks from his daily allowance.")
                print(f"{self.name} has gained 5 happiness from sleeping.")
                print(f"{self.name} has lost 20 hunger from sleeping.")
                break
            elif x == "no": 
                print("You have ended the game.")
                exit()
            else:
                print("That is an invalid option")
                x = input("Start next day?")
    def work(self, job):
        spins = 0
        r = 0
        shiny = 0
        s = 0
        self.__money += 25
        for i in range(1000000000000000000000):
            number = random.randint(1,20000)
            spins += 1
            if number == 1:
                r+=1
                number1 = random.randint(1,100)
                if number1 == 1 or number1 == 2 or number1 == 3 or number1 == 4 or number1 == 5 or number1 == 6:
                    shiny += 1
                    number2 = random.randint(1,200)
                    if number2 == 1 or number2 == 2 or number2 == 3 or number2 == 4 or number2 == 5 or number2 == 6 or number2 == 7 or number2 == 8 or number2 == 9 or number2 == 10 or number2 == 11 or number2 == 12 or number2 == 13 or number2 == 14 or number2 == 15 or number2 == 16 or number2 == 17 or number2 == 18 or number2 == 19 or number2 == 20 or number2 == 21 or number2 == 22 or number2 == 23 or number2 == 24 or number2 == 25:
                        print(f"{self.name} has earned a bonus and has gained triple the amount of money {self.name} was suppose to.")
                        s += 1
                        self.__money += 50 
                        break
        print(f"{spins} spins, {r} rukias {shiny} shinies, {s} sera")

    
pboy = Pet("Pboy", 100, 20, 50)
pboy.spend("racket", 20, 3)
pboy.work("games")
pboy.balance()
""" NO SMTH SHINY
7350000 + 546084 + 5813184 + 3060212 + 5192727 + 342152 + 1694415 + 1275877 + 2680826 + 404054 + 1237860 spins
? + 150 + 286 + 272 + 17 + 108 + 86 + 125 + 24 + 80 rukia
14 + 1 + 11 + 6 + 9 + 1 + 1 + 2 + 10 + 1 + 4 shinies
0 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 seralized"""

""" SMTH SHINY
5176662 + 465503 + 3922665 + 214219 + 2203115 + 2585969 + 2187745 + 4330 + 2337970 + 2097858 + 643448 spins 
257 + 19 + 197 + 12 + 111 + 135 + 91 + 1 + 102 + 108 + 36 rukia
8 + 2 + 8 + 2 + 8 + 11 + 7 + 1 + 6 + 8 + 3 shinies
1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 seralized """
""" unlucky spin:
9939229 spins
508 rukia
33 shinies
1 seralized """