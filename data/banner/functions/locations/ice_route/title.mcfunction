title @s[scores={bn.title_cooldown=-1}] times 0 5 2
title @s title {"text":""}
title @s subtitle {"text":"Ice Route","color":"#ACFFA6","bold":true}
execute as @s[scores={mc.talked_to_villager=1..}] run function banner:locations/ice_route/tellraw
scoreboard players set @s bn.title_cooldown 10
