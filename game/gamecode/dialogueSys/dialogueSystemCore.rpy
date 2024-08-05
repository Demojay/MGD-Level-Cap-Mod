init python:
    def getSpeaker(speakerNumber, EventDatabase, MonsterDatabase):
        while len(actorNames) <= speakerNumber:
            actorNames.append("")

        characterDataLocation = getFromName(EventDatabase[DataLocation].Speakers[speakerNumber].name, MonsterDatabase)
        actorNames[speakerNumber] = MonsterDatabase[characterDataLocation].name + EventDatabase[DataLocation].Speakers[speakerNumber].postName

        if EventDatabase[DataLocation].Speakers[speakerNumber].SpeakerType == "?":
            actorNames[speakerNumber] = EventDatabase[DataLocation].Speakers[speakerNumber].name

        return Character(_(actorNames[speakerNumber] +attackTitle), what_prefix='"', what_suffix='"')

    def SceneRequiresCheck():
        global displayingScene, lineOfScene, ProgressEvent, display, DataLocation, finalOption, eventMenuJumps, finalOptionEvent, finalOptionEventScene, ShuffleMenuOptions

        whatStatisIt = ""
        whatItemIsIt = ""
        whatSkillIsIt = ""
        whatPerkIsIt = ""
        statToCheck = 0
        needsStat = 0
        eAmount = ""
        vAmount = ""
        hasVirilityCheck = 0
        hasEnergyCheck = 0
        hasStatCheck = 0
        #CODEMOD
        hasCapCheck = 0

        passcheck = 0

        passStatcheck = 1

        passItemCheck = 0
        passItemChecks = 0
        passEquipmentCheck = 0
        passEquipmentChecks = 0
        passSkillCheck = 0
        passSkillChecks = 0
        passPerkCheck = 0
        passPerkChecks = 0
        passEnergyCheck = 1
        passVirilityCheck = 1
        #CODEMOD
        passCapCheck = 1
        passLocalProgressCheck = 0
        passLocalProgressChecks = 0
        passFetCheck = 0
        passFetChecks = 0
        passProgressCheck = 0
        passProgressChecks = 0
        passLocalChoiceCheck = 0
        passLocalChoiceChecks = 0
        passTimeCheck = 0
        passTimeChecks = 0
        passChoiceCheck = 0
        passChoiceChecks = 0
        hideFailedMenuChoice = 0
        isFinalOption = 0
        inverseRequirement = 0
        failedItemChecked = 0
        failedEquipmentChecked = 0
        failedSkillChecked = 0
        failedPerkChecked = 0
        Overriding = 0
        global override

        checkPreFuncs = 0
        while checkPreFuncs == 0:
            if displayingScene.theScene[lineOfScene] == "HideOptionOnRequirementFail" and hideFailedMenuChoice == 0:
                hideFailedMenuChoice = 1
                lineOfScene += 1
            elif displayingScene.theScene[lineOfScene] == "InverseRequirement":
                inverseRequirement = 1
                lineOfScene += 1
            elif displayingScene.theScene[lineOfScene] == "ShuffleMenu":
                ShuffleMenuOptions = 1
                lineOfScene += 1
            elif displayingScene.theScene[lineOfScene] == "OverrideOption":
                Overriding = 1
                lineOfScene += 1
            elif displayingScene.theScene[lineOfScene] == "FinalOption":
                #REMEMBER U NEED TO CALL THIS LAST OUT OF THE FUNCTIONS
                lineOfScene += 1
                finalOption = copy.deepcopy(displayingScene.theScene[lineOfScene])
                #lineOfScene += 1

                isFinalOption = 1
                finalOptionEvent = copy.deepcopy(eventMenuJumps[-1])
                finalOptionEventScene = copy.deepcopy(eventMenuSceneJumps[-1])
            elif displayingScene.theScene[lineOfScene] == "EventJump":
                lineOfScene += 1
                eventMenuJumps[-1] = copy.deepcopy(displayingScene.theScene[lineOfScene])
                lineOfScene += 1
                if isFinalOption == 1:
                    finalOptionEvent = copy.deepcopy(eventMenuJumps[-1])

                if displayingScene.theScene[lineOfScene] ==  "ThenJumpToScene":
                    lineOfScene += 1
                    eventMenuSceneJumps[-1] = copy.deepcopy(displayingScene.theScene[lineOfScene])
                    lineOfScene += 1
                    if isFinalOption == 1:
                        finalOptionEventScene = copy.deepcopy(eventMenuSceneJumps[-1])


            elif displayingScene.theScene[lineOfScene] == "RequiresMinimumProgress":
                passLocalProgressChecks += 1
                lineOfScene += 1
                DataLocation = getFromName(ProgressEvent[DataLocation].name, ProgressEvent)
                if int(displayingScene.theScene[lineOfScene]) <= ProgressEvent[DataLocation].eventProgress:
                    passLocalProgressCheck += 1

                lineOfScene += 1
            elif displayingScene.theScene[lineOfScene] == "RequiresMinimumProgressFromEvent":
                passProgressChecks += 1
                lineOfScene += 1
                CheckEvent = getFromName(displayingScene.theScene[lineOfScene], ProgressEvent)
                lineOfScene += 1
                if int(displayingScene.theScene[lineOfScene]) <= ProgressEvent[CheckEvent].eventProgress:
                    passProgressCheck += 1

                lineOfScene += 1

            elif displayingScene.theScene[lineOfScene] == "RequiresLessProgress":
                passLocalProgressChecks += 1
                lineOfScene += 1
                DataLocation = getFromName(ProgressEvent[DataLocation].name, ProgressEvent)
                if int(displayingScene.theScene[lineOfScene]) > ProgressEvent[DataLocation].eventProgress:
                    passLocalProgressCheck += 1

                lineOfScene += 1
            elif displayingScene.theScene[lineOfScene] == "RequiresLessProgressFromEvent":
                passProgressChecks += 1
                lineOfScene += 1
                CheckEvent = getFromName(displayingScene.theScene[lineOfScene], ProgressEvent)
                lineOfScene += 1
                if int(displayingScene.theScene[lineOfScene]) > ProgressEvent[CheckEvent].eventProgress:
                    passProgressCheck += 1

                lineOfScene += 1

            elif displayingScene.theScene[lineOfScene] == "RequiresChoice":
                passLocalChoiceChecks += 1
                lineOfScene += 1
                choiceToCheck = int(displayingScene.theScene[lineOfScene])
                lineOfScene += 1
                DataLocation = getFromName(ProgressEvent[DataLocation].name, ProgressEvent)

                while choiceToCheck-1 >= len(ProgressEvent[DataLocation].choices):
                    ProgressEvent[DataLocation].choices.append("")

                if displayingScene.theScene[lineOfScene] == ProgressEvent[DataLocation].choices[choiceToCheck-1]:
                    passLocalChoiceCheck += 1
                lineOfScene += 1

            elif displayingScene.theScene[lineOfScene] == "RequiresChoiceFromEvent":
                passChoiceChecks += 1
                lineOfScene += 1
                CheckEvent = getFromName(displayingScene.theScene[lineOfScene], ProgressEvent)
                lineOfScene += 1
                choiceToCheck = int(displayingScene.theScene[lineOfScene])

                while choiceToCheck-1 >= len(ProgressEvent[CheckEvent].choices):
                    ProgressEvent[CheckEvent].choices.append("")

                lineOfScene += 1
                if displayingScene.theScene[lineOfScene] == ProgressEvent[CheckEvent].choices[choiceToCheck-1]:
                    passChoiceCheck += 1
                lineOfScene += 1

            elif displayingScene.theScene[lineOfScene] == "RequiresTime":
                passTimeChecks += 1
                lineOfScene += 1
                if IfTime(displayingScene.theScene[lineOfScene]) == 1:
                    passTimeCheck += 1
                lineOfScene += 1

            elif displayingScene.theScene[lineOfScene] == "RequiresStat":
                passStatcheck = 0
                lineOfScene += 1
                whatStatisIt = displayingScene.theScene[lineOfScene]
                statToCheck = player.stats.getStat(displayingScene.theScene[lineOfScene])
                lineOfScene += 1
                needsStat = int(displayingScene.theScene[lineOfScene])
                if needsStat <= statToCheck:
                    passStatcheck = 1
                lineOfScene += 1

            elif displayingScene.theScene[lineOfScene] == "RequiresFetishLevelEqualOrGreater":
                passFetCheck += 1
                lineOfScene += 1
                fetchFetish = displayingScene.theScene[lineOfScene]
                lineOfScene += 1
                fetishLvl = int(displayingScene.theScene[lineOfScene])

                if player.getFetish(fetchFetish) >= fetishLvl:
                    passFetChecks += 1

                lineOfScene += 1
            elif displayingScene.theScene[lineOfScene] == "RequiresFetishLevelEqualOrLess":
                passFetCheck += 1
                lineOfScene += 1
                fetchFetish = displayingScene.theScene[lineOfScene]
                lineOfScene += 1
                fetishLvl = int(displayingScene.theScene[lineOfScene])

                if player.getFetish(fetchFetish) <= fetishLvl:
                    passFetChecks += 1

                lineOfScene += 1

            elif displayingScene.theScene[lineOfScene] == "RequiresItem":
                passItemCheck += 1
                lineOfScene += 1

                if player.inventory.RuneSlotOne.name == displayingScene.theScene[lineOfScene]:
                    passItemChecks += 1
                elif player.inventory.RuneSlotTwo.name == displayingScene.theScene[lineOfScene]:
                    passItemChecks += 1
                elif player.inventory.RuneSlotThree.name == displayingScene.theScene[lineOfScene]:
                    passItemChecks += 1
                elif player.inventory.AccessorySlot.name == displayingScene.theScene[lineOfScene]:
                    passItemChecks += 1
                else:
                    for each in player.inventory.items:
                        if each.name == displayingScene.theScene[lineOfScene]:
                            passItemChecks += 1
                if passItemCheck != passItemChecks and failedItemChecked == 0:
                    failedItemChecked = 1
                    whatItemIsIt = displayingScene.theScene[lineOfScene]
                elif inverseRequirement == 1:
                    whatItemIsIt = displayingScene.theScene[lineOfScene]
                lineOfScene += 1
            elif displayingScene.theScene[lineOfScene] == "RequiresItemEquipped":
                passEquipmentCheck += 1
                lineOfScene += 1

                if player.inventory.RuneSlotOne.name == displayingScene.theScene[lineOfScene]:
                    passEquipmentChecks += 1
                elif player.inventory.RuneSlotTwo.name == displayingScene.theScene[lineOfScene]:
                    passEquipmentChecks += 1
                elif player.inventory.RuneSlotThree.name == displayingScene.theScene[lineOfScene]:
                    passEquipmentChecks += 1
                elif player.inventory.AccessorySlot.name == displayingScene.theScene[lineOfScene]:
                    passEquipmentChecks += 1
                if passEquipmentCheck != passEquipmentChecks and failedEquipmentChecked == 0:
                    failedEquipmentChecked = 1
                    whatEquipmentIsIt = displayingScene.theScene[lineOfScene]
                elif inverseRequirement == 1:
                    whatEquipmentIsIt = displayingScene.theScene[lineOfScene]
                lineOfScene += 1

            elif displayingScene.theScene[lineOfScene] == "RequiresSkill":
                passSkillCheck += 1
                lineOfScene += 1

                for each in player.skillList:
                    if each.name == displayingScene.theScene[lineOfScene]:
                        passSkillChecks += 1
                if passSkillCheck != passSkillChecks and failedSkillChecked == 0:
                    failedSkillChecked = 1
                    whatSkillIsIt = displayingScene.theScene[lineOfScene]
                elif inverseRequirement == 1:
                    whatSkillIsIt = displayingScene.theScene[lineOfScene]

                lineOfScene += 1
            elif displayingScene.theScene[lineOfScene] == "RequiresPerk":
                passPerkCheck += 1
                lineOfScene += 1

                for each in player.perks:
                    if each.name == displayingScene.theScene[lineOfScene]:
                        passPerkChecks += 1
                if passPerkCheck != passPerkChecks and failedPerkChecked == 0:
                    failedPerkChecked = 1
                    whatPerkIsIt = displayingScene.theScene[lineOfScene]
                elif inverseRequirement == 1:
                    whatPerkIsIt = displayingScene.theScene[lineOfScene]
                lineOfScene += 1
            elif displayingScene.theScene[lineOfScene] == "RequiresEnergy":
                passEnergyCheck = 0
                hasEnergyCheck = 1
                lineOfScene += 1
                eAmount = displayingScene.theScene[lineOfScene]

                if player.stats.ep >= int(eAmount):
                    passEnergyCheck = 1

                lineOfScene += 1
            elif displayingScene.theScene[lineOfScene] == "RequiresVirility":
                passVirilityCheck = 0
                hasVirilityCheck = 1
                lineOfScene += 1
                vAmount = displayingScene.theScene[lineOfScene]

                if getVirility(player) >= int(vAmount):
                    passVirilityCheck = 1

                lineOfScene += 1
            #CODEMOD
            elif displayingScene.theScene[lineOfScene] == "RequiresLevelCapPassed":
                passCapCheck = 0
                hasCapCheck = 1 

                if levelCapEnabled() and player.stats.lvl > getMaxLevelCap():
                    passCapCheck = 1

                lineOfScene += 1
            else:
                if Overriding == 1:
                    override = copy.deepcopy(displayingScene.theScene[lineOfScene])
                checkPreFuncs += 1


        if inverseRequirement == 0:
            if passStatcheck == 1 and passFetCheck == passFetChecks and passItemCheck == passItemChecks and passEquipmentCheck == passEquipmentChecks and passSkillCheck == passSkillChecks and passPerkCheck == passPerkChecks and passEnergyCheck == 1 and passVirilityCheck == 1 and passProgressCheck == passProgressChecks and passLocalProgressCheck == passLocalProgressChecks and passLocalChoiceCheck == passLocalChoiceChecks and passChoiceCheck == passChoiceChecks and passTimeCheck == passTimeChecks and passCapCheck == 1:
                passcheck = 1
            else:
                if hideFailedMenuChoice == 0:
                    if passLocalChoiceCheck == passLocalChoiceChecks and passProgressCheck == passProgressChecks and passLocalProgressCheck == passLocalProgressChecks and passChoiceCheck == passChoiceChecks:
                        if passStatcheck == 0:
                            display = "Requires " + str(needsStat) + " " + whatStatisIt + "."
                        elif passItemCheck != passItemChecks:
                            display = "Requires a " + whatItemIsIt + " in your inventory."
                        elif passEquipmentCheck != passEquipmentChecks:
                            display = "Must not have " + whatEquipmentIsIt + " equipped."
                        elif passSkillCheck != passSkillChecks and failedSkillChecked == 1:
                            display = "Requires you to know the " + whatSkillIsIt + " skill."
                        elif passPerkCheck != passPerkChecks:
                            display = "Requires you to have the " + whatPerkIsIt + " perk."
                        elif passEnergyCheck == 0:
                            display = "Requires " + eAmount + " energy."
                        elif passVirilityCheck == 0:
                            display = "Requires " + vAmount + " virility."
                        #CODEMOD
                        elif passCapCheck == 0:
                            display = "Requires you to have passed the level cap."
        elif inverseRequirement == 1:
            if passStatcheck == 1 and passFetCheck == passFetChecks and passItemCheck == passItemChecks and passEquipmentCheck == passEquipmentChecks and passSkillCheck == passSkillChecks and passPerkCheck == passPerkChecks and passEnergyCheck == 1 and passVirilityCheck == 1 and passProgressCheck == passProgressChecks and passLocalProgressCheck == passLocalProgressChecks and passLocalChoiceCheck == passLocalChoiceChecks and passChoiceCheck == passChoiceChecks and passTimeCheck == passTimeChecks:
                if hideFailedMenuChoice == 0:
                    if passLocalChoiceCheck == passLocalChoiceChecks and passProgressCheck == passProgressChecks and passLocalProgressCheck == passLocalProgressChecks and passChoiceCheck == passChoiceChecks:
                        if passVirilityCheck == 1 and hasVirilityCheck == 1:
                            display = "Must have less than " + vAmount + " virility."
                        if passEnergyCheck == 1 and hasEnergyCheck == 1:
                            display = "Must have less than " + eAmount + " energy."
                        if passPerkCheck == passPerkChecks and passPerkCheck == 1:
                            display = "Must not have the " + whatPerkIsIt + " perk."
                        if passSkillCheck == passSkillChecks and passSkillCheck == 1:
                            display = "Must not know the " + whatSkillIsIt + " skill."
                        if passItemCheck == passItemChecks and passItemCheck == 1:
                            display = "Must not have " + whatItemIsIt + " in your inventory."
                        if passEquipmentCheck == passEquipmentChecks and passEquipmentCheck == 1:
                            display = "Must not have " + whatEquipmentIsIt + " equipped."
                        if passStatcheck == 1 and hasStatCheck == 1:
                            display = "Must have less than " + str(needsStat) + " " + whatStatisIt + "."
                        #CODEMOD
                        if passCapCheck == 1 and hasCapCheck == 1:
                            display = "Must not have passed the level cap."

            else:
                passcheck = 1
        return passcheck

label displayScene:
    if SceneBookMarkRead == 1:

        $ displayingScene = copy.deepcopy(HoldingScene)
        $ lineOfScene = copy.deepcopy(HoldingLine)
        $ DataLocation = copy.deepcopy(HoldingDataLoc)
        $ HoldingDataLoc = -1
        $ HoldingLine =-1
        $ HoldingScene = LossScene()
        $ SceneBookMarkRead = 2
    else:
        $ lineOfScene = 0

label resumeSceneAfterCombat:

    $ showOnSide = 0
    $ showSpeakers = 1
    $ display1 = ""
    $ display2 = ""
    $ display3 = ""
    $ display4 = ""
    $ display5 = ""
    $ display6 = ""

    if len(actorNames) < 12:
        $ actorNames.append("")
        $ actorNames.append("")
        $ actorNames.append("")
        $ actorNames.append("")
        $ actorNames.append("")
        $ actorNames.append("")
        $ actorNames.append("")
        $ actorNames.append("")
        $ actorNames.append("")
        $ actorNames.append("")


    python:
        try:
            displayingScene.theScene
        except:
            displayingScene = Dialogue()

    while lineOfScene < len(displayingScene.theScene):
        $ readLine = 0
        $ notFunction = 0
        $ noDFunction = 0
        $ noCombatFunction = 0
        $ dialogueLineForSure = 0
        $ noSpecificFuntion = 0

        #if DialogueIsFrom == "Event" or DialogueIsFrom == "Monster":
        #    if displayHealthInEvent == 1:
        #        show screen ON_HealthDisplayBacking
        #        show screen ON_HealthDisplay
        #    else:
        #        hide screen ON_HealthDisplayBacking
        #        hide screen ON_HealthDisplay
        #$ showTheLine = displayingScene.theScene[lineOfScene]
        #"[showTheLine]"
        if showSpeakers == 1:
            show screen ON_CharacterDialogueScreen onlayer master
            if len(monsterEncounter) > 0:
                show screen ON_EnemyCardScreen onlayer master
        else:
            hide screen ON_CharacterDialogueScreen


        $ lengthOfInitalLine = 0
        $ lengthOfInitalLine = len(displayingScene.theScene[lineOfScene])

        if lengthOfInitalLine > 80:
            $ dialogueLineForSure = 1


        if dialogueLineForSure == 0 and displayingScene.theScene[lineOfScene] != "":
            $ noSpecificFuntion = 0

            if lengthOfInitalLine >= 4:
                if noSpecificFuntion == 0: #If
                    if displayingScene.theScene[lineOfScene][0] == "I":
                        call dialogueICategory from _call_dialogueIfCategory

                if noSpecificFuntion == 0: #Go
                    if lineOfScene < len(displayingScene.theScene):
                        if displayingScene.theScene[lineOfScene][0] == "G":
                            if displayingScene.theScene[lineOfScene][1] == "o":
                                call dialogueGoCategory from _call_dialogueGoCategory
                            elif displayingScene.theScene[lineOfScene][1] == "i" and displayingScene.theScene[lineOfScene][2] == "v" and displayingScene.theScene[lineOfScene][3] == "e":
                                call dialogueGiveCategory from _call_dialogueGiveCategory
                            elif displayingScene.theScene[lineOfScene][1] == "e" and displayingScene.theScene[lineOfScene][2] == "t":
                                call dialogueGetCategory from _call_dialogueGetCategory

                if lineOfScene < len(displayingScene.theScene): #Get/Set
                    if noSpecificFuntion == 0:
                        if displayingScene.theScene[lineOfScene][0] == "S":
                            if displayingScene.theScene[lineOfScene][1] == "e" and displayingScene.theScene[lineOfScene][2] == "t":
                                call dialogueSetCategory from _call_dialogueSetCategory
                            else:
                                call dialogueSCategory from _call_dialogueSCategory

                if lineOfScene < len(displayingScene.theScene): #End
                    if noSpecificFuntion == 0:
                        if displayingScene.theScene[lineOfScene][0] == "E":
                            if displayingScene.theScene[lineOfScene][1] == "n" and displayingScene.theScene[lineOfScene][2] == "d":
                                call dialogueEndCategory from _call_dialogueEndCategory

                if lineOfScene < len(displayingScene.theScene): #Play
                    if noSpecificFuntion == 0:
                        if displayingScene.theScene[lineOfScene][0] == "P":
                            if displayingScene.theScene[lineOfScene][1] == "l" and displayingScene.theScene[lineOfScene][2] == "a" and displayingScene.theScene[lineOfScene][3] == "y":
                                call dialoguePlayCategory from _call_dialoguePlayCategory

            if lengthOfInitalLine >= 6:
                if lineOfScene < len(displayingScene.theScene):
                    if noSpecificFuntion == 0: #Clear
                        if displayingScene.theScene[lineOfScene][0] == "C":
                            if displayingScene.theScene[lineOfScene][1] == "l" and displayingScene.theScene[lineOfScene][2] == "e":
                                call dialogueClearCategory from _call_dialogueClearCategory
                            elif displayingScene.theScene[lineOfScene][1] == "h" and displayingScene.theScene[lineOfScene][2] == "a" and displayingScene.theScene[lineOfScene][3] == "n":
                                call dialogueChangeCategory from _call_dialogueChangeCategory

                if lineOfScene < len(displayingScene.theScene):
                    if noSpecificFuntion == 0: #Remove
                        if displayingScene.theScene[lineOfScene][0] == "R" and displayingScene.theScene[lineOfScene][1] == "e" and displayingScene.theScene[lineOfScene][2] == "m" and displayingScene.theScene[lineOfScene][3] == "o":
                            call dialogueRemoveCategory from _call_dialogueRemoveCategory


        #noSpecificFuntion == 1 means a specific thing has been checked, but it didnt find a function, so its then a text line
        #noSpecificFuntion == 2 means it found and did its function!!!


        if noSpecificFuntion == 0 and dialogueLineForSure == 0 and lineOfScene < len(displayingScene.theScene):
            if displayingScene.theScene[lineOfScene] == "FlexibleSpeaks":

                if len(monsterEncounter) >= 2:
                    $ Speaker = monsterEncounter[FlexibleSpeaker].name+attackTitle
                else:
                    $ Speaker = getSpeaker(FlexibleSpeaker, EventDatabase, MonsterDatabase)

                $ lineOfScene += 1
                $ readLine = 1

            elif displayingScene.theScene[lineOfScene] == "DisplayCharacters":
                $ showSpeakers = 1
                $ lineOfScene += 1
                $ SceneCharacters = []
                $ RoledCGOn = 0
                $ CgRoleKeeper = []
                if len(monsterEncounter) == 0:
                    $ hidingCombatEncounter = 0

                if hidingCombatEncounter == 0:
                    $ monsterEncounter = []
                    $ monsterEncounterCG = []
                    $ DefeatedEncounterMonsters = []
                    $ trueMonsterEncounter = []
                while displayingScene.theScene[lineOfScene] != "EndLoop":

                    python:
                        try:
                            targetChar = int(displayingScene.theScene[lineOfScene]) - 1
                        except:
                            targetChar = getFromName(displayingScene.theScene[lineOfScene], SceneCharacters)

                    $ characterDataLocation = getFromName(EventDatabase[DataLocation].Speakers[targetChar].name, MonsterDatabase)
                    if characterDataLocation != -1:
                        $ SceneCharacters.append(copy.deepcopy(MonsterDatabase[characterDataLocation]))
                    if EventDatabase[DataLocation].Speakers[targetChar].SpeakerType == "?":
                        $ SceneCharacters.append(copy.deepcopy(Monster(Stats(),0,  "?", "?")))

                    $ lineOfScene += 1
                python:
                    for each in SceneCharacters:
                        each = initiateImageLayers(each)

                        for SetData in persistantMonSetData:
                            if SetData.name == each.IDname:
                                each.currentSet = getFromName(SetData.startingSet, each.ImageSets)

                #if hidingCombatEncounter == 0:
                #    hide screen ON_HealthDisplayBacking
                #    hide screen ON_HealthDisplay
                show screen ON_CharacterDialogueScreen onlayer master
                #if hidingCombatEncounter == 0:
                #    if displayHealthInEvent == 1:
                #        hide screen ON_HealthDisplayBacking
                #        hide screen ON_HealthDisplay
                #    else:
                #        hide screen ON_HealthDisplayBacking
                #        hide screen ON_HealthDisplay


            elif displayingScene.theScene[lineOfScene] == "AnimateImageLayer":
                $ lineOfScene += 1
                $ settingToImage = displayingScene.theScene[lineOfScene]

                $ lineOfScene += 1
                $ layerToChange = displayingScene.theScene[lineOfScene]
                $ lineOfScene += 1

                python:
                    try:
                        settingCharcter = int(displayingScene.theScene[lineOfScene]) - 1

                    except:
                        ifIsInScene = 0
                        if len(monsterEncounter) > 0 and hidingCombatEncounter == 0:
                            searchingCharacters = monsterEncounter
                        else:
                            searchingCharacters = SceneCharacters
                        if len(searchingCharacters) > 0 and hidingCombatEncounter == 0:
                            #during combat layer change
                            if getFromName(displayingScene.theScene[lineOfScene], searchingCharacters)!= -1:
                                ifIsInScene = 1
                                settingCharcter = getFromName(displayingScene.theScene[lineOfScene], searchingCharacters)

                        if ifIsInScene == 0:
                            settingCharcter = CombatFunctionEnemytarget
                if settingToImage == "Animation":
                    $ animationList = []
                    $ animationChoice = ""
                    $ currentAnimationImg = 0
                elif settingToImage == "Animation2":
                    $ animationList2 = []
                    $ animationChoice2 = ""
                    $ currentAnimationImg2 = 0
                elif settingToImage == "Animation3":
                    $ animationList3 = []
                    $ animationChoice3 = ""
                    $ currentAnimationImg3 = 0

                $ lineOfScene += 1
                if settingToImage == "Animation":
                    $ animationSpeed = float(displayingScene.theScene[lineOfScene])
                    $ animationTime = float(displayingScene.theScene[lineOfScene])
                elif settingToImage == "Animation2":
                    $ animationSpeed2 = float(displayingScene.theScene[lineOfScene])
                    $ animationTime2 = float(displayingScene.theScene[lineOfScene])
                elif settingToImage == "Animation3":
                    $ animationSpeed3 = float(displayingScene.theScene[lineOfScene])
                    $ animationTime3 = float(displayingScene.theScene[lineOfScene])
                $ lineOfScene += 1

                if settingToImage == "Animation":
                    $ animationList = []
                elif settingToImage == "Animation2":
                    $ animationList2 = []
                elif settingToImage == "Animation3":
                    $ animationList3 = []
                if displayingScene.theScene[lineOfScene] != "EndLoop":
                    while displayingScene.theScene[lineOfScene] != "EndLoop":
                        if displayingScene.theScene[lineOfScene] != "EndLoop":
                            if settingToImage == "Animation":
                                $ animationList.append(displayingScene.theScene[lineOfScene])
                            elif settingToImage == "Animation2":
                                $ animationList2.append(displayingScene.theScene[lineOfScene])
                            elif settingToImage == "Animation3":
                                $ animationList3.append(displayingScene.theScene[lineOfScene])
                            $ lineOfScene += 1

                if settingToImage == "Animation":
                    if len(animationList) > 0:
                        $ animationChoice = animationList[0]
                elif settingToImage == "Animation2":
                    if len(animationList2) > 0:
                        $ animationChoice2 = animationList2[0]
                elif settingToImage == "Animation3":
                    if len(animationList3) > 0:
                        $ animationChoice3 = animationList3[0]

                $ searchingCharacters = AnimateImgLayer(searchingCharacters, settingCharcter, layerToChange, settingToImage)

            elif  displayingScene.theScene[lineOfScene] == "HideHealth":
                $ displayHealthInEvent = 0

            elif displayingScene.theScene[lineOfScene] == "HoldCurrentVirility":
                $ heldVirility = copy.deepcopy(getVirility(player))
            elif displayingScene.theScene[lineOfScene] == "HoldCurrentVirilityEnd":
                $ heldVirility = 0

            elif displayingScene.theScene[lineOfScene] == "EventsProgressEqualsOtherEventsProgress":
                $ lineOfScene += 1
                $ CheckEvent = getFromName(displayingScene.theScene[lineOfScene], ProgressEvent)
                $ lineOfScene += 1
                $ CheckEvent2 = getFromName(displayingScene.theScene[lineOfScene], ProgressEvent)

                if ProgressEvent[CheckEvent].eventProgress == ProgressEvent[CheckEvent2].eventProgress:
                    $ lineOfScene += 1
                    $ display = displayingScene.theScene[lineOfScene]
                    call sortMenuD from _call_sortMenuD_66
                    if len(monsterEncounter) > 0:
                        return
                else:
                    $ lineOfScene += 1
            elif displayingScene.theScene[lineOfScene] == "EventsProgressEqualsOrGreaterThanOtherEventsProgress":
                $ lineOfScene += 1
                $ CheckEvent = getFromName(displayingScene.theScene[lineOfScene], ProgressEvent)
                $ lineOfScene += 1
                $ CheckEvent2 = getFromName(displayingScene.theScene[lineOfScene], ProgressEvent)

                if ProgressEvent[CheckEvent].eventProgress >= ProgressEvent[CheckEvent2].eventProgress:
                    $ lineOfScene += 1
                    $ display = displayingScene.theScene[lineOfScene]
                    call sortMenuD from _call_sortMenuD_67
                    if len(monsterEncounter) > 0:
                        return
                else:
                    $ lineOfScene += 1

            elif displayingScene.theScene[lineOfScene] == "VirilityEqualsOrGreater":
                $ lineOfScene += 1

                if int(displayingScene.theScene[lineOfScene]) <= getVirility(player) :
                    $ lineOfScene += 1
                    $ display = displayingScene.theScene[lineOfScene]
                    call sortMenuD from _call_sortMenuD_71
                    if len(monsterEncounter) > 0:
                        return
                else:
                    $ lineOfScene += 1

            elif displayingScene.theScene[lineOfScene] == "ChoiceToDisplayPlayer":
                $ lineOfScene += 1
                $ choiceToCheck = int(displayingScene.theScene[lineOfScene])
                $ DataLocation = getFromName(ProgressEvent[DataLocation].name, ProgressEvent)

                while choiceToCheck-1 >= len(ProgressEvent[DataLocation].choices):
                    $ ProgressEvent[DataLocation].choices.append("")

                $ PlayerChoiceToDisplay = ProgressEvent[DataLocation].choices[choiceToCheck-1]
            elif displayingScene.theScene[lineOfScene] == "ChoiceToDisplayMonster":
                $ lineOfScene += 1
                $ choiceToCheck = int(displayingScene.theScene[lineOfScene])
                $ DataLocation = getFromName(ProgressEvent[DataLocation].name, ProgressEvent)

                while choiceToCheck-1 >= len(ProgressEvent[DataLocation].choices):
                    $ ProgressEvent[DataLocation].choices.append("")

                $ MonsterChoiceToDisplay = ProgressEvent[DataLocation].choices[choiceToCheck-1]

            elif displayingScene.theScene[lineOfScene] == "ChoiceToDisplayPlayerFromOtherEvent":
                $ lineOfScene += 1
                $ CheckEvent = getFromName(displayingScene.theScene[lineOfScene], ProgressEvent)
                $ lineOfScene += 1
                $ choiceToCheck = int(displayingScene.theScene[lineOfScene])

                while choiceToCheck-1 >= len(ProgressEvent[CheckEvent].choices):
                    $ ProgressEvent[CheckEvent].choices.append("")

                $ PlayerChoiceToDisplay = ProgressEvent[DataLocation].choices[choiceToCheck-1]
            elif displayingScene.theScene[lineOfScene] == "ChoiceToDisplayMonsterFromOtherEvent":
                $ lineOfScene += 1
                $ CheckEvent = getFromName(displayingScene.theScene[lineOfScene], ProgressEvent)
                $ lineOfScene += 1
                $ choiceToCheck = int(displayingScene.theScene[lineOfScene])

                while choiceToCheck-1 >= len(ProgressEvent[CheckEvent].choices):
                    $ ProgressEvent[CheckEvent].choices.append("")

                $ MonsterChoiceToDisplay = ProgressEvent[DataLocation].choices[choiceToCheck-1]

            elif displayingScene.theScene[lineOfScene] == "HealingSickness":
                $ HealingSickness = 6

            elif displayingScene.theScene[lineOfScene] == "AdvanceTime":
                $ lineOfScene += 1
                if int(displayingScene.theScene[lineOfScene]) > 0:
                    $ number = int(displayingScene.theScene[lineOfScene])
                    $ lineOfScene += 1
                    python:
                        try:
                            if displayingScene.theScene[lineOfScene] == "DelayNotifications":
                                timeNotify = 1
                            else:
                                lineOfScene -= 1
                        except:
                            lineOfScene -= 1
                    call advanceTime(number) from _call_advanceTime_4
            elif displayingScene.theScene[lineOfScene] == "RestPlayer":
                $ lineOfScene += 1
                if displayingScene.theScene[lineOfScene] == "DelayNotifications":
                    $ timeNotify = 1
                else:
                    $ lineOfScene -= 1
                call advanceTime(TimeIncrease=1) from _call_advanceTime_1
                $ favorPool = CalcGoddessFavor(player)
                $ favorStrain = 0
                $ player = Resting(player)
                $ notFunction = 0
                $ noCombatFunction = 0
                $ noDFunction = 0

            elif displayingScene.theScene[lineOfScene] == "RefreshPlayer":
                $ player = player.statusEffects.refresh(player)
                $ player.stats.refresh()
                $ favorPool = CalcGoddessFavor(player)
                $ favorStrain = 0

            elif displayingScene.theScene[lineOfScene] == "PermanentlyChangeSensitivity":
                $ lineOfScene += 1
                $ resTarget = displayingScene.theScene[lineOfScene]
                $ lineOfScene += 1
                $ resAmount = int(displayingScene.theScene[lineOfScene])

                $ player.BodySensitivity.changeRes (resTarget, resAmount)

                if (int(displayingScene.theScene[lineOfScene]) < 0):
                    $ amountLost = resAmount*-1
                    if resTarget == "Breasts":
                        $ resTarget = "Nipple"
                    if resTarget == "Sex":
                        $ resTarget = "Cock"
                    $ display = "You {i}permanently{/i} lost " + str(amountLost) + " " + resTarget +  " sensitivity!"
                else:
                    if resTarget == "Breasts":
                        $ resTarget = "Nipple"
                    if resTarget == "Sex":
                        $ resTarget = "Cock"
                    $ display = "You {i}permanently{/i} gained " + displayingScene.theScene[lineOfScene] + " " + resTarget +  " sensitivity!"
                if (int(displayingScene.theScene[lineOfScene]) != 0):
                    "[display!i]"

            elif displayingScene.theScene[lineOfScene] == "PermanentChangeStatusEffectResistances":
                $ lineOfScene += 1
                $ resTarget = displayingScene.theScene[lineOfScene]
                $ lineOfScene += 1
                $ resAmount = int(displayingScene.theScene[lineOfScene])

                $ player.resistancesStatusEffects.changeRes (resTarget, resAmount)

                if (int(displayingScene.theScene[lineOfScene]) < 0):
                    $ amountLost = resAmount*-1

                    $ display = "You lost " + str(amountLost) + " " + resTarget +  " resistance!"
                else:
                    $ display = "You gained " + displayingScene.theScene[lineOfScene] + " " + resTarget +  " resistance!"
                if (int(displayingScene.theScene[lineOfScene]) != 0):
                    "[display!i]"

            elif displayingScene.theScene[lineOfScene] == "PermanentlyChangeFetish":
                $ lineOfScene += 1
                $ resTarget = displayingScene.theScene[lineOfScene]
                $ lineOfScene += 1
                $ resAmount = int(displayingScene.theScene[lineOfScene])

                $ baseFetish = player.getFetish(resTarget)
                $ baseFetish += resAmount

                $ player.setFetish(resTarget, baseFetish)

                $ fetchFetish = getFromName(resTarget, player.FetishList)
                if player.FetishList[fetchFetish].Type == "Fetish":

                    if baseFetish < 100:
                        if (int(displayingScene.theScene[lineOfScene]) >= 1):
                            if resAmount > 1:
                                $ display = "You {i}permanently{/i} gained " + str(resAmount) + " fetish levels for " + resTarget +  "..."
                            else:
                                $ display = "You have {i}permanently{/i} gained a fetish level for " + resTarget +  "."

                        elif (int(displayingScene.theScene[lineOfScene]) < 0):
                            $ resAmount *= -1
                            if resAmount > 1:
                                $ display = "You have {i}permanently{/i} lost " + str(resAmount) +" fetish levels for " + resTarget +  "."
                            else:
                                $ display = "You have {i}permanently{/i} lost a fetish level for " + resTarget +  "."
                    if baseFetish > 100 and resAmount >= 1:
                        $ display = "Fantasies of " + resTarget +  " swirl through your mind, and your heart beats faster, you have {i}permanently{/i} gained a fetish level for " + resTarget + ", exceeding your normal obsession..."

                    if (resAmount != 0):
                        "[display!i]"


            elif displayingScene.theScene[lineOfScene] == "EmptySpiritCounter":
                $ spiritLost0 = 0
            elif displayingScene.theScene[lineOfScene] == "RoledCGEnd":
                $ monsterEncounterCG = []
                $ RoledCGOn = 0
                $ CgRoleKeeper = []

            elif displayingScene.theScene[lineOfScene] == "Menu":
                $ index = 0
                $ lineOfScene += 1
                $ MenuLineSceneCheckMark = copy.deepcopy(lineOfScene)

                #$ check = ProgressEvent[DataLocation].choices[1]
                #"[check]"

                label recheckMenu:
                    $ ind = index
                    $ lineOfScene = copy.deepcopy(MenuLineSceneCheckMark)
                    $ menuArray = []
                    $ passedArray = []


                $ MaxMenuSlots = 6
                if displayingScene.theScene[lineOfScene] == "MaxMenuSlots":
                    $ lineOfScene += 1
                    $ MaxMenuSlots = int(displayingScene.theScene[lineOfScene])
                    $ lineOfScene += 1

                $ eventMenuJumps = []
                $ eventMenuSceneJumps = []
                $clear1 = 0
                $clear2 = 0
                $clear3 = 0
                $clear4 = 0
                $clear5 = 0
                $clear6 = 0

                $ display1 = ""
                $ display2 = ""
                $ display3 = ""
                $ display4 = ""
                $ display5 = ""
                $ display6 = ""

                $ finalOption = ""
                $ finalOptionEvent = ""
                $ finalOptionEventScene = ""
                $ finalSet = 0

                $ ShuffleMenuOptions = 0
                #$ showOnSide = 1
                while displayingScene.theScene[lineOfScene] != "EndLoop":

                    $ passcheck = 0
                    $ override = ""
                    $ display = ""
                    $ eventMenuJumps.append("")
                    $ eventMenuSceneJumps.append("")

                    $ passcheck = SceneRequiresCheck()

                    #"[override]"

                    if override != "":
                        python:
                            ova = 0
                            for each in menuArray:
                                if each == override:
                                    del menuArray[ova]
                                    del passedArray[ova]
                                    del eventMenuJumps[ova]
                                    del eventMenuSceneJumps[ova]
                                    ova -= 1
                                ova +=1

                    if displayingScene.theScene[lineOfScene] != "EndLoop":

                        if passcheck == 1 :
                            $ display = ""
                            $ display = displayingScene.theScene[lineOfScene]
                            $ passedArray.append(1)

                        else:
                            if display != "":
                                $ passedArray.append(0)
                    if display != "":
                        $ menuArray.append(copy.deepcopy(display))
                    else:
                        $ del eventMenuJumps[-1]
                        $ del eventMenuSceneJumps[-1]


                    if displayingScene.theScene[lineOfScene] != "EndLoop":
                        $ lineOfScene += 1

                if ShuffleMenuOptions == 1:
                    $ menuArrays = list(zip(menuArray, passedArray, eventMenuJumps, eventMenuSceneJumps))
                    $ renpy.random.shuffle(menuArrays)
                    $ menuArray, passedArray, eventMenuJumps, eventMenuSceneJumps = zip(*menuArrays)


                $ choiceName = ""

                $ exist1 = 0
                $ exist2 = 0
                $ exist3 = 0
                $ exist4 = 0
                $ exist5 = 0
                $ exist6 = 0

                $ setEventJump1 = ""
                $ setEventJump2 = ""
                $ setEventJump3 = ""
                $ setEventJump4 = ""
                $ setEventJump5 = ""
                $ setEventJump6 = ""

                $ setEventSceneJump1 = ""
                $ setEventSceneJump2 = ""
                $ setEventSceneJump3 = ""
                $ setEventSceneJump4 = ""
                $ setEventSceneJump5 = ""
                $ setEventSceneJump6 = ""



                if finalOption != "" and finalSet == 0:
                    python:
                        ova = 0
                        for each in menuArray:
                            if each == finalOption:
                                del menuArray[ova]
                                del passedArray[ova]
                                del eventMenuJumps[ova]
                                del eventMenuSceneJumps[ova]
                                ova -= 1
                            ova +=1

                    if MaxMenuSlots == 6:
                        $ MaxMenuSlots = 5

                if len(menuArray) > MaxMenuSlots:
                    show screen MenuPageButtons
                else:
                    hide screen MenuPageButtons

                while ind < len(menuArray):
                    if display1 == ""and MaxMenuSlots >= 1:
                        $ display1 = menuArray[ind]
                        $ clear1 = passedArray[ind]
                        $ setEventJump1 = eventMenuJumps[ind]
                        $ setEventSceneJump1 = eventMenuSceneJumps[ind]
                    elif display2 == "" and MaxMenuSlots >= 2:
                        $ display2 = menuArray[ind]
                        $ clear2 = passedArray[ind]
                        $ setEventJump2 = eventMenuJumps[ind]
                        $ setEventSceneJump2 = eventMenuSceneJumps[ind]
                    elif display3 == "" and MaxMenuSlots >= 3:
                        $ display3 = menuArray[ind]
                        $ clear3 = passedArray[ind]
                        $ setEventJump3 = eventMenuJumps[ind]
                        $ setEventSceneJump3 = eventMenuSceneJumps[ind]
                    elif display4 == "" and MaxMenuSlots >= 4:
                        $ display4 = menuArray[ind]
                        $ clear4 = passedArray[ind]
                        $ setEventJump4 = eventMenuJumps[ind]
                        $ setEventSceneJump4 = eventMenuSceneJumps[ind]
                    elif display5 == "" and MaxMenuSlots >= 5:
                        $ display5 = menuArray[ind]
                        $ clear5 = passedArray[ind]
                        $ setEventJump5 = eventMenuJumps[ind]
                        $ setEventSceneJump5 = eventMenuSceneJumps[ind]
                    elif display6 == "" and finalOption == "" and MaxMenuSlots >= 6:
                        $ display6 = menuArray[ind]
                        $ clear6 = passedArray[ind]
                        $ setEventJump6 = eventMenuJumps[ind]
                        $ setEventSceneJump6 = eventMenuSceneJumps[ind]
                    $ ind +=1


                if display1 != "":
                    $ exist1 = 1
                if display2 != "":
                    $ exist2 = 1
                if display3 != "":
                    $ exist3 = 1
                if display4 != "":
                    $ exist4 = 1
                if display5 != "":
                    $ exist5 = 1
                if finalOption != "" and finalSet == 0:
                    $ finalSet =1
                elif display6 != "":
                    $ exist6 = 1


                $ damageToPlayer = " [CritText] [EffectiveText]" + "You gain " + str(finalDamage) + " arousal."
                if len(monsterEncounter) > 0 and CombatFunctionEnemytarget < len(monsterEncounter):
                    $ damageToEnemy = " [CritText] [EffectiveText]" + monsterEncounter[CombatFunctionEnemytarget].name + " gains " + str(finalDamage) + " arousal."
                else:
                    $ damageToEnemy = ""

                $ DataLocation = getFromName(ProgressEvent[DataLocation].name, ProgressEvent)
                $ progressDisplay = copy.deepcopy(ProgressEvent[DataLocation].eventProgress)

                if savedLine != "" and savedLineInMenu == 1:
                    $ LastLine = copy.deepcopy(savedLine)
                    $ savedLine = ""
                    $ savedLineInMenu = 0
                elif LastLine != "StartCombat" and LastLine != "EndLoop" and LastLine != "end":
                    pass
                else:
                    $ LastLine = ""


                call playSpecialEffects(VisualEffect, 1) from _call_playSpecialEffects
                call playSpecialEffects(VisualEffect2, 2) from _call_playSpecialEffects_1
                call playSpecialEffects(VisualEffect3, 3) from _call_playSpecialEffects_2

                show screen fakeTextBox
                window hide

                if mgdAutosaveCount <= 0:
                    $ renpy.force_autosave()
                    #$ renpy.pause(1, True)
                    $ mgdAutosaveCount = copy.deepcopy(mgdAutosaveFrequency)
                else:
                    if len(monsterEncounter) == 0:
                        $ mgdAutosaveCount -= 2
                    else:
                        $ mgdAutosaveCount -= 1

                menu menuList:
                    "[display1!i]" if exist1 == 1:
                        if clear1 == 1:
                            hide screen MenuPageButtons
                            hide screen fakeTextBox
                            if setEventJump1 == "":
                                $ display = display1
                                $ choiceName = display1
                                $ MenuLineSceneCheckMark = -1
                                call sortMenuD from _call_sortMenuD_9
                                if len(monsterEncounter) > 0:
                                    return
                            else:
                                $ isEventNow = 1
                                $ currentChoice = 0
                                $ DataLocation = getFromName(setEventJump1, EventDatabase)
                                if setEventSceneJump1 != "":
                                    $ currentChoice = getFromNameOfScene(setEventSceneJump1, EventDatabase[DataLocation].theEvents)
                                jump sortMenuD
                        else:
                            call recheckMenu from _call_recheckMenu
                            if len(monsterEncounter) > 0:
                                return
                    "[display2!i]" if exist2 == 1 :
                        if clear2 == 1:
                            hide screen MenuPageButtons
                            hide screen fakeTextBox
                            if setEventJump2 == "":
                                $ display = display2
                                $ choiceName = display2
                                $ MenuLineSceneCheckMark = -1
                                call sortMenuD from _call_sortMenuD_10
                                if len(monsterEncounter) > 0:
                                    return
                            else:
                                $ isEventNow = 1
                                $ currentChoice = 0
                                $ DataLocation = getFromName(setEventJump2, EventDatabase)
                                if setEventSceneJump2 != "":
                                    $ currentChoice = getFromNameOfScene(setEventSceneJump2, EventDatabase[DataLocation].theEvents)
                                jump sortMenuD
                        else:
                            call recheckMenu from _call_recheckMenu_1
                            if len(monsterEncounter) > 0:
                                return
                    "[display3!i]" if exist3 == 1:
                        if clear3 == 1:
                            hide screen MenuPageButtons
                            hide screen fakeTextBox
                            if setEventJump3 == "":
                                $ display = display3
                                $ choiceName = display3
                                $ MenuLineSceneCheckMark = -1
                                call sortMenuD from _call_sortMenuD_14
                                if len(monsterEncounter) > 0:
                                    return
                            else:
                                $ isEventNow = 1
                                $ currentChoice = 0
                                $ DataLocation = getFromName(setEventJump3, EventDatabase)
                                if setEventSceneJump3 != "":
                                    $ currentChoice = getFromNameOfScene(setEventSceneJump3, EventDatabase[DataLocation].theEvents)
                                jump sortMenuD
                        else:
                            call recheckMenu from _call_recheckMenu_2
                            if len(monsterEncounter) > 0:
                                return
                    "[display4!i]" if exist4 == 1:
                        if clear4 == 1:
                            hide screen MenuPageButtons
                            hide screen fakeTextBox
                            if setEventJump4 == "":
                                $ display = display4
                                $ choiceName = display4
                                $ MenuLineSceneCheckMark = -1
                                call sortMenuD from _call_sortMenuD_16
                                if len(monsterEncounter) > 0:
                                    return
                            else:
                                $ isEventNow = 1
                                $ currentChoice = 0
                                $ DataLocation = getFromName(setEventJump4, EventDatabase)
                                if setEventSceneJump4 != "":
                                    $ currentChoice = getFromNameOfScene(setEventSceneJump4, EventDatabase[DataLocation].theEvents)
                                jump sortMenuD
                        else:
                            call recheckMenu from _call_recheckMenu_3
                            if len(monsterEncounter) > 0:
                                return
                    "[display5!i]" if exist5 == 1:
                        if clear5 == 1:
                            hide screen MenuPageButtons
                            hide screen fakeTextBox
                            if setEventJump5 == "":
                                $ display = display5
                                $ choiceName = display5
                                $ MenuLineSceneCheckMark = -1
                                call sortMenuD from _call_sortMenuD_18
                                if len(monsterEncounter) > 0:
                                    return
                            else:
                                $ isEventNow = 1
                                $ currentChoice = 0
                                $ DataLocation = getFromName(setEventJump5, EventDatabase)
                                if setEventSceneJump5 != "":
                                    $ currentChoice = getFromNameOfScene(setEventSceneJump5, EventDatabase[DataLocation].theEvents)
                                jump sortMenuD
                        else:
                            call recheckMenu from _call_recheckMenu_4
                            if len(monsterEncounter) > 0:
                                return
                    "[display6!i]" if exist6 == 1 :
                        if clear6 == 1:
                            hide screen MenuPageButtons
                            hide screen fakeTextBox
                            if setEventJump6 == "":
                                $ display = display6
                                $ choiceName = display6
                                $ MenuLineSceneCheckMark = -1
                                call sortMenuD from _call_sortMenuD_19
                                if len(monsterEncounter) > 0:
                                    return
                            else:
                                $ isEventNow = 1
                                $ currentChoice = 0
                                $ DataLocation = getFromName(setEventJump6, EventDatabase)
                                if setEventSceneJump6 != "":
                                    $ currentChoice = getFromNameOfScene(setEventSceneJump6, EventDatabase[DataLocation].theEvents)
                                jump sortMenuD
                        else:
                            call recheckMenu from _call_recheckMenu_5
                            if len(monsterEncounter) > 0:
                                return
                    "[finalOption!i]" if hasattr(store, "finalSet") and finalSet == 1:
                        hide screen MenuPageButtons
                        hide screen fakeTextBox
                        if finalOptionEvent == "":
                            $ display = finalOption
                            $ choiceName = finalOption
                            $ MenuLineSceneCheckMark = -1
                            call sortMenuD from _call_sortMenuD_82
                            if len(monsterEncounter) > 0:
                                return
                        else:
                            $ isEventNow = 1
                            $ currentChoice = 0
                            $ DataLocation = getFromName(finalOptionEvent, EventDatabase)
                            if finalOptionEventScene != "":
                                $ currentChoice = getFromNameOfScene(finalOptionEventScene, EventDatabase[DataLocation].theEvents)
                            jump sortMenuD

            elif displayingScene.theScene[lineOfScene] == "ApplyStatusEffect":
                $ lineOfScene += 1
                $ skillAt = getFromName(displayingScene.theScene[lineOfScene], SkillsDatabase)
                $ statusSkill = SkillsDatabase[skillAt]

                if statusSkill.statusEffect != "Damage" and statusSkill.statusEffect != "Defence" and statusSkill.statusEffect != "Power" and statusSkill.statusEffect != "Technique" and statusSkill.statusEffect != "Willpower" and statusSkill.statusEffect != "Intelligence" and statusSkill.statusEffect != "Allure" and statusSkill.statusEffect != "Luck" and skillChoice.statusEffect != "%Power" and skillChoice.statusEffect != "%Technique" and skillChoice.statusEffect != "%Intelligence" and skillChoice.statusEffect != "%Willpower" and skillChoice.statusEffect != "%Allure" and skillChoice.statusEffect != "%Luck" and statusSkill.statusEffect != "Escape" and statusSkill.statusEffect != "Crit":
                    if len(monsterEncounter) > 0:
                        $ player = statusAfflict(player, statusSkill, monsterEncounter[CombatFunctionEnemytarget])
                    else:
                        $ player = statusAfflict(player, statusSkill)
                else:
                    if len(monsterEncounter) > 0:
                        $ holder = statusBuff(player, monsterEncounter[CombatFunctionEnemytarget], statusSkill, 1)
                    else:
                        $ holder = statusBuff(player, player, statusSkill, 1)

                    $ player = holder[0]

                if statusSkill.statusEffect == "Restrain":
                    $ player.restraintStruggle = copy.deepcopy(statusSkill.restraintStruggle)
                    $ player.restraintStruggleCharmed = copy.deepcopy(statusSkill.restraintStruggleCharmed)
                    $ player.restraintEscaped = copy.deepcopy(statusSkill.restraintEscaped)
                    $ player.restraintEscapedFail = copy.deepcopy(statusSkill.restraintEscapedFail)
                    if len(monsterEncounter) >= 1:
                        $ player.restrainer = monsterEncounter[CombatFunctionEnemytarget]

            elif displayingScene.theScene[lineOfScene] == "AllowRunning":
                $ canRun = True

            elif displayingScene.theScene[lineOfScene] == "CombatEncounter":
                $ lineOfScene += 1
                $ monsterEncounter = []
                $ monsterEncounterCG = []
                $ trueMonsterEncounter = []
                $ monNum = 0
                $ runBG = ""
                $ runAndStayInEvent = 0
                $ checkPreFuncs = 0
                $ combatItems = 0

                while checkPreFuncs == 0:
                    if displayingScene.theScene[lineOfScene] == "NoRunning":
                        $ canRun = False
                        $ lineOfScene += 1

                    elif displayingScene.theScene[lineOfScene] == "SetBGOnRun":
                        $ lineOfScene += 1
                        $ runBG = changeBG(displayingScene.theScene[lineOfScene])
                        $ lineOfScene += 1
                    elif displayingScene.theScene[lineOfScene] == "DenyInventory":
                        $ combatItems = 1
                        $ lineOfScene += 1
                    elif displayingScene.theScene[lineOfScene] == "RunningWontSkipEvent":
                        $ runAndStayInEvent = 1
                        $ lineOfScene += 1
                    else:
                        $ checkPreFuncs += 1

                while displayingScene.theScene[lineOfScene] != "StartCombat":
                    $ insertToLocation = len(monsterEncounter)
                    $ addMonsterTo(displayingScene.theScene[lineOfScene], monsterEncounter, insertToLocation)
                    #$ monsterEncounter[monNum] = monsterEncounter[monNum].statusEffects.refresh( monsterEncounter[monNum])
                    $ addMonsterTo(displayingScene.theScene[lineOfScene], trueMonsterEncounter, insertToLocation)
                    #$ trueMonsterEncounter[monNum] = trueMonsterEncounter[monNum].statusEffects.refresh(trueMonsterEncounter[monNum])
                    $ lineOfScene += 1
                    $ checkPreFuncs = 0
                    while checkPreFuncs == 0:
                        if displayingScene.theScene[lineOfScene] == "ApplyStance":
                            $ lastAttack = Skill()
                            $ lineOfScene += 1
                            $ givingStance = displayingScene.theScene[lineOfScene]
                            $ lineOfScene += 1
                            python:
                                try:
                                    if displayingScene.theScene[lineOfScene] == "SetAttack":
                                         lineOfScene += 1
                                         lastAttack = SkillsDatabase[getFromName(displayingScene.theScene[lineOfScene], SkillsDatabase)]
                                    else:
                                        lineOfScene -= 1
                                except:
                                    lineOfScene -= 1
                            $ monsterEncounter[monNum].giveStance(givingStance, player, lastAttack)
                            $ player.giveStance(givingStance, monsterEncounter[monNum], lastAttack)
                            $ lineOfScene += 1
                        elif displayingScene.theScene[lineOfScene] == "Restrainer":
                            $ player.restrainer = monsterEncounter[monNum]
                            $ lineOfScene += 1
                        else:
                            $ checkPreFuncs += 1
                    $ monNum += 1
                $ monsterEncounter = NumberMonsters(monsterEncounter)
                $ SceneCharacters = []
                if len(monsterEncounter) > 0:
                    $ HoldingSceneForCombat = copy.deepcopy(displayingScene)
                    $ HoldingLineForCombat = copy.deepcopy(lineOfScene)
                    $ HoldingDataLocForCombat = copy.deepcopy(DataLocation)
                    call combat from _call_combat_1
                    label endCombatCalled:
                    if HoldingSceneForCombat != Dialogue():
                        #$ test = HoldingSceneForCombat[HoldingLineForCombat].NameOfScene
                        $ displayingScene = copy.deepcopy(HoldingSceneForCombat)
                        $ lineOfScene = copy.deepcopy(HoldingLineForCombat)
                        $ DataLocation = copy.deepcopy(HoldingDataLocForCombat)
                        $ HoldingSceneForCombat = Dialogue()
                        $ HoldingLineForCombat = 0
                        $ HoldingDataLocForCombat = 0

                $ stunnedGridPlayer = -1
            elif displayingScene.theScene[lineOfScene] == "MiniGameSnake":
                call ParadeGameInit from _call_ParadeGameInit
                hide screen SnakeGameScreen

            elif displayingScene.theScene[lineOfScene] == "FishingMiniGame":
                $ AppearTimerMin = 100
                $ AppearTimerMax = 500
                $ DifficultyTimerMin = 175
                $ DifficultyTimerMax = 250
                $ ReelsNeeded = 1
                $ FishingPassJump = ""
                $ FishingFailJump = ""
                $ FishingJump = ""

                while displayingScene.theScene[lineOfScene] != "EndLoop":
                    $ lineOfScene += 1
                    if displayingScene.theScene[lineOfScene] == "AppearTimerRange":
                        $ lineOfScene += 1
                        $ AppearTimerMin = int(displayingScene.theScene[lineOfScene])
                        $ lineOfScene += 1
                        $ AppearTimerMax = int(displayingScene.theScene[lineOfScene])
                    elif displayingScene.theScene[lineOfScene] == "FailTimerRange":
                        $ lineOfScene += 1
                        $ DifficultyTimerMin = int(displayingScene.theScene[lineOfScene])
                        $ lineOfScene += 1
                        $ DifficultyTimerMax = int(displayingScene.theScene[lineOfScene])
                    elif displayingScene.theScene[lineOfScene] == "ReelsNeeded":
                        $ lineOfScene += 1
                        $ ReelsNeeded = int(displayingScene.theScene[lineOfScene])
                    elif displayingScene.theScene[lineOfScene] == "FishingPassJump":
                        $ lineOfScene += 1
                        $ FishingPassJump = displayingScene.theScene[lineOfScene]
                    elif displayingScene.theScene[lineOfScene] == "FishingFailJump":
                        $ lineOfScene += 1
                        $ FishingFailJump = displayingScene.theScene[lineOfScene]

                call fishingMiniGame from _call_fishingMiniGame

                $ display = FishingJump

                call sortMenuD from _call_sortMenuD_102

            elif displayingScene.theScene[lineOfScene] == "JumpToScene":
                $ lineOfScene += 1
                $ display = displayingScene.theScene[lineOfScene]

                call sortMenuD from _call_sortMenuD_20

                if len(monsterEncounter) > 0:
                    return
            elif displayingScene.theScene[lineOfScene] == "JumpToRandomScene":
                $ lineOfScene += 1

                $ randomSelection = []

                while displayingScene.theScene[lineOfScene] != "EndLoop":
                    $ passcheck = 0
                    $ display = ""
                    $ passcheck = SceneRequiresCheck()

                    if passcheck == 1:
                        $ randomSelection.append(displayingScene.theScene[lineOfScene])
                    $ lineOfScene += 1

                $ renpy.random.shuffle(randomSelection)
                $ display = randomSelection[0]
                $ randomSelection = []
                call sortMenuD from _call_sortMenuD_22
                if len(monsterEncounter) > 0:
                    return
            elif displayingScene.theScene[lineOfScene] == "JumpToEvent":
                $ lineOfScene += 1
                $ DialogueIsFrom = "Event"
                $ isEventNow = 1
                $ currentChoice = 0
                $ Speaker = Character(_(''))
                $ DataLocation = getFromName(displayingScene.theScene[lineOfScene], EventDatabase)

                jump sortMenuD
            elif displayingScene.theScene[lineOfScene] == "JumpToEventThenScene":
                $ lineOfScene += 1
                $ DialogueIsFrom = "Event"
                $ isEventNow = 1
                $ currentChoice = 0
                $ Speaker = Character(_(''))
                $ DataLocation = getFromName(displayingScene.theScene[lineOfScene], EventDatabase)
                $ lineOfScene += 1
                $ currentChoice = getFromNameOfScene(displayingScene.theScene[lineOfScene], EventDatabase[DataLocation].theEvents)

                jump sortMenuD

            elif displayingScene.theScene[lineOfScene] == "CallNextSceneJumpThenReturn":
                $ callNextJump = 2
                $ inCalledSceneJump = 2

                $ specifyCurrentChoice = 0
                $ showingDream = []

                label playSceneJump:
                    if callNextJump == 1:
                        $ specifyCurrentChoice = getFromNameOfScene(display, EventDatabase[DataLocation].theEvents)
                        $ showingDream.append(copy.deepcopy(EventDatabase[DataLocation]))
                        $ callNextJump = 0
                        $ inCalledSceneJump = 0
                        call TimeEvent(CardType="Any", LoopedList=showingDream) from _call_TimeEvent_17
                        $ noDFunction = 0
                        return

            elif displayingScene.theScene[lineOfScene] == "CallSceneThenReturn":
                $ lineOfScene += 1
                $ specifyCurrentChoice = 0
                $ specifyCurrentChoice = getFromNameOfScene(displayingScene.theScene[lineOfScene], EventDatabase[DataLocation].theEvents)

                $ showingDream = []
                $ showingDream.append(copy.deepcopy(EventDatabase[DataLocation]))
                call TimeEvent(CardType="Any", LoopedList=showingDream) from _call_TimeEvent_8
                $ noDFunction = 0

            elif displayingScene.theScene[lineOfScene] == "CallEventAndSceneThenReturn":
                $ lineOfScene += 1

                $ specifyDataLocation = getFromName(displayingScene.theScene[lineOfScene], EventDatabase)

                $ lineOfScene += 1
                $ specifyCurrentChoice = 0
                $ specifyCurrentChoice = getFromNameOfScene(displayingScene.theScene[lineOfScene], EventDatabase[specifyDataLocation].theEvents)

                $ showingDream = []
                $ showingDream.append(copy.deepcopy(EventDatabase[specifyDataLocation]))

                call TimeEvent(CardType="Any", LoopedList=showingDream) from _call_TimeEvent_9

                $ noDFunction = 0

            elif displayingScene.theScene[lineOfScene] == "CallCombatEventAndScene":
                $ lineOfScene += 1
                $ DialogueIsFrom = "Event"
                $ isEventNow = 1
                $ currentChoice = 0
                $ HideOrgasmLine = 1

                $ DataLocation = getFromName(displayingScene.theScene[lineOfScene], EventDatabase)
                $ lineOfScene += 1
                $ currentChoice = getFromNameOfScene(displayingScene.theScene[lineOfScene], EventDatabase[DataLocation].theEvents)

                call sortMenuD from _call_sortMenuD_30
                return
            elif displayingScene.theScene[lineOfScene] == "JumpToNPCEvent":
                $ lineOfScene += 1
                $ DialogueIsFrom = "NPC"
                $ isEventNow = 1
                $ currentChoice = 0
                $ EnteringLocationCheck = 0
                $ DataLocation = getFromName(displayingScene.theScene[lineOfScene], EventDatabase)
                jump sortMenuD
            elif displayingScene.theScene[lineOfScene] == "JumpToNPCEventThenScene":
                $ lineOfScene += 1
                $ DialogueIsFrom = "NPC"
                $ isEventNow = 1
                $ currentChoice = 0

                $ DataLocation = getFromName(displayingScene.theScene[lineOfScene], EventDatabase)
                $ lineOfScene += 1
                $ currentChoice = getFromNameOfScene(displayingScene.theScene[lineOfScene], EventDatabase[DataLocation].theEvents)
                $ EnteringLocationCheck = 0
                jump sortMenuD
            elif displayingScene.theScene[lineOfScene] == "JumpToLossEvent":
                hide screen ON_EnemyCardScreen
                $ lineOfScene += 1
                $ DialogueIsFrom = "LossEvent"
                $ isEventNow = 1
                $ currentChoice = 0

                $ DataLocation = getFromName(displayingScene.theScene[lineOfScene], EventDatabase)
                jump sortMenuD
            elif displayingScene.theScene[lineOfScene] == "ForceAutoSave":
                $ renpy.force_autosave()

    ############################################### Grid map functions ########################################################

            elif displayingScene.theScene[lineOfScene] == "ExitGridmap":
                $ onGridMap = 0
                $ runAndStayInEvent = 0
                $ RanAway = "False"
                $ InventoryAvailable = True
                $ DenyGridInventory = False
                hide screen Gridmap
                hide screen GridmapPlayer
                hide screen GridmapNPCs
                hide screen GridmapObstacles
                hide screen gridMoveKeys
                $ TheGrid = []


    ####################################################combat specific functions######################################################


            elif displayingScene.theScene[lineOfScene] == "ResetStatCheckDifficultyModifer":
                $ increaseStatCheck = 0


            elif displayingScene.theScene[lineOfScene] == "AddMonsterToEncounter":
                $ lineOfScene += 1
                $ replacingMonster = 0
                $ insertToLocation = len(monsterEncounter)
                if displayingScene.theScene[lineOfScene] == "ChangeForm":
                    $ lineOfScene += 1
                    $ replacingMonster = 1
                    $ insertToLocation = copy.deepcopy(CombatFunctionEnemytarget)
                    $ KeepingHP = copy.deepcopy(monsterEncounter[CombatFunctionEnemytarget].stats.hp)
                    $ KeepingSP = copy.deepcopy(monsterEncounter[CombatFunctionEnemytarget].stats.sp)
                    $ KeepingStatusEffects = copy.deepcopy(monsterEncounter[CombatFunctionEnemytarget].statusEffects)
                    $ KeepingStances = copy.deepcopy(monsterEncounter[CombatFunctionEnemytarget].combatStance)

                    python:
                        del monsterEncounter[CombatFunctionEnemytarget]
                        del trueMonsterEncounter[CombatFunctionEnemytarget]

                $ addMonsterTo(displayingScene.theScene[lineOfScene], monsterEncounter, insertToLocation)
                $ monsterEncounter[insertToLocation] = monsterEncounter[insertToLocation].statusEffects.refresh(monsterEncounter[insertToLocation])
                $ addMonsterTo(displayingScene.theScene[lineOfScene], trueMonsterEncounter,insertToLocation)
                $ trueMonsterEncounter[insertToLocation] = trueMonsterEncounter[insertToLocation].statusEffects.refresh(trueMonsterEncounter[insertToLocation])

                if replacingMonster == 0:
                    $ monInititive.append(-999)
                    $ monSkillChoice.append( getSkill(" ", SkillsDatabase))

                else:
                    $ monsterEncounter[insertToLocation].stats.hp = copy.deepcopy(KeepingHP)
                    $ monsterEncounter[insertToLocation].stats.sp = copy.deepcopy(KeepingSP)
                    $ monsterEncounter[insertToLocation].statusEffects = copy.deepcopy(KeepingStatusEffects)
                    $ monsterEncounter[insertToLocation].combatStance = copy.deepcopy(KeepingStances)

                    python:
                        del KeepingHP, KeepingStatusEffects, KeepingStances
                        try:
                            del KeepingStatusEffects
                        except:
                            pass

                if nightmare == 1:
                    $ goToLevel = player.stats.lvl
                    python:
                        if goToLevel > monsterEncounter[insertToLocation].stats.lvl:
                            monsterEncounter[insertToLocation].levelUp(goToLevel)

                            eroMod = 0.5
                            lvlchek = monsterEncounter[insertToLocation].stats.lvl
                            monsterEncounter[insertToLocation].moneyDropped = int(((lvlchek)^2+(lvlchek*10)+48)*eroMod)

                            expMod = 0.35
                            lvlchek = monsterEncounter[insertToLocation].stats.lvl
                            monsterEncounter[insertToLocation].stats.Exp = int(((0.4*(lvlchek*lvlchek))+(2*lvlchek)+(15*math.sqrt(lvlchek)-8))*expMod)

                $ monsterEncounter[insertToLocation] = initiateImageLayers(monsterEncounter[insertToLocation])
                python:
                    for SetData in persistantMonSetData:
                        if SetData.name == monsterEncounter[insertToLocation].IDname:
                            monsterEncounter[insertToLocation].currentSet = getFromName(SetData.startingSet, monsterEncounter[insertToLocation].ImageSets)

                    c = 0
                    for each in monsterEncounter:
                        monsterEncounter[c].name = copy.deepcopy(trueMonsterEncounter[c].name)

                        c += 1
                $ monsterEncounter = NumberMonsters(monsterEncounter)

                $ m = -1
                $ ar = 0
                while ar < len(monsterEncounter[m].combatDialogue):
                    $ specifyStance = 0
                    if ar < len(monsterEncounter[m].combatDialogue):
                        if monsterEncounter[m].combatDialogue[ar].lineTrigger == "MonsterArrived":
                            $ CombatFunctionEnemytarget = m
                            $ Speaker = Character(_(monsterEncounter[m].name))
                            $ display = monsterEncounter[m].combatDialogue[ar].theText[renpy.random.randint(-1, len(monsterEncounter[m].combatDialogue[ar].theText)-1)]
                            call read from _call_read_55
                    $ ar += 1

            elif displayingScene.theScene[lineOfScene] == "DamagePlayerFromMonster":
                $ recoil = 0
                $ critText = ""
                $ effectiveText = ""
                $ lineOfScene += 1
                $ MonAt = getFromName(displayingScene.theScene[lineOfScene], MonsterDatabase)
                $ holder = MonsterDatabase[MonAt]
                $ lineOfScene += 1
                $ skillAt = getFromName(displayingScene.theScene[lineOfScene], SkillsDatabase)
                $ holder = AttackCalc(holder, player,  SkillsDatabase[skillAt], 1)
                $ finalDamage = holder[0]
                $ critText = holder[2]
                $ effectiveText = holder[5]
                if len(monsterEncounter) >= 1:
                    $ recoil = holder[4]
                    $ recoil =  int(math.floor(recoil))
                    $ monsterEncounter[CombatFunctionEnemytarget].stats.hp += recoil

                $ player.stats.hp += holder[0]
                $ holder = []

    ###########################################Assorted functions####################################################


            elif displayingScene.theScene[lineOfScene] == "TimeBecomesNight":
                if TimeOfDay == Morning:
                    $ TimeOfDay = MorningNight
                elif TimeOfDay == Noon:
                    $ TimeOfDay = NoonNight
                elif TimeOfDay == Afternoon:
                    $ TimeOfDay = AfternoonNight
                elif TimeOfDay == DuskDay:
                    $ TimeOfDay = Dusk
                elif TimeOfDay == EveningDay:
                    $ TimeOfDay = Evening
                elif TimeOfDay == MidnightDay:
                    $ TimeOfDay = Midnight
                $ bg =  bgToNightDay(bg, ".png", "Night.png")
            elif displayingScene.theScene[lineOfScene] == "TimeBecomesDay":
                if TimeOfDay == MorningNight:
                    $ TimeOfDay = Morning
                elif TimeOfDay == NoonNight:
                    $ TimeOfDay = Noon
                elif TimeOfDay == AfternoonNight:
                    $ TimeOfDay = Afternoon
                elif TimeOfDay == Dusk:
                    $ TimeOfDay = DuskDay
                elif TimeOfDay == Evening:
                    $ TimeOfDay = EveningDay
                elif TimeOfDay == Midnight:
                    $ TimeOfDay = MidnightDay
                $ bg = bgToNightDay(bg, "Night.png", ".png")
            elif displayingScene.theScene[lineOfScene] == "TimeBecomesNormal":
                if TimeOfDay == MorningNight:
                    $ TimeOfDay = Morning
                    $ bg = bgToNightDay(bg, "Night.png", ".png")
                elif TimeOfDay == NoonNight:
                    $ TimeOfDay = Noon
                    $ bg = bgToNightDay(bg, "Night.png", ".png")
                elif TimeOfDay == AfternoonNight:
                    $ TimeOfDay = Afternoon
                    $ bg = bgToNightDay(bg, "Night.png", ".png")

                if TimeOfDay == DuskDay:
                    $ TimeOfDay = Dusk
                    $ bg =  bgToNightDay(bg, ".png", "Night.png")
                elif TimeOfDay == EveningDay:
                    $ TimeOfDay = Evening
                    $ bg =  bgToNightDay(bg, ".png", "Night.png")
                elif TimeOfDay == MidnightDay:
                    $ TimeOfDay = Midnight
                    $ bg =  bgToNightDay(bg, ".png", "Night.png")

            elif displayingScene.theScene[lineOfScene] == "DisplaySavedLine":
                $ display = savedLine
                call read from _call_read_52
            elif displayingScene.theScene[lineOfScene] == "UseSavedLineInMenu":
                $ savedLineInMenu = 1
            elif displayingScene.theScene[lineOfScene] == "CallLossLevelUp":
                $ NoGameOver = 1
                call lostExpCheck from _call_lostExpCheck

            elif displayingScene.theScene[lineOfScene] == "UseHeldBG":
                if heldBG != "":
                    $ heldBG =  bgToNightDay(heldBG, "Night.png", ".png")
                    $ bg  = changeBG(copy.deepcopy(heldBG))

                $ heldBG = ""

            elif displayingScene.theScene[lineOfScene] == "HideTreasureChest":
                hide chest

            elif displayingScene.theScene[lineOfScene] == "HasErosLessThan":
                $ lineOfScene += 1
                if int(displayingScene.theScene[lineOfScene]) > player.inventory.money:
                    $ lineOfScene += 1
                    $ display = displayingScene.theScene[lineOfScene]
                    call sortMenuD from _call_sortMenuD_15
                    if len(monsterEncounter) > 0:
                        return
                else:
                    $ lineOfScene += 1

            elif displayingScene.theScene[lineOfScene] == "AllowInventory":
                $ InventoryAvailable = True
            elif displayingScene.theScene[lineOfScene] == "DenyInventory":
                $ InventoryAvailable = False

            elif displayingScene.theScene[lineOfScene] == "BumpToTown":
                jump Town

            elif displayingScene.theScene[lineOfScene] == "GameOver":
                $ LostGameOver = 1
                $ NoGameOver = 0

                jump lostExpCheck
            elif displayingScene.theScene[lineOfScene] == "TrueGameOver":
                $ renpy.full_restart()
            elif displayingScene.theScene[lineOfScene] == "QuestComplete":
                if DialogueIsFrom == "Event":
                    $ ProgressEvent[DataLocation].questComplete = 1
            elif displayingScene.theScene[lineOfScene] == "AdventureComplete":
                $ lineOfScene += 1
                $ AdvLocation = getFromName(displayingScene.theScene[lineOfScene], ProgressAdventure)
                $ ProgressAdventure[AdvLocation].questComplete = 1

            elif displayingScene.theScene[lineOfScene] == "HasErosLessThanInput":
                if debt > player.inventory.money:
                    $ lineOfScene += 1
                    $ display = displayingScene.theScene[lineOfScene]
                    call sortMenuD from _call_sortMenuD_3
                    if len(monsterEncounter) > 0:
                        return
                else:
                    $ lineOfScene += 1

            elif displayingScene.theScene[lineOfScene] == "AddInputToProgress":
                $ DataLocation = getFromName(ProgressEvent[DataLocation].name, ProgressEvent)
                $ ProgressEvent[DataLocation].eventProgress += int(math.floor(debt))

            elif displayingScene.theScene[lineOfScene] == "RespecPlayer":
                $ player.respec()
                $ sexResCap = 150
                $ assResCap = 150
                $ nipResCap = 200
                $ chuResCap = 150
                $ seducResCap = 150
                $ magResCap = 150
                $ painResCap = 150
                $ hpFloor = 50
                $ epFloor = 20
                $ spFloor = 1
                $ powFloor = 1
                $ spdFloor = 1
                $ intFloor = 1
                $ allFloor = 1
                $ wilFloor = 1
                $ lukFloor = 1
                $ respeccing = 1
                $ hasResPoints = 1
                hide screen ON_HealthDisplay
                hide screen ON_HealthDisplayBacking

                $ tentativeStats = copy.deepcopy(player)
                call characterCreation from _call_characterCreation_2
                call setStatFloors from _call_setStatFloors_5
                show screen ON_HealthDisplayBacking #(_layer="hplayer")
                show screen ON_HealthDisplay #(_layer="sayScreen")
                $ respeccing = 0
            #CODEMOD
            elif displayingScene.theScene[lineOfScene] == "AdjustPlayerLevel":
                $ lineOfScene += 1
                $ newLevel = 1
                if displayingScene.theScene[lineOfScene] == "Cap":
                    if levelCapEnabled():
                        $ newLevel = getMaxLevelCap()
                    else:
                        $ newLevel = -1
                elif displayingScene.theScene[lineOfScene] == "Input":
                    $ newLevel = renpy.input(_("What level should the player be changed to (Currently [player.stats.lvl])?"), length=3, allow="0123456789") or _("-1")
                else:
                    $ newLevel = displayingScene.theScene[lineOfScene]
                
                python:
                    try:
                        newLevel = int(newLevel)
                    except:
                        newLevel = -1
                    
                    if newLevel != -1:
                        respecPlayerToLevel(newLevel)

            elif displayingScene.theScene[lineOfScene] == "DonateToGoddess":
                call DonateToGoddess from _call_DonateToGoddess

            elif displayingScene.theScene[lineOfScene] == "PurgeFetishes":
                call PurgeFetishes from _call_PurgeFetishes
            elif displayingScene.theScene[lineOfScene] == "AddTributeToProgress":
                $ DataLocation = getFromName(ProgressEvent[DataLocation].name, ProgressEvent)
                $ ProgressEvent[DataLocation].eventProgress += int(math.floor(tribute))
                $ tribute = 0
            else:
                $ noDFunction = 1

            if len(monsterEncounter) > 0:
                if noDFunction == 1 and lineOfScene < len(displayingScene.theScene):
                    if displayingScene.theScene[lineOfScene] == "LevelUpMonster":
                        $ lineOfScene += 1
                        $ goToLevel = monsterEncounter[CombatFunctionEnemytarget].stats.lvl
                        if displayingScene.theScene[lineOfScene] == "MatchPlayer":
                            $ goToLevel = player.stats.lvl
                        elif displayingScene.theScene[lineOfScene] == "GoUpByProgress":
                            $ goToLevel += ProgressEvent[DataLocation].eventProgress
                        elif displayingScene.theScene[lineOfScene] == "GoUpByProgressFromOtherEvent":
                            $ lineOfScene += 1
                            $ locOfProg = getFromName(displayingScene.theScene[lineOfScene], ProgressEvent)
                            $ goToLevel += ProgressEvent[locOfProg].eventProgress
                        else:
                            $ goToLevel += int(displayingScene.theScene[lineOfScene])

                        if goToLevel > monsterEncounter[CombatFunctionEnemytarget].stats.lvl:
                            $ monsterEncounter[CombatFunctionEnemytarget].levelUp(goToLevel)

                    elif displayingScene.theScene[lineOfScene] == "EnergyDrain":
                        $ lineOfScene += 1
                        $ energyLost = int(displayingScene.theScene[lineOfScene])
                        $ Drain = energyLost * (1+getVirility(player)*0.01)
                        $ Drain *= (renpy.random.randint(75, 125)*0.01)
                        $ Drain = math.floor(Drain)
                        $ Drain = int(Drain)
                        $ player.stats.ep -= Drain
                        $ finalDamage = Drain

                    elif displayingScene.theScene[lineOfScene] == "ApplyStance":
                        if len(monsterEncounter) > 0:
                            $ lineOfScene += 1
                            $ givingStance = displayingScene.theScene[lineOfScene]

                            $ lineOfScene += 1
                            python:
                                try:
                                    if displayingScene.theScene[lineOfScene] == "SetAttack":
                                         lineOfScene += 1
                                         lastAttack = SkillsDatabase[getFromName(displayingScene.theScene[lineOfScene], SkillsDatabase)]
                                    else:
                                        lineOfScene -= 1
                                except:
                                    lineOfScene -= 1

                            $ monsterEncounter[CombatFunctionEnemytarget].giveStance(givingStance, player, lastAttack, holdoverDura=stanceDurabilityHoldOverAttacker)
                            $ player.giveStance(givingStance, monsterEncounter[CombatFunctionEnemytarget], lastAttack, holdoverDura=stanceDurabilityHoldOverTarget)

                    elif displayingScene.theScene[lineOfScene] == "ApplyStanceToOtherMonster":
                        if len(monsterEncounter) > 0:
                            $ lineOfScene += 1
                            $ monName = displayingScene.theScene[lineOfScene]
                            $ lineOfScene += 1
                            $ givingStance = displayingScene.theScene[lineOfScene]

                            $ stancePass = 0
                            $ found = -1
                            $ C = 0
                            python:
                                for each in trueMonsterEncounter:
                                    stancePass = 0
                                    if C != CombatFunctionEnemytarget:
                                        if each.name == monName:
                                            for stance in monsterEncounter[C].combatStance:
                                                if stance.Stance == givingStance:
                                                    stancePass = 2
                                            if stancePass != 2:
                                                stancePass = 1
                                                found = copy.deepcopy(C)
                                    C += 1
                            if found != -1:
                                $ lineOfScene += 1
                                python:
                                    try:
                                        if displayingScene.theScene[lineOfScene] == "SetAttack":
                                             lineOfScene += 1
                                             lastAttack = SkillsDatabase[getFromName(displayingScene.theScene[lineOfScene], SkillsDatabase)]
                                        else:
                                            lineOfScene -= 1
                                    except:
                                        lineOfScene -= 1

                                $ monsterEncounter[found].giveStance(givingStance, player, lastAttack, holdoverDura=stanceDurabilityHoldOverAttacker)
                                $ player.giveStance(givingStance, monsterEncounter[found], lastAttack, holdoverDura=stanceDurabilityHoldOverTarget)
                                $ CombatFunctionEnemytarget = copy.deepcopy(found)

                    elif displayingScene.theScene[lineOfScene] == "EncounterSizeGreaterOrEqualTo":
                        if len(monsterEncounter) > 0:
                            $ lineOfScene += 1
                            if len(monsterEncounter) >= int(displayingScene.theScene[lineOfScene]):
                                $ lineOfScene += 1
                                $ display = displayingScene.theScene[lineOfScene]
                                call sortMenuD from _call_sortMenuD_37
                                return
                            else:
                                $ lineOfScene += 1
                    elif displayingScene.theScene[lineOfScene] == "EncounterSizeLessOrEqualTo":
                        if len(monsterEncounter) > 0:
                            $ lineOfScene += 1
                            if len(monsterEncounter) <= int(displayingScene.theScene[lineOfScene]):
                                $ lineOfScene += 1
                                $ display = displayingScene.theScene[lineOfScene]
                                call sortMenuD from _call_sortMenuD_38
                                return
                            else:
                                $ lineOfScene += 1

                    elif displayingScene.theScene[lineOfScene] == "RecalculateMonsterErosDrop":
                        $ lineOfScene += 1
                        $ eroMod = 1
                        if lineOfScene < len(displayingScene.theScene):
                            if displayingScene.theScene[lineOfScene] == "AlterByPercent":
                                $ lineOfScene += 1
                                $ eroMod = int(displayingScene.theScene[lineOfScene])*0.01
                            else:
                                $ lineOfScene -= 1
                        else:
                            $ lineOfScene -= 1
                        $ lvlchek = monsterEncounter[CombatFunctionEnemytarget].stats.lvl
                        $ monsterEncounter[CombatFunctionEnemytarget].moneyDropped = int(((lvlchek)^2+(lvlchek*10)+48)*eroMod)

                    elif displayingScene.theScene[lineOfScene] == "RecalculateMonsterExpDrop":
                        $ lineOfScene += 1
                        $ expMod = 1
                        if lineOfScene < len(displayingScene.theScene):
                            if displayingScene.theScene[lineOfScene] == "AlterByPercent":
                                $ lineOfScene += 1
                                $ expMod = int(displayingScene.theScene[lineOfScene])*0.01
                            else:
                                $ lineOfScene -= 1
                        else:
                            $ lineOfScene -= 1
                        $ lvlchek = monsterEncounter[CombatFunctionEnemytarget].stats.lvl
                        $ monsterEncounter[CombatFunctionEnemytarget].stats.Exp = int(((0.4*(lvlchek*lvlchek))+(2*lvlchek)+(15*math.sqrt(lvlchek)-8))*expMod)

                    elif displayingScene.theScene[lineOfScene] == "RefreshMonster":
                        $ monsterEncounter[CombatFunctionEnemytarget] = monsterEncounter[CombatFunctionEnemytarget].statusEffects.refresh(monsterEncounter[CombatFunctionEnemytarget])
                        $ monsterEncounter[CombatFunctionEnemytarget].stats.refresh()

                    elif displayingScene.theScene[lineOfScene] == "CallMonsterEncounterOrgasmCheck":
                        $ orgasmTarget = monsterEncounter[CombatFunctionEnemytarget]
                        $ orgasmCauser = player
                        call setDefender(monsterEncounter[CombatFunctionEnemytarget]) from _call_setDefender_2

                        call theOrgasmCheck from _call_theOrgasmCheck_1
                        call MonsterLossCheck from _call_MonsterLossCheck_2

                        if len(monsterEncounter) <= 0:
                            jump combatWin
                    elif displayingScene.theScene[lineOfScene] == "MonsterOrgasm":
                        $ lineOfScene += 1
                        $ monsterEncounter[CombatFunctionEnemytarget].stats.hp = 0
                        $ spiritLost = SpiritCalulation(monsterEncounter[CombatFunctionEnemytarget], int(displayingScene.theScene[lineOfScene]))
                        $ monsterEncounter[CombatFunctionEnemytarget].stats.sp -= spiritLost
                        if monsterEncounter[CombatFunctionEnemytarget].stats.sp <= 0:
                            $ monsterEncounter[CombatFunctionEnemytarget].stats.sp = 0
                        if monsterEncounter[CombatFunctionEnemytarget].stats.sp > monsterEncounter[CombatFunctionEnemytarget].stats.max_true_sp:
                            $ monsterEncounter[CombatFunctionEnemytarget].stats.sp = monsterEncounter[CombatFunctionEnemytarget].stats.max_true_sp
                    elif displayingScene.theScene[lineOfScene] == "ApplyStatusEffectToMonster":
                        $ lineOfScene += 1
                        $ skillAt = getFromName(displayingScene.theScene[lineOfScene], SkillsDatabase)
                        $ statusSkill = SkillsDatabase[skillAt]

                        if statusSkill.statusEffect != "Damage" and statusSkill.statusEffect != "Defence" and statusSkill.statusEffect != "Power" and statusSkill.statusEffect != "Technique" and statusSkill.statusEffect != "Intelligence" and statusSkill.statusEffect != "Willpower" and statusSkill.statusEffect != "Allure" and statusSkill.statusEffect != "Luck" and skillChoice.statusEffect != "%Power" and skillChoice.statusEffect != "%Technique" and skillChoice.statusEffect != "%Intelligence" and skillChoice.statusEffect != "%Willpower" and skillChoice.statusEffect != "%Allure" and skillChoice.statusEffect != "%Luck" and statusSkill.statusEffect != "Escape" and statusSkill.statusEffect != "Crit":
                            $ monsterEncounter[CombatFunctionEnemytarget] = statusAfflict(monsterEncounter[CombatFunctionEnemytarget], statusSkill)
                        else:
                            $ holder = statusBuff(monsterEncounter[CombatFunctionEnemytarget], monsterEncounter[CombatFunctionEnemytarget], statusSkill, 1)
                            $ monsterEncounter[CombatFunctionEnemytarget] = holder[0]
                        if statusSkill.statusEffect == "Restrain":
                            $ monsterEncounter[CombatFunctionEnemytarget].restraintStruggle = copy.deepcopy(statusSkill.restraintStruggle)
                            $ monsterEncounter[CombatFunctionEnemytarget].restraintStruggleCharmed = copy.deepcopy(statusSkill.restraintStruggleCharmed)
                            $ monsterEncounter[CombatFunctionEnemytarget].restraintEscaped = copy.deepcopy(statusSkill.restraintEscaped)
                            $ monsterEncounter[CombatFunctionEnemytarget].restraintEscapedFail = copy.deepcopy(statusSkill.restraintEscapedFail)
                            $ monsterEncounter[CombatFunctionEnemytarget].restrainer = player

                    elif displayingScene.theScene[lineOfScene] == "RefocusOnInitialMonster":
                        $ CombatFunctionEnemytarget = copy.deepcopy(CombatFunctionEnemyInitial)
                    elif displayingScene.theScene[lineOfScene] == "FocusOnMonster":
                        $ lineOfScene += 1
                        if int(displayingScene.theScene[lineOfScene]) <= len(monsterEncounter):
                            $ CombatFunctionEnemytarget = int(displayingScene.theScene[lineOfScene])-1
                        else:
                            $ CombatFunctionEnemytarget = len(monsterEncounter)-1
                    elif displayingScene.theScene[lineOfScene] == "FocusOnRandomMonster":
                        if len(monsterEncounter) >= 1:
                            $ CombatFunctionEnemytarget = renpy.random.randint(0, len(monsterEncounter)-1)
                    elif displayingScene.theScene[lineOfScene] == "FocusedSpeaks":
                        if len(monsterEncounter) >= 1:
                            #$ Speaker = monsterEncounter[CombatFunctionEnemytarget].name + attackTitle

                            $ Speaker = Character(_(monsterEncounter[CombatFunctionEnemytarget].name) + attackTitle,
                                                    what_prefix='"',
                                                    what_suffix='"')
                            $ lineOfScene += 1
                            $ readLine = 1
                    elif displayingScene.theScene[lineOfScene] == "FocusedSpeaksSkill":
                        if len(monsterEncounter) >= 1:
                            #$ Speaker = monsterEncounter[CombatFunctionEnemytarget].name + attackTitle

                            $ Speaker = Character(_(monsterEncounter[CombatFunctionEnemytarget].name) + attackTitle )
                            $ lineOfScene += 1
                            $ readLine = 1
                    elif displayingScene.theScene[lineOfScene] == "CallMonsterAttack":
                        if len(monsterEncounter) > 0:
                            $ specified = 0
                            $ lineOfScene += 1
                            $ m = CombatFunctionEnemytarget
                            python:
                                try:
                                    if displayingScene.theScene[lineOfScene] == "SpecificAttack":
                                         lineOfScene += 1
                                         specified = 1
                                         monSkillChoice[CombatFunctionEnemytarget] = SkillsDatabase[getFromName(displayingScene.theScene[lineOfScene], SkillsDatabase)]
                                    else:
                                        lineOfScene -= 1
                                except:
                                    lineOfScene -= 1

                            $ HoldingSceneCA = copy.deepcopy(displayingScene)
                            $ HoldingLineCA = copy.deepcopy(lineOfScene+1)
                            $ HoldingDataLocCA = copy.deepcopy(DataLocation)

                            if(monsterEncounter[CombatFunctionEnemytarget].statusEffects.stunned.duration > 0):
                                $ display = monsterEncounter[CombatFunctionEnemytarget].name + " is stunned and cannot act!"
                                "[display!i]"
                            else:
                                if specified == 0:
                                    $ pickNewSkill = 1
                                    call enemySkillChoice(mSC=CombatFunctionEnemytarget) from _call_enemySkillChoice_1

                                $ skillcheck = monSkillChoice[CombatFunctionEnemytarget]
                                if player.statusEffects.sleep.potency < 5:
                                    $ Speaker = Character(_(monsterEncounter[CombatFunctionEnemytarget].name + " - " + monSkillChoice[CombatFunctionEnemytarget].name))
                                else:
                                    $ Speaker = Character(_(monsterEncounter[CombatFunctionEnemytarget].name))
                                $ attacker = monsterEncounter[CombatFunctionEnemytarget]
                                $ defender = player
                                $ skillChoice = monSkillChoice[CombatFunctionEnemytarget]
                                call combatActionTurn from _call_combatActionTurn_2
                                #call EnemyTurn from _call_EnemyTurn

                            #$ display = ""
                            $ LastDisplayOrder = []
                            if HoldingSceneCA != Dialogue():
                                $ displayingScene = copy.deepcopy(HoldingSceneCA)
                                $ lineOfScene = copy.deepcopy(HoldingLineCA)
                                $ DataLocation = copy.deepcopy(HoldingDataLocCA)
                            $ HoldingSceneCA = Dialogue()
                            $ HoldingLineCA = 0
                            $ HoldingDataLocCA = 0

                            if len(monsterEncounter) == 0: #combat is over due to recoil
                                jump combatWin

                            jump resumeSceneAfterCombat

                    elif displayingScene.theScene[lineOfScene] == "HitPlayerWith":
                        $ recoil = 0
                        $ lineOfScene += 1
                        $ skillAt = getFromName(displayingScene.theScene[lineOfScene], SkillsDatabase)
                        $ holder = AttackCalc(monsterEncounter[CombatFunctionEnemytarget], player,  SkillsDatabase[skillAt], 1)
                        $ finalDamage = holder[0]
                        $ critText = holder[2]
                        $ effectiveText = holder[5]
                        $ recoil = holder[4]
                        $ recoil =  int(math.floor(recoil))
                        $ monsterEncounter[CombatFunctionEnemytarget].stats.hp += recoil
                        $ player.stats.hp += holder[0]

                    elif displayingScene.theScene[lineOfScene] == "HitMonsterWith":
                        $ lineOfScene += 1
                        $ skillAt = getFromName(displayingScene.theScene[lineOfScene], SkillsDatabase)
                        $ holder = AttackCalc(player, monsterEncounter[CombatFunctionEnemytarget],  SkillsDatabase[skillAt], 1)
                        $ finalDamage = holder[0]
                        $ critText = holder[2]
                        $ effectiveText = holder[5]
                        $ recoil = holder[4]
                        $ recoil =  int(math.floor(recoil))
                        $ player.stats.hp += recoil
                        $ monsterEncounter[CombatFunctionEnemytarget].stats.hp += holder[0]

                    elif displayingScene.theScene[lineOfScene] == "DamageMonsterFromMonster":
                        $ recoil = 0
                        $ lineOfScene += 1
                        $ MonAt = getFromName(displayingScene.theScene[lineOfScene], MonsterDatabase)
                        $ holder = MonsterDatabase[MonAt]
                        $ lineOfScene += 1
                        $ skillAt = getFromName(displayingScene.theScene[lineOfScene], SkillsDatabase)
                        $ holder = AttackCalc(holder, monsterEncounter[CombatFunctionEnemytarget],  SkillsDatabase[skillAt], 1)
                        $ finalDamage = holder[0]
                        if len(monsterEncounter) >= 1:
                            $ critText = holder[2]
                            $ effectiveText = holder[5]
                        #    $ recoil = holder[4]
                        #    $ recoil =  int(math.floor(recoil))
                            #$ monsterEncounter[CombatFunctionEnemytarget].stats.hp += recoil
                        $ monsterEncounter[CombatFunctionEnemytarget].stats.hp += holder[0]
                        $ holder = []

                    elif displayingScene.theScene[lineOfScene] == "DenyPlayerOrgasm":
                        $ skipPlayerOrgasm = 1
                    elif displayingScene.theScene[lineOfScene] == "DenyMonsterOrgasm":
                        $ skipMonsterOrgasm = 1
                    elif displayingScene.theScene[lineOfScene] == "DenyTargetOrgasm":
                        $ skipTargetOrgasm = 1
                    elif displayingScene.theScene[lineOfScene] == "DenyAttackerOrgasm":
                        $ skipAttackOrgasm = 1

                    elif displayingScene.theScene[lineOfScene] == "ResumeMonsterAttack":
                        $ monsterEncounter[CombatFunctionEnemytarget].skippingAttack = 0

                    elif displayingScene.theScene[lineOfScene] == "ResumeAllMonsterAttacks":
                        python:
                            for each in monsterEncounter:
                                each.skippingAttack = 0

                    elif displayingScene.theScene[lineOfScene] == "HideMonsterEncounter":
                        if len(monsterEncounter) >= 1:
                            hide screen ON_EnemyCardScreen onlayer master
                            $ hidingCombatEncounter = 1

                    elif displayingScene.theScene[lineOfScene] == "DefeatMonster":

                        if monsterEncounter[CombatFunctionEnemytarget].restraintOnLoss[0] != "":
                            $ restrainholdyLine = copy.deepcopy(lineOfScene)
                            $ restrainholdyScene= copy.deepcopy(displayingScene)
                            $ restrainholdyData = copy.deepcopy(DataLocation)

                            $ display = monsterEncounter[CombatFunctionEnemytarget].restraintOnLoss[renpy.random.randint(-1, len(monsterEncounter[CombatFunctionEnemytarget].restraintOnLoss)-1)]
                            call read from _call_read_41

                            $ lineOfScene = copy.deepcopy(restrainholdyLine)
                            $ displayingScene = copy.deepcopy(restrainholdyScene)
                            $ DataLocation = copy.deepcopy(restrainholdyData)

                        $ DefeatMonster(CombatFunctionEnemytarget)

                        if len(monsterEncounter) <=0:
                            call combatWin from _call_combatWin
                    else:
                        $ noCombatFunction = 1
                else:
                    $ noCombatFunction = 1
            else:
                $ noCombatFunction = 1


        #End of functions

        $ notFunction = 0
        if noCombatFunction == 1 and noDFunction == 1 and noSpecificFuntion != 2:
            $ notFunction = 1

        if dialogueLineForSure == 1 or noSpecificFuntion == 1:
            $ notFunction = 1
        $ dialogueLineForSure = 0
        $ noSpecificFuntion = 0

        if notFunction == 1:
            $ Speaker = Character(_(''))
            $ readLine = 1

        python:
            try:
                displayingScene.theScene
            except:
                displayingScene = Dialogue()

        #if onGridMap == 1:
        #    jump displayTileMap

        if lineOfScene < len(displayingScene.theScene):
            if displayingScene.theScene[lineOfScene] == "SwapLineIf":
                $ lineOfScene += 1
                $ checking = displayingScene.theScene[lineOfScene]
                #Virility, Progress, Choice, OtherEventsProgress, OtherEventsChoice
                $ linefound = 0
                if checking == "Stat":
                    while displayingScene.theScene[lineOfScene] != "EndLoop":
                        $ lineOfScene += 1
                        if displayingScene.theScene[lineOfScene] != "EndLoop":
                            $ statToCheck = player.stats.getStat(displayingScene.theScene[lineOfScene])
                            $ lineOfScene += 1

                            if statToCheck >= int(displayingScene.theScene[lineOfScene]) and linefound == 0:
                                $ linefound = 1
                                $ lineOfScene += 1
                                $ display = displayingScene.theScene[lineOfScene]
                            else:
                                $ lineOfScene += 1
                elif checking == "Level":
                    while displayingScene.theScene[lineOfScene] != "EndLoop":
                        $ lineOfScene += 1
                        if displayingScene.theScene[lineOfScene] != "EndLoop":
                            if player.stats.lvl >= int(displayingScene.theScene[lineOfScene]) and linefound == 0:
                                $ linefound = 1
                                $ lineOfScene += 1
                                $ display = displayingScene.theScene[lineOfScene]
                            else:
                                $ lineOfScene += 1
                elif checking == "Arousal":
                    while displayingScene.theScene[lineOfScene] != "EndLoop":
                        $ lineOfScene += 1
                        if displayingScene.theScene[lineOfScene] != "EndLoop":
                            if player.stats.hp >= int(displayingScene.theScene[lineOfScene]) and linefound == 0:
                                $ linefound = 1
                                $ lineOfScene += 1
                                $ display = displayingScene.theScene[lineOfScene]
                            else:
                                $ lineOfScene += 1
                elif checking == "MaxArousal":
                    while displayingScene.theScene[lineOfScene] != "EndLoop":
                        $ lineOfScene += 1
                        if displayingScene.theScene[lineOfScene] != "EndLoop":
                            if player.stats.max_true_hp >= int(displayingScene.theScene[lineOfScene]) and linefound == 0:
                                $ linefound = 1
                                $ lineOfScene += 1
                                $ display = displayingScene.theScene[lineOfScene]
                            else:
                                $ lineOfScene += 1
                elif checking == "Energy":
                    while displayingScene.theScene[lineOfScene] != "EndLoop":
                        $ lineOfScene += 1
                        if displayingScene.theScene[lineOfScene] != "EndLoop":
                            if player.stats.ep >= int(displayingScene.theScene[lineOfScene]) and linefound == 0:
                                $ linefound = 1
                                $ lineOfScene += 1
                                $ display = displayingScene.theScene[lineOfScene]
                            else:
                                $ lineOfScene += 1
                elif checking == "MaxEnergy":
                    while displayingScene.theScene[lineOfScene] != "EndLoop":
                        $ lineOfScene += 1
                        if displayingScene.theScene[lineOfScene] != "EndLoop":
                            if player.stats.max_true_ep >= int(displayingScene.theScene[lineOfScene]) and linefound == 0:
                                $ linefound = 1
                                $ lineOfScene += 1
                                $ display = displayingScene.theScene[lineOfScene]
                            else:
                                $ lineOfScene += 1
                elif checking == "Virility":
                    while displayingScene.theScene[lineOfScene] != "EndLoop":
                        $ lineOfScene += 1
                        if displayingScene.theScene[lineOfScene] != "EndLoop":
                            if getVirility(player) >= int(displayingScene.theScene[lineOfScene]) and linefound == 0:
                                $ linefound = 1
                                $ lineOfScene += 1
                                $ display = displayingScene.theScene[lineOfScene]
                            else:
                                $ lineOfScene += 1
                elif checking == "HasFetish":
                    while displayingScene.theScene[lineOfScene] != "EndLoop":
                        $ lineOfScene += 1
                        if displayingScene.theScene[lineOfScene] != "EndLoop":
                            if player.getFetish(displayingScene.theScene[lineOfScene]) >= 25 and linefound == 0:
                                $ linefound = 1
                                $ lineOfScene += 1
                                $ display = displayingScene.theScene[lineOfScene]
                            else:
                                $ lineOfScene += 1
                elif checking == "HasFetishLevelEqualOrGreater":
                    $ lineOfScene += 1
                    $ fetchFetish = displayingScene.theScene[lineOfScene]
                    while displayingScene.theScene[lineOfScene] != "EndLoop":
                        $ lineOfScene += 1
                        if displayingScene.theScene[lineOfScene] != "EndLoop" and linefound == 0:
                            $ fetishLvl = int(displayingScene.theScene[lineOfScene])

                            if player.getFetish(fetchFetish) >= fetishLvl:
                                $ linefound = 1
                                $ lineOfScene += 1
                                $ display = displayingScene.theScene[lineOfScene]
                            else:
                                $ lineOfScene += 1
                elif checking == "EncounterSize":
                    while displayingScene.theScene[lineOfScene] != "EndLoop":
                        $ lineOfScene += 1
                        if displayingScene.theScene[lineOfScene] != "EndLoop" and linefound == 0:
                            if len(monsterEncounter) >= int(displayingScene.theScene[lineOfScene]):
                                $ linefound = 1
                                $ lineOfScene += 1
                                $ display = displayingScene.theScene[lineOfScene]
                            else:
                                $ lineOfScene += 1

                elif checking == "Progress":
                    while displayingScene.theScene[lineOfScene] != "EndLoop":
                        $ lineOfScene += 1
                        if displayingScene.theScene[lineOfScene] != "EndLoop":
                            if int(displayingScene.theScene[lineOfScene]) <= ProgressEvent[DataLocation].eventProgress and linefound == 0:
                                $ linefound = 1
                                $ lineOfScene += 1
                                $ display = displayingScene.theScene[lineOfScene]
                            else:
                                $ lineOfScene += 1
                elif checking == "Choice":
                    while displayingScene.theScene[lineOfScene] != "EndLoop":
                        $ lineOfScene += 1
                        if displayingScene.theScene[lineOfScene] != "EndLoop":
                            $ choiceToCheck = int(displayingScene.theScene[lineOfScene])
                            $ lineOfScene += 1
                            $ DataLocation = getFromName(ProgressEvent[DataLocation].name, ProgressEvent)

                            while choiceToCheck-1 >= len(ProgressEvent[DataLocation].choices):
                                $ ProgressEvent[DataLocation].choices.append("")

                            if displayingScene.theScene[lineOfScene] == ProgressEvent[DataLocation].choices[choiceToCheck-1] and linefound == 0:
                                $ linefound = 1
                                $ lineOfScene += 1
                                $ display = displayingScene.theScene[lineOfScene]
                            else:
                                $ lineOfScene += 1
                elif checking == "OtherEventsProgress":
                    $ lineOfScene += 1
                    $ CheckEvent = getFromName(displayingScene.theScene[lineOfScene], ProgressEvent)

                    while displayingScene.theScene[lineOfScene] != "EndLoop":
                        $ lineOfScene += 1
                        if displayingScene.theScene[lineOfScene] != "EndLoop":
                            if int(displayingScene.theScene[lineOfScene]) <= ProgressEvent[CheckEvent].eventProgress and linefound == 0:
                                $ linefound = 1
                                $ lineOfScene += 1
                                $ display = displayingScene.theScene[lineOfScene]
                            else:
                                $ lineOfScene += 1
                elif checking == "OtherEventsChoice":
                    $ lineOfScene += 1
                    $ CheckEvent = getFromName(displayingScene.theScene[lineOfScene], ProgressEvent)
                    while displayingScene.theScene[lineOfScene] != "EndLoop":
                        $ lineOfScene += 1
                        if displayingScene.theScene[lineOfScene] != "EndLoop":
                            $ choiceToCheck = int(displayingScene.theScene[lineOfScene])
                            $ lineOfScene += 1
                            $ CheckEvent = getFromName(ProgressEvent[CheckEvent].name, ProgressEvent)

                            while choiceToCheck-1 >= len(ProgressEvent[CheckEvent].choices):
                                $ ProgressEvent[CheckEvent].choices.append("")

                            if displayingScene.theScene[lineOfScene] == ProgressEvent[CheckEvent].choices[choiceToCheck-1] and linefound == 0:
                                $ linefound = 1
                                $ lineOfScene += 1
                                $ display = displayingScene.theScene[lineOfScene]
                            else:
                                $ lineOfScene += 1
                elif checking == "IfTimeIs":
                    while displayingScene.theScene[lineOfScene] != "EndLoop":
                        $ lineOfScene += 1
                        if displayingScene.theScene[lineOfScene] != "EndLoop":
                            if 1 == IfTime(displayingScene.theScene[lineOfScene]) and linefound == 0:
                                $ linefound = 1
                                $ lineOfScene += 1
                                $ display = displayingScene.theScene[lineOfScene]
                            else:
                                $ lineOfScene += 1


                elif checking == "Eros":
                    while displayingScene.theScene[lineOfScene] != "EndLoop":
                        $ lineOfScene += 1
                        if displayingScene.theScene[lineOfScene] != "EndLoop":
                            if player.inventory.money >= int(displayingScene.theScene[lineOfScene]) and linefound == 0:
                                $ linefound = 1
                                $ lineOfScene += 1
                                $ display = displayingScene.theScene[lineOfScene]
                            else:
                                $ lineOfScene += 1

                elif checking == "Item":
                    while displayingScene.theScene[lineOfScene] != "EndLoop":
                        $ lineOfScene += 1
                        if displayingScene.theScene[lineOfScene] != "EndLoop":
                            $ hasThing = 0
                            python:
                                for item in player.inventory.items:
                                    if item.name == displayingScene.theScene[lineOfScene]:
                                        hasThing = 1

                            if hasThing == 1 and linefound == 0:
                                $ linefound = 1
                                $ lineOfScene += 1
                                $ display = displayingScene.theScene[lineOfScene]
                            else:
                                $ lineOfScene += 1
                elif checking == "Perk":
                    while displayingScene.theScene[lineOfScene] != "EndLoop":
                        $ lineOfScene += 1
                        if displayingScene.theScene[lineOfScene] != "EndLoop":
                            $ hasThing = 0
                            python:
                                for each in player.perks:
                                    if each.name == displayingScene.theScene[lineOfScene]:
                                        hasThing = 1

                            if hasThing == 1 and linefound == 0:
                                $ linefound = 1
                                $ lineOfScene += 1
                                $ display = displayingScene.theScene[lineOfScene]
                            else:
                                $ lineOfScene += 1

                            $ hasThing = 0
                elif checking == "Random":
                    $ lineOfScene += 1
                    $ linefound = 1
                    $ randomSelection = []

                    while displayingScene.theScene[lineOfScene] != "EndLoop":
                        $ randomSelection.append(displayingScene.theScene[lineOfScene])
                        $ lineOfScene += 1

                    $ renpy.random.shuffle(randomSelection)
                    $ display = randomSelection[0]

                if linefound == 1:
                    $ readLine = 3
                else:
                    $ readLine = 3
                    $ display = displayingScene.theScene[lineOfScene-1]

                if display == "":
                    $ readLine = 0



        if RanAway == "True" and runAndStayInEvent == 0:
            $ RanAway = "False"
            return

        $ player.stats.BarMinMax()

        if callNextJump == 2:
            $ callNextJump = 1
        else:
            $ callNextJump = 0


        python:
            try:
                if lineOfScene < len(displayingScene.theScene) and readLine == 1:
                    readLine = 2
            except:
                readLine = -10

        if readLine == -10:
            return


        if readLine >= 2 and lineOfScene < len(displayingScene.theScene):
            if readLine == 2 :
                $ display = displayingScene.theScene[lineOfScene]

            $ LastSpeaker = Speaker
            $ LastLine = copy.deepcopy(display)
            if displayingScene.theScene[lineOfScene] != "StartCombat" and display != "EndLoop":
                call read from _call_read_11

        $ lineOfScene += 1




    if len(monsterEncounter) > 0:
        return

    if itemEvent == 1:
        return

    if onGridMap == 2:
        return
    if onGridMap == 3 and dontJumpOutOfGridEvents == 0:
        jump postGridEvent

    if HoldingLine != -1 and len(DialogueTypeHolderArray) == 0:
        $ SceneBookMarkRead = 1
        jump displayScene

    if SceneBookMarkRead == 2:
        $ SceneBookMarkRead = 0
        $ DialogueIsFrom = "Event"
        call PostCombatWin from _call_PostCombatWin


    $ displayingScene = Dialogue()

    if len(explorationDeck) >= deckProgress and len(monsterEncounter) == 0  and runAndStayInEvent == 1 and TimeAdvancedCheckArray[-1] == 0:
        $ runAndStayInEvent = 0
        $ DialogueIsFrom = "Event"
        jump PostCombatWin


    return

label sortMenuD:
    #if TimeAdvancedCheck == 1:
        #$ DialogueIsFrom = "NPC"
        #$ isEventNow = 0
    if callNextJump == 1:
        call playSceneJump from _call_playSceneJump
        if len(monsterEncounter) > 0:
            $ lineOfScene += 1
            jump resumeSceneAfterCombat
        return


    if EventDatabase[EventConsisterTarget].name != EventConsister and EventConsister != "": # This is intended to fix incorrect event adresses
        $ DataLocation = getFromName(EventConsister, EventDatabase)

    $ EventConsister = copy.deepcopy(EventDatabase[DataLocation].name)
    $ EventConsisterTarget = copy.deepcopy(DataLocation)



    if callNextJump == 99:
        $ callNextJump = 0
        $ inCalledSceneJump = 1
        $ specifyCurrentChoice = 0
        $ specifyCurrentChoice = getFromNameOfScene(display, EventDatabase[DataLocation].theEvents)

        $ showingDream = []
        $ showingDream.append(copy.deepcopy(EventDatabase[DataLocation]))
        call TimeEvent(CardType="Any", LoopedList=showingDream) from _call_TimeEvent_10
        #$ specifyCurrentChoice = 0

        if callLoopTei != []:
            $ del callLoopTei[-1]
            $ lineOfScene += 1
            $ isEventNow = 0
            jump resumeSceneAfterCombat
        else:
            return



    call postSpecialEffectsCall(VisualEffect, 1) from _call_postSpecialEffectsCall
    call postSpecialEffectsCall(VisualEffect2, 2) from _call_postSpecialEffectsCall_1
    call postSpecialEffectsCall(VisualEffect3, 3) from _call_postSpecialEffectsCall_2

    #if DialogueIsFrom == "NPC":
    #    call npcDialogueMenu from _call_npcDialogueMenu
    #elif DialogueIsFrom == "Monster" or DialogueIsFrom == "LossEvent":
    #    call combatDialogueMenu from _call_combatDialogueMenu
    #elif DialogueIsFrom == "Event":
    #    if InIntro == 0:
        #    call eventDialogueMenu from _call_eventDialogueMenu
        #else:
            #call InIntroDialogueMenu from _call_InIntroDialogueMenu

    if DialogueIsFrom == "Monster":
        if VicChosenScene == -5:
            $ currentChoice = getFromNameOfScene(display, theLastAttacker.lossScenes)
            if currentChoice != -1:
                $ displayingScene = theLastAttacker.lossScenes[currentChoice]
            else:
                $ currentChoice = getFromNameOfScene(display, theLastAttacker.victoryScenes)
                $ displayingScene = theLastAttacker.victoryScenes[currentChoice]
            $ actorNames[0] =  theLastAttacker.name
        else:
            $ currentChoice = getFromNameOfScene(display, DefeatedEncounterMonsters[-1].victoryScenes)
            if currentChoice != -1:
                $ displayingScene = DefeatedEncounterMonsters[-1].victoryScenes[currentChoice]
            else:
                $ currentChoice = getFromNameOfScene(display, DefeatedEncounterMonsters[-1].lossScenes)
                $ displayingScene = DefeatedEncounterMonsters[-1].lossScenes[currentChoice]
            $ actorNames[0] =  DefeatedEncounterMonsters[-1].name
    else:
        if isEventNow == 0:
            $ currentChoice = getFromNameOfScene(display, EventDatabase[DataLocation].theEvents)
        else:
            $ isEventNow = 0

        $ displayingScene = EventDatabase[DataLocation].theEvents[currentChoice]

        $ characterDataLocation = getFromName(EventDatabase[DataLocation].Speakers[0].name, MonsterDatabase)
        $ actorNames[0] = MonsterDatabase[characterDataLocation].name + EventDatabase[DataLocation].Speakers[0].postName
        if EventDatabase[DataLocation].Speakers[0].SpeakerType == "?":
            $ actorNames[0] = EventDatabase[DataLocation].Speakers[0].name


    #$ DialogueIsFrom = "Event"
    #$ DialogueIsFrom = "NPC"

    call displayScene from _call_displayScene_1


    if itemEvent == 1:
        return

    if len(TimeAdvancedCheckArray) > 0 and len(monsterEncounter) == 0 and dontJumpOutOfGridEvents == 0:
        if TimeAdvancedCheckArray[-1] == 1:
            jump postTimeAdvancedEvent

    if EnteringLocationCheck == 1 and len(monsterEncounter) == 0 :
        jump postEntryEvent

    if len(monsterEncounter) > 0 or LostGameOver == -1:
        $ LostGameOver = 0
        return

    if TimeAdvancedCheckArray[-1] == 1:
        return



    if InIntro == 1:
        return



    if DialogueIsFrom == "Event":
        jump postAdventureEvent


label TownLocation:
    $ LastLine = ""
    $ index = 0
    $ SceneCharacters = []

    $ timeNotify = 0
    call advanceTime(TimeIncrease=0) from _call_advanceTime_9

    label getNPCPage:
        $ i = index
        $ LocationCurrentList = []

        $ npcCount = 0
        $ displayTown1 = ""
        $ displayTown2 = ""
        $ displayTown3 = ""
        $ displayTown4 = ""
        $ displayTown5 = ""


    python:
        for each in LocationList:
            if each.CardType == currentLocation and each.description != "EnterArea":
                hasReq = 0
                hasReq = requiresCheck(each.requires, each.requiresEvent, player, ProgressEvent)

                if hasReq >= len(each.requires) + len(each.requiresEvent):
                    LocationCurrentList.append(copy.deepcopy(each))
                    npcCount += 1

        while i < len(LocationCurrentList):
            if i < len(LocationCurrentList):
                display = LocationCurrentList[i].name

                if displayTown1 == "":
                    displayTown1 = LocationCurrentList[i].name
                elif displayTown2 == "":
                    displayTown2  = LocationCurrentList[i].name
                elif displayTown3 == "":
                    displayTown3  = LocationCurrentList[i].name
                elif displayTown4 == "":
                    displayTown4 = LocationCurrentList[i].name
                elif displayTown5 == "":
                    displayTown5 = LocationCurrentList[i].name
                i += 1

    if currentLocation == "Guild":
        $ locationDescrip = "You stand in the small guildhall, and you can see Elena standing attentively behind the front desk.  Multiple stylistic engravings decorate the stone walls, and a few wooden chairs and tables are haphazardly scattered across the floor with most seats left unoccupied. Elly sits alone in the corner reading a book."
    elif currentLocation == "Inn":
        $ locationDescrip = "You stand in the elegantly decorated entryway of the inn. Vivian stands in the center of the room behind a fancy podium, at the perfect height to show off her ample cleavage while still allowing for business transactions to occur on it. Directly behind Vivian are stairs to the bedrooms, and to your right a set of large double doors lead off to the bar and brothel."
    elif currentLocation == "Church":
        $ locationDescrip = "The church is rather spacious for how small it is, with pews lining the sides and a well kept white carpet going down the center aisle leading to a stone statue of the Goddess Venereae. The only person who never seems to leave is the cleric girl, while others drift in and out to offer prayers or give small donations."
    elif currentLocation == "Shopping":
        $ locationDescrip = "You stand in the rustic looking adventuring store in the market district of town. The walls and shelves are lined with all different kinds of gear an adventurer in Lucidia could use, ranging from potions, runes and magical artifacts, to just straight up sex toys."
    elif currentLocation == "Bed":
        $ DialogueIsFrom = "NPC"
        $ isEventNow = 1
        $ currentChoice = 0
        $ npcCount = 0
        $ DataLocation = getFromName("Go to your room.", EventDatabase)
        $ EventConsister = ""
        $ currentLocation = "Inn"
        call sortMenuD from _call_sortMenuD_103


    if npcCount > 5:
        show screen NPCPageButtons
    else:
        hide screen NPCPageButtons
    window hide
    $ LastLine = locationDescrip
    #show screen fakeTextBox

    menu LocationList:
        "[locationDescrip]"
        "[displayTown1]" if displayTown1 != "":
            hide screen FetPageButtons
            #hide screen fakeTextBox
            $ DialogueIsFrom = "NPC"
            $ isEventNow = 1
            $ currentChoice = 0
            $ npcCount = 0
            $ DataLocation = getFromName(displayTown1, EventDatabase)
            $ EventConsister = ""
            call sortMenuD from _call_sortMenuD_76
        "[displayTown2]" if displayTown2 != "":
            hide screen FetPageButtons
            #hide screen fakeTextBox
            $ DialogueIsFrom = "NPC"
            $ isEventNow = 1
            $ currentChoice = 0
            $ npcCount = 0
            $ DataLocation = getFromName(displayTown2, EventDatabase)
            $ EventConsister = ""
            call sortMenuD from _call_sortMenuD_77
        "[displayTown3]" if displayTown3 != "":
            hide screen FetPageButtons
            hide screen fakeTextBox
            $ DialogueIsFrom = "NPC"
            $ isEventNow = 1
            $ currentChoice = 0
            $ npcCount = 0
            $ DataLocation = getFromName(displayTown3, EventDatabase)
            $ EventConsister = ""
            call sortMenuD from _call_sortMenuD_78
        "[displayTown4]" if displayTown4 != "":
            hide screen FetPageButtons
            #hide screen fakeTextBox
            $ DialogueIsFrom = "NPC"
            $ isEventNow = 1
            $ currentChoice = 0
            $ npcCount = 0
            $ DataLocation = getFromName(displayTown4, EventDatabase)
            $ EventConsister = ""
            call sortMenuD from _call_sortMenuD_79
        "[displayTown5]" if displayTown5 != "":
            hide screen FetPageButtons
            #hide screen fakeTextBox
            $ DialogueIsFrom = "NPC"
            $ isEventNow = 1
            $ currentChoice = 0
            $ npcCount = 0
            $ DataLocation = getFromName(displayTown5, EventDatabase)
            $ EventConsister = ""
            call sortMenuD from _call_sortMenuD_83
        "Leave.":
            hide screen FetPageButtons
            #hide screen fakeTextBox
            jump LeaveBuilding
    jump TownLocation

label nextNPCPage:
    $ index += 5
    if index >  npcCount:
        $ index = 0
    jump getNPCPage

label lastNPCPage:
    $ index -= 5
    if index < 0:
        $ index = 0

        $ index = npcCount/5
        $ index = math.floor(index)
        $ index = index*5
        $ index = math.floor(index)
        #$ b =  fetCount - index
        #$ index = index + b
        $ index = int(index)

    jump getNPCPage


label nextMenuPage:
    $ index += MaxMenuSlots

    if index >=  len(menuArray):
        $ index = 0

    jump recheckMenu

label lastMenuPage:

    $ indent = MaxMenuSlots
    $ index -= indent
    if index < 0:
        $ index = 0

        while index < len(menuArray):
            $ index += indent
        $ index -= indent
    #    $ index = len(menuArray)/indent
        $ index = math.floor(index)
        #$ index = index*indent
        $ index = math.floor(index)
        #$ b =  fetCount - index
        #$ index = index + b
        $ index = int(index)


    jump recheckMenu



label EnterTownLocation:
    $ LastLine = ""

    $ SceneCharacters = []
    $ EnteringLocationCheck = 1
    $ etl = 0

    while etl < len(LocationList):
        $ Speaker = Character(_(''))
        $ hasReq = 0

        if LocationList[etl].CardType == currentLocation and LocationList[etl].description == "EnterArea":
            $ DialogueIsFrom = "NPC"
            $ isEventNow = 1
            $ currentChoice = 0
            $ DataLocation = getFromName(LocationList[etl].name, EventDatabase)
            call sortMenuD from _call_sortMenuD_80
        label postEntryEvent:
            $ etl += 1
    $ Speaker = Character(_(''))
    $ EnteringLocationCheck = 0
    jump TownLocation
