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

# Close any settings windows
pkill -f "kortex-settings" || true
pkill -f "kortex-ai" || true
sleep 0.5

# Launch AI Assistant
/usr/local/bin/kortex-open ai
"""
out, err, rc = vm_cmd.run_ssh(cmd)
print("RC:", rc)
