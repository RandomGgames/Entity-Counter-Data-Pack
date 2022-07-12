import os
import json
import shutil

if os.path.exists("Entity_Counter"): shutil.rmtree("Entity_Counter")

directories = [
		"data/functions",
		"data/minecraft/tags/functions",
		"data/disable/functions",
]
for path in directories:
	if not os.path.exists(path): os.makedirs(path)

with open("data/disable/functions/entity_counter.mcfunction", "w") as f: f.write(f"scoreboard objectives remove EntityCount\nscoreboard objectives remove EntityCounterTimeout\n\ndatapack disable \"file/Entity_Counter\"\ndatapack disable \"file/Entity_Counter.zip\"")
with open("pack.mcmeta", "w") as f: json.dump({"pack": {"pack_format": 10,"description": "RandomGgames' Entity Counter Data Pack"}}, f, indent = "\t")
with open("data/minecraft/tags/functions/load.json", "w") as f: json.dump({"values": ["entity_counter:load"]}, f, indent = "\t")
with open("data/functions/load.mcfunction", "w") as f: f.write(f"scoreboard objectives add EntityCount dummy\nscoreboard objectives add EntityCounterTimeout dummy\nscoreboard objectives setdisplay sidebar EntityCount")
with open("data/minecraft/tags/functions/tick.json", "w") as f: json.dump({"values": ["entity_counter:tick"]}, f, indent = "\t")
with open("data/functions/tick.mcfunction", "w") as f: f.write(f"scoreboard players add Interval EntityCounterTimeout 0\nexecute unless score Interval EntityCounterTimeout matches 1.. run scoreboard players set Interval EntityCounterTimeout 5\n\nscoreboard players add Timeout EntityCounterTimeout 1\nexecute if score Timeout EntityCounterTimeout >= Interval EntityCounterTimeout run function entity_counter:count")
count_file = open("data/functions/count.mcfunction", "a")

with open("Entities.txt", "r") as f: entities = f.read()
entities = entities.split("\n")
if entities[-1] == "": entities = entities[:-1]

for i, entity_id in enumerate(entities):
	entity_name = entity_id.replace("_", " ")
	entity_name = entity_name.title()
	entity_name = entity_name.replace(" ", "")
	
	count_file.write(f"execute if entity @e[type=minecraft:{entity_id}] store result score {entity_name} EntityCount if entity @e[type=minecraft:{entity_id}]\nexecute if score {entity_name} EntityCount matches 1.. unless entity @e[type=minecraft:{entity_id}] run scoreboard players reset {entity_name} EntityCount\n\n")

count_file.write(f"scoreboard players set Timeout EntityCounterTimeout 0\n\nexecute if entity @e store result score Total EntityCount if entity @e\nexecute if score Total EntityCount matches 1.. unless entity @e run scoreboard players reset Total EntityCount\n\n")
