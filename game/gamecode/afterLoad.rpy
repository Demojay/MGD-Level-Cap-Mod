label after_load:

    if _version.startswith("Renpy-8") or _version.startswith("Alpha-v20") or _version.startswith("Alpha-v19") or _version.startswith("Alpha-v25") or _version.startswith("Alpha-v24") or _version.startswith("Alpha-v23") or _version.startswith("Alpha-v22") or _version.startswith("Alpha-v21"):
        $ save_name = copy.copy(player.name)
        $ _version = "Alpha-v26"
        #$ print("Updated") #Do prints to verify behavior.
        #You can console insert '_version' in the in-game console to see if it applied.
        #Make sure to first interact with the game before saving again to see if it remembered,
        #Ren'Py does not overwite a save that only had changes made via autoload,
        #the actual game itself needs its state changed first.

    # if _version in ["Alpha-v26", "Alpha-v26a", "Alpha-v26b", "Alpha-v26.1", "Alpha-v26.1b"]:
    #Do this to update saves that were on the last set of versions that were on an afflicted save.
    #Then, once done, update it to the current game version to be shipped.
    #     $ _version = "Alpha-v26.2"
    #Now during the after_load it is considered a v26.2 save.
    #Let's say the actual current version of the game is v27.
    #You then run the next conditional that will catch it:
    # if _version in ["Alpha-v26.2", "Alpha-v26.2a", "Alpha-v26.3", "Alpha-v26.3a"]:
    #Now any save being loaded marked the above, including those that just did the previous if will
    #apply these changes to the save next.
    #     _version = "Alpha-v27"
    #Now any save between 26 in the first if condition to v26.3a in the second are up to date as v27.
    #You don't have to worry about it applying to a v27 save again as v27 isn't checked for in any conditional.
    #Thus, it is impossible to apply to an already up to date save by mistake for as long as your if condition
    #never contains the current game version you are intending to ship.

    if (_version in ["Alpha-v26", "Alpha-v26a", "Alpha-v26b", "Alpha-v26.3"]) or _version.startswith("Alpha-v26.1") or _version.startswith("Alpha-v26.2"):
        "The wind blows in a sudden gust and a small silver ticket flies into your face. It seems like you happend across a Guild Approved respec ticket!"
        $ player.inventory.give("Respec Ticket", 1)
        $ _version = "Alpha-v26.3a"

    hide screen ON_MapMenu 

    if onGridMap == 0:
        hide screen gridMoveKeys

    if favorPool == -1:
        $ favorPool = CalcGoddessFavor(player)

    $ needToUpdate = 0
    hide screen FishingHitEffect
    show screen input_detection
    python:
        UpdatedGameCheck = len(SkillsDatabase) + len(ItemDatabase) + len(MonsterDatabase) + len(PerkDatabase) + len(LocationDatabase) + len(EventDatabase) + len(AdventureDatabase)

        try:
            CurrentIteration
        except NameError:
            needToUpdate = 1
            CurrentIteration = copy.deepcopy(UpdatedGameCheck)

    if CurrentIteration != UpdatedGameCheck:
        $ needToUpdate = 1
        $ CurrentIteration = copy.deepcopy(UpdatedGameCheck)

    if needToUpdate == 1 or CurrentVersion != config.version:

        if historyUpdate == 0:
            # For the markup change in v25.6
            $ _history_list = []
            define SexAdjective = Alias(lambda: getPenetrationAjectives(player))
            #define SexWord = Alias(lambda: getPenetration(player))
            $ historyUpdate = 1

        $ CurrentVersion = config.version
        call AutoReloadDatabase from _call_AutoReloadDatabase_1
    #CODEMOD
    else:
        python:
            loadLevelCapJSON()
    
    #CODEMOD
    #Check to see whether the player has already taken the extra perk point from the church, to properly update the number of extra perk points the player has
    if additionalPerkPointUpdate == 0:
        $ additionalPerkPointUpdate = 1
        python:
            try:
                player.additionalPerkPoints
            except:
                player.additionalPerkPoints = 0
                
            churchReq = Requirements("Pray to the Goddess Statue.", -99, 10, "insight")
            if requiresCheck([], [churchReq], player, ProgressEvent):
                player.additionalPerkPoints += 1

    jump exitCombatFunction



    # if persistent.genModData == True:
    #     call setDatabase
    #     $ set_lists()
    #     $ loadingDatabaseType = 0
    #     call loadDatabase
    #     $ loadingDatabaseType = 1
    #     $ persistent.genModData = False
    #     if persistent.modCount == None:
    #         $ persistent.modCount = 0
    #     if persistent.modCount != 0:
    #         $ renpy.notify("[persistent.modCount] Mods loaded.")
