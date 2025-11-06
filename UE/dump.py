import re

input_file = "BluprintGeneratedClass.txt"
output_file = "BluprintGeneratedClass_new.txt"

pattern = re.compile(r"BlueprintGeneratedClass\s+([^\s\[]+)")

with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
    for line in infile:
        if "] BlueprintGeneratedClass" in line:
            match = pattern.search(line)
            if match:
                full_path = match.group(1)
                last_part = full_path.split(".")[-1]
                base_name = last_part[:-2] if last_part.endswith("_C") else last_part
                outfile.write(f"{base_name}: {full_path}\n")
