# Text only RPG
# venombash@gmail.com
#
# This is a text only Role-Playing Game. This is based off of a DND story that
# I wrote a while back.
# Enjoy!

player = ""# the players name
health = 0# the players health
armor = 0# the players armor
hd = 0# the players hit die
race = ""# the players race
Class = ""# the players class
lang = []# the languages the players character knows
enemies = [""]# the list of enemies in a battle
enemy_health = 0# the enemies health(the one that the players currently fighting)
enemy_armor = 0# the current enemies armor
enemy_hd = 0# the enemies hit die
gp = 0# the players gold pieces
sp = 0# the players silver pieces
bp = 0# the players bronze pieces
inventory = []# the players inventory
hunger = 0# the players hunger
num_enemies = 0# the number of enemies the player has to fight

def menu():
    global player, health, armor, hd, race, Class, lang

    MENU = """
0 - Exit
1 - Name your player
2 - Choose race
3 - Choose class
4 - Start your adventure!
"""

    print(MENU)# prints the menu

    choice = input()

    if choice == "0":
        import sys
        sys.exit()
    elif choice == "1":# the player wants to name their character
        i = input("Name: ")
        player = i
    elif choice == "2":# the player wants to choose their characters race
        RACES = """
1 - Human, 6 HP, 10 Armor, Languages: Basic
2 - Dwarf, 8 HP, 15 Armor, Languages: Basic, Dwarfish
3 - Elf, 6 HP, 10 Armor, Languages: Basic, Elvish, Ald Tang
4 - Halfling, 4 HP, 5 Armor, Languages: Basic, Plesant
"""

        print(RACES)
        i = input("Race: ")
        if i == "1":
            race = "Human"
            hp = 6
            armor = 10
            lang.append("Basic")
        elif i == "2":
            race = "Dwarf"
            hp = 8
            armor = 15
            lang.append("Basic")
            lang.append("Dwarfish")
        elif i == "3":
            race = "Elf"
            hp = 6
            armor = 10
            lang.append("Basic")
            lang.append("Elvish")
            lang.append("Ald Tang")
        elif i == "4":
            race = "Halfling"
            hp = 4
            armor = 5
            lang.append("Basic")
            lang.append("Plesant")
        else:
            print("Please choose one of the above.")
    elif choice == "3":# the player wants to choose their characters class
        CLASSES = """
1 - Warrior, 6 HD
2 - Priest, 6 HD
3 - Hunter, 8 HD
4 - Rouge, 10 HD
"""
        print(CLASSES)
        i = input("Class: ")

        if i == "1":
            Class = "Warrior"
            hd = 6
        elif i == "2":
            Class = "Priest"
            hd = 6
        elif i == "3":
            Class = "Hunter"
            hd = 8
        elif i == "4":
            Class = "Rouge"
            hd = 10
        else:
            print("Please choose one of the options above.")
    elif choice == "4":# the player wants to start their adventure
        if player != "" and Class != "" and race != "":
            scene1()
        else:# the player has not finished creating their character
            print("Not done creating your player.")
    else:# the player has entered some unknown option
        print("Please enter one of the options above.")

def scene1():

    SCENE = """
You are riding to a place called Lathos for it's exquisite purple. When you get
there you are increasingly thirsty, and decide to stop for a drink at The White
Horse. A big tavern/inn.
"""
    print(SCENE)

    playerTurn('White Horse')

def playerTurn(location):
    
    global num_enemies

    if location == "White Horse":
        options = """
0 - Exit
1 - Inspect the Tavern
2 - Talk to the barman
3 - Leave the tavern
4 - Check Inventory
"""
        print(options)
        choice = input()

        if choice == "1":
            inspect('White Horse')
        elif choice == "2":
            talk('Barman')
        elif choice == "3":
            scene2(1)
        elif choice == "4":
            print(inventory)
            go(1)
        elif choice == "0":
            import sys
            sys.exit()

    elif location == "Lathos":
        options = """
0 - Exit
1 - Go to The White Horse
2 - Inspect the village
3 - Check inventory
"""
        print(options)
        choice = input()

        if choice == "1":
            scene3(1)
        elif choice == "2":
            inspect("Lathos")
        elif choice == "3":
            print(inventory)
            go(2)
        elif choice == "0":
            import sys
            sys.exit()

    elif location == "Bar":
        options = """
1 - \"I want a couple bottles of ale.
2 - \"I want to talk to the mayor.
"""

        print(options)
        choice = input()

        if choice == "1":
            scene4(1)
        elif choice == "2":
            scene4(2)

    elif location == "bakery":
        options = """
0 - Exit
1 - Buy some bread
2 - Talk to the baker
3 - Leave the bakery
4 - Check inventory
"""

        print(options)
        choice = input()

        if choice == "1":
            buy("bread")
        elif choice == "2":
            talk("Baker")
        elif choice == "3":
            scene2(1)
        elif choice == "4":
            print(inventory)
            go(3)
        elif choice == "0":
            import sys
            sys.exit()
    elif location == "baker":
        options = """
1 - \"I want to buy some pastries
2 - \"I want to talk to the mayor
"""
        print(options)
        choice = input()
        
        if choice == "1":
            buy("paste")
        elif choice == "2":
            scene6(1)
            
    elif location == "lib?":
        options = """
0 - Exit
1 - Go to the library
2 - Go to the White Horse
"""
        
        print(options)
        choice = input()
        
        if choice == "1":
            go('library')
        elif choice == "2":
            go(1)
        elif choice == "0":
            import sys
            sys.exit()
            
    elif location == "library":
        options = """
0 - Exit
1 - Inspect the library
2 - Ask about Cron
3 - Check inventory
"""
        
        print(options)
        choice = input()
        
        if choice == "1":
            inspect('lib')
        elif choice == "2":
            ask('cron')
        elif choice == "3":
            print(inventory)
            go('library')
        elif choice == "0":
            import sys
            sys.exit()
            
    elif location == "cron":
        SCENE = """
You go up to a man sitting at a table, by himself, sipping slowly
from an iron flask. You approch the man with caution,
\"Hello sir. I am looking for a Cron?\"
He slowly turns one eyepatched eye toward you,
\"Looks like you found him.\"
"""

        print(SCENE)
        options = """
0 - Exit
1 - \"Someone told me you knew about the fall.\"
2 - \"Sorry to bother you.\"
"""
        print(options)
        choice = input()
        
        if choice == "1":
            talk('cron')
        elif choice == "2":
            go('library')
        elif choice == "0":
            import sys
            sys.exit()
            
    elif location == "fort?":
        options = """
0 - Exit
1 - Start travling North to the fort
2 - Stay in Lathos
"""

        print(options)
        choice = input()
        
        if choice == "1":
            scene9(1)
        elif choice == "2":
            go('library')
        elif choice == "0":
            import sys
            sys.exit()
            
    elif location == 'camp':
        options = """
0 - Exit
1 - Set up camp in the clearing
2 - Set up camp in the woods
"""

        print(options)
        choice = input()
        
        if choice == "1":
            scene9(2)
            num_enemies = 3
        elif choice == "2":
            scene9(3)
        elif choice == "0":
            import sys
            sys.exit()
            
    elif location == "cave":
        options = """
0 - Exit
1 - Go through the cave
2 - Go over the cave
"""
        
        print(options)
        choice = input()
        
        if choice == "1":
            scene10(1)
        elif choice == "2":
            scene10(2)
        elif choice == "3":
            callExit()
            
    elif location == "woods":
        SCENE = """
As you walk you come to woods with a sign that says beware.
There is a narrow path around it.
"""
        print(SCENE)
        options = """
0 - Exit
1 - Go through woods
2 - Go around
"""
        print(options)
        choice = input()
        
        if choice == "1":
            endStory('woods')
        elif choice == "2":
            scene11(1)
        elif choice == "3":
            callExit()
            
    elif location == "canyon":
        options = """
0 - Exit
1 - Try to climb down
2 - Give up
3 - Set up camp
"""
        print(options)
        choice = input()
        
        if choice == "1":
            scene12(1)
        elif choice == "2":
            print("You still regret that choice")
            endGame()
        elif choice == "3":
            scene12(2)
        elif choice == "0":
            callExit()
            
    elif location == "beg":
        options = """
0 - Exit
1 - Attack the begger
2 - Scream at him
3 - Offer him  some meat
"""
        print(options)
        choice = input()
        
        if choice == "1":
            battle('begger', 1)
            scene13(1)
        elif choice == "2":
            scene13(2)
        elif choice == "3":
            scene13(3)
            
    elif location == "begger":
        options = """
1 - Give him some meat
2 - Force him to help you
3 - Check inventory
"""
        print(options)
        choice = input()
        
        if choice == "1":
            scene14(1)
        elif choice == "2":
            scene14(2)
        elif choice == "3":
            print(inventory)
            
    elif location == "talon":
        options = """
1 - Let him come with you
2 - Abandon him
"""
        print(options)
        choice = input()
        
        if choice == "1":
            scene15(1)
        elif choice == "2":
            scene15(2)
            
    elif location == "orc_pack":
        options = """
1 - Try to fight your way out
2 - Hide behind some rocks
"""
        print(options)
        choice = input()
        
        if choice == "1":
            battle('orcs, talon', 5)
        elif choice == "2":
            scene16(1)
            
    elif location == "orc_slave":
        SCENE = """
As you raise your sword again, it flies out of your hand and into a
nearby rock. As you look up you see a wizard, holding a staff of fire.
\"That's enough!\" he roared. 
\"Take these scumbags into my dungeon!\"
As told the pack of orcs drags you and Talon a short way, and into the
dungeon.
\"Do you suppose that wizard was Drastone?\" you ask Talon.
He looks at you with fire in his eyes,
\"I have no doubt.\"
"""
        print(SCENE)
        goodbye()
            



def inspect(location):
    global gp, sp, bp, armor, inventory, hd

    if location == "White Horse":
        import random
        roll = random.randint(1, 2)
        if roll == 1:
            print("You found 10 GP!")
            gp += 10
            playerTurn("White Horse")
        elif roll == 2:
            print("You found 10 GP and Leather armor!")
            gp += 10
            armor += 15
            playerTurn("White Horse")

    elif location == "Lathos":
        import random
        roll = random.randint(1, 2)
        if roll == 1:
            print("You found a bakery!")
            playerTurn("bakery")
        elif roll == 2:
            print("You found a sword!")
            inventory.append("sword")
            hd += 5
            playerTurn("Lathos")
            
    elif location == "lib":
        import random
        roll = random.randint(1, 2)
        if roll == 1:
            print("You found a book in Ald Tang!")# ald tang = old tounge
            playerTurn('library')
        elif roll == 2:
            print("You found 5 SP!")
            sp += 5
            playerTurn('libarary')

def talk(person):
    global health, armor, enemies, iventory, gp, sp, bp

    if person == "Barman":
        import random
        roll = random.randint(1, 6)

        if roll < 4:
            print("Go away kid.")
            scene2(3)
        else:
            print("What do you need kid?")
            scene2(2)

    elif person == "Baker":
        import random
        roll = random.randint(1, 4)

        if roll < 3:
            print("Go away.")
            scene5(1)
        else:
            print("What do you need?")
            scene5(2)
            
    elif person == "cron":
        import random
        roll = random.randint(1, 2)
        
        if roll == 1:
            print("Go away")
            playerTurn('library')
        elif roll == 2:
            print('"Aye"')
            scene8("cron's story")

def scene2(scene):

    if scene == 1:
        SCENE = """
You walk out into the village and see a busy, bustling population. As you
realize the sun is going down, you have no place to sleep."""
        print(SCENE)

        playerTurn("Lathos")

    elif scene == 2:
        SCENE = """
The bartender leans across the bar toward you."""
        print(SCENE)

        playerTurn("Bar")

    elif scene == 3:

        playerTurn("White Horse")

def scene3(scene):

    if scene == 1:
        SCENE = """
You walk back to the White Horse
"""
        playerTurn("White Horse")

def buy(product):
    global gp, sp, bp, inventory, armor

    if product == "bread":# the player wants to buy bread
        if gp > 0:# the player is not broke
            if gp == 10 or gp > 10:# the player has enough money
                gp -= 10
                inventory.append("bread")
                print("You have bought some bread!")
                playerTurn('bakery')
            else:
                print("You don't have enough money")
                playerTurn('bakery')
        else:
            print("You are broke")
            playerTurn('bakery')
            
    elif product == "alex2":# the player wants to buy ale x2
        if gp > 0:# the player is not broke
            if gp == 20 or gp > 20:# the player has enough money
                gp -= 20
                inventory.append('ale')
                inventory.append('ale')
                print("You have bought ale x2!")
                playerTurn("White Horse")
            else:
                print("You don't have enough money")
                playerTurn('White Horse')
        else:
            print("You are broke")
            playerTurn('White Horse')
            
            
    elif product == "paste":# the player wants to buy pastries
        if gp > 0:# the player is not broke
            if gp == 5 or gp > 5:# the player has enough money
                gp -= 5
                inventory.append('pastry')
                print("You have bought a pastry!")
                playerTurn("bakery")
            else:
                print("You don't have enough money")
                playerTurn('bakery')
        else:
            print("You are broke")
            playerTurn('bakery')

def scene4(scene):
	
	if scene == 1:
		buy('alex2')
	elif scene == 2:
		print("No can do kid.")
		playerTurn('White Horse')
		
def scene5(scene):
	
	if scene == 1:
		playerTurn('bakery')
	elif scene == 2:
		playerTurn('baker')
        
def go(location):
    
    if location == 1:
        playerTurn("White Horse")
    elif location == 2:
        playerTurn("Lathos")
    elif location == 3:
        playerTurn("bakery")
    elif location == "library":
        playerTurn('library')
    elif location == "cave":
        scene9(3)
        
def scene6(scene):
    
    if scene == 1:
        SCENE = """
The baker looks at you with sad eyes,
\"Dead\", she says. \"Been dead for a long time\". 
You look at her, puzzled,
\"So who rules this place?\", you ask.
\"No one, not since the fall. Go to the library, Cron will tell
you everyhing\""""
        
        print(SCENE)
        playerTurn('lib?')
        
def ask(person):
    
    if person == "cron":
        import random
        roll = random.randint(1, 2)
        if roll == 1:
            scene7(1)
        else:
            scene7(2)
            
def scene7(scene):
    
    if scene == 1:
        playerTurn('cron')
    elif scene == 2:
        print("Nobody knew where cron was")
        playerTurn('library')
        
def scene8(scene):
    
    if scene == "cron's story":
        STORY = """
\"Once, long time ago, this village was the heart of the world.
Busy, bustling, Lathos sold the finest purple that you would ever see.
There was a very old family, called the Strongs, had a very tempramental
son named Drastone.

Well old Drastone was always up to some trouble, when he got mad,
he took it out on others. Well, one day he got into a disagreement
with another farmer down the way. Killed the entire family and sent
a darkness over the village like a plague.

The witch doctor had a right old time clearing it all up, destroyed
Drastone's father. Then one morning, Drastone's father was dead. They
took Flaco, the old killer into custody, but they had to let him go
couldn't prove it was him.\"

Cron got an ugly look on his face.

\"I'd bet money that old Drastone hired him to do it. We'd all like to
see his head on a spit.\"

You look over at cron.

\"I can bring you Drastone.\"

Cron looked at you,

\"What's your name kid?\"

\"%s sir.\"

\"Well %s, if you do it I will pay you handsomly.\"

\"Consider it done sir.\""""

        print(STORY % (player,player))
        playerTurn('fort?')
        
def scene9(scene):
    
    global num_enemies
    
    if scene == 1:
        SCENE = """
You walk down the road North for hours until the sunset.
When you come to a mile marker, you decide to set up camp
with the tent Cron gave you.
"""

        print(SCENE)
        playerTurn('camp')
        
    elif scene == 2:
        battle('orcs', 1)
        battle('orcs', 1)
        battle('orcs', 1)
        print("You won the battle!")
        go('cave')
        
    elif scene == 3:
        SCENE = """
After a refreshing night of sleep, you get up and start to walk again.
Soon you come to a cave.
"""

        print(SCENE)
        playerTurn('cave')
        
def battle(enemy, number):
    global armor, enemy_armor, enemy_health, hd, health, inventory
    
    if enemy == 'orcs':
        import random
        enemy_health = 5
        enemy_armor = 5
        for i in range(number):
            enemies.insert(0, 'orc')
        player_roll = random.randint(1, hd)
        print("You rolled a %d" % (player_roll))
        checkDead('enemy', player_roll)
        enemy_roll = random.randint(1, 6)
        print("%s rolled a %s" % (enemy, enemy_roll))
        checkDead('player', enemy_roll)
        playerTurn('battle?')
        
    elif enemy == 'goblin':
        import random
        enemy_health = 5
        enemy_armor = 5
        for i in range(number):
            enemies.insert(0, 'goblin')
        player_roll = random.randint(1, hd)
        print("You rolled a %d" % (player_roll))
        checkDead('enemy', player_roll)
        enemy_roll = random.randint(1, 6)
        print("%s rolled a %s" % (enemy, enemy_roll))
        checkDead('player', enemy_roll)
        playerTurn('battle?')
        
    elif enemy == 'begger':
        import random
        enemy_health = 10
        enemy_armor = 0
        for i in range(number):
            enemies.insert(0, 'begger')
        player_roll = random.randint(1, hd)
        print("You rolled a %d" % (player_roll))
        checkDead('enemy', player_roll)
        enemy_roll = random.randint(1, 8)
        print("%s rolled a %s" % (enemy, enemy_roll))
        checkDead('player', enemy_roll)
        playerTurn('battle?')
        
    elif enemy == "orcs, talon":
        import random
        enemy_health = 5
        enemy_armor = 5
        for i in range(number):
            enemies.insert(0, 'orc')
        player_roll = random.randint(1, hd)
        print("You rolled a %d" % (player_roll))
        checkDead('enemy', player_roll)
        enemy_roll = random.randint(1, 6)
        print("%s rolled a %s" % (enemy, enemy_roll))
        checkDead('player', enemy_roll)
        talon_roll = random.randint(1, 10)
        print("Talon rolled a %d" % (talon_roll))
        checkDead('enemy', talon_roll)
        playerTurn('orc_slave')
                
def checkDead(pawn, roll):
    
    global enemy_health, enemy_armor, armor, health
    
    if pawn == 'enemy':
        if enemy_health > 0 and enemy_armor < 0 or enemy_armor == 0:
            enemy_health -= roll
            if enemy_health < 0 or enemy_health == 0:
                print("Enemy died")
        else:
            enemy_armor -= roll
    elif pawn == 'player':
        if health > 0 and armor < 0 or armor == 0:
            health -= roll
            if health < 0 or health == 0:
                print("Hero died")
                import sys
                sys.exit()
        else:
            armor -= roll
            
def callExit():
    import sys
    sys.exit()
    
def scene10(scene):
    
    if scene == 1:
        SCENE = """
As you walk into the cave you see a bright light coming from a hole
in the celing and water pooling on the floor underneath it. As you
walk through it three Goblins drop from the celing.
"""
        print(SCENE)
        battle('goblin', 1)
        battle('goblin', 1)
        battle('goblin', 1)
        print("You won the battle!")
        playerTurn('woods')
        
    elif scene == 2:
        SCENE = """
As you climb over the cave you see three goblins sitting with their
feet dangling over the edge of the hole. You just manage to escape
them.
"""
        
        print(SCENE)
        playerTurn('woods')
        
def endStory(where):
    
    if where == "woods":
        SCENE = """
As you walk through the woods you see a big pack of orcs. You try
to hide but it's too late. You get destroyed by a mace.
"""
        print(SCENE)
        endGame()
        
def endGame():
    import time
    print("Game Over.")
    time.sleep(10)
    callExit()
    
def scene11(scene):
    
    SCENE = """
As you walk down the path you come to a big canyon. So deep you
can't even see the bottom. You have to cross.
"""
    print(SCENE)
    playerTurn('canyon')
    
def scene12(scene):
    
    if scene == 1:
    
        SCENE = """
As you begin to climb down you slip and fall into the black...
"""
        print(SCENE)
        endGame()
        
    elif scene == 2:
        SCENE = """
After a night of refreshing sleep, you get up to find a begger eating
your food.
"""
        print(SCENE)
        playerTurn('beg')
        
def scene13(scene):
    
    if scene == 1:
        SCENE = """
As your raise your weapon again the begger turns into a large eagle
and flies over the caynon. As you wait for him to come back, your
food slowly runs out.
"""
        print(SCENE)
        endGame()
        
    elif scene == 2:
        SCENE = """
\"Hey!\" you scream. \"Get out of my food!\"
The begger jumps and turns into a big eagle and flies over the canyon.
As you wait your food slowly runs out.
"""
        print(SCENE)
        endGame()
        
    elif scene == 3:
        SCENE = """
\"Hey.\" you say. \"Need some food?\"
He looks at you,
\"You need a ride?\" he asks.
You look at him, suprised.
\"Yeah, can you help me?\"
\"Let's see about that meat first.\"
"""
        print(SCENE)
        playerTurn('begger')
        
def scene14(scene):
    
    if scene == 1:
        SCENE = """
As the man eats, you wait impatiently for him to help you.
Finally he tears the last of the meat off and looks at you.
\"Get on,\" he says, as he turns into a large eagle.
When you get across to the other side the man extends his hand,
\"Talon,\" he said.
\"%s,\" you say shaking his hand.
\"Right let's get moving then.\"
"""
        print(SCENE % (player))
        playerTurn('talon')
        
    elif scene == 2:
        if "sword" in inventory:
            SCENE = """
As you draw your sword and approach him, he turns into an eagle and
fly away. As you wait your food runs out.
"""
        else:
            SCENE = """
As you reach into your pack you realize you have no weapons.
"""
        print(SCENE)
        endGame()
        
def scene15(scene):
    
    if scene == 1:
        SCENE = """
As you begin to travel down the road on the other side, you stumble 
upon a pack of orcs.
"""
        print(SCENE)
        playerTurn('orc_pack')
        
    elif scene == 2:
        SCENE = """
\"You can't come,\" you say. \"It will be to dangerous.\"
He looks at you sadly.
\"Too bad,\" he says suddenly knocking you over the edge.
\"I was looking forward to it.\"
"""
        print(SCENE)
        endGame()
        
def scene16(scene):
    
    if scene == 1:
        SCENE = """
As you dive behind some rocks you fall into the den of a
giant bear.
"""
        print(SCENE)
        endGame()
        
def goodbye():
    print("\n")
    goodbye = """
Thanks for playing The Evil Wizard!
leave feedback at venombash@gmail.com

don't miss coming soon,
The Evil Wizard II Wrath of Drastone.

Thanks for playing!
"""
    import time, sys
    print(goodbye)
    input("\n\nPress enter to exit.")
    sys.exit()
        
            
        

    


        

if __name__ == "__main__":
    while True:
        menu()
