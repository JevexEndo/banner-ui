# Create scoreboards
scoreboard objectives add bn.constants dummy
scoreboard objectives add bn.timers dummy
scoreboard objectives add bn.title_cooldown dummy
scoreboard objectives add bn.variables dummy
scoreboard objectives add mc.talked_to_villager minecraft.custom:minecraft.talked_to_villager

# Create constants
scoreboard players set $2 bn.constants 2
scoreboard players set $5 bn.constants 5
scoreboard players set $10 bn.constants 10
scoreboard players set $20 bn.constants 20

#> Summon Offsets
#> Facing   1st Villager        2nd Villager
#  North    ~0.2 ~-0.9 ~0.5     ~-0.2 ~-0.9 ~0.5
#  East     ~-0.5 ~-0.9 ~0.2    ~-0.5 ~-0.9 ~-0.2
#  South    ~0.2 ~-0.9 ~-0.5    ~-0.2 ~-0.9 ~-0.5
#  West     ~0.5 ~-0.9 ~0.2     ~0.5 ~-0.9 ~-0.2

function banner:load/summon
