import random
import pprint
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''
class Person:
    def __init__(self,name,hp,mp,atk,df,magic,items):
        self.maxhp=hp
        self.hp=hp
        self.maxmp=mp
        self.mp=mp
        self.atkl=atk-10
        self.atkh=atk+10
        self.df=df
        self.magic=magic
        self.items=items
        self.action=["Attack","Magic","Items"]
        self.name = name
    def generate_damage(self):
        return random.randrange(self.atkl,self.atkh)
    
    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp <0:
            self.hp=0
        return self.hp
    def heal(self,dmg) :
        self.hp += dmg
        if self.hp > self.maxhp :
            self.hp=self.maxhp
    def get_hp(self):
        return self.hp
    def get_max_hp(self):
        return self.maxhp
    def get_max_mp(self):
        return self.maxmp
    def get_mp(self):
        return self.mp
    def reduce_mp(self,cost):
        self.mp -=cost
 
    def choose_action(self):
        i=1
        print("\n" + bcolors.BOLD + self.name + bcolors.ENDC)
        print("\n ACTIONS")   
        for item in self.action:
            print("        "+str(i) + ":", item)
            i+=1
    def choose_magic(self):
        i = 1
        print("\n MAGIC")
        for spell in self.magic:
            print("        "+str(i)+":",spell.name, "(cost:",str(spell.cost)+")")
            i+=1

    def choose_item(self):
        i = 1
        print("\n"+ bcolors.OKGREEN + bcolors.BOLD + "ITEMS: "+ bcolors.ENDC)
        for item in self.items:
            print("        "+str(i)+":",item["item"].name,":",item["item"].description, " (x" + str(item["quantity"]) + ")")
            i+=1
    def get_stats(self) :
        print("                            ________________________           _________")
        print(bcolors.BOLD + self.name + "       " + str(self.hp) + "/" + str(self.maxhp) + "    |"
             + bcolors.OKGREEN +"████████████████████████" + bcolors.ENDC + bcolors.BOLD + "|   "
             + str(self.mp) + "/" + str(self.maxmp) + " |"
             + bcolors.OKBLUE + "█████████" + bcolors.ENDC + "|")
        


    
    

        
