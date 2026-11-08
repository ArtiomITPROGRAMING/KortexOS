import vm_cmd

cmd = """
export XDG_RUNTIME_DIR=/run/user/1000
export WAYLAND_DISPLAY=wayland-1
kitty --class kortex-ai sh -c '/usr/local/bin/kortex-ai 2>/tmp/ai_err.log' &
sleep 1
cat /tmp/ai_err.log
"""
out, err, rc = vm_cmd.run_ssh(cmd)
print("OUT:", out)
print("ERR:", err)
