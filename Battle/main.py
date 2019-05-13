import colorama
from classes.game import Person, bcolors
colorama.init()
magic=[{"name":"Fire", "cost":10, "dmg":100},
{"name":"Thunder", "cost":12, "dmg":124},
{"name":"Blizzard", "cost":10, "dmg":100}]
player=Person(460,65,60,34, magic)
ennemy=Person(1200,65,45,25, magic)

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
        magic_dmg=player.generate_spell_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_mp_cost(magic_choice)
        current_mp=player.get_mp()
        if cost > current_mp :
            print(bcolors.FAIL + "\nNot enough MP\n"+ bcolors.ENDC)
            continue
        player.reduce_mp(cost)
        ennemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE+"\n" + spell + " deals",str(magic_dmg), "points of damage"+bcolors.ENDC)

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
    

