#CODEMOD
init 1000 python:
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
            return sys.maxsize

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

    def levelCapReached():
        return player.stats.lvl >= getMaxLevelCap()

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
        global player, displayingScene, lineOfScene

        if player.stats.lvl == newLevel:
            return
        elif player.stats.lvl < newLevel:
            lvlDifference = newLevel - player.stats.lvl

            expGain = player.stats.ExpNeeded

            lvlCount = lvlDifference - 1
            currentLvl = player.stats.lvl + 1
            while lvlCount > 0:
                expGain +=  int((0.4*(currentLvl*currentLvl)) + (2*currentLvl) + (15*math.sqrt(currentLvl)-8))
                currentLvl += 1
                lvlCount -= 1

            player.stats.Exp += expGain
            renpy.jump("levelCapForceLvlCheck")
        elif player.stats.lvl > newLevel:
            lvlDifference = player.stats.lvl - newLevel

            if displayingScene and displayingScene.theScene: 
                displayingScene.theScene.insert(lineOfScene + 1, lvlDifference)
            elif displayingScene and not displayingScene.theScene:
                displayingScene.theScene = [lvlDifference]
                lineOfScene = -1
            else:
                displayingScene = Dialogue()
                displayingScene.theScene = [lvlDifference]
                lineOfScene = -1
            renpy.jump("JsonFuncDrainLevel")
    
    def setUpCharacterScreen():
        targetScreen = GetScreen("ON_CharacterDisplayScreen")
        targetNameText = SLSearch(targetScreen, "Positional", targetPositional = '"[player.name]"')[0]
        targetLvlText = SLSearch(targetScreen, "Positional", targetPositional = '"Level [player.stats.lvl]"')[0]
        ChangeSLNodePositional(targetLvlText, 0, "Level [player.stats.lvl][cap]")
        InsertScreenCode(targetNameText, '$ cap = ("/" + str(getMaxLevelCap())) if levelCapEnabled() else ""')
    
    def setUpLevelCapCheckAddition():
        levelUpSpotCheck = GetLabel("levelUpSpot")
        scriptStatement = FindNode(levelUpSpotCheck, "Python", "culmitiveLeveling += 1")
        if scriptStatement:
            testBlock = CreateBlock('if levelCapReached():\n $ player.stats.Exp = player.stats.ExpNeeded - 1')[0]

            prevNext = scriptStatement.next
            scriptStatement.next = testBlock
            testBlock.next = prevNext

            scriptStatementIndex = levelUpSpotCheck.block.index(scriptStatement)
            levelUpSpotCheck.block.insert(scriptStatementIndex + 1, testBlock)
    
    def setUpAdditionalFunctions():
        global JsonFuncRegistry
        JsonFuncRegistry["AdjustPlayerLevel"] = ["JsonFuncAdjustPlayerLevel"]

    def setUpAfterLoadHook():
        loadDatabaseLabel = GetLabel("loadDatabase")
        validatorIf = FindNode(loadDatabaseLabel, "Python", "")
        if validatorIf:
            #testBlock = CreateBlock("if loadingDatabaseType == 0:\n $ loadLevelCapJSON()")[0]
            testBlock = CreateBlock("$ loadLevelCapJSON()")[0]

            prevNext = validatorIf.next
            validatorIf.next = testBlock
            testBlock.next = prevNext

            validatorIfIndex = loadDatabaseLabel.block.index(validatorIf)
            loadDatabaseLabel.block.insert(validatorIfIndex + 1, testBlock)
    
    loadLevelCapJSON()
    setUpCharacterScreen()
    setUpAdditionalFunctions()
    setUpLevelCapCheckAddition()
    setUpAfterLoadHook()

        
label levelCapForceLvlCheck:
    call refreshLevelVar from _call_refreshLevelVar_1
    call levelUpSpot from _call_levelUpSpot_2
    return

label JsonFuncAdjustPlayerLevel:
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
    return
