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

# Azalea Ruin [South]
execute positioned -47 172 18 run summon villager ~0.2 ~-0.9 ~-0.5 {Silent:1b,Invulnerable:1b,UUID:[I;1278143526,1323450386,-1854172994,-120571652],NoAI:1b,CanPickUpLoot:0b,ActiveEffects:[{Id:14b,Amplifier:0b,Duration:20000000,ShowParticles:0b}],Offers:{}}
execute positioned -47 172 18 run summon villager ~-0.2 ~-0.9 ~-0.5 {Silent:1b,Invulnerable:1b,UUID:[I;-325862411,-401389423,-1525807663,-3376499],NoAI:1b,CanPickUpLoot:0b,ActiveEffects:[{Id:14b,Amplifier:0b,Duration:20000000,ShowParticles:0b}],Offers:{}}

# The Monument [North]
execute positioned 15 203 6 run summon villager ~0.2 ~-0.9 ~0.5 {Silent:1b,Invulnerable:1b,UUID:[I;338261825,-248627052,-1205868560,172198090],NoAI:1b,CanPickUpLoot:0b,ActiveEffects:[{Id:14b,Amplifier:0b,Duration:20000000,ShowParticles:0b}],Offers:{}}
execute positioned 15 203 6 run summon villager ~-0.2 ~-0.9 ~0.5 {Silent:1b,Invulnerable:1b,UUID:[I;-818525857,-1574286318,-1965160796,1136995985],NoAI:1b,CanPickUpLoot:0b,ActiveEffects:[{Id:14b,Amplifier:0b,Duration:20000000,ShowParticles:0b}],Offers:{}}

# The Tainted Oasis [North]
execute positioned -79 167 95 run summon villager ~0.2 ~-0.9 ~0.5 {Silent:1b,Invulnerable:1b,UUID:[I;-607795189,-1430567171,-1813999646,1268173761],NoAI:1b,CanPickUpLoot:0b,ActiveEffects:[{Id:14b,Amplifier:0b,Duration:20000000,ShowParticles:0b}],Offers:{}}
execute positioned -79 167 95 run summon villager ~-0.2 ~-0.9 ~0.5 {Silent:1b,Invulnerable:1b,UUID:[I;-2017597218,-1849276994,-2002516019,1062670431],NoAI:1b,CanPickUpLoot:0b,ActiveEffects:[{Id:14b,Amplifier:0b,Duration:20000000,ShowParticles:0b}],Offers:{}}
