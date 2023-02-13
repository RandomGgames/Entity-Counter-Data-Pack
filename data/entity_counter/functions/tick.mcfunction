execute unless score Interval EntityCounter.Timeout matches 1.. run scoreboard players set Interval EntityCounter.Timeout 5

scoreboard players add Timeout EntityCounter.Timeout 1
execute if score Timeout EntityCounter.Timeout >= Interval EntityCounter.Timeout run function entity_counter:count