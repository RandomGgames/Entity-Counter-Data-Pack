"""
This script creates a predicate.json file that checks
for if any of the listed objectives in the txt file
are not equal to 0
The first line is the file name!!
"""
import os
import json

"""LOADING DATA FROM ENTITIES.TXT"""
print("Loading entity list... ", end = "")
file_lines = open("entities.txt").readlines()
entities = []
for line in file_lines:
	line = line.replace("\n", "")
	entities.append(line)
print("Done")

"""CREATE DIRECTORIES"""
print("Creating directories... ", end = "")
directories = (
		"data/disable/functions",
		"data/entity_counter/functions/",
		"data/minecraft/tags/functions"
	)
for path in directories:
	if not os.path.exists(path):
		os.makedirs(path)
print("Done")

"""DISABLE FUNCTION"""
print("Generating disable function... ", end = "")
text = (
	"scoreboard objectives remove EntityCount\n\n"
	"datapack disable \"file/Entity Counter\"\n"
	"datapack disable \"file/Entity Counter.zip\"\n"
	)
#Create functions for each type and write the text to thems
with open(f"data/disable/functions/entity_counter.mcfunction", "w") as f:
	f.write(text)
print("Done")

"""TICK.JSON"""
print("Generating tick.json... ", end = "")
tag = {}
tag["values"] = ["entity_counter:tick"]
#Create functions for each type and write the text to thems
with open(f"data/minecraft/tags/functions/tick.json", "w") as f:
	json.dump(tag, f, indent="\t")
print("Done")

"""LOAD.JSON"""
print("Generating load.json... ", end = "")
tag = {}
tag["values"] = ["entity_counter:load"]
#Create functions for each type and write the text to thems
with open(f"data/minecraft/tags/functions/load.json", "w") as f:
	json.dump(tag, f, indent="\t")
print("Done")

"""COUNT.MCFUNCTION"""
print("Generating count.mcfunction... ", end = "")
text = (
	"execute store result score Total EntityCount if entity @e\n\n"

	"execute if entity @a store result score Players EntityCount if entity @a\n"
	"execute unless entity @a if score Players EntityCount matches 1.. run scoreboard players reset Players EntityCount\n\n"
)
for entity in entities:
	text = (
		f"{text}"
		f"execute if entity @e[type=minecraft:{entity}] store result score {entity} EntityCount if entity @e[type=minecraft:{entity}]\n"
		f"execute unless entity @e[type=minecraft:{entity}] if score {entity} EntityCount matches 1.. run scoreboard players reset {entity} EntityCount\n\n"
	)
text = f"{text[:-1]}"
with open(f"data/entity_counter/functions/count.mcfunction", "w") as f:
	f.write(text)
print("Done")

"""LOAD.MCFUNCTION"""
print("Generating load.mcfunction... ", end = "")
text = (
	"scoreboard objectives add EntityCount dummy\n"
)
#Create functions for each type and write the text to them
with open(f"data/entity_counter/functions/load.mcfunction", "w") as f:
	f.write(text)
print("Done")
