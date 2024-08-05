label dialogueGiveCategory: #playX or even Player functions!
    $ noSpecificFuntion = 2

    if displayingScene.theScene[lineOfScene] == "GiveTreasure":
        $ searchHere = 0
        $ numberFound = 0
        $ lineOfScene += 1
        if displayingScene.theScene[lineOfScene] == "Common":
            $ searchHere = 0
            $ numberFound = renpy.random.randint(1, 3)
        elif displayingScene.theScene[lineOfScene] == "Uncommon":
            $ searchHere = 1
            $ numberFound = renpy.random.randint(1, 2)
        elif displayingScene.theScene[lineOfScene] == "Rare":
            $ searchHere = 2
            $ numberFound = 1
        if onAdventure == 0:
            $ datahere = LocationDatabase[targetLocation]
        else:
            $ datahere = AdventureHolder

        $ treasureFound = renpy.random.randint(0, len(datahere.Treasure[searchHere]) - 1)
        $ erosFound = datahere.Eros[searchHere]

        $ bonusMoney = 100
        python:
            for perk in attacker.perks:
                p = 0
                while  p < len(perk.PerkType):
                    if perk.PerkType[p] == "ErosBoost":
                        bonusMoney += perk.EffectPower[p]
                    p += 1

        $ erosFound *= (bonusMoney*0.01)
        $ erosFound *= (renpy.random.randint(75, 125)*0.01)
        $ erosFound *= (player.stats.Luck*0.01 + 1)
        $ erosFound =  int(math.floor(erosFound))

        $ numberFoundDis = ""
        $ pluralS = ""
        if numberFound > 1:
            $ numberFoundDis = str(numberFound) + " "
            $ pluralS = "s"
        if datahere.Treasure[searchHere][treasureFound] == "":
            $ display = "You plunder " + str(erosFound) + " Eros!"
        else:
            $ display = "You acquire " + numberFoundDis + datahere.Treasure[searchHere][treasureFound] + pluralS + "!"
            $ display += "\nYou also plunder " + str(erosFound) + " Eros!"
        "[display!i]"
        $ player.inventory.earn(erosFound)
        if datahere.Treasure[searchHere][treasureFound] != "":
            $ player.inventory.give(datahere.Treasure[searchHere][treasureFound], numberFound)
    elif displayingScene.theScene[lineOfScene] == "GiveExp":
        $ lineOfScene += 1
        $ player.stats.Exp += int(displayingScene.theScene[lineOfScene])
        if int(displayingScene.theScene[lineOfScene]) > 0:
            $ display = "Gained " + str(displayingScene.theScene[lineOfScene]) + " exp!"
        else:
            $ amountLost = moneyEarned*-1
            $ display = "Lost " + str(displayingScene.theScene[lineOfScene]) + " exp!"
        "[display!i]"
        $ expGiven = 1
        call refreshLevelVar from _call_refreshLevelVar_2
        call levelUpSpot from _call_levelUpSpot_1
        $ expGiven = 0
    elif displayingScene.theScene[lineOfScene] == "GiveItem":
        $ lineOfScene += 1
        $ amount = int(displayingScene.theScene[lineOfScene])
        $ lineOfScene += 1

        if amount > 0:
            $ player.inventory.give(displayingScene.theScene[lineOfScene] , amount)
            $ display = "Acquired " + str(amount) + " " + displayingScene.theScene[lineOfScene] + "!"
            "[display!i]"
        else:
            $ amount *= -1
            $ It = 0
            while It < amount:
                $ player.inventory.useItem(displayingScene.theScene[lineOfScene])
                $ It += 1

            $ display = "Lost " + str(amount) + " " + displayingScene.theScene[lineOfScene] + "!"
            "[display!i]"
    elif displayingScene.theScene[lineOfScene] == "GiveItemQuietly":
        $ lineOfScene += 1
        $ amount = int(displayingScene.theScene[lineOfScene])
        $ lineOfScene += 1

        if amount > 0:
            $ player.inventory.give(displayingScene.theScene[lineOfScene], amount)
        else:
            $ amount *= -1
            $ It = 0
            while It < amount:
                $ player.inventory.useItem(displayingScene.theScene[lineOfScene])
                $ It += 1

    elif displayingScene.theScene[lineOfScene] == "GiveSkill":
        $ lineOfScene += 1
        $ check = 1
        python:
            for each in player.skillList:
                if each.name == displayingScene.theScene[lineOfScene]:
                    check = 0
        if check == 1:
            $ fetchSkill = getFromName(displayingScene.theScene[lineOfScene], SkillsDatabase)
            $ player.learnSkill(SkillsDatabase[fetchSkill])
            $ display = "Learned " + SkillsDatabase[fetchSkill].name + "!"
            "[display!i]"
    elif displayingScene.theScene[lineOfScene] == "GiveSkillQuietly":
        $ lineOfScene += 1
        $ check = 1
        python:
            for each in player.skillList:
                if each.name == displayingScene.theScene[lineOfScene]:
                    check = 0
        if check == 1:
            $ fetchSkill = getFromName(displayingScene.theScene[lineOfScene], SkillsDatabase)
            $ player.learnSkill(SkillsDatabase[fetchSkill])
    elif displayingScene.theScene[lineOfScene] == "GivePerkPoint":
        $ player.perkPoints += 1
        #CODEMOD
        $ player.additionalPerkPoints += 1

    elif displayingScene.theScene[lineOfScene] == "GivePerk":
        $ lineOfScene += 1
        $ check = 1
        python:
            for each in player.perks:
                if each.name == displayingScene.theScene[lineOfScene]:
                    check = 0
        if check == 1:
            $ player.giveOrTakePerk(displayingScene.theScene[lineOfScene], 1)
            $ display = "Got the " + displayingScene.theScene[lineOfScene] + " perk!"
            "[display!i]"
    elif displayingScene.theScene[lineOfScene] == "GivePerkQuietly":
        $ lineOfScene += 1
        $ check = 1
        python:
            for each in player.perks:
                if each.name == displayingScene.theScene[lineOfScene]:
                    check = 0
        if check == 1:
            $ player.giveOrTakePerk(displayingScene.theScene[lineOfScene], 1)
    elif displayingScene.theScene[lineOfScene] == "GiveSkillToMonster":
        $ lineOfScene += 1
        $ fetchSkill = getFromName(displayingScene.theScene[lineOfScene], SkillsDatabase)
        $ monsterEncounter[CombatFunctionEnemytarget].skillList.append(SkillsDatabase[fetchSkill])
    elif displayingScene.theScene[lineOfScene] == "GivePerkToMonster":
        $ lineOfScene += 1
        $ monsterEncounter[CombatFunctionEnemytarget].giveOrTakePerk(displayingScene.theScene[lineOfScene], 1)

    elif displayingScene.theScene[lineOfScene] == "GiveSkillThatWasTemporarilyRemoved":
        $ lineOfScene += 1
        $ check = 1
        python:
            for each in player.skillList:
                if each.name == displayingScene.theScene[lineOfScene]:
                    check = 0
        if check == 1:
            python:
                foundS = 0
                fetchSkill = 0
                for each in removedSkill:
                    if each == displayingScene.theScene[lineOfScene] or foundS == 1:
                        foundS = 1
                    else:
                        fetchSkill += 1
            if foundS != 0:
                $ player.skillList.insert(removedSkillPosition[fetchSkill], SkillsDatabase[getFromName(removedSkill[fetchSkill], SkillsDatabase)])
                $ del removedSkillPosition[fetchSkill]
                $ del removedSkill[fetchSkill]
    else:
        $ noSpecificFuntion = 1

    if noSpecificFuntion != 1:
        $ noSpecificFuntion = 2

    return

label dialogueRemoveCategory: #playX or even Player functions!
    $ noSpecificFuntion = 2

    if displayingScene.theScene[lineOfScene] == "RemoveStatusEffect":
        $ lineOfScene += 1
        $ player = removeThisStatusEffect(displayingScene.theScene[lineOfScene], player)
    elif displayingScene.theScene[lineOfScene] == "RemovePerk":
        $ lineOfScene += 1
        $ check = 0
        python:
            for each in player.perks:
                if each.name == displayingScene.theScene[lineOfScene]:
                    check = 1
        if check == 1:
            $ player.giveOrTakePerk(displayingScene.theScene[lineOfScene], -1)
            $ display = "Lost the " + displayingScene.theScene[lineOfScene] + " perk!"
            "[display!i]"
    elif displayingScene.theScene[lineOfScene] == "RemovePerkQuietly":
        $ lineOfScene += 1
        $ check = 0
        python:
            for each in player.perks:
                if each.name == displayingScene.theScene[lineOfScene]:
                    check = 1
        if check == 1:
            $ player.giveOrTakePerk(displayingScene.theScene[lineOfScene], -1)
    elif displayingScene.theScene[lineOfScene] == "RemoveInputFromPlayerEros":
        $ DataLocation = getFromName(ProgressEvent[DataLocation].name, ProgressEvent)
        $ player.inventory.money -= int(math.floor(debt))

    elif displayingScene.theScene[lineOfScene] == "RemoveInputFromProgress":
        $ DataLocation = getFromName(ProgressEvent[DataLocation].name, ProgressEvent)
        $ ProgressEvent[DataLocation].eventProgress -= int(math.floor(debt))

    elif displayingScene.theScene[lineOfScene] == "RemoveProgressFromEros":
        $ DataLocation = getFromName(ProgressEvent[DataLocation].name, ProgressEvent)
        $ player.inventory.money -= int(math.floor(ProgressEvent[DataLocation].eventProgress))
    elif displayingScene.theScene[lineOfScene] == "RemoveSkillFromPlayer":
        $ lineOfScene += 1
        $ fetchSkill = getFromName(displayingScene.theScene[lineOfScene], player.skillList)
        if fetchSkill != -1:
            $ display = "Forgot how to use " + player.skillList[fetchSkill].name + "!"
            $ del player.skillList[fetchSkill]
            "[display!i]"
    elif displayingScene.theScene[lineOfScene] == "RemoveSkillFromPlayerQuietly":
        $ lineOfScene += 1
        $ fetchSkill = getFromName(displayingScene.theScene[lineOfScene], player.skillList)
        if fetchSkill != -1:
            $ del player.skillList[fetchSkill]

    elif displayingScene.theScene[lineOfScene] == "RemoveSkillFromPlayerTemporarily":
        $ lineOfScene += 1
        $ fetchSkill = getFromName(displayingScene.theScene[lineOfScene], player.skillList)
        if fetchSkill != -1:
            $ removedSkillPosition.append(fetchSkill)
            $ removedSkill.append(displayingScene.theScene[lineOfScene])
            $ del player.skillList[fetchSkill]
    elif displayingScene.theScene[lineOfScene] == "RemoveGridNPC":
        if TheGrid != []:
            $ lineOfScene += 1
            if displayingScene.theScene[lineOfScene] == "Current":
                $ del ActiveGridNPCs[currentGridNPC]
                $ gridMapDethAdjuster += 1
            elif displayingScene.theScene[lineOfScene] == "Specific":
                $ lineOfScene += 1
                $ passcheck = 0
                $ currentGridNPC = 0
                $ v = 0
                python:
                    for each in ActiveGridNPCs:
                        if each.name == displayingScene.theScene[lineOfScene]:
                            currentGridNPC = copy.deepcopy(v)
                            passcheck = 1
                        v += 1
                if passcheck == 1:
                    $ del ActiveGridNPCs[currentGridNPC]
                    $ gridMapDethAdjuster += 1

            $ currentGridNPC -= 1
        else:
            $ lineOfScene += 1
    elif displayingScene.theScene[lineOfScene] == "RemoveSkillFromMonster":
        $ lineOfScene += 1
        $ fetchSkill = getFromName(displayingScene.theScene[lineOfScene], monsterEncounter[CombatFunctionEnemytarget].skillList)
        if fetchSkill != -1:
            $ del monsterEncounter[CombatFunctionEnemytarget].skillList[fetchSkill]
    elif displayingScene.theScene[lineOfScene] == "RemoveMonster":
        python:
            if monsterEncounter[CombatFunctionEnemytarget].combatStance[0].Stance != "None":
                for monStance in monsterEncounter[CombatFunctionEnemytarget].combatStance:
                    player.removeStanceByName(monStance.Stance)

        if monsterEncounter[CombatFunctionEnemytarget].restraintOnLoss[0] != "":
            $ restrainholdyLine = copy.deepcopy(lineOfScene)
            $ restrainholdyScene = copy.deepcopy(displayingScene)
            $ restrainholdyData = copy.deepcopy(DataLocation)
            $ display = monsterEncounter[CombatFunctionEnemytarget].restraintOnLoss[renpy.random.randint(-1, len(monsterEncounter[CombatFunctionEnemytarget].restraintOnLoss)-1)]
            call read from _call_read_40
            $ lineOfScene = copy.deepcopy(restrainholdyLine)
            $ displayingScene = copy.deepcopy(restrainholdyScene)
            $ DataLocation = copy.deepcopy(restrainholdyData)

        python:
            del monsterEncounter[CombatFunctionEnemytarget]
            del trueMonsterEncounter[CombatFunctionEnemytarget]
            del monInititive[CombatFunctionEnemytarget]
            if len(monSkillChoice) > 0 and len(monSkillChoice) > CombatFunctionEnemytarget:
                del monSkillChoice[CombatFunctionEnemytarget]
    elif displayingScene.theScene[lineOfScene] == "RemoveStatusEffectFromMonster":
        $ lineOfScene += 1
        $ monsterEncounter[CombatFunctionEnemytarget] = removeThisStatusEffect(displayingScene.theScene[lineOfScene], monsterEncounter[CombatFunctionEnemytarget])
    elif displayingScene.theScene[lineOfScene] == "RemovePerkFromMonster":
        $ lineOfScene += 1
        $ monsterEncounter[CombatFunctionEnemytarget].giveOrTakePerk(displayingScene.theScene[lineOfScene], -1)
    else:
        $ noSpecificFuntion = 1

    if noSpecificFuntion != 1:
        $ noSpecificFuntion = 2

    return
