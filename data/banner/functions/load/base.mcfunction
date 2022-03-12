# Create scoreboards
scoreboard objectives add bn.title_cooldown dummy
scoreboard objectives add bn.variables dummy
scoreboard objectives add mc.talked_to_villager minecraft.custom:minecraft.talked_to_villager

# Ensure villagers exist
execute positioned 8.50 -59.00 -4.62 align x align y align z run summon villager ~0.7 ~0.1 ~ {Silent:1b,Invulnerable:1b,UUID:[I;-2017597218,-1849276994,-2002516019,1062670431],NoAI:1b,CanPickUpLoot:0b,ActiveEffects:[{Id:14b,Amplifier:0b,Duration:20000000,ShowParticles:0b}],Offers:{}}
execute positioned 8.50 -59.00 -4.62 align x align y align z run summon villager ~0.3 ~0.1 ~ {Silent:1b,Invulnerable:1b,UUID:[I;-607795189,-1430567171,-1813999646,1268173761],NoAI:1b,CanPickUpLoot:0b,ActiveEffects:[{Id:14b,Amplifier:0b,Duration:20000000,ShowParticles:0b}],Offers:{}}
