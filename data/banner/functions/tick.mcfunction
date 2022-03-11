# Operate on scoreboard values
execute as @a at @s if score banner_cooldown bn.variables matches 0 if score @s mc.talked_to_villager matches 1.. run function banner:locations/barren_void

# Adjust counters
execute if score banner_cooldown bn.variables matches 1.. run scoreboard players remove banner_cooldown bn.variables 1

# Reset scoreboards after finalizing operations
scoreboard players set @a mc.talked_to_villager 0