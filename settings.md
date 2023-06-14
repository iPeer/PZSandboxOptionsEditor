This file contains information of all available settings' values present within map_sand.bin in PZ build 41. Note that these are not necessarily in the same order they will appear in a dumped file.

* Default values are based on regular apocalypse difficulty
* More obscurely named settings will have some text to explain what they do.
* With integer values, the number increments going **down** the list. The top option being 1, the second 2, third 3 and so on.
  * Example: For **ZombieLore.Transmission**, setting this to **1** would set it to Blood + Saliva transmition, while setting it to **2** would set it to Saliva only.

# Map.AllowMiniMap

*Boolean*
* true
* false

# Map.AllowWorldMap

*Boolean*
* true
* false

# Map.MapAllKnown

*Boolean*
* true
* false

## Zombie Lore

# ZombieLore.Speed

*Integer*
* Sprinters
* Fast Shamblers [**default**]
* Shamblers
* Random

# ZombieLore.Strength

*Integer*
* Superhuman
* Normal [**default**]
* Weak
* Random

# ZombieLore.Toughness

*Integer*
* Tough
* Normal [**default**]
* Fragile
* Random

# ZombieLore.Transmission

*Integer*
* Blood + Saliva [**default**]
* Saliva Only
* Everyone's Infected
* None

# ZombieLore.Mortality

*How fast, once infected, it will take the player to die*

*Integer*
* Instant
* 0-30 seconds
* 0-1 minutes
* 0-12 hours
* 2-3 days [**default**]
* 1-2 weeks
* Never

# ZombieLore.Reanimate

*How long it takes a player's corpse to reanimate as a zombie after dying from infection*

*Integer*
* Instant
* 0-30 seconds
* 0-1 minutes [**default**]
* 0-12 hours
* 2-3 days
* 1-2 weeks

# ZombieLore.Cognition

*What zombies can do when trying to get where they're going*

*Integer*
* Navigate + use doors
* Navigate
* Basic navigation [**default**]
* Random


# ZombieLore.CrawlUnderVehicle

*Integer*
* Crawlers only
* Extremely rare
* Rare
* Sometimes
* Often [**default**]
* Very Often
* Always

# ZombieLore.Memory

*How long a zombie will attempt to persue the player before giving up*

*Integer*
* Long
* Normal [**default**]
* Short
* None
* Random

# ZombieLore.Sight

*Integer*
* Eagle
* Normal [**default**]
* Poor
* Random


# ZombieLore.Hearing

*Integer*
* Pinpoint
* Normal [**default**]
* Poor
* Random


# ZombieLore.ThumpNoChasing

*Will zombies bang on doors/windows idly (ie. when just roaming, and not trying to reach the player)*

*Boolean*
* true [**default**]
* false

# ZombieLore.ThumpOnConstruction

*Can zombies attack and destroy player constructed things*

*Boolean*
* true [**default**]
* false


# ZombieLore.ActiveOnly

*When are zombies active*

*Integer*
* Both [**default**]
* Night
* Day

# ZombieLore.TriggerHouseAlarm

*Can zombies trigger house alarms?*

*Boolean*
* true
* false [**default**]

# ZombieLore.ZombiesDragDown

*Can zombies drag the player down when attacking*

*Boolean*
* true [**default**]
* false

# ZombieLore.ZombiesFenceLunge

*Can zombies lunge at the player when climbing fences*

*Boolean*
* true [**default**]
* false

# ZombieLore.DisableFakeDead

*Can zombies fake being dead?*

*Integer*
* Some zombies in the world will pretend to be dead [**default**]
* Some zombies in the world, as well as some you 'kill', can pretend to be dead	
* Zombies will never pretend to be dead

## Advanced Zombie Options

# ZombieConfig.PopulationMultiplier

*The multiplier for the overall population of zombies*

*Float*
* Minimum: 0.0
* Maximum: 4.0
* Default: 1.0
UI Values:
* Insane = 4.0
* High = 2.0
* Normal = 1.0
* Low = 0.35
* None = 0.0

# ZombieConfig.PopulationStartMultiplier

*The adjustment to the overall population of zombies **at the start of the game***

*Float*
* Minimum: 0.0
* Maximum: 4.0
* Default: 1.0


# ZombieConfig.PopulationPeakMultiplier

*Adjustment for the overall zombie population on the "peak day"*

*Float*
* Minimum: 0.0
* Maximum: 4.0
* Default: 1.5

# ZombieConfig.PopulationPeakDay

*The day on which zombie population reaches its peak*

*Integer*
* Minimum: 1
* Maximum: 365
* Default: 28

# ZombieConfig.RespawnHours

*The number of hours before zombies respawn. Set to 0 to disable respawn.*

*Float*
* Minimum: 0.0
* Maximum: 8760.0
* Default: 72.0

# ZombieConfig.RespawnUnseenHours

*The number of hours a "chunk" must not be seen for before zombies are allowed to respawn within it*

*Float*
* Minimum: 0.0
* Maximum: 8760.0
* Default: 16.0

# ZombieConfig.RespawnMultiplier

*How much of the cell's zombie population is allowed to respawn per respawn cycle (ZombieConfig.RespawnHours). **1.0 = 100%**.*

*Float*
* Minimum: 0.0
* Maximum: 1.0
* Default 0.1

# ZombieConfig.RedistributeHours

*How many hours need to pass before zombies will attempt to migrate to unoccupied locations in the same cell. Set to 0.0 to disable migration*

*Float*
* Minimum: 0.0
* Maximum: 8760.0
* Default: 12.0


# ZombieConfig.FollowSoundDistance

*If a zombie hears something, what is the maximum distance it will travel to get to the sound*

*Integer*
* Minimum: 0
* Maximum: 1000
* Default: 100

# ZombieConfig.RallyGroupSize

*The size of groups real zombies will form. Set to 0 to disable grouping.*

*Integer*
* Minimum: 0
* Maximum: 1000
* Default: 20


# ZombieConfig.RallyTravelDistance

*How far will zombies travel to form a group*

*Integer*
* Minimum: 5
* Maximum: 50
* Default: 20

# ZombieConfig.RallyGroupSeparation

*How far between groups of zombies*

*Integer*
* Minimum: 5
* Maximum: 25
* Default: 15

# ZombieConfig.RallyGroupRadius

*How close the other zombies in a group stay to the "leader"*

*Integer*
* Minimum: 1
* Maximum: 10
* Default: 3

## Population

# Zombies

*Overall population of zombies*

*Integer*
* Insane
* Very High
* High
* Normal [**default**]
* Low
* None


# Distribution

*Are zombies scattered uniformally, or concetrated in urban areas?*

*Integer*
* Urban Focused [**default**]
* Uniform

## Time

# DayLength

*How long an in-game day lasts.*
* If the setting you want is in the hours, take the number of hours and add 2, this will give you the integer you need fo the setting (ex. 13 hours would be *15*, 24 hours would be *26*)

*Integer*
* 15 minutes
* 30 minutes
* 1 hour [**default**]
* 2 hours
* 3 hours
* *[...]*
* Real-time (24 hours)

# StartYear

***Unused?***
*Integer*
* Defaults to 1.

# StartMonth

*The month the game starts in*
*Integer*
* Number of the month = number for the setting. **July** (*7*) is the default.

# StartDay

*The day the game starts on*
*Integer*
* Number of the day = the integer required. The default is **9**.

# StartTime

*The time when starting the game for the first time*

*Integer*
* 7 am
* 9 am [**default**]
* 12 pm (midday)
* 2 pm
* 5 pm
* 9 pm
* 12 am (midnight)
* 2 am
* 5 am

## World

# WaterShut

*How long until water is cut off*

*Integer*
* Instant
* 0-30 days [**default**]
* 0-2 months
* 0-6 months
* 0-1 year
* 0-5 years
* 2-6 months
* 6-12 months

# ElecShut

*How long until the electricity is cut off*

*Integer*
* Instant
* 0-30 days [**default**]
* 0-2 months
* 0-6 months
* 0-1 year
* 0-5 years
* 2-6 months
* 6-12 months

# WaterShutModifier

*The number of days after which the Water will shut off*
* Cannot be directly modified during world creation, instead generated upon entering the world for the first time.

*Integer*
* -1 (instant)
* 0+ (# of days, 0 meaning it will shut off during the first day)

# ElecShutModifier

*The number of days after which the Electrcity will shut off*
* Cannot be directly modified during world creation, instead generated upon entering the world for the first time.

*Integer*
* -1 (instant)
* 0+ (# of days, 0 meaning it will shut off during the first day)


# Alarm

*How frequently houses have alarms*

*Integer*
* Never
* Ectremely rare
* Rare
* Sometimes [**default**]
* Often
* Very Often

# LockedHouses

*How often do houses have all doors and windows locked*

*Integer*
* Never
* Ectremely rare
* Rare
* Sometimes
* Often
* Very Often [**default**]


# FoodRotSpeed

*How fast food rots when not refrigerated*

*Integer*
* Very Fast
* Fast
* Normal [**default**]
* Slow
* Very Slow

# FridgeFactor

*How effected are fridges are preserving food*

*Integer*
* Very Low
* Low
* Normal [**default**]
* High
* Very High

# DaysForRottenFoodRemoval

*The number of days required for rotten food to be removed from the map. -1 means no removal.*

*Integer*
* Default: -1

# LootRespawn

*How often does loot respawn in containers*

*Integer*
* None [**default**]
* Every day
* Every week
* Every month
* Every 2 months

# SeenHoursPreventLootRespawn

*How long must a chunk not be seen by the player before allowing loot to respawn*

*Integer*
* Default: 0

# WorldItemRemovalList

*Items which will be removed from the world each time `HoursForWorldRemoval` passes*
* Takes a list of in-game items by their internal ID names
* Defaults to `Base.Hat,Base.Glasses,Base.Maggots`

# HoursForWorldItemRemoval

*After how many hours should items in W`orldItemRemovalList` be removed from the game world*

*Float*
* Default: 24.0

# ItemRemovalListBlacklistToggle

*Is `WorldItemRemovalList` treated as a whitelist, or a blacklist*

* If true, items **not** present in `WorldItemRemovalList` will be removed from the game world, instead of those listed in it.

*Boolean*
* true
* false [**default**]

# TimeSinceApo

*How many months have passed since the apocalypse started*

*Integer*
* Value of 1-13, 1 being "no time has passed", and 13 being 12 months after the start


# NightDarkness

*How dark are night*

*Integer*
* Pitch black
* Dark
* Normal [**default**]
* Bright

# NightLength

***Unused?***
*Integer*

# FireSpread

*Is fire spread enabled?*

*Boolean*
* true [**default**]
* false

# AllowExteriorGenerator

*Are generators able to be placed outdoors*

*Boolean*
* true [**default**]
* false

# FuelStationGas

*How much gas (fuel) gas stations start with*
* Empty
* Super Low
* Very low
* Normal [**default**]
* High
* Very High
* Full
* Infinite

# LightBulbLifespan

*How long lightbulbs last. Set to 0 to have them never break. Does not effect vechicles.*

*Float*
* Default: 1.0

## Nature

# Temperature

*The climate type for the world*

*Integer*
* Very cold
* Cold
* Normal [**default**]
* Hot
* very hot

# Rain

*How arid the world is*

*Integer*
* Very dry
* Dry
* Normal [**default**]
* Rainy
* Very rainy

# ErosionSpeed

*How fast erosion (degradation of roads and buildings) happens*

*Integer*
* Very fast (20 days)
* Fast (50 days)
* Normal (100 days) [**default**]
* Slow (200 days)
* Very slow (500 days)

# ErosionDays

***Unused?***
*Integer*
* Always 0

# Farming

*How fast crops grow*

*Integer*
* Very fast
* Fast
* Normal [**default**]
* Slow
* Very slow

# PlantResilience

*How often do plants need watering, and how good are they at fighting disease*

*Integer*
* Very low
* Low
* Normal [**default**]
* High
* Very high

# PlantAbundance

*Changes how many items farmed crops can produce*

*Integer*
* Very poor
* Poor
* Normal [**default**]
* Abundant
* Very abundant

# NatureAbundance

*How difficult is fishing or foraging*

*Integer*
* Very poor
* Poor
* Normal [**default**]
* Abundant
* very abundant

# CompostTime

*How long food takes to decay into compost in a composter*

* 1 Week
* 2 Weeks [**default**]
* 3 Weeks
* 4 Weeks
* 6 Weeks
* 8 Weeks
* 10 Weeks
* 12 Weeks

# MaxFogIntensity

*How dense the fog can get*

*Integer*
* Normal [**default**]
* Moderate
* Low

# MaxRainFxIntensity

*Influences maximum rainfall*

*Integer*
* Normal [**default**]
* Moderate
* Low

# EnableSnowOnGround

*how much snow accumulates on the ground*

*Integer*
* Normal [**default**]
* Moderate
* Low

# EnableTaintedWaterText

*Enables or disables the tainted water tooltip*
* true = enabled, false = disabled

*Boolean
* true [**default**]
* false

## Sadistic AI Director

# Helicopter

*How often helicopters pass over the map*

*Integer*
* Never
* Once [**default**]
* Sometimes
* Often

# MetaEvent

*How often do meta events (ie. random gunshots, screams, etc.) occur*

*Integer*
* Never
* Once
* Sometimes [**default**]
* Often

# SleepingEvent

*How often do sleeping events happen (such as night terrors) occur*

*Integer*
* Never [**default**]
* Once
* Sometimes
* Often

## Meta

# GeneratorSpawning

*Spawn rate of generators*

*Integer*
* Extremely rare
* Rare
* Sometimes [**default**]
* Often
* Very Often

# GeneratorFuelConsumption

*The rate at which generators consume fuel. Set to 0.0 to disable consumption*

*Float*
* Minimum: 0.0
* Maximum: 100.0
* Default: 1.0

# SurvivorHouseChance

*Effects the rarity of survivor houses/bodies etc.*

*Integer*
* Never
* Extremely rare
* Rare [**default**]
* Sometimes
* Often
* Very often


# VehicleStoryChance

*Effects frequency of "vehicle stories"; crashes, police blockades, etc.*


*Integer*
* Never
* Extremely rare
* Rare [**default**]
* Sometimes
* Often
* Very often

# ZoneStoryChance

*Unknown what this one does*

*Integer*
* Never
* Extremely rare
* Rare [**default**]
* Sometimes
* Often
* Very often

# AnnotatedMapChance

*Chance of the player finding an annotated map when looting a map*

*Integer*
* Never
* Extremely rare
* Rare
* Sometimes [**default**]
* Often
* Very often

# HoursForCorpseRemoval

*The number of hours after which zombie corpses are removed from the world*

*Float or Integer*
* Set to -1 to disable removal
* Default: 216.0

# DecayingCorpseHealthImpact

*How much do decaying corpses effect the health of the player*

* None
* Low
* Normal [**default**]
* High

# BloodLevel

*How much gore do you want?*

* None
* Low
* Normal [**default**]
* High
* Ultra Gore

# MaggotSpawn

*How do maggots spawn around decaying bodies*

*Integer*
* In and around bodies [**default**]
* In bodies only
* Never

## Loot Rarity

# FoodLoot

*The rarity of **non-canned** food items*

*Integer*
* None (not recommended)
* Insanely rare
* Extremely rare
* Rare [**default**]
* Normal
* Common
* Adundant
# CannedFoodLoot

*The rarity of **canned** food items*

*Integer*
* None (not recommended)
* Insanely rare
* Extremely rare
* Rare [**default**]
* Normal
* Common
* Adundant

# WeaponLoot

*Rarity of melee weapons*

*Integer*
* None (not recommended)
* Insanely rare
* Extremely rare
* Rare [**default**]
* Normal
* Common
* Adundant

# RangedWeaponLoot

*Rarity of ranged weapons*

*Integer*
* None (not recommended)
* Insanely rare
* Extremely rare
* Rare [**default**]
* Normal
* Common
* Adundant

# AmmoLoot

*Rarity of ammo*

*Integer*
* None (not recommended)
* Insanely rare
* Extremely rare
* Rare [**default**]
* Normal
* Common
* Adundant

# MedicalLoot

*Rarity of medical items*

*Integer*
* None (not recommended)
* Insanely rare
* Extremely rare
* Rare [**default**]
* Normal
* Common
* Adundant

# SurvivalGearsLoot

*Rarity of "survival" loot; nails, saws, fishing rods, tools, etc.*

*Integer*
* None (not recommended)
* Insanely rare
* Extremely rare
* Rare [**default**]
* Normal
* Common
* Adundant

# MechanicsLoot

*Integer*
* None (not recommended)
* Insanely rare
* Extremely rare
* Rare [**default**]
* Normal
* Common
* Adundant

# LiteratureLoot

*Rarity of readable items, such as books and comics*

*Integer*
* None (not recommended)
* Insanely rare
* Extremely rare
* Rare [**default**]
* Normal
* Common
* Adundant

# OtherLoot

*Rarity of "everything else" loot*

*Integer*
* None (not recommended)
* Insanely rare
* Extremely rare
* Rare [**default**]
* Normal
* Common
* Adundant

# XpMultiplier

*Effects how much XP is obtained from doing various actions*

*Float*
* Minimum: 0.001
* Maximum: 1000.0
* Default: 1.0

# XpMultiplierAffectsPassive

*If true, fitness are strength are effected by `XpMultiplier`*

*Boolean*
* true
* false [**default**]

# StatsDecrease

*How fast the player gets hungry, thirsty and fatigued*

*Integer*
* Very fast
* Fast
* Normal [**default**]
* Slow
* Very slow

# EndRegen

*How quickly the player's fatigue decreases*

*Integer*
* Very fast
* Fast
* Normal [**default**]
* Slow
* Very slow

# Nutrition

*Does the nutritional value of foods have an effect on the player?*

*Boolean*
* true [**default**]
* false

# StarterKit

*Spawn with a backpack with some basic supplies*

*Boolean*
* true
* false [**default**]


# CharacterFreePoints

*How many free skill points to give during character creation*

*Integer*
* Theortical maximum of 2^31
* Defaults to 0

# ConstructionBonusPoints

*HP values of player-built structures*

*Integer*
* Very low
* Low
* Normal [**default**]
* high
* Very high

# InjurySeverity

*Adjust the severity of induries*

*Integer*
* Low
* Normal [**default**]
* High

# BoneFracture

*Can the mplayer break limbs?*

*Boolean*
* true [**default**]
* false

# ClothingDegradation

*How quickly clothing degrades, or dirties/bloodied*

* Disabled
* Slow
* Normal [**default**]
* Fast

# RearVulnerability

*Vulnerability to bites when attacked by zombies from behind*

*Integer*
* Low
* Medium
* High [**default**]

# MultiHitZombies

*Can melee weapons hit multiple zombies in a single swing?*

*Boolean*
* true
* false [**default**]

# AttackBlockMovements

*Does attacking slow player movements*

*Boolean*
* true [**default**]
* false

# AllClothesUnlocked

*Allows or restricts the use of all clothing items during character creation*

*Boolean*
* true [**default**]
* false

# EnablePoisoning

*Poisoning enabled?*

*Integer*
* True [**default**]
* False
* Only bleach poisoning is disabled

## Vehicle

# EnableVehicles

*Boolean*
* true [**default**]
* false

# VehicleEasyUse

*If enabled, all cars have full gas and do not require keys*

*Boolean*
* true
* false [**default**]

# RecentlySurvivorVehicles

*Chance of the player finding "maintained" vehicles*

*Integer*
* None
* Low [**default**]
* Normal
* High

# ZombieAttractionMultiplier

*Loudness of car engines to zombies*

*Float*
* Minimum: 0.0
* Maximum: 100.0
* Default: 1.0

# CarSpawnRate

* Low [**default**]
* Normal
* High

# ChanceHasGas

*Chance of a spawned vehicle having gas in the tank*

* Low [**default**]
* Normal
* High

# InitialGas

*How much gas a vehicle can spawn with*

* Very low
* Low [**default**]
* Normal
* High
* Very high
* Full

# CarGasConsumption

*Modifier for how fast vehicles consume fuel. 0.0 = no consumption*

*Float*
* Minimum: 0.0
* Maximum: 100.0
* Default 1.0

# LockedCar

*How often a spawned vehicle's doors will be locked*

*Integer*
* Never
* Extremely rare
* Rare [**default**]
* Sometimes
* Often
* Very often

# CarGeneralCondition

*The general condition of spawned vehicles*

* Very low
* Low [**default**]
* Normal
* High
* Very high

# TrafficJam

*Enable or disable the spawning of traffic jams*

*Boolean*
* true [**default**]
* false

# CarAlarm

*How often cars spawn with an alarm*

*Integer*
* Never
* Extremely rare [**default**]
* Rare
* Sometimes
* Often
* Very often

# PlayerDamageFromCrash

*Can the player take damage from crashing a car?*

*Boolean*
* true [**default**]
* false

# CarDamageOnImpact

*How much damage vehicles take from crashes*

*Integer*
* Very low
* Low
* Normal [**default**]
* High
* Very high

# SirenShutoffHours

*After how many hours do the sirens of emergency vehicles automatically turn off. 0.0 will make it only turn off when the vehicle's battery dies*

*Float*
* Minimum: 0.0
* Maximum: 168.0
* Default: 0.0

# DamageToPlayerFromHitByACar

*How much damage the player takes from being hit by a car*

* None [**default**]
* Low
* Normal
* High
* Very high
