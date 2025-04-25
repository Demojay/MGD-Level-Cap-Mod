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

    JsonFuncRegistry = {
    # If funcs
    "IfChoice": ["JsonFuncIfChoice"],
    "IfProgressEqualsOrGreater": ["JsonFuncIfProgressEqualsOrGreater"],
        "IfProgressEquals": ["JsonFuncIfProgressEquals"],
        "IfProgressEqualsOrLess": ["JsonFuncIfProgressEqualsOrLess"],
        "IfEventsProgressEqualsOrLessThanOtherEventsProgress": ["JsonFuncIfEventsProgressEqualsOrLessThanOtherEventsProgress"],
    "IfEventExists": ["JsonFuncIfEventExists"],
    "IfRanAway": ["JsonFuncIfRanAway"],
    "IfHealingSickness": ["JsonFuncIfHealingSickness"],
    "IfDelayingNotifications": ["JsonFuncIfDelayingNotifications"],
    "IfPlayerOrgasm": ["JsonFuncIfPlayerOrgasm"],
        "IfPlayerArousalOverPercentOfMax": ["JsonFuncIfPlayerArousalOverPercentOfMax"],
        "IfPlayerEnergyLessThanPercent": ["JsonFuncIfPlayerEnergyLessThanPercent"],
        "IfPlayerEnergyGone": ["JsonFuncIfPlayerEnergyGone"],
        "IfPlayerSpiritGone": ["JsonFuncIfPlayerSpiritGone"],
    "IfHasItem": ["JsonFuncIfHasItem", "IfHasItem"],
        "IfDoesntHaveItem": ["JsonFuncIfHasItem", "IfDoesntHaveItem"],
        "IfHasItemEquipped": ["JsonFuncIfHasItem", "IfHasItemEquipped"],
        "IfDoesntHaveItemEquipped": ["JsonFuncIfHasItem", "IfDoesntHaveItemEquipped"],
    "IfHasItems": ["JsonFuncIfHasItems", "IfHasItems"],
        "IfDoesntHaveItems": ["JsonFuncIfHasItems", "IfDoesntHaveItems"],
    "IfHasItemInInventory": ["JsonFuncIfHasItemInInventory", "IfHasItemInInventory"],
        "IfDoesntHaveItemInInventory": ["JsonFuncIfHasItemInInventory", "IfDoesntHaveItemInInventory"],
    "IfHasRunesEquipped": ["JsonFuncIfHasRunesEquipped"],
    "IfHasSkill": ["JsonFuncIfHasSkill"],
        "IfHasSkills": ["JsonFuncIfHasSkills"],
        "IfPlayerIsUsingThisSkill": ["JsonFuncIfPlayerIsUsingThisSkill"],
    "IfHasPerk": ["JsonFuncIfHasPerk"],
    "IfSensitivityEqualOrGreater": ["JsonFuncIfSensitivityEqualOrGreater"],
    "IfHasFetish": ["JsonFuncIfHasFetish"],
        "IfFetishLevelEqualOrGreater": ["JsonFuncIfFetishLevelEqualOrGreater"],
    "IfInExploration": ["JsonFuncIfInExploration"],
    "IfGridPlayerStunned": ["JsonFuncIfGridPlayerStunned"],
        "IfGridNPCSeesPlayer": ["JsonFuncIfGridNPCSeesPlayer"],
        "IfGridNPCThere": ["JsonFuncIfGridNPCThere"],
        "IfGridVisonOn": ["JsonFuncIfGridVisonOn"],
    "IfPlayerHasStatusEffect": ["JsonFuncIfPlayerHasStatusEffect", "IfPlayerHasStatusEffect"],
        "IfPlayerDoesntHaveStatusEffect": ["JsonFuncIfPlayerHasStatusEffect", "IfPlayerDoesntHaveStatusEffect"],
        "IfPlayerStunnedByParalysis": ["JsonFuncIfPlayerStunnedByParalysis"],
        "IfPlayerHasStatusEffectWithPotencyEqualOrGreater": ["JsonFuncIfPlayerHasStatusEffectWithPotencyEqualOrGreater"],
    "IfPlayerLevelGreaterThan": ["JsonFuncIfPlayerLevelGreaterThan"],
    "IfAttackCrits": ["JsonFuncIfAttackCrits"],
    "IfTimeIs": ["JsonFuncIfTimeIs"],
    "IfDifficultyIs": ["JsonFuncIfDifficultyIs"],
    "IfInputEquals": ["JsonFuncIfInputEquals"],
        "IfInputEqualsOrLessThan": ["JsonFuncIfInputEqualsOrLessThan"],
        "InputProgress": ["JsonFuncInputProgress"],
    "IfPlayerHasStance": ["JsonFuncIfPlayerHasStance"],
        "IfPlayerHasStances": ["JsonFuncIfPlayerHasStances"],
        "IfPlayerDoesntHaveStance": ["JsonFuncIfPlayerDoesntHaveStance"],
    "IfMonsterHasStance": ["JsonFuncIfMonsterHasStance"],
        "IfMonsterDoesntHaveStance": ["JsonFuncIfMonsterDoesntHaveStance"],
        "IfOtherMonsterHasStance": ["JsonFuncIfOtherMonsterHasStance"],
        "IfOtherMonsterDoesntHaveStance": ["JsonFuncIfOtherMonsterDoesntHaveStance"],
        "IfThisMonsterIsInEncounter": ["JsonFuncIfThisMonsterIsInEncounter"],
    "IfMonsterHasStatusEffect": ["JsonFuncIfMonsterHasStatusEffect", "IfMonsterHasStatusEffect"],
        "IfMonsterDoesntHaveStatusEffect": ["JsonFuncIfMonsterHasStatusEffect", "IfMonsterDoesntHaveStatusEffect"],
    "IfMonsterLevelGreaterThan": ["JsonFuncIfMonsterLevelGreaterThan"],
        "IfMonsterHasStatusEffectWithPotencyEqualOrGreater": ["JsonFuncIfMonsterHasStatusEffectWithPotencyEqualOrGreater"],
    "IfOtherMonsterHasStatusEffect": ["JsonFuncIfOtherMonsterHasStatusEffect", "IfOtherMonsterHasStatusEffect"],
        "IfOtherMonsterDoesntHaveStatusEffect": ["JsonFuncIfOtherMonsterHasStatusEffect", "IfOtherMonsterDoesntHaveStatusEffect"],
    "IfMonsterOrgasm": ["JsonFuncIfMonsterOrgasm"],
        "IfMonsterArousalGreaterThan": ["JsonFuncIfMonsterArousalGreaterThan"],
        "IfMonsterEnergyGone": ["JsonFuncIfMonsterEnergyGone"],
        "IfMonsterSpiritGone": ["JsonFuncIfMonsterSpiritGone"],
        "IfMonsterHasSkill": ["JsonFuncIfMonsterHasSkill"],
        "IfMonsterHasPerk": ["JsonFuncIfMonsterHasPerk"],
    # Give funcs
    "GiveTreasure": ["JsonFuncGiveTreasure"],
        "GiveExp": ["JsonFuncGiveExp"],
    "GiveItem": ["JsonFuncGiveItem"],
        "GiveItemQuietly": ["JsonFuncGiveItemQuietly"],
    "GiveSkill": ["JsonFuncGiveSkill"],
        "GiveSkillQuietly": ["JsonFuncGiveSkillQuietly"],
    "GivePerkPoint": ["JsonFuncGivePerkPoint"],
        "GivePerk": ["JsonFuncGivePerk"],
        "GivePerkQuietly": ["JsonFuncGivePerkQuietly"],
    "GiveSkillToMonster": ["JsonFuncGiveSkillToMonster"],
        "GivePerkToMonster": ["JsonFuncGivePerkToMonster"],
    "GiveSkillThatWasTemporarilyRemoved": ["JsonFuncGiveSkillThatWasTemporarilyRemoved"],
    # Remove funcs
    "RemoveStatusEffect": ["JsonFuncRemoveStatusEffect"],
    "RemovePerk": ["JsonFuncRemovePerk"],
        "RemovePerkQuietly": ["JsonFuncRemovePerkQuietly"],
    "RemoveInputFromPlayerEros": ["JsonFuncRemoveInputFromPlayerEros"],
        "RemoveInputFromProgress": ["JsonFuncRemoveInputFromProgress"],
        "RemoveProgressFromEros": ["JsonFuncRemoveProgressFromEros"],
    "RemoveSkillFromPlayer": ["JsonFuncRemoveSkillFromPlayer"],
        "RemoveSkillFromPlayerQuietly": ["JsonFuncRemoveSkillFromPlayerQuietly"],
        "RemoveSkillFromPlayerTemporarily": ["JsonFuncRemoveSkillFromPlayerTemporarily"],
    "RemoveGridNPC": ["JsonFuncRemoveGridNPC"],
    "RemoveSkillFromMonster": ["JsonFuncRemoveSkillFromMonster"],
        "RemoveMonster": ["JsonFuncRemoveMonster"],
        "RemoveStatusEffectFromMonster": ["JsonFuncRemoveStatusEffectFromMonster"],
        "RemovePerkFromMonster": ["JsonFuncRemovePerkFromMonster"],
    # Play funcs
    "PlayerSpeaks": ["JsonFuncPlayerSpeaks"],
        "PlayerSpeaksSkill": ["JsonFuncPlayerSpeaksSkill"],
    "PlayerCurrentEnergyCost": ["JsonFuncPlayerCurrentEnergyCost"],
    "PlayerOrgasm": ["JsonFuncPlayerOrgasm"],
        "PlayerOrgasmNoSpiritLoss": ["JsonFuncPlayerOrgasmNoSpiritLoss"],
    "PlayerStep": ["JsonFuncPlayerStep"],
    "PlayStoredBGM": ["JsonFuncPlayStoredBGM"],
        "PlayThisSongAfterCombat": ["JsonFuncPlayThisSongAfterCombat"],
    "PlaySoundEffect": ["JsonFuncPlaySoundEffect"],
        "PlaySoundEffect2": ["JsonFuncPlaySoundEffect2"],
    "PlaySoundBankOnce": ["JsonFuncPlaySoundBankOnce"],
    "PlayLoopingSoundEffect": ["JsonFuncPlayLoopingSoundEffect"],
        "PlayLoopingSoundEffect2": ["JsonFuncPlayLoopingSoundEffect2"],
    "PlayVisualEffect": ["JsonFuncPlayVisualEffect"],
        "PlayVisualEffect2": ["JsonFuncPlayVisualEffect2"],
        "PlayVisualEffect3": ["JsonFuncPlayVisualEffect3"],
    "PlayImagePulseLoopingList": ["JsonFuncPlayImagePulseLoopingList"],
        "PlayImagePulseLoopingList2": ["JsonFuncPlayImagePulseLoopingList2"],
    "PlayImagePulseLoopingRandom": ["JsonFuncPlayImagePulseLoopingRandom"],
    "PlayHypnoSpiral": ["JsonFuncPlayHypnoSpiral"],
        "PlayPendulum": ["JsonFuncPlayPendulum"],
        "PlayKiss": ["JsonFuncPlayKiss"],
        "PlayKissingBarrage": ["JsonFuncPlayKissingBarrage"],
        "PlayKissingBarrageOnce": ["JsonFuncPlayKissingBarrageOnce"],
    "PlayCustomBarrage": ["JsonFuncPlayCustomBarrage"],
        "PlayCustomBarrage2": ["JsonFuncPlayCustomBarrage2"],
    "PlayBlackOut": ["JsonFuncPlayBlackOut"],
    "PlayMotionEffect": ["JsonFuncPlayMotionEffect"],
        "PlayMotionEffectLoop": ["JsonFuncPlayMotionEffectLoop"],
        "PlayMotionEffectCustom": ["JsonFuncPlayMotionEffectCustom"],
    "PlayerLosesCombat": ["JsonFuncPlayerLosesCombat"],
    # End funcs
    "EndVisualEffect": ["JsonFuncEndVisualEffect"],
        "EndVisualEffect2": ["JsonFuncEndVisualEffect2"],
        "EndVisualEffect3": ["JsonFuncEndVisualEffect3"],
    "EndImagePulseLoopingList": ["JsonFuncEndImagePulseLoopingList"],
        "EndImagePulseLoopingList2": ["JsonFuncEndImagePulseLoopingList2"],
        "EndImagePulseLoopingRandom": ["JsonFuncEndImagePulseLoopingRandom"],
    "EndHypnoSpiral": ["JsonFuncEndHypnoSpiral"],
        "EndPendulum": ["JsonFuncEndPendulum"],
    "EndKissingBarrage": ["JsonFuncEndKissingBarrage"],
        "EndCustomBarrage": ["JsonFuncEndCustomBarrage"],
        "EndCustomBarrage2": ["JsonFuncEndCustomBarrage2"],
    "EndBlackOut": ["JsonFuncEndBlackOut"],
    "EndAllVisualEffects": ["JsonFuncEndAllVisualEffects"],
        "EndMotionEffect": ["JsonFuncEndMotionEffect"],
    "EndCounterChecks": ["JsonFuncEndCounterChecks"],
    "EndCombat": ["JsonFuncEndCombat"],
    # Set funcs
    "SetFlexibleSpeaker": ["JsonFuncSetFlexibleSpeaker"],
    "SetProgress": ["JsonFuncSetProgress"],
    "SetChoice": ["JsonFuncSetChoice"],
        "SetChoiceToPlayerName": ["JsonFuncSetChoiceToPlayerName"],
        "SetChoiceToPlayerNameFromOtherEvent": ["JsonFuncSetChoiceToPlayerNameFromOtherEvent"],
    "SetArousalToMax": ["JsonFuncSetArousalToMax"],
        "SetArousalToXUnlessHigherThanX": ["JsonFuncSetArousalToXUnlessHigherThanX"],
        "SetArousalToXUnlessHigherThanXThenAddY": ["JsonFuncSetArousalToXUnlessHigherThanXThenAddY"],
    "SetSpirit": ["JsonFuncSetSpirit"],
    "SetFetish": ["JsonFuncSetFetish"],
    "SetPlayerGridPosition": ["JsonFuncSetPlayerGridPosition"],
        "SetActiveGridNPC": ["JsonFuncSetActiveGridNPC"],
    "SetPostName": ["JsonFuncSetPostName"],
    "SetEros": ["JsonFuncSetEros"],
    "SetStoredColor": ["JsonFuncSetStoredColor"],
    # Get funcs
    "GetEventAndSetProgress": ["JsonFuncGetEventAndSetProgress"],
        "GetEventAndChangeProgress": ["JsonFuncGetEventAndChangeProgress"],
    "GetAnEventsProgressThenIfEquals": ["JsonFuncGetAnEventsProgressThenIfEquals"],
        "GetAnEventsProgressThenIfEqualsOrGreater": ["JsonFuncGetAnEventsProgressThenIfEqualsOrGreater"],
        "GetAnEventsProgressThenIfEqualsOrLess": ["JsonFuncGetAnEventsProgressThenIfEqualsOrLess"],
    "GetEventAndIfChoice": ["JsonFuncGetEventAndIfChoice"],
    "GetEventAndSetChoice": ["JsonFuncGetEventAndSetChoice"],
    # GoTo funcs
    "GoToTown": ["JsonFuncGoToTown"],
    "GoToChurch": ["JsonFuncGoToChurch"],
    "GoToRandomBrothelWaiterScene": ["JsonFuncGoToRandomBrothelWaiterScene"],
        "GoToRandomBrothelBarScene": ["JsonFuncGoToRandomBrothelBarScene"],
        "GoToRandomBrothelHoleScene": ["JsonFuncGoToRandomBrothelHoleScene"],
        "GoToRandomBrothelDayScene": ["JsonFuncGoToRandomBrothelDayScene"],
    "GoBackToStoredEvent": ["JsonFuncGoBackToStoredEvent"],
    "GoToMap": ["JsonFuncGoToMap"],
    # 'S' funcs
    "Speak": ["JsonFuncSpeak"],
    "Speaks": ["JsonFuncSpeaks"],
        "Speaks2": ["JsonFuncSpeaks2", 2],"Speaks3": ["JsonFuncSpeaks2", 3],
        "Speaks4": ["JsonFuncSpeaks2", 4],"Speaks5": ["JsonFuncSpeaks2", 5],
        "Speaks6": ["JsonFuncSpeaks2", 6],"Speaks7": ["JsonFuncSpeaks2", 7],
        "Speaks8": ["JsonFuncSpeaks2", 8],"Speaks9": ["JsonFuncSpeaks2", 9],
        "Speaks10": ["JsonFuncSpeaks2", 10],"Speaks11": ["JsonFuncSpeaks2", 11],
        "Speaks12": ["JsonFuncSpeaks2", 12],
    "SpawnGridNPC": ["JsonFuncSpawnGridNPC"],
    "SleepPlayer": ["JsonFuncSleepPlayer"],
    "StatCheck": ["JsonFuncStatCheck", "StatCheck"],
        "StatCheckRollUnder": ["JsonFuncStatCheck", "StatCheckRollUnder"],
    "StatEqualsOrMore": ["JsonFuncStatEqualsOrMore"],
    "StunGridPlayer": ["JsonFuncStunGridPlayer"],
    "StoreCurrentEventSpotSkippingLines": ["JsonFuncStoreCurrentEventSpotSkippingLines"],
        "SaveNextLine": ["JsonFuncSaveNextLine"],
        "StoreCurrentBG": ["JsonFuncStoreCurrentBG"],
    "StopBGM": ["JsonFuncStopBGM"],
        "StopBGMHard": ["JsonFuncStopBGMHard"],
        "StoreCurrentBGM": ["JsonFuncStoreCurrentBGM"],
    "StopSoundEffect": ["JsonFuncStopSoundEffect"],
        "StopSoundEffect2": ["JsonFuncStopSoundEffect2"],
        "StopSoundEffectLoop": ["JsonFuncStopSoundEffectLoop"],
        "StopSoundEffectLoop2": ["JsonFuncStopSoundEffectLoop2"],
    "ShowTreasureChest": ["JsonFuncShowTreasureChest"],
    "SkillShoppingMenu": ["JsonFuncSkillShoppingMenu"],
        "ShoppingMenu": ["JsonFuncShoppingMenu"],
    "SensitivityRestore": ["JsonFuncSensitivityRestore"],
    "SemenHeal": ["JsonFuncSemenHeal"],
    "ShuffleMonsterEncounter": ["JsonFuncShuffleMonsterEncounter"],
    "SkipPlayerAttack": ["JsonFuncSkipPlayerAttack"],
        "SkipMonsterAttack": ["JsonFuncSkipMonsterAttack"],
        "SkipAllMonsterAttacks": ["JsonFuncSkipAllMonsterAttacks"],
    "ShowMonsterEncounter": ["JsonFuncShowMonsterEncounter"],
    # Clear funcs
    "ClearPlayerStatusEffects": ["JsonFuncClearPlayerStatusEffects"],
        "ClearNonPersistentStatusEffects": ["JsonFuncClearNonPersistentStatusEffects"],
    "ClearMonsterSkillList": ["JsonFuncClearMonsterSkillList"],
    "ClearMonsterPerks": ["JsonFuncClearMonsterPerks"],
    "ClearStances": ["JsonFuncClearStances"],
    "ClearStanceFromMonsterAndPlayer": ["JsonFuncClearStanceFromMonsterAndPlayer"],
    "ClearMonsterEncounter": ["JsonFuncClearMonsterEncounter"],
    "ClearMonsterEncounterBossFight": ["JsonFuncClearMonsterEncounterBossFight"],
    "ClearFightForVictory": ["JsonFuncClearFightForVictory"],
    # Change funcs
    "ChangeImageFor": ["JsonFuncChangeImageFor"],
        "ChangeImageLayer": ["JsonFuncChangeImageLayer"],
    "ChangeProgress": ["JsonFuncChangeProgress"],
        "ChangeProgressBasedOnVirility": ["JsonFuncChangeProgressBasedOnVirility"],
    "ChangeArousal": ["JsonFuncChangeArousal", "ChangeArousal"],
        "ChangeArousalQuietly": ["JsonFuncChangeArousal", "ChangeArousalQuietly"],
        "ChangeArousalByPercent": ["JsonFuncChangeArousalByPercent"],
    "ChangeEnergy": ["JsonFuncChangeEnergy", "ChangeEnergy"],
        "ChangeEnergyQuietly": ["JsonFuncChangeEnergy", "ChangeEnergyQuietly"],
        "ChangeEnergyByPercent": ["JsonFuncChangeEnergyByPercent"],
    "ChangeSpirit": ["JsonFuncChangeSpirit", "ChangeSpirit"],
        "ChangeSpiritQuietly": ["JsonFuncChangeSpirit", "ChangeSpiritQuietly"],
    "ChangeMaxArousal": ["JsonFuncChangeMaxArousal"],
        "ChangeMaxEnergy": ["JsonFuncChangeMaxEnergy"],
        "ChangeMaxSpirit": ["JsonFuncChangeMaxSpirit"],
    "ChangePower": ["JsonFuncChangePower"],
        "ChangeWill": ["JsonFuncChangeWill"],
        "ChangeInt": ["JsonFuncChangeInt"],
        "ChangeTech": ["JsonFuncChangeTech"],
        "ChangeAllure": ["JsonFuncChangeAllure"],
        "ChangeLuck": ["JsonFuncChangeLuck"],
    "ChangeSensitivity": ["JsonFuncChangeSensitivity"],
        "ChangeFetish": ["JsonFuncChangeFetish"],
    "ChangeGridNPCMovement": ["JsonFuncChangeGridNPCMovement"],
        "ChangeGridVision": ["JsonFuncChangeGridVision"],
        "ChangeMapTile": ["JsonFuncChangeMapTile"],
    "ChangeNextStatCheckDifficulty": ["JsonFuncChangeNextStatCheckDifficulty"],
    "ChangeBG": ["JsonFuncChangeBG"],
    "ChangeBGM": ["JsonFuncChangeBGM"],
        "ChangeBGM-OverrideCombatMusic": ["JsonFuncChangeBGMOverrideCombatMusic"],
        "ChangeBGM-NoFade": ["JsonFuncChangeBGMNoFade"],
        "ChangeBGM-List": ["JsonFuncChangeBGMList"],
    "ChangeEros": ["JsonFuncChangeEros"],
        "ChangeErosByPercent": ["JsonFuncChangeErosByPercent"],
    "ChangePerkDuration": ["JsonFuncChangePerkDuration"],
    # Change monster funcs
    "ChangeMonsterArousal": ["JsonFuncChangeMonsterArousal"],
        "ChangeMonsterEnergy": ["JsonFuncChangeMonsterEnergy"],
        "ChangeMonsterLevel": ["JsonFuncChangeMonsterLevel"],
        "ChangeMonsterSpirit": ["JsonFuncChangeMonsterSpirit"],
    "ChangeMonsterMaxArousal": ["JsonFuncChangeMonsterMaxArousal"],
        "ChangeMonsterMaxEnergy": ["JsonFuncChangeMonsterMaxEnergy"],
        "ChangeMonsterMaxSpirit": ["JsonFuncChangeMonsterMaxSpirit"],
    "ChangeMonsterPower": ["JsonFuncChangeMonsterPower"],
        "ChangeMonsterWill": ["JsonFuncChangeMonsterWill"],
        "ChangeMonsterInt": ["JsonFuncChangeMonsterInt"],
        "ChangeMonsterTech": ["JsonFuncChangeMonsterTech"],
        "ChangeMonsterAllure": ["JsonFuncChangeMonsterAllure"],
        "ChangeMonsterLuck": ["JsonFuncChangeMonsterLuck"],
    "ChangeMonsterSensitivity": ["JsonFuncChangeMonsterSensitivity"],
    "ChangeMonsterStatusEffectResistances": ["JsonFuncChangeMonsterStatusEffectResistances"],
    "ChangeMonsterFetish": ["JsonFuncChangeMonsterFetish"],
    "ChangeMonsterErosDrop": ["JsonFuncChangeMonsterErosDrop"],
    "ChangeMonsterExpDrop": ["JsonFuncChangeMonsterExpDrop"],
    # The rest just dumped out of Core for now.
    "FlexibleSpeaks": ["JsonFuncFlexibleSpeaks"],
    "DisplayCharacters": ["JsonFuncDisplayCharacters"],
    "AnimateImageLayer": ["JsonFuncAnimateImageLayer"],
    "HideHealth": ["JsonFuncHideHealth"],
    "HoldCurrentVirility": ["JsonFuncHoldCurrentVirility"],
    "HoldCurrentVirilityEnd": ["JsonFuncHoldCurrentVirilityEnd"],
    "EventsProgressEqualsOtherEventsProgress": ["JsonFuncEventsProgressEqualsOtherEventsProgress"],
    "EventsProgressEqualsOrGreaterThanOtherEventsProgress": ["JsonFuncEventsProgressEqualsOrGreaterThanOtherEventsProgress"],
    "VirilityEqualsOrGreater": ["JsonFuncVirilityEqualsOrGreater"],
    "ChoiceToDisplayPlayer": ["JsonFuncChoiceToDisplayPlayer"],
    "ChoiceToDisplayMonster": ["JsonFuncChoiceToDisplayMonster"],
    "ChoiceToDisplayPlayerFromOtherEvent": ["JsonFuncChoiceToDisplayPlayerFromOtherEvent"],
    "ChoiceToDisplayMonsterFromOtherEvent": ["JsonFuncChoiceToDisplayMonsterFromOtherEvent"],
    "HealingSickness": ["JsonFuncHealingSickness"],
    "AdvanceTime": ["JsonFuncAdvanceTime"],
    "RestPlayer": ["JsonFuncRestPlayer"],
    "RefreshPlayer": ["JsonFuncRefreshPlayer"],
    "PermanentlyChangeSensitivity": ["JsonFuncPermanentlyChangeSensitivity"],
    "PermanentChangeStatusEffectResistances": ["JsonFuncPermanentChangeStatusEffectResistances"],
    "PermanentlyChangeFetish": ["JsonFuncPermanentlyChangeFetish"],
    "EmptySpiritCounter": ["JsonFuncEmptySpiritCounter"],
    "RoledCGEnd": ["JsonFuncRoledCGEnd"],
    "Menu": ["JsonFuncMenu"],
    "ApplyStatusEffect": ["JsonFuncApplyStatusEffect"],
    "AllowRunning": ["JsonFuncAllowRunning"],
    "CombatEncounter": ["JsonFuncCombatEncounter"],
    "MiniGameSnake": ["JsonFuncMiniGameSnake"],
    "FishingMiniGame": ["JsonFuncFishingMiniGame"],
    "JumpToScene": ["JsonFuncJumpToScene"],
    "JumpToRandomScene": ["JsonFuncJumpToRandomScene"],
    "JumpToEvent": ["JsonFuncJumpToEvent"],
    "JumpToEventThenScene": ["JsonFuncJumpToEventThenScene"],
    "CallNextSceneJumpThenReturn": ["JsonFuncCallNextSceneJumpThenReturn"],
    "CallSceneThenReturn": ["JsonFuncCallSceneThenReturn"],
    "CallEventAndSceneThenReturn": ["JsonFuncCallEventAndSceneThenReturn"],
    "CallCombatEventAndScene": ["JsonFuncCallCombatEventAndScene"],
    "JumpToNPCEvent": ["JsonFuncJumpToNPCEvent"],
    "JumpToNPCEventThenScene": ["JsonFuncJumpToNPCEventThenScene"],
    "JumpToLossEvent": ["JsonFuncJumpToLossEvent"],
    "ForceAutoSave": ["JsonFuncForceAutoSave"],
    "ExitGridmap": ["JsonFuncExitGridmap"],
    # Combat funcs
    "ResetStatCheckDifficultyModifer": ["JsonFuncResetStatCheckDifficultyModifer"],
    "AddMonsterToEncounter": ["JsonFuncAddMonsterToEncounter"],
    "HideMonsterEncounter": ["JsonFuncHideMonsterEncounter"],
    "DamagePlayerFromMonster": ["JsonFuncDamagePlayerFromMonster"],
    # Assorted funcs
    "TimeBecomesNight": ["JsonFuncTimeBecomesNight"],
    "TimeBecomesDay": ["JsonFuncTimeBecomesDay"],
    "TimeBecomesNormal": ["JsonFuncTimeBecomesNormal"],
    "DisplaySavedLine": ["JsonFuncDisplaySavedLine"],
    "UseSavedLineInMenu": ["JsonFuncUseSavedLineInMenu"],
    "CallLossLevelUp": ["JsonFuncCallLossLevelUp"],
    "UseHeldBG": ["JsonFuncUseHeldBG"],
    "HideTreasureChest": ["JsonFuncHideTreasureChest"],
    "HasErosLessThan": ["JsonFuncHasErosLessThan"],
    "AllowInventory": ["JsonFuncAllowInventory"],
    "DenyInventory": ["JsonFuncDenyInventory"],
    "BumpToTown": ["JsonFuncBumpToTown"],
    "GameOver": ["JsonFuncGameOver"],
    "TrueGameOver": ["JsonFuncTrueGameOver"],
    "QuestComplete": ["JsonFuncQuestComplete"],
    "AdventureComplete": ["JsonFuncAdventureComplete"],
    "HasErosLessThanInput": ["JsonFuncHasErosLessThanInput"],
    "AddInputToProgress": ["JsonFuncAddInputToProgress"],
    "RespecPlayer": ["JsonFuncRespecPlayer"],
    "AdjustPlayerLevel": ["JsonFuncAdjustPlayerLevel"],
    "DonateToGoddess": ["JsonFuncDonateToGoddess"],
    "PurgeFetishes": ["JsonFuncPurgeFetishes"],
    "AddTributeToProgress": ["JsonFuncAddTributeToProgress"],
    "LevelUpMonster": ["JsonFuncLevelUpMonster"],
    "EnergyDrain": ["JsonFuncEnergyDrain"],
    "ApplyStance": ["JsonFuncApplyStance"],
    "ApplyStanceToOtherMonster": ["JsonFuncApplyStanceToOtherMonster"],
    "EncounterSizeGreaterOrEqualTo": ["JsonFuncEncounterSizeGreaterOrEqualTo"],
    "EncounterSizeLessOrEqualTo": ["JsonFuncEncounterSizeLessOrEqualTo"],
    "RecalculateMonsterErosDrop": ["JsonFuncRecalculateMonsterErosDrop"],
    "RecalculateMonsterExpDrop": ["JsonFuncRecalculateMonsterExpDrop"],
    "RefreshMonster": ["JsonFuncRefreshMonster"],
    "CallMonsterEncounterOrgasmCheck": ["JsonFuncCallMonsterEncounterOrgasmCheck"],
    "MonsterOrgasm": ["JsonFuncMonsterOrgasm"],
    "ApplyStatusEffectToMonster": ["JsonFuncApplyStatusEffectToMonster"],
    "RefocusOnInitialMonster": ["JsonFuncRefocusOnInitialMonster"],
    "FocusOnMonster": ["JsonFuncFocusOnMonster"],
    "FocusOnRandomMonster": ["JsonFuncFocusOnRandomMonster"],
    "FocusedSpeaks": ["JsonFuncFocusedSpeaks"],
    "FocusedSpeaksSkill": ["JsonFuncFocusedSpeaksSkill"],
    "CallMonsterAttack": ["JsonFuncCallMonsterAttack"],
    "HitPlayerWith": ["JsonFuncHitPlayerWith"],
    "HitMonsterWith": ["JsonFuncHitMonsterWith"],
    "DamageMonsterFromMonster": ["JsonFuncDamageMonsterFromMonster"],
    "DenyPlayerOrgasm": ["JsonFuncDenyPlayerOrgasm"],
    "DenyMonsterOrgasm": ["JsonFuncDenyMonsterOrgasm"],
    "DenyTargetOrgasm": ["JsonFuncDenyTargetOrgasm"],
    "DenyAttackerOrgasm": ["JsonFuncDenyAttackerOrgasm"],
    "ResumeMonsterAttack": ["JsonFuncResumeMonsterAttack"],
    "ResumeAllMonsterAttacks": ["JsonFuncResumeAllMonsterAttacks"],
    "DefeatMonster": ["JsonFuncDefeatMonster"]
    
    }

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
        #$ benchstart = time.perf_counter()
        if displayingScene.theScene[lineOfScene] != "" and displayingScene.theScene[lineOfScene] in JsonFuncRegistry:
            $ theJsonFunc = JsonFuncRegistry[displayingScene.theScene[lineOfScene]]
            $ renpy.call(*theJsonFunc)
                # except:
                #     print(theJsonFunc,functionNameToPass, jsonFuncArgs)
            $ notFunction = 0
        else:
            $ notFunction = 1
        
        #End of functions
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
        #$ benchtime = time.perf_counter()
        #$ benchtimeseconds = benchtime - benchstart
        #$ print("FuncLoadTimes:", f"{benchtimeseconds:.6f} seconds") 
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
                elif checking == "ArousalByPercent":
                    while displayingScene.theScene[lineOfScene] != "EndLoop":
                        $ lineOfScene += 1
                        if displayingScene.theScene[lineOfScene] != "EndLoop":
                            if player.stats.hp >= player.stats.max_true_hp*float(displayingScene.theScene[lineOfScene])*0.01 and linefound == 0:
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
                elif checking == "EnergyByPercent":
                    while displayingScene.theScene[lineOfScene] != "EndLoop":
                        $ lineOfScene += 1
                        if displayingScene.theScene[lineOfScene] != "EndLoop":
                            if player.stats.ep >= player.stats.max_true_ep*float(displayingScene.theScene[lineOfScene])*0.01 and linefound == 0:
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
                $ finalDamage = 0
                $ statusEffectiveText = ""
                $ recoilHit = 0

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
        $ locationDescrip = "You stand before the rustic looking adventuring store in the market district of town. Peeking through the window you see the walls and shelves are lined with all different kinds of gear an adventurer in Lucidia could use, ranging from potions, runes and magical artifacts, to just straight up sex toys."
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
