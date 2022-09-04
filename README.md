# Entity Counter Data Pack
This data pack generates a scoreboard that stores the count of every entity in the world, which is automatically displayed on the sidebar when first loaded. It updates (by default) every 5 ticks.

To change the update interval, use the command `/scoreboard players set Interval EntityCounter.Timeout #` where # is a number > 0. This number is the ticks to wait before entities are counted again. A larger number helps to reduce lag. 1 is every tick.

To disable, either hide the sidebar objective (it will still be running in the background) with the command  `/scoreboard objectives setdisplay sidebar` or completly disable the data pack using the command `/datapack disable "file/EntityCounter.zip"`
