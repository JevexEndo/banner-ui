# Ensure scoreboards are preloaded
scoreboard players add @s bn.title_cooldown 0

# Operate on scoreboard values
execute at @s if score @s mc.talked_to_villager matches 1.. if score @s bn.title_cooldown matches 0 if predicate banner:looking_at/barren_void_banner run function banner:locations/barren_void

# Adjust counters
execute if score @s bn.title_cooldown matches 1.. run scoreboard players remove @s bn.title_cooldown 1

# Reset scoreboards after finalizing operations
scoreboard players set @s mc.talked_to_villager 0
