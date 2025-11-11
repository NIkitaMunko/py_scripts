import re
import json

input_file = "items.lua"
output_file = "items.json"

pattern = re.compile(r'\[\s*"([^"]+)"\s*\]\s*=\s*"([^"]+)"')

keys = []

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        match = pattern.search(line)
        if match:
            key = match.group(1)
            keys.append(key)

data = {
    "name": "spawn_item",
    "command": "spawn_item",
    "value": {
        "required": True,
        "name": "Entity Type",
        "defaultValue": keys[0] if keys else "",
        "ngSelect": True,
        "description": "Select which item to spawn",
        "values": [
            {"name": k, "command": k} for k in keys
        ]
    },
    "disabled": False
}

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print(f"Found {len(keys)} elements. Result: {output_file}")
