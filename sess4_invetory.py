inventory = {
    "gold": 500,
    "pouch": ["flint,", "twine", "gemstone"],
    "backpack": ["xylophone", "dagger", "bedroll", "bread loaf"]
}
new_key = "pocket"
new_value = ["seashell", "strange berry", "lint"]
inventory[new_key] = new_value
inventory["backpack"].remove("dagger")
inventory["gold"] += 50
print(inventory)