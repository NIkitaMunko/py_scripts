import re
import json

targets = ['BigGloom', 'DeathChomper', 'DoomJalapeno', 'DoomSeaShroom', 'FireSunshroom_a', 'FireSunshroom_b', 'FireSunshroom_c', 'HelmetGatling', 'IceSeashroom', 'IronMelon', 'KelpNut', 'LanternNut', 'LuckyBlover', 'MagnetMelon', 'NutFume', 'NutPot', 'NutPumpkin', 'PeaFume', 'PeaPumpkin', 'PortalMelon', 'PuffSeaShroom', 'ScaredyNut', 'SeaHypno', 'SmallUmbrella', 'SunJalapeno', 'SunStar', 'ThreeNut', 'TorchSunflower', 'Tower_lilyPad', 'Tower_squashNut', 'Tower_threeMine', 'TreasureMine', 'UltimateLunarCabbage', 'UltimateMinigun', 'UltimateRedLunar', 'UltimateSunflower']
def extract_enum_constants(filename):
    with open(filename, encoding="utf-8") as f:
        text = f.read()

    match = re.search(r'enum\s+\w+\s*\{([\s\S]*?)\}', text)
    if not match:
        return {}

    body = match.group(1)

    constants = {}
    for line in body.splitlines():
        line = line.strip()
        if not line or line.startswith("//"):
            continue
        line = re.split(r'//|/\*', line)[0].strip().rstrip(',')
        if not line:
            continue
        parts = [p.strip() for p in line.split("=", 1)]
        name = parts[0]
        value = int(parts[1], 0) if len(parts) > 1 else None
        constants[name] = value
    return constants

def make_json(enumfile, outfile):
    enum_map = extract_enum_constants(enumfile)

    results = []
    for name in targets:
        if name not in enum_map:
            print(f"⚠️ {name} not found in enum")
            continue
        obj = {
            "name": f"Spawn {name}",
            "command": f"spawnplant?effect={enum_map[name]}",
            "description": f"Spawn {name}",
            "disabled": False,
            "category":"NEW"
        }
        results.append(obj)

    with open(outfile, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"JSON saved to {outfile}")

if __name__ == "__main__":
    # example: python script.py PlantType.cs output.json
    import sys
    if len(sys.argv) != 3:
        print("Usage: python script.py PlantType.cs output.json")
        sys.exit(1)
    make_json(sys.argv[1], sys.argv[2])
