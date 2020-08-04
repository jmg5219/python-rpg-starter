"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
#Creating Warrior Class
class Warrior:
    #Contructor for Warrior class
    def __init__(self, name, health, power):
        self.health = health
        self.power = power
        self.name = name
        
    def status (self):
        return "%s has %d health and %d power." % (self.name, self.health, self.power)



# Creating Sub Class Hero 
class Hero(Warrior):
    #Contructor for hero class
    def __init__(self, name, health, power):
        super().__init__(name, health, power)


#Creating Sub Class goblin 
class Goblin(Warrior):
    #Contructor for goblin class
    def __init__(self, name, health, power):
        super().__init__(name, health, power)

#Creating Instances
hiro =  Hero("Hiro",10,5)
spike = Goblin("Spike",6,2)


def main():
    while spike.health > 0 and hiro.health > 0:
        print ()
        print(hiro.status())
        print(spike.status())
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            spike.health -= hiro.power
            print("You do %d damage to the goblin." % hiro.power)
            if spike.health <= 0:
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if spike.health > 0:
            # Goblin attacks hero
            hiro.health -= spike.power
            print("The goblin does %d damage to you." % spike.power)
            if hiro.health <= 0:
                print("You are dead.")

main()
