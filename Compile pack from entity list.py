import os
import json
import shutil

directories = [
		"data/entity_counter/functions",
		"data/minecraft/tags/functions",
		"data/disable/functions",
]
for path in directories:
	if not os.path.exists(path): os.makedirs(path)

with open("data/disable/functions/entity_counter.mcfunction", "w") as f: f.write(f"scoreboard objectives remove EntityCounter.Count\nscoreboard objectives remove EntityCounter.Timeout\n\ndatapack disable \"file/EntityCounter\"\ndatapack disable \"file/EntityCounter.zip\"")
with open("pack.mcmeta", "w") as f: json.dump({"pack": {"pack_format": 10,"description": "RandomGgames' Entity Counter Data Pack"}}, f, indent = "\t")
with open("data/minecraft/tags/functions/load.json", "w") as f: json.dump({"values": ["entity_counter:load"]}, f, indent = "\t")
with open("data/entity_counter/functions/load.mcfunction", "w") as f: f.write(f"scoreboard objectives add EntityCounter.Count dummy [{{\"text\":\"Entity Count\"}}]\nscoreboard objectives add EntityCounter.Timeout dummy\nscoreboard objectives setdisplay sidebar EntityCounter.Count")
with open("data/minecraft/tags/functions/tick.json", "w") as f: json.dump({"values": ["entity_counter:tick"]}, f, indent = "\t")
with open("data/entity_counter/functions/tick.mcfunction", "w") as f: f.write(f"scoreboard players add Interval EntityCounter.Timeout 0\nexecute unless score Interval EntityCounter.Timeout matches 1.. run scoreboard players set Interval EntityCounter.Timeout 5\n\nscoreboard players add Timeout EntityCounter.Timeout 1\nexecute if score Timeout EntityCounter.Timeout >= Interval EntityCounter.Timeout run function EntityCounter:count")

count_file = open("data/entity_counter/functions/count.mcfunction", "w")
with open("Entities.txt", "r") as f: entities = f.read()
entities = entities.split("\n")
if entities[-1] == "": entities = entities[:-1]
count_text = ""
for i, entity_id in enumerate(entities):
	entity_name = entity_id.replace("_", " ")
	entity_name = entity_name.title()
	entity_name = entity_name.replace(" ", "")
	count_text = count_text + f"execute if entity @e[type=minecraft:{entity_id}] store result score {entity_name} EntityCounter.Count if entity @e[type=minecraft:{entity_id}]\nexecute if score {entity_name} EntityCounter.Count matches 1.. unless entity @e[type=minecraft:{entity_id}] run scoreboard players reset {entity_name} EntityCounter.Count\n\n"
count_text = count_text + f"scoreboard players set Timeout EntityCounter.Timeout 0\n\nexecute if entity @e store result score Total EntityCounter.Count if entity @e\nexecute if score Total EntityCounter.Count matches 1.. unless entity @e run scoreboard players reset Total EntityCounter.Count\n\n"
count_file.write(count_text)
