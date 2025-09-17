import re

input_path = "/mnt/data/fullGame.py"
output_path = "/mnt/data/fullGame_comments_aligned.py"

with open(input_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

output_lines = []
for i, line in enumerate(lines, start=1):
    if "#" in line:
        comment = re.split(r"#", line, maxsplit=1)[1].strip()
        output_lines.append(f"LINE {i}: {comment}\n")
    else:
        # Keep empty line placeholder to preserve alignment
        output_lines.append("\n")

with open(output_path, "w", encoding="utf-8") as f:
    f.writelines(output_lines)

output_path

