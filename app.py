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
        if amount > 1: 
            print(f"{self.name} has spent {cost*amount} on {amount} {item}s")
        elif amount == 1:
            print(f"{self.name} has spent {cost} on {amount} {item}")
        else: 
            print(f"{self.name} cannot buy that amount here.")
    
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
        for i in range(100000):
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
        self.__money += 25
        print(f"{self.name} has made 25 bucks from {job}")
        for i in range(1000):
            number = random.randint(1,25000)
            if number == 1:
                print(f"{self.name} has earned a bonus and has gained triple the amount of money {self.name} was suppose to.")
                self.__money += 50
            else: 
                print(f"{self.name} did not earn a bonus")

    
pboy = Pet("Pboy", 100, 20, 50)
pboy.balance()
pboy.spend("racket", 20, 3)
pboy.balance()  
pboy.play("badminton")
pboy.feed("atomic wings")
pboy.show_status()
pboy.work("games")
pboy.show_status()
pboy.balance()
