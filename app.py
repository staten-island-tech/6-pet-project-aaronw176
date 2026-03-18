class Pet:
    def __init__(self, name, happiness, money):
        self.name = name
        self.happiness = happiness
        self.__money = money

    def play(self, activity):
        self.happiness += 10
        print(f"{self.name} is playing {activity}!")
    
    def show_status(self):
        print(f"{self.name} happiness is now {self.happiness}")
    
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
            print(f"{self.name} is in very big debt")
        else: 
            print(f"{self.name} has ${self.__money}")
pboy = Pet("Pboy", 100, 20)
pboy.balance()
pboy.spend("racket", 20, -1)
pboy.balance()  
pboy.play("badminton")
pboy.show_status()