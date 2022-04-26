import random

def simpleMelee():
    print("--------------------")
    print("SIMPLE MELEE WEAPONS")
    print("--------------------")
    print("Club")
    print("Dagger")
    print("Greatclub")
    print("Handaxe")
    print("Javelin")
    print("Light hammer")
    print("Mace")
    print("Quarterstaff")
    print("Sickle")
    print("Spear")
    print("--------------------")

def simpleRanged():
    print("--------------------")
    print("SIMPLE RANGED WEAPONS")
    print("--------------------")
    print("Light crossbow")
    print("Dart")
    print("Shortbow")
    print("Sling")
    print("--------------------")

def martialMelee():
    print("--------------------")
    print("MARTIAL MELEE WEAPONS")
    print("--------------------")
    print("Battleaxe")
    print("Flail")
    print("Glaive")
    print("Greatsword")
    print("Halberd")
    print("Lance")
    print("Longsword")
    print("Maul")
    print("Morningstar")
    print("Pike")
    print("Rapier")
    print("Scimitar")
    print("Shortsword")
    print("Trident")
    print("War pick")
    print("Warhammer")
    print("Whip")
    print("--------------------")

def martialRanged():
    print("--------------------")
    print("MARTIAL RANGED WEAPONS")
    print("--------------------")
    print("Blowgun")
    print("Hand crossbow")
    print("Heavy crossbow")
    print("Longbow")
    print("Net")
    print("--------------------")

def simpleOrMartial():
    print("--------------------")
    choice1 = input("Simple or Martial? ").lower()
    print("--------------------")
    return choice1

def meleeOrRanged():
    choice2 = input("Melee or Ranged? ").lower()
    return choice2

def weaponChoice():
    choice1 = simpleOrMartial()
    choice2 = meleeOrRanged()

    if choice1 == "simple" and choice2 == "melee":
        simpleMelee()
        choice3 = input("Which weapon: ").lower()
        if choice3 == "club":
            clubFile = open("dungeonsAndDragons/weaponRoller/weapons/simpleMelee/club.txt", "r")
            print("--------------------")
            print(clubFile.read())
            clubFile.close()
        elif choice3 == "dagger":
            daggerFile = open("dungeonsAndDragons/weaponRoller/weapons/simpleMelee/dagger.txt", "r")
            print("--------------------")
            print(daggerFile.read())
            daggerFile.close()
        elif choice3 == "greatclub":
            greatclubFile = open("dungeonsAndDragons/weaponRoller/weapons/simpleMelee/greatclub.txt", "r")
            print("--------------------")
            print(greatclubFile.read())
            greatclubFile.close()
        elif choice3 == "handaxe":
            handaxeFile = open("dungeonsAndDragons/weaponRoller/weapons/simpleMelee/handaxe.txt", "r")
            print("--------------------")
            print(handaxeFile.read())
            handaxeFile.close()
        elif choice3 == "javelin":
            javelinFile = open("dungeonsAndDragons/weaponRoller/weapons/simpleMelee/javelin.txt", "r")
            print("--------------------")
            print(javelinFile.read())
            javelinFile.close()
        elif choice3 == "light hammer":
            lightHammerFile = open("dungeonsAndDragons/weaponRoller/weapons/simpleMelee/lightHammer.txt", "r")
            print("--------------------")
            print(lightHammerFile.read())
            lightHammerFile.close()
        elif choice3 == "mace":
            maceFile = open("dungeonsAndDragons/weaponRoller/weapons/simpleMelee/mace.txt", "r")
            print("--------------------")
            print(maceFile.read())
            maceFile.close()
        elif choice3 == "quarterstaff":
            quarterstaffFile = open("dungeonsAndDragons/weaponRoller/weapons/simpleMelee/quarterstaff.txt", "r")
            print("--------------------")
            print(quarterstaffFile.read())
            quarterstaffFile.close()
        elif choice3 == "sickle":
            sickleFile = open("dungeonsAndDragons/weaponRoller/weapons/simpleMelee/sickle.txt", "r")
            print("--------------------")
            print(sickleFile.read())
            sickleFile.close()
        elif choice3 == "spear":
            spearFile = open("dungeonsAndDragons/weaponRoller/weapons/simpleMelee/spear.txt", "r")
            print("--------------------")
            print(spearFile.read())
            spearFile.close()
    elif choice1 == "simple" and choice2 == "ranged":
        simpleRanged()
        choice3 = input("Which weaopn: ").lower()
        if choice3 == "light crossbow":
            lightCrossbowFile = open("dungeonsAndDragons/weaponRoller/weapons/simpleRanged/lightCrossbow.txt", "r")
            print("--------------------")
            print(lightCrossbowFile.read())
            lightCrossbowFile.close()
        elif choice3 == "dart":
            dartFile = open("dungeonsAndDragons/weaponRoller/weapons/simpleRanged/dart.txt", "r")
            print("--------------------")
            print(dartFile.read())
            dartFile.close()
        elif choice3 == "shortbow":
            shortbowFile = open("dungeonsAndDragons/weaponRoller/weapons/simpleRanged/shortbow.txt", "r")
            print("--------------------")
            print(shortbowFile.read())
            shortbowFile.close()
        elif choice3 == "sling":
            slingFile = open("dungeonsAndDragons/weaponRoller/weapons/simpleRanged/sling.txt", "r")
            print("--------------------")
            print(slingFile.read())
            slingFile.close()
    elif choice1 == "martial" and choice2 == "melee":
        martialMelee()
        choice3 = input("Which weapon: ").lower()
        if choice3 == "battleaxe":
            battleaxeFile = open("dungeonsAndDragons/weaponRoller/weapons/maritalMelee/battleaxe.txt", "r")
            print("--------------------")
            print(battleaxeFile.read())
            battleaxeFile.close()
        elif choice3 == "flail":
            flailFile = open("dungeonsAndDragons/weaponRoller/weapons/maritalMelee/flail.txt", "r")
            print("--------------------")
            print(flailFile.read())
            flailFile.close()
        elif choice3 == "glaive":
            glaiveFile = open("dungeonsAndDragons/weaponRoller/weapons/maritalMelee/glaive.txt", "r")
            print("--------------------")
            print(glaiveFile.read())
            glaiveFile.close()
        elif choice3 == "greataxe":
            greataxeFile = open("dungeonsAndDragons/weaponRoller/weapons/maritalMelee/greataxe.txt", "r")
            print("--------------------")
            print(greataxeFile.read())
            greataxeFile.close()
        elif choice3 == "greatsword":
            greatswordFile = open("dungeonsAndDragons/weaponRoller/weapons/maritalMelee/greatsword.txt", "r")
            print("--------------------")
            print(greatswordFile.read())
            greatswordFile.close()
        elif choice3 == "halberd":
            halberdFile = open("dungeonsAndDragons/weaponRoller/weapons/maritalMelee/halberd.txt", "r")
            print("--------------------")
            print(halberdFile.read())
            halberdFile.close()
        elif choice3 == "lance":
            lanceFile = open("dungeonsAndDragons/weaponRoller/weapons/maritalMelee/lance.txt", "r")
            print("--------------------")
            print(lanceFile.read())
            lanceFile.close()
        elif choice3 == "longsword":
            longswordFile = open("dungeonsAndDragons/weaponRoller/weapons/maritalMelee/longsword.txt", "r")
            print("--------------------")
            print(longswordFile.read())
            longswordFile.close()
        elif choice3 == "maul":
            maulFile = open("dungeonsAndDragons/weaponRoller/weapons/maritalMelee/maul.txt", "r")
            print("--------------------")
            print(maulFile.read())
            maulFile.close()
        elif choice3 == "morningstar":
            morningstarFile = open("dungeonsAndDragons/weaponRoller/weapons/maritalMelee/morningstar.txt", "r")
            print("--------------------")
            print(morningstarFile.read())
            morningstarFile.close()
        elif choice3 == "pike":
            pikeFile = open("dungeonsAndDragons/weaponRoller/weapons/maritalMelee/pike.txt", "r")
            print("--------------------")
            print(pikeFile.read())
            pikeFile.close()
        elif choice3 == "rapier":
            rapierFile = open("dungeonsAndDragons/weaponRoller/weapons/maritalMelee/rapier.txt", "r")
            print("--------------------")
            print(rapierFile.read())
            rapierFile.close()
        elif choice3 == "scimitar":
            scimitarFile = open("dungeonsAndDragons/weaponRoller/weapons/maritalMelee/scimitar.txt", "r")
            print("--------------------")
            print(scimitarFile.read())
            scimitarFile.close()
        elif choice3 == "shortsword":
            shortswordFile = open("dungeonsAndDragons/weaponRoller/weapons/maritalMelee/shortsword.txt", "r")
            print("--------------------")
            print(shortswordFile.read())
            shortswordFile.close()
        elif choice3 == "trident":
            tridentFile = open("dungeonsAndDragons/weaponRoller/weapons/maritalMelee/trident.txt", "r")
            print("--------------------")
            print(tridentFile.read())
            tridentFile.close()
        elif choice3 == "war pick":
            warPickFile = open("dungeonsAndDragons/weaponRoller/weapons/maritalMelee/warPick.txt", "r")
            print("--------------------")
            print(warPickFile.read())
            warPickFile.close()
        elif choice3 == "warhammer":
            warhammerFile = open("dungeonsAndDragons/weaponRoller/weapons/maritalMelee/warhammer.txt")
            print("--------------------")
            print(warhammerFile.read())
            warhammerFile.close()
        elif choice3 == "whip":
            whipFile = open("dungeonsAndDragons/weaponRoller/weapons/maritalMelee/whip.txt", "r")
            print("--------------------")
            print(whipFile.read())
            whipFile.close()
    elif choice1 == "martial" and choice2 == "ranged":
        martialRanged()
        choice3 = input("Which weapon: ")
        if choice3 == "blowgun":
            blowgunFile = open("dungeonsAndDragons/weaponRoller/weapons/martialRanged/blowgun.txt", "r")
            print("--------------------")
            print(blowgunFile.read())
            blowgunFile.close()
        elif choice3 == "hand crossbow":
            handCrossbowFile = open("dungeonsAndDragons/weaponRoller/weapons/martialRanged/handCrossbow.txt", "r")
            print("--------------------")
            print(handCrossbowFile.read())
            handCrossbowFile.close()
        elif choice3 == "heavy crossbow":
            heavyCrossbowFile = open("dungeonsAndDragons/weaponRoller/weapons/martialRanged/heavyCrossbow.txt", "r")
            print("--------------------")
            print(heavyCrossbowFile.read())
            heavyCrossbowFile.close()
        elif choice3 == "longbow":
            longbowFile = open("dungeonsAndDragons/weaponRoller/weapons/martialRanged/longbow.txt", "r")
            print("--------------------")
            print(longbowFile.read())
            longbowFile.close()
        elif choice3 == "net":
            netFile = open("dungeonsAndDragons/weaponRoller/weapons/martialRanged/net.txt", "r")
            print("--------------------")
            print(netFile.read())
            netFile.close()

def rollToHit():
    print("--------------------")
    print("ROLL TO HIT")
    print("--------------------")
    enemyAC = int(input("What is your enemy's AC? "))
    playerWeapon = input("What weapon are you using? ")
    playerModifier = int(input("What is your weapon modifier? "))
    toHit = random.randint(1, 20)
    toHitModifier = int(toHit + playerModifier)
    if toHitModifier >= enemyAC:
        print(toHitModifier, "vs", enemyAC)
        print("You hit the enemy with your", playerWeapon)
    elif toHit < enemyAC:
        print(toHitModifier, "vs", enemyAC)
        print("You missed!")    

def rollDamage():
    playerWeapon = input("What weapon are you using? ").lower()

    #1d4 bludgeoning
    if playerWeapon == "club" or "light hammer" or "sling":
        diceRoll = random.randint(1, 4)
        print("You deal " + str(diceRoll) + " bludgeoning damage")
    #1d4 piercing
    elif playerWeapon == "dagger" or "dart":
        diceRoll = random.randint(1, 4)
        print("You deal " + str(diceRoll) + " piercing damage")
    #1d4 slashing
    elif playerWeapon == "sickle" or "whi[":
        diceRoll = random.randint(1, 4)
        print("You deal " + str(diceRoll) + " slashing damage")
    
    #1d6 bludgeoning
    elif playerWeapon == "mace" or "quarterstaff":
        diceRoll = random.randint(1, 6)
        print("You deal " + str(diceRoll) + " bludgeoning damage")
    #1d6 piercing
    elif playerWeapon == "javelin" or "spear" or "shortbow" or "shortsword" or "trident" or "hand crossbow":
        diceRoll = random.randint(1, 6)
        print("You deal " + str(diceRoll) + " piercing damage")
    #1d6 slashing
    elif playerWeapon == "handaxe" or "scimitar":
        diceRoll = random.randint(1, 6)
        print("You deal" + str(diceRoll) + "slashing damage")
    
    #2d6 bludgeoning
    elif playerWeapon == "maul":
        diceRoll1 = str(random.randint(1, 6))
        diceRoll2 = str(random.randint(1, 6))
        diceRollTotal = diceRoll1 + diceRoll2
        print("You deal (" + str(diceRoll1) + " + " + str(diceRoll2) + ") " + str(diceRollTotal) + " bludgeoning damage")
    #2d6 slashing
    elif playerWeapon == "greatsword":
        diceRoll1 = str(random.randint(1, 6))
        diceRoll2 = str(random.randint(1, 6))
        diceRollTotal = diceRoll1 + diceRoll2
        print("You deal (" + str(diceRoll1) + " + " + str(diceRoll2) + ") " + str(diceRollTotal) + " slashing damage")

    #1d8 bludgeoning
    elif playerWeapon == "greatclub" or "flail" or "warhammer":
        diceRoll = random.randint(1, 8)
        print("You deal " + str(diceRoll) + " bludgeoning damage")
    #1d8 piercing
    elif playerWeapon == "light crossbow" or "morningstar" or "rapier" or "war pick" or "longbow":
        diceRoll = random.randint(1, 8)
        print("You deal " + str(diceRoll) + " piercing damage")
    #1d8 slashing
    elif playerWeapon == "battleaxe" or "halberd" or "longsword":
        diceRoll = random.randint(1, 8)
        print("You deal " + str(diceRoll) + " slashing damage")

    #1d10 bludgeoning
    elif playerWeapon == "":
        diceRoll = random.randint(1, 10)
        print("You deal " + str(diceRoll) + " bludgeoning damage")
    #1d10 piercing
    elif playerWeapon == "pike" or "heavy crossbow":
        diceRoll = random.randint(1, 10)
        print("You deal" + str(diceRoll) + " piercing damage")
    #1d10 slashing
    elif playerWeapon == "glaive":
        diceRoll = random.randint(1, 10)
        print("You deal " + str(diceRoll) + " slashing damage")

    #1d12 bludgeoning
    elif playerWeapon == "":
        diceRoll = random.randint(1, 12)
        print("You deal " + str(diceRoll) + " bludgeoning damage")
    #1d12 piercing
    elif playerWeapon == "lance":
        diceRoll = random.randint(1, 12)
        print("You deal " + str(diceRoll) + " piercing damage")
    #1d12 slashing
    elif playerWeapon == "greataxe":
        diceRoll = random.randint(1, 12)
        print("You deal " + str(diceRoll) + " slashing damage")

    #1 piercing
    elif playerWeapon == "blowgun":
        print("You deal 1 piercing damage")

    #net
    elif playerWeapon == "net":
        print("Your enemy is now restrained")

def menu():
    print("--------------------")
    print("MENU")
    print("--------------------")
    print("1. Weapon Information")
    print("2. Roll to hit")
    print("3. Roll for damage")
    print("--------------------")
    menuChoice = input("Choose an option: ")
    if menuChoice == "1":
        weaponChoice()
    elif menuChoice == "2":
        rollToHit()
    elif menuChoice == "3":
        rollDamage()

menu()