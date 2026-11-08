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

hyprctl dispatch closewindow class:kortex-settings || true
hyprctl reload
sleep 0.5
kitty --class kortex-settings -e /usr/local/bin/kortex-settings &
sleep 1.2
"""
out, err, rc = vm_cmd.run_ssh(cmd)
print("OUT:", out)
