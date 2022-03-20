# Ensure scoreboards are preloaded
scoreboard players add @s bn.title_cooldown 0

# Operate on title scoreboards
title @s[scores={bn.title_cooldown=0}] times 10 80 10
execute if score @s bn.title_cooldown matches 0.. run scoreboard players remove @s bn.title_cooldown 1

# Show titles
execute at 4c2eec26-4ee2-4012-917b-90bef8d038fc if entity @s[distance=..10] at @s if predicate banner:looking_at/azalea_ruin run function banner:locations/azalea_ruin/title
execute at 14297741-f12e-4094-b81f-e7f00a4388ca if entity @s[distance=..10] at @s if predicate banner:looking_at/the_monument run function banner:locations/the_monument/title
execute at dbc5c80b-aabb-46fd-93e0-8fe24b96cbc1 if entity @s[distance=..10] at @s if predicate banner:looking_at/the_tainted_oasis run function banner:locations/the_tainted_oasis/title

# Reset scoreboards after finalizing operations
scoreboard players set @s mc.talked_to_villager 0
