import re
import sys

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
        value = parts[1] if len(parts) > 1 else None
        constants[name] = value

    return constants

def compare_enums(file1, file2):
    e1 = extract_enum_constants(file1)
    e2 = extract_enum_constants(file2)

    names1 = set(e1.keys())
    names2 = set(e2.keys())

    added = names2 - names1
    removed = names1 - names2
    common = names1 & names2

    print(f"Common elements ({len(common)}):")
    for name in sorted(common):
        v1, v2 = e1[name], e2[name]
        if v1 != v2:
            print(f"  {name}: {v1} -> {v2}")
        else:
            print(f"  {name} = {v1}")
    print()

    print(f"Added ({len(added)}): {sorted(added)}\n")
    print(f"Deleted ({len(removed)}): {sorted(removed)}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compare_enums.py enum1.cs enum2.cs")
        sys.exit(1)

    compare_enums(sys.argv[1], sys.argv[2])
