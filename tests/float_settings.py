import vm_cmd

cmd = """
export XDG_RUNTIME_DIR=/run/user/1000
for d in /run/user/1000/hypr/*; do
    if [ -d "$d" ] || [ -S "$d/.socket.sock" ]; then
        export HYPRLAND_INSTANCE_SIGNATURE=$(basename "$d")
        break
    fi
done
hyprctl dispatch focuswindow class:kortex-settings
hyprctl dispatch togglefloating
hyprctl dispatch resizewindowpixel exact 1200 800,class:kortex-settings
hyprctl dispatch movewindowpixel exact 360 140,class:kortex-settings
"""
out, err, rc = vm_cmd.run_ssh(cmd)
print("OUT:", out)
print("ERR:", err)
