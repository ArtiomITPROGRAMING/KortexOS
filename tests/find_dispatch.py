import re

with open("/usr/bin/Hyprland", "rb") as f:
    s = f.read()

for m in re.finditer(b"dispatch", s):
    snippet = s[max(0, m.start()-40):min(len(s), m.start()+80)]
    if b"hl." in snippet:
        print(snippet)
