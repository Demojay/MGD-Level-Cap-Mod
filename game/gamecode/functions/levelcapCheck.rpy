#CODEMOD
label LevelCapCheck:
    python:
        def levelCapEnabled():
            return getDiffLevelCapObj().get("enableCap", False)

        def getDiffLevelCapObj():
            global difficulty

            return LevelCapObj.get(difficulty, {
                "enableCap": False
            })

        def getMaxLevelCap():
            if levelCapEnabled():
                return calcLevelCap()
            else:
                return Integer.MAX_VALUE

        def getLevelCapFilePath():
            if renpy.android:
                return "Mods/LevelCapCheck.json"
            else:
                return "../Mods/LevelCapCheck.json"

        def loadLevelCapJSON():
            global LevelCapObj
            try:
                levelCapJSONStr = renpy.file(getLevelCapFilePath()).read().decode("utf-8")
                loadedCapList = json.loads(levelCapJSONStr).items()
                LevelCapObj = {}
                
                for diffSetting in loadedCapList:
                    newDiffSettings = {}
                    loadedSettings = diffSetting[1]

                    newDiffSettings["enableCap"] = loadedSettings.get("enableCap", False)
                    newDiffSettings["lvls"] = []

                    for newLevel in loadedSettings["lvls"]:
                        newLevelObj = {
                            "lvl": newLevel["lvl"],
                            "item": newLevel.get("item", [])
                        }

                        if "events" in newLevel:
                            newLevelObj["events"] = []
                            for eventReq in newLevel["events"]:
                                newRequirement = Requirements()
                                newRequirement.NameOfEvent = eventReq["NameOfEvent"]
                                newRequirement.Progress = int(eventReq["Progress"])
                                newRequirement.ChoiceNumber = int(eventReq["ChoiceNumber"])
                                newRequirement.Choice = eventReq["Choice"]

                                newLevelObj["events"].append(newRequirement)
                        
                        newDiffSettings["lvls"].append(newLevelObj)
                    
                    LevelCapObj[diffSetting[0]] = newDiffSettings
            except:
                LevelCapObj = {
                    "Normal": {
                        "enableCap": False
                    }
                }

            return LevelCapObj

        def levelCapNotReached():
            return player.stats.lvl < getMaxLevelCap()

        def calcLevelCap():
            currentCapObj = getDiffLevelCapObj()
            currentCap = -1
            maxLevelCap = currentCapObj.get("maxLevel", 100)

            levelArr = currentCapObj.get("lvls", [])

            for levelCheck in levelArr:
                capPassed = False
                if levelCheck["lvl"] <= maxLevelCap and levelCheck["lvl"] > currentCap:
                    itemsToCheck = levelCheck.get("item", [])
                    eventsToCheck = levelCheck.get("events", [])
                    capPassed = requiresCheck(itemsToCheck, eventsToCheck, player, ProgressEvent)

                if capPassed:
                    currentCap = levelCheck["lvl"]

            if currentCap == -1:
                currentCap = maxLevelCap
            
            return currentCap

        def respecPlayerToLevel(levelToSet):
            newLevel = levelToSet
            if newLevel < 1:
                newLevel = 1

            if levelCapEnabled():
                maxLevel = getMaxLevelCap()
                if newLevel > maxLevel:
                    newLevel = maxLevel
            
            #Code taken from "RespecPlayer" function code
            global player, sexResCap, assResCap, nipResCap, chuResCap, seducResCap, magResCap, painResCap, hpFloor, epFloor, spFloor, powFloor, spdFloor
            global intFloor, allFloor, wilFloor, lukFloor, respeccing, hasResPoints 

            player.respec()
            sexResCap = 150
            assResCap = 150
            nipResCap = 200
            chuResCap = 150
            seducResCap = 150
            magResCap = 150
            painResCap = 150
            hpFloor = 50
            epFloor = 20
            spFloor = 1
            powFloor = 1
            spdFloor = 1
            intFloor = 1
            allFloor = 1
            wilFloor = 1
            lukFloor = 1
            hasResPoints = 1

            #Reset stat, perk and sens points to level 1, without affecting points given by non-level up perks
            tempPerksList = copy.deepcopy(player.perks)
            for each in tempPerksList:
                player.giveOrTakePerk(each.name, -1)

            #Reset Stat, Sens and Perk points dependent on difficulty
            spiritStatPointChange = (player.stats.max_true_sp - 3) * -3
            
            if difficulty == "Hard":
                player.statPoints = 20 + min(0, spiritStatPointChange)
                player.perkPoints = 0
                player.SensitivityPoints = 1
            elif difficulty == "Easy":
                player.statPoints = 10 + spiritStatPointChange
                player.perkPoints = 0
                player.SensitivityPoints = 5
            else:
                player.statPoints = 5 + min(0, spiritStatPointChange)
                player.perkPoints = 0
                player.SensitivityPoints = 3
            
            player.perkPoints += player.additionalPerkPoints


            for each in tempPerksList:
                player.giveOrTakePerk(each.name, 1)


            expToGive = 0
            currentLvl = 1
            player.stats.lvl = 1
            player.stats.ExpNeeded = 10
            player.stats.Exp = 0

            while currentLvl < newLevel:
                expToGive += int((0.4*(currentLvl*currentLvl)) + (2*currentLvl) + (15*math.sqrt(currentLvl)-8))
                currentLvl += 1
            
            player.stats.Exp = expToGive + 1

            renpy.say("", f"Level set to {newLevel}!")
            renpy.jump("forceRepecLevelUpCheck")