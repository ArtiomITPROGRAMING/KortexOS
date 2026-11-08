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

# Kill any stray popups
pkill -f "kortex-settings" || true
pkill -f "kortex-ai" || true
sleep 0.5

# Reinit clean grid
/usr/local/bin/kortex-grid-init
sleep 1.5

# Launch single clean settings popup
/usr/local/bin/kortex-open settings &
sleep 1.5
"""
out, err, rc = vm_cmd.run_ssh(cmd)
print("RC:", rc)
