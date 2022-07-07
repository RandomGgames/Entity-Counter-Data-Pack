# Entity Counter Data Pack
This data pack generates a scoreboard that stores the count of every entity in the world, which is automatically displayed on the sidebar when first loaded. It updates (by default) every 5 ticks.

To change the update interval, use the command `/scoreboard players set Interval EntityCounterTimeout #` where # is a number > 0. This number is the ticks to wait before entities are counted again. A larger number helps to reduce lag.

To disable, either just hide the sidebar objective (it will still be running in the background) with the command  `/scoreboard objectives setdisplay sidebar`

or completly disable the data pack using the command `/datapack disable "file/EntityCounter"`

# How to Install
Download the data pack and either drag and drop into the data pack selection screen or drop into your save's datapacks folder than reload it.
