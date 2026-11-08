import vm_cmd
import time

cmd = """
export XDG_RUNTIME_DIR=/run/user/1000
export WAYLAND_DISPLAY=wayland-1
for d in /run/user/1000/hypr/*; do
    if [ -d "$d" ] || [ -S "$d/.socket.sock" ]; then
        export HYPRLAND_INSTANCE_SIGNATURE=$(basename "$d")
        break
    fi
done

# Restart grid so left panel has only 1 tab
/usr/local/bin/kortex-grid-init
sleep 1.5

# Open kortex-ai as a separate instance
kitty --single-instance=no --class kortex-ai -e /usr/local/bin/kortex-ai &
sleep 1.0

# Focus and ensure floating
hyprctl dispatch focuswindow "class:kortex-ai"
hyprctl dispatch setfloating active
hyprctl dispatch resizewindowpixel exact 1150 750,class:kortex-ai
hyprctl dispatch centerwindow
"""
out, err, rc = vm_cmd.run_ssh(cmd)
print("RC:", rc)
