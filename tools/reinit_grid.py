import vm_cmd

cmd = """
export XDG_RUNTIME_DIR=/run/user/1000
for d in /run/user/1000/hypr/*; do
    if [ -d "$d" ] || [ -S "$d/.socket.sock" ]; then
        export HYPRLAND_INSTANCE_SIGNATURE=$(basename "$d")
        break
    fi
done

hyprctl dispatch exec /usr/local/bin/kortex-grid-init
"""
out, err, rc = vm_cmd.run_ssh(cmd)
print("RC:", rc)
