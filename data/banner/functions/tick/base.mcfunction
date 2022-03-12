# Run timers
scoreboard players add $5t bn.timers 1
scoreboard players add $10t bn.timers 1
scoreboard players add $20t bn.timers 1
scoreboard players operation $5t bn.timers %= $5 bn.constants
scoreboard players operation $10t bn.timers %= $10 bn.constants
scoreboard players operation $20t bn.timers %= $20 bn.constants

# Run tick functions on players
execute as @a run function banner:tick/players
