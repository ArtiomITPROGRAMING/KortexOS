import re

with open("/usr/bin/Hyprland", "rb") as f:
    s = f.read()

# search for "window."
matches = set(re.findall(rb"window\.[a-z_]+", s))
for m in sorted(matches):
    print(m.decode("ascii"))
