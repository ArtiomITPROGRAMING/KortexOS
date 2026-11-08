with open("/usr/bin/Hyprland", "rb") as f:
    s = f.read()

pos = s.find(b"WINDOW_RULE_EFFECT_DESCS")
print("Around pos:")
print(s[pos:pos+4000])
