import vm_cmd

cmd = """
export XDG_RUNTIME_DIR=/run/user/1000
for d in /run/user/1000/hypr/*; do
    if [ -d "$d" ] || [ -S "$d/.socket.sock" ]; then
        export HYPRLAND_INSTANCE_SIGNATURE=$(basename "$d")
        break
    fi
done

hyprctl dispatch "hl.dsp.focus({ window = 'class:kortex-ai' })"
hyprctl dispatch "hl.dsp.window.toggle_floating()"
hyprctl dispatch "hl.dsp.window.resize({ x = 1200, y = 800 })"
hyprctl dispatch "hl.dsp.window.move({ x = 360, y = 140 })"
"""
out, err, rc = vm_cmd.run_ssh(cmd)
print("RC:", rc)
print("OUT:", out.replace('\u2192', '->'))
