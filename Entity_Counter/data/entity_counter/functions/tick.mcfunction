scoreboard players add Interval EntityCounterTimeout 0
execute unless score Interval EntityCounterTimeout matches 1.. run scoreboard players set Interval EntityCounterTimeout 5

scoreboard players add Timeout EntityCounterTimeout 1
execute if score Timeout EntityCounterTimeout >= Interval EntityCounterTimeout run function entity_counter:count