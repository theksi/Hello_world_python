import colorama
from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random
colorama.init()

# Create Spell list
fire = Spell("Fire", 10, 100, "black")
Thunder = Spell("Thunder", 12, 124, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")
cure = Spell("cure", 12, 120, "white")
cura = Spell("cura", 18, 200, "white")

player_spells=[fire,Thunder,blizzard,meteor,cure,cura]


# Create some Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 100)
elixer = Item("Elixer", "elixer", "Fully restores MP/HP of one party member", 9999)
megaelixer = Item("MagaElixer", "elixer", "Fully restores MP/HP party's member", 9999)
grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_items=[{ "item": potion,"quantity": 15}, {"item": hipotion,"quantity": 5}, 
                {"item": superpotion,"quantity" : 1},
                {"item": elixer,"quantity": 5},
                {"item":megaelixer, "quantity" : 5},
                {"item": grenade, "quantity": 5}]

# Defining players and ennemies
player1=Person("Valos :", 1800, 132, 60, 34, player_spells,player_items) 
player2=Person("Nick  :",4160,188,60,34, player_spells,player_items) 
player3=Person("Robot :",3089,174,60,34, player_spells,player_items) 

ennemy1=Person("Imp   :",1200,130,560,3255, [],[])
ennemy2=Person("Dwarf :",10200,221,500,25, [],[])
ennemy3=Person("Imp   :",1200,130,560,3255, [],[])

players=[player1, player2, player3]
ennemies=[ennemy1, ennemy2, ennemy3]


running = True
i=0
print(bcolors.FAIL + bcolors.BOLD + "An ENEMY ATTACKS!" + bcolors.ENDC)
while running:
    print("\n==============================================================================================")
    print("\n\n")
    print("NAME                        HP                                      MP")
    for player in players :
        player.get_stats()
    
    print("\n")   
    for ennemy in ennemies :
        ennemy.get_ennemy_stats()
 
    for player in players :
        player.choose_action()
        choice=input("Choose action: ")
        index = int(choice) -1
        if index == 0 :
            dmg=player.generate_damage()
            enemy = player.choose_target (ennemies)
            ennemies[enemy].take_damage(dmg)
            print("\n You attacked "+ennemies[enemy].name+ " for", dmg, "points of damage.")
        elif index==1:
            player.choose_magic()
            magic_choice=int(input("Choose Magic: "))-1
            if magic_choice == -1 :
                    continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()
        
            current_mp=player.get_mp()
            if spell.cost > current_mp :
                print(bcolors.FAIL + "\nNot enough MP\n"+ bcolors.ENDC)
                continue
            player.reduce_mp(spell.cost)
            
            if spell.type=="white" :
                player.heal(magic_dmg)
                print(bcolors.OKBLUE+"\n" + spell.name + " heals for",str(magic_dmg), "Hit Points"+bcolors.ENDC)
            elif spell.type=="black" :
                enemy = player.choose_target (ennemies)
                ennemies[enemy].take_damage(magic_dmg)
                print(bcolors.OKBLUE+"\n" + spell.name + " deals",str(magic_dmg), "points of damage on " +ennemies[enemy].name +bcolors.ENDC)
        elif index==2 :
            player.choose_item()
            item_choice = int(input("Choose item: ")) - 1
            if item_choice== -1 :
                continue
            item = player.items[item_choice]["item"]
            if player.items[item_choice]["quantity"] ==0:
                print(bcolors.FAIL + "\n"+ "None Left"+bcolors.ENDC)
                continue
            player.items[item_choice]["quantity"]-=1
            
            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n"+ item.name + " heals for ", str(item.prop),"HP"+bcolors.ENDC)
            elif item.type == "elixer" :
                if item.name=="megaelixer" :
                    for i in players :
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else :
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print(bcolors.OKGREEN+"\n"+item.name + " fully restores HP/MP"+bcolors.ENDC)
            elif item.type == "attack":
                enemy = player.choose_target (ennemies)
                ennemies[enemy].take_damage(item.prop)
                print(bcolors.FAIL+"\n"+ item.name + " grenade deals ", str(item.prop) , " damages to " + ennemies[enemy].name + bcolors.ENDC)

    ennemy_choice = 1
    target = random.randrange(0,3)
    ennemy_dmg=ennemies[0].generate_damage()
    players[target].take_damage(ennemy_dmg)
    
    if ennemy.get_hp() == 0 :
        print(bcolors.OKGREEN+"You win" + bcolors.ENDC)
        running=False
    elif player.get_hp() == 0 :
        print(bcolors.FAIL+"You loose" + bcolors.ENDC)
        running=False
    

