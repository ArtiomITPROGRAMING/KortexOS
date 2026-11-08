import subprocess

test_cases = [
    ('move_str', 'move = "100 100"'),
    ('move_exact', 'move = "exact 100 100"'),
    ('move_expr', 'move = "monitor_w*0.2 monitor_h*0.04"'),
    ('size_str', 'size = "500 500"'),
    ('size_exact', 'size = "exact 500 500"'),
    ('min_max_size', 'minsize = "500 500", maxsize = "500 500"'),
    ('min_size_num', 'min_size = { 500, 500 }'),
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
