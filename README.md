# Monster Girl Dreams - Level Cap Mod

A mod for [Monster Girl Dreams](https://threshold.itch.io/monster-girl-dreams) that enforces strict level caps into the game, ensuring that the players cannot gain levels past certain points depending on game progression. This mod is designed to work on v26.1a.

This mod only focuses on blocking levelling up, meaning saves from unmodded games can be freely used with this mod and vice-versa.

## Installation

Extract the downloaded zip file from the latest [release](https://github.com/Demojay/MGD-Level-Cap-Mod/releases/latest) into the root folder of the game, overwriting any files where necessary.

## Configuration

These level gates are defined in _game/Mods/LevelCapCheck.json_. By default, the level caps are set so the player can only level up to the same level as the next main story boss, with a final level of 70 once all currently created story bosses have been defeated. These can be edited as desired, and will be automatically loaded by the game whenever a save file is loaded.

## Example JSON Format

```
{
  "Easy": {
    "enableCap": false
  },
  "Normal" : {
        "enableCap" : true,
        "maxLevel": 150,
        "lvls" : [
            {
                "lvl": 5,
                "item": [""]
            },
            {
                "lvl": 10,
                "item": ["Vandal Note"]
            },
            {
                "lvl": 15,
                "events": [
                  {
                    "NameOfEvent": "ExploreLabyrinthExplain",
                    "Progress": "-1",
                    "ChoiceNumber": "1",
                    "Choice": "ExplorationUnlocked"
                  }
                ]
            }
        ]
  }
}
```

## Keys

- enableCap
  - Determines whether level caps should be used for the defined difficulty settings. If not included, defaults to False. If False, the other keys for a specific difficulty aren't needed.
- maxLevel
  - Optional. The maximum level for which the player can still gain levels, regardless of the level gates defined. If not included, defaults to 100
- lvls
  - An array of objects, each detailing a specific level gate. These objects will each contain the following keys:
    - lvl
      - The maxmium level that the player can level up to if they pass this level gate.
    - item
      - Optional. An array of item names that if the player has any of them, will pass the level gate
    - events
      - Optional. An array of event progress requirements, that the player must have any of in order to pass the level gate. The format of these progress definintions are the same as defining requirements for a [custom location](https://mgd-modding-docs.readthedocs.io/Doc/Manual/Adventures/Adventures.html#requires-requiresevent).
