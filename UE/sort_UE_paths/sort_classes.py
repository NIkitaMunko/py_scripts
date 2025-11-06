import re
from pathlib import Path

INPUT_FILE = "actorPaths.lua"

ZOMBIE_FILE = "actorZombiePaths.lua"
ITEMS_FILE = "actorItemsPaths.lua"
OTHER_FILE = "actorOtherPaths.lua"

ENTRY_PATTERN = re.compile(
    r'\s*(?:\["([^"]+)"\]|([a-zA-Z0-9_]+))\s*=\s*"([^"]+)"\s*,?'
)

def parse_lua_table(lua_text: str):
    result = {}
    for match in ENTRY_PATTERN.findall(lua_text):
        key = match[0] if match[0] else match[1]
        value = match[2]
        result[key] = value
    return result

def write_lua_file(filename: str, data: dict, table_name: str):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"local {table_name} = {{\n")
        for k, v in sorted(data.items()):
            f.write(f'    ["{k}"] = "{v}",\n')
        f.write("}\n\n")
        f.write(f"return {table_name}\n")

def main():
    lua_text = Path(INPUT_FILE).read_text(encoding="utf-8")

    data = parse_lua_table(lua_text)

    zombies = {k: v for k, v in data.items() if v.startswith("/Game/AI/Zombies/")}
    items   = {k: v for k, v in data.items() if v.startswith("/Game/Inventory/Items/")}
    others  = {k: v for k, v in data.items() if k not in zombies and k not in items}

    write_lua_file(ZOMBIE_FILE, zombies, "actorZombiePaths")
    write_lua_file(ITEMS_FILE, items, "actorItemsPaths")
    write_lua_file(OTHER_FILE, others, "actorOtherPaths")

    print(f"Done:")
    print(f"  Zombies: {len(zombies)}")
    print(f"  Items:   {len(items)}")
    print(f"  Others:  {len(others)}")

if __name__ == "__main__":
    main()
