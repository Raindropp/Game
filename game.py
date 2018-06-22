menu = ['Dungeon','Blacksmith', 'Marketplace']

menu_response = ''

location = 'menu'

from time import sleep

player_hp = 100
player_atk = 10
player_armour = 0
gold = 0
orc_hp = 50
orc_atk = 10

while menu_response not in menu and location == 'menu':
    print(menu)
    menu_response = input("What would you like to do adventurer? Go to the: ")
    
    if menu_response == 'Dungeon':
        location = 'Dungeon'
        orc_hp = 50
    elif menu_response == 'Blacksmith':
        location = 'Blacksmith'
    elif menu_response == 'Marketplace':
        location = 'Marketplace'

    if location == 'Dungeon':
        print("An orc has appeared!")
        while player_hp > 0 and orc_hp > 0:

            face_enemy = input("Attack? y/n ")
            if face_enemy == 'y':
                orc_hp = orc_hp - player_atk
                print('You attacked the orc!')
                sleep(0.25)
                print('Orc Health: ' + str(orc_hp))
                if orc_hp > 0:
                    sleep(0.5)
                    print('The orc attacked you!')
                    player_hp = player_hp - orc_atk
                    sleep(0.25)
                    print('Your Health: ' + str(player_hp))
                    sleep(0.5)
            elif face_enemy == 'n':
                print('The orc attacked you!')
                player_hp = player_hp - orc_atk
                sleep(0.25)
                print('Your Health: ' + str(player_hp))
                sleep(0.5)
        if orc_hp < 1:
            print('You killed the orc!')
            player_hp = 100 + player_armour
            sleep(0.5)
            print('Returning you to the menu!')
            sleep(1)
            menu_response = ''
            location = 'menu'

    if location == 'Blacksmith':
        print('hello')

    if location == 'Marketplace':
        print('hey')
