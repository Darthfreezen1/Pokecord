# PokeBot Notes

   ## GEN III Rules    
   ### Calculate HP:
   >``hp=(((2*Base+IV+(EV/4))*Level)/100)+Level+10``
   ### Calculate Stat (any):
   >``stat = ((((2*base+iv+(ev/4))*level)/100)+5)*nature``
***
## Notes on Calculating Stats
When calculating a regualar stats (not hp), remember to checkwhich stat (or stats) is being increased or decreased.

If the stat has no nature value to apply to it, do NOT
calculate as (*0), just forget nature exists in the equation!

Ex: value = SELECT statin, statde FROM natures
>``if value['statin'] == monstats``

>>``increase by 10%``

>``elif value['statde] == monstats ``

>>``decr by 10%``

>``else``

>>``stat=(((2*Base+IV+(sqrt(EV)/4)*Level)/100)+5)``

>>*Remove Nature from equation if a nature does not affect stat*

### How IV's Affect Stat Calculation:
IV values are essentially a Pokemons *genes*, they help determine how fast a stat develops

IV's for each stat have a range from 0 to 31
***
## Notes on EV's
EV's for newly generated Pokemon start at 0. 

Different Pokemon you battle will give your current Pokemon either 1 or 2 *EV Points*

The highest base stat of the Pokemon you battle determines what stat a given *EV Point* allocates to

This means if the Pokemon you fights highest stat is Attack, you will gain up to 2 *EV Points* to your Attack stat

Every 4 EV = +1 in that stat at level 100

If not level 100, every 4 EV = +%level in that stat

### Ex:
lvl 100: +1 to n stat

lvl  67: +.67% to n stat

***
## Notes on Determening Hit Chance
>``ThreshholdToHit = AccuracyOfMove * AdjustedStages * Other_mods``

*-AccuracyOfMove: Moves accuracy value. 1-100*

*-AdjustedStages: fraction% of a boosted stat like evasion*

*-see bulbagarden on stage adjustments*
***

## Notes on Dealing Damage

>``((((2*Level/5)+2) * Power * A/D)/50)+2) * Modifier``

Where
>Level is the level of the attacking pokemon (*2 for a critical hit)

>A is the effective attack stat or special attack stat

>D is the effective defense stat or special defense stat

>Power is the attack power of the move used

***
>``Modifier = Targets * Weather * Critical * random * STAB * Type * Burn * other``

Where

>Targets is 0.75 if the move has more than one target, 1 otherwise

>Weather is 1.5 if a typed move is used during its types weather (water type = rain etc)

>Critical is 2 in gen II-V, or 1.5 for VI, otherwise 1

>random is a random % from 0.85 to 1.00 inclusive

>STAB is same type attack boner. Equal to 1.5 if the moves type is the same as the users type

>Type is type affectiveness
>>0 - ineffective, 0.25, 0.5 - not very effective, 1 - normal effective, 2 or 4 - super effective

>Burn
>>0.5 if the attacker is burned, abiliy != Gutes, and used move is a physical move, and 1 otherwise

>other
>>1 in most cases, and a different multiplier when specific interactions of moved, Abilities, or items take effect

***

## Other Notes
### Determining Battle Stage Effect Boost:
- Grab currently selected pokemon's stats
- Store those stats as temporary "*battle*" stats
- When a move that boosts a stat by a *stage*, affect only the *battle* stats
- If HP is affected, change the original stat value from the battle temp stat


-Gather pokemon stats and store them temporarily for the battle

-Modify ONLY those temp stats. If pokemon levels up or loses
        health, modify the original stats at end of battle

***
# TODO
        -ADD ROUTES AND *OTHER* LOCATIONS TO METODS MOVE AND ROUTES
        -Gather pokemon base stats
        -Gather movesets
        -Gather move stats
        -Stage multipliers??? (see battle modifiers)
        -Take notes on calculating damage
        -Take notes on type advantages
        -Take notes on how attacks function
        CLEAN UP CODE!!!!!!!!!!!!!!!!!!!!!