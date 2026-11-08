import vm_cmd
import time

cmd = """
export XDG_RUNTIME_DIR=/run/user/1000
for d in /run/user/1000/hypr/*; do
    if [ -d "$d" ] || [ -S "$d/.socket.sock" ]; then
        export HYPRLAND_INSTANCE_SIGNATURE=$(basename "$d")
        break
    fi
done

pkill -f "class kortex-ai" || true
hyprctl reload
sleep 0.5
nohup kitty --class kortex-ai -e /usr/local/bin/kortex-ai >/dev/null 2>&1 &
sleep 1.2

# Check floating status
hyprctl dispatch focuswindow class:kortex-ai
hyprctl dispatch setfloating active
hyprctl dispatch resizewindowpixel exact 1220 800,class:kortex-ai
hyprctl dispatch movewindowpixel exact 350 140,class:kortex-ai
"""
out, err, rc = vm_cmd.run_ssh(cmd)
print("RC:", rc)
