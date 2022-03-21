# Ensure scoreboards are preloaded
scoreboard players add @s bn.title_cooldown 0

# Operate on title scoreboards
title @s[scores={bn.title_cooldown=0}] times 10 80 10
execute if score @s bn.title_cooldown matches 0.. run scoreboard players remove @s bn.title_cooldown 1

# Show titles
function banner:tick/banners

# Reset scoreboards after finalizing operations
scoreboard players set @s mc.talked_to_villager 0
