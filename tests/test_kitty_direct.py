import vm_cmd

cmd = """
export XDG_RUNTIME_DIR=/run/user/1000
export WAYLAND_DISPLAY=wayland-1
for d in /run/user/1000/hypr/*; do
    if [ -d "$d" ] || [ -S "$d/.socket.sock" ]; then
        export HYPRLAND_INSTANCE_SIGNATURE=$(basename "$d")
        break
    fi
done

kitty -o allow_remote_control=yes --class kortex-ai bash -c "python3 /usr/local/bin/kortex-ai" >/tmp/kitty_ai.log 2>&1 &
sleep 1.5
cat /tmp/kitty_ai.log
"""
out, err, rc = vm_cmd.run_ssh(cmd)
print("OUT:", out)
print("ERR:", err)
