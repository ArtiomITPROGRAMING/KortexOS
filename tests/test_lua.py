import subprocess

lua_code = """
print("HL keys:")
for k, v in pairs(hl) do
    print(k, type(v))
end

print("\\nWindow rule test:")
local res, err = pcall(function()
    local r = hl.window_rule({
        name = "test",
        match = { class = "test" },
        float = true,
        size = "100 100",
        move = "10 10"
    })
    print("rule created:", type(r))
    for k, v in pairs(r) do
        print(k, type(v))
    end
end)
if not res then
    print("Error:", err)
end
"""

# Hyprland doesn't expose a standalone lua CLI for hl, but hyprctl might have lua eval or we can inspect debug log!
