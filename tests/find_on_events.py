import re

with open("/usr/bin/Hyprland", "rb") as f:
    s = f.read()

for m in re.finditer(rb'window\.open', s):
    print(s[max(0, m.start()-40):min(len(s), m.start()+100)])
