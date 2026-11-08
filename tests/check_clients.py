import vm_cmd
import json

cmd = """
export XDG_RUNTIME_DIR=/run/user/1000
for d in /run/user/1000/hypr/*; do
    if [ -d "$d" ] || [ -S "$d/.socket.sock" ]; then
        export HYPRLAND_INSTANCE_SIGNATURE=$(basename "$d")
        break
    fi
done
hyprctl -j clients
"""
out, err, rc = vm_cmd.run_ssh(cmd)
try:
    clients = json.loads(out)
    for c in clients:
        print(f"Class: {c.get('class')}, Title: {c.get('title')}, Floating: {c.get('floating')}, At: {c.get('at')}, Size: {c.get('size')}")
except Exception as e:
    print("Err parsing:", e, out)
