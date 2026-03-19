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
    
pboy = Pet("Pboy", 100, 20, 50)
pboy.balance()
pboy.spend("racket", 20, 3)
pboy.balance()  
pboy.play("badminton")
pboy.feed("atomic wings")
pboy.show_status()
print(pboy.__dict__)