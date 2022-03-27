title @s[scores={bn.title_cooldown=-1}] times 0 5 2
title @s title {"text":""}
title @s subtitle {"text":"The Inferno Chamber","color":"#615959","bold":true}
execute as @s[scores={mc.talked_to_villager=1..}] run function banner:locations/the_inferno_chamber/tellraw
scoreboard players set @s bn.title_cooldown 10
