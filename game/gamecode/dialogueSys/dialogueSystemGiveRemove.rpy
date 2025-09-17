
# Give funcs
label JsonFuncGiveTreasure:
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
    return
label JsonFuncGiveExp:
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
    return
label JsonFuncGiveItem:
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
    return
label JsonFuncGiveItemQuietly:
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
    return
label JsonFuncGiveSkill:
    $ lineOfScene += 1
    $ check = 1
    python:
        skill_name = displayingScene.theScene[lineOfScene]
        check = int(not any(skill.name == skill_name for skill in player.skillList))
    if check == 1:
        $ fetchSkill = getFromName(displayingScene.theScene[lineOfScene], SkillsDatabase)
        $ player.learnSkill(SkillsDatabase[fetchSkill])
        $ display = "Learned " + SkillsDatabase[fetchSkill].name + "!"
        "[display!i]"
    return
label JsonFuncGiveSkillQuietly:
    $ lineOfScene += 1
    $ check = 1
    python:
        skill_name = displayingScene.theScene[lineOfScene]
        check = int(not any(skill.name == skill_name for skill in player.skillList))
    if check == 1:
        $ fetchSkill = getFromName(displayingScene.theScene[lineOfScene], SkillsDatabase)
        $ player.learnSkill(SkillsDatabase[fetchSkill])
    return
label JsonFuncGivePerkPoint:
    $ player.perkPoints += 1
    #CODEMOD
    $ player.additionalPerkPoints += 1
    return
label JsonFuncGivePerk:
    $ lineOfScene += 1
    $ check = 1
    python:
        perk_name = displayingScene.theScene[lineOfScene]
        check = int(not any(perk.name == perk_name for perk in player.perks))
    if check == 1:
        $ player.giveOrTakePerk(displayingScene.theScene[lineOfScene], 1)
        $ display = "Got the " + displayingScene.theScene[lineOfScene] + " perk!"
        "[display!i]"
    return
label JsonFuncGivePerkQuietly:
    $ lineOfScene += 1
    $ check = 1
    python:
        perk_name = displayingScene.theScene[lineOfScene]
        check = int(not any(perk.name == perk_name for perk in player.perks))
    if check == 1:
        $ player.giveOrTakePerk(displayingScene.theScene[lineOfScene], 1)
    return
label JsonFuncGiveSkillToMonster:
    $ lineOfScene += 1
    $ fetchSkill = getFromName(displayingScene.theScene[lineOfScene], SkillsDatabase)
    $ monsterEncounter[CombatFunctionEnemytarget].skillList.append(SkillsDatabase[fetchSkill])
    return
label JsonFuncGivePerkToMonster:
    $ lineOfScene += 1
    $ monsterEncounter[CombatFunctionEnemytarget].giveOrTakePerk(displayingScene.theScene[lineOfScene], 1)
    return
label JsonFuncGiveSkillThatWasTemporarilyRemoved:
    $ lineOfScene += 1
    $ check = 1
    python:
        skill_name = displayingScene.theScene[lineOfScene]
        check = int(not any(skill.name == skill_name for skill in player.skillList))
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
    return

# Remove funcs
label JsonFuncRemoveStatusEffect:
    $ lineOfScene += 1
    $ player = removeThisStatusEffect(displayingScene.theScene[lineOfScene], player)
    return
label JsonFuncRemovePerk:
    $ lineOfScene += 1
    $ check = 0
    python:
        perk_name = displayingScene.theScene[lineOfScene]
        check = int(any(perk.name == perk_name for perk in player.perks))
    if check == 1:
        $ player.giveOrTakePerk(displayingScene.theScene[lineOfScene], -1)
        $ display = "Lost the " + displayingScene.theScene[lineOfScene] + " perk!"
        "[display!i]"
    return
label JsonFuncRemovePerkQuietly:
    $ lineOfScene += 1
    $ check = 0
    python:
        perk_name = displayingScene.theScene[lineOfScene]
        check = int(any(perk.name == perk_name for perk in player.perks))
    if check == 1:
        $ player.giveOrTakePerk(displayingScene.theScene[lineOfScene], -1)
    return
label JsonFuncRemoveInputFromPlayerEros:
    $ DataLocation = getFromName(ProgressEvent[DataLocation].name, ProgressEvent)
    $ player.inventory.money -= int(math.floor(debt))
    return
label JsonFuncRemoveInputFromProgress:
    $ DataLocation = getFromName(ProgressEvent[DataLocation].name, ProgressEvent)
    $ ProgressEvent[DataLocation].eventProgress -= int(math.floor(debt))
    return
label JsonFuncRemoveProgressFromEros:
    $ DataLocation = getFromName(ProgressEvent[DataLocation].name, ProgressEvent)
    $ player.inventory.money -= int(math.floor(ProgressEvent[DataLocation].eventProgress))
    return
label JsonFuncRemoveSkillFromPlayer:
    $ lineOfScene += 1
    $ fetchSkill = getFromName(displayingScene.theScene[lineOfScene], player.skillList)
    if fetchSkill != -1:
        $ display = "Forgot how to use " + player.skillList[fetchSkill].name + "!"
        $ del player.skillList[fetchSkill]
        "[display!i]"
    return
label JsonFuncRemoveSkillFromPlayerQuietly:
    $ lineOfScene += 1
    $ fetchSkill = getFromName(displayingScene.theScene[lineOfScene], player.skillList)
    if fetchSkill != -1:
        $ del player.skillList[fetchSkill]
    return
label JsonFuncRemoveSkillFromPlayerTemporarily:
    $ lineOfScene += 1
    $ fetchSkill = getFromName(displayingScene.theScene[lineOfScene], player.skillList)
    if fetchSkill != -1:
        $ removedSkillPosition.append(fetchSkill)
        $ removedSkill.append(displayingScene.theScene[lineOfScene])
        $ del player.skillList[fetchSkill]
    return
label JsonFuncRemoveGridNPC:
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
    return
label JsonFuncRemoveSkillFromMonster:
    $ lineOfScene += 1
    $ fetchSkill = getFromName(displayingScene.theScene[lineOfScene], monsterEncounter[CombatFunctionEnemytarget].skillList)
    if fetchSkill != -1:
        $ del monsterEncounter[CombatFunctionEnemytarget].skillList[fetchSkill]
    return
label JsonFuncRemoveMonster:
    python:
        if monsterEncounter[CombatFunctionEnemytarget].combatStance[0].Stance != "None":
            for monStance in monsterEncounter[CombatFunctionEnemytarget].combatStance:
                player.removeStanceByName(monStance.Stance)

    if monsterEncounter[CombatFunctionEnemytarget].restraintOnLoss[0] != "":
        $ restrainholdyLine = copy.copy(lineOfScene)
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
    return
label JsonFuncRemoveStatusEffectFromMonster:
    $ lineOfScene += 1
    $ monsterEncounter[CombatFunctionEnemytarget] = removeThisStatusEffect(displayingScene.theScene[lineOfScene], monsterEncounter[CombatFunctionEnemytarget])
    return
label JsonFuncRemovePerkFromMonster:
    $ lineOfScene += 1
    $ monsterEncounter[CombatFunctionEnemytarget].giveOrTakePerk(displayingScene.theScene[lineOfScene], -1)
    return
