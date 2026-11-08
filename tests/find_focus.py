import re

with open("/usr/bin/Hyprland", "rb") as f:
    s = f.read()

for m in re.finditer(rb'hl\.dsp\.focus|hl\.focus', s):
    print(s[max(0, m.start()-20):min(len(s), m.start()+80)])
