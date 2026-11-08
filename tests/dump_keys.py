import re

with open("/usr/bin/Hyprland", "rb") as f:
    data = f.read()

# Find occurrences of "WINDOW_RULE_EFFECT_DESCS"
pos = data.find(b"WINDOW_RULE_EFFECT_DESCS")
print("pos:", pos)

# Find all null-terminated strings
strings = re.findall(b"[\x20-\x7e]{3,50}", data)
for s in strings:
    s_str = s.decode("latin1")
    if any(k in s_str for k in ["move", "size", "exact", "float", "tile", "pin", "fullscreen"]):
        if any(x in s_str for x in ["rule", "window", "effect", "match"]):
            print(s_str)
