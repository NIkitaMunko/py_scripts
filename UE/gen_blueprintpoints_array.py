import re

input_file = "BluprintGeneratedClass_new.txt"
output_file = "actorPaths.lua"

pattern = re.compile(r'^(.*?):\s*(\/.*?(BP_[A-Za-z0-9_]+_C))$')

entries = {}

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        match = pattern.match(line)
        if match:
            full_path = match.group(2)
            class_name = match.group(3)
            if class_name.startswith("BP_") and class_name.endswith("_C"):
                key_name = class_name[3:-2].lower()
                entries[key_name] = full_path

sorted_entries = dict(sorted(entries.items()))

with open(output_file, "w", encoding="utf-8") as f:
    f.write("local actorPaths = {\n")
    for key, value in sorted_entries.items():
        if key[0].isdigit():
            f.write(f'    ["{key}"] = "{value}",\n')
        else:
            f.write(f'    {key} = "{value}",\n')
    f.write("}\n\nreturn actorPaths\n")

print(f"Done! Found {len(entries)} elements, result write to {output_file}")
