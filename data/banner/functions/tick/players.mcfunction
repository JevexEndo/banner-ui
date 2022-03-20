# Ensure scoreboards are preloaded
scoreboard players add @s bn.title_cooldown 0

# Operate on scoreboard values
title @s[scores={bn.title_cooldown=0}] times 10 80 10
execute if score @s bn.title_cooldown matches 0.. run scoreboard players remove @s bn.title_cooldown 1

execute at dbc5c80b-aabb-46fd-93e0-8fe24b96cbc1 if entity @s[distance=..10] at @s if predicate banner:looking_at/north run function banner:locations/north
execute at dbc5c80b-aabb-46fd-93e0-8fe24b96cbc2 if entity @s[distance=..10] at @s if predicate banner:looking_at/east run function banner:locations/east
execute at dbc5c80b-aabb-46fd-93e0-8fe24b96cbc3 if entity @s[distance=..10] at @s if predicate banner:looking_at/south run function banner:locations/south
execute at dbc5c80b-aabb-46fd-93e0-8fe24b96cbc4 if entity @s[distance=..10] at @s if predicate banner:looking_at/west run function banner:locations/west

# Reset scoreboards after finalizing operations
scoreboard players set @s mc.talked_to_villager 0
