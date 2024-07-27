import os
import json

directories = [
		"data/entity_counter/function",
]
for path in directories:
	if not os.path.exists(path): os.makedirs(path)

count_file = open("data/entity_counter/function/count.mcfunction", "w")
with open("Entities.txt", "r") as f:
    entities = f.read()
entities = entities.split("\n")
if entities[-1] == "": entities = entities[:-1]
count_text = ""
for i, entity_id in enumerate(entities):
	entity_name = entity_id.replace("_", " ")
	entity_name = entity_name.title()
	entity_name = entity_name.replace(" ", "")
	count_text = count_text + f"execute if entity @e[type=minecraft:{entity_id}] store result score {entity_name} EntityCounter.Count if entity @e[type=minecraft:{entity_id}]\nexecute if score {entity_name} EntityCounter.Count matches 1.. unless entity @e[type=minecraft:{entity_id}] run scoreboard players reset {entity_name} EntityCounter.Count\n\n"
count_text = count_text + f"scoreboard players set Timeout EntityCounter.Timeout 0\n\nexecute if entity @e store result score Total EntityCounter.Count if entity @e\nexecute if score Total EntityCounter.Count matches 1.. unless entity @e run scoreboard players reset Total EntityCounter.Count\n\n"
count_text = count_text[:-2]
count_file.write(count_text)