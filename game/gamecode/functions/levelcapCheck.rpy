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