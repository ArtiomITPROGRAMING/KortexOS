import vm_cmd

cmd = """
export XDG_RUNTIME_DIR=/run/user/1000
for d in /run/user/1000/hypr/*; do
    if [ -d "$d" ] || [ -S "$d/.socket.sock" ]; then
        export HYPRLAND_INSTANCE_SIGNATURE=$(basename "$d")
        break
    fi
done

pkill -f "class kortex-ai" || true
pkill -f "class kortex-settings" || true
sleep 0.5

hyprctl dispatch exec "[float;size 1200 800;center] kitty --class kortex-ai -e /usr/local/bin/kortex-ai"
"""
out, err, rc = vm_cmd.run_ssh(cmd)
print("OUT:", out)
print("ERR:", err)
print("RC:", rc)
