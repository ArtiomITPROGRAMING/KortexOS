import subprocess

test_cases = [
    ('move_exact_percent', 'move = "exact 20% 4%"'),
    ('size_exact_percent', 'size = "exact 57% 62%"'),
    ('move_exact_pixels', 'move = "exact 384 43"'),
    ('size_exact_pixels', 'size = "exact 1094 670"'),
    ('move_expr', 'move = "monitor_w*0.20 monitor_h*0.04"'),
]

for name, rule_body in test_cases:
    content = f"""
local r = hl.window_rule({{
    name = "{name}",
    match = {{ class = "test" }},
    float = true,
    {rule_body}
}})
"""
    with open("/tmp/test_case.lua", "w") as f:
        f.write(content)
    
    res = subprocess.run(["Hyprland", "--i-am-really-stupid", "-c", "/tmp/test_case.lua", "--verify-config"], capture_output=True, text=True)
    success = "config ok" in res.stdout or (res.returncode == 0 and "error" not in res.stdout.lower() and "error" not in res.stderr.lower())
    print(f"Test {name}: {'OK' if success else 'FAIL'}")
    if not success:
        print("  Stdout:", res.stdout.strip())
        print("  Stderr:", res.stderr.strip())
