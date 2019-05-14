import colorama
from classes.game import Person, bcolors
from classes.magic import Spell
colorama.init()
fire = Spell("Fire", 10, 100, "black")
Thunder = Spell("Thunder", 12, 124, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
Meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")
cure = Spell("cure", 12, 120, "white")
cura = Spell("cura", 18, 200, "white")



player=Person(460,65,60,34, [fire,Thunder,blizzard,cure,cura])
ennemy=Person(1200,65,45,25, [])

running = True
i=0
print(bcolors.FAIL + bcolors.BOLD + "An ENEMY ATTACKS!" + bcolors.ENDC)
while running:
    print("=================")
    player.choose_action()
    choice=input("Choose action:")
    index = int(choice) -1
    if index == 0 :
        dmg=player.generate_damage()
        ennemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage.")
    elif index==1:
        player.choose_magic()
        magic_choice=int(input("Choose Magic:"))-1

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()
     
        current_mp=player.get_mp()
        if spell.cost > current_mp :
            print(bcolors.FAIL + "\nNot enough MP\n"+ bcolors.ENDC)
            continue
        player.reduce_mp(spell.cost)
        ennemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE+"\n" + spell.name + " deals",str(magic_dmg), "points of damage"+bcolors.ENDC)

    ennemy_choice = 1
    ennemy_dmg=ennemy.generate_damage()
    player.take_damage(ennemy_dmg)
    print("Ennemy attacked for", ennemy_dmg, "points of damage.")

    print("------------------------------------")
    print("Ennemy HP:",bcolors.FAIL + str(ennemy.get_hp())+ "/"+ str(ennemy.get_max_hp())+bcolors.ENDC)
    print("Your HP:",bcolors.OKGREEN + str(player.get_hp())+ "/"+ str(player.get_max_hp())+bcolors.ENDC)
    print("Your MP:",bcolors.OKBLUE + str(player.get_mp())+ "/"+ str(player.get_max_mp())+bcolors.ENDC)
    if ennemy.get_hp() == 0 :
        print(bcolors.OKGREEN+"You win" + bcolors.ENDC)
        running=False
    elif player.get_hp() == 0 :
        print(bcolors.FAIL+"You loose" + bcolors.ENDC)
        running=False
    

