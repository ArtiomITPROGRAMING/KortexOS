import vm_cmd

cmd = """
export XDG_RUNTIME_DIR=/run/user/1000
export WAYLAND_DISPLAY=wayland-1
kitty --class kortex-ai /bin/bash -c '/usr/local/bin/kortex-ai >/tmp/ai_out.log 2>&1' &
sleep 1
cat /tmp/ai_out.log
"""
out, err, rc = vm_cmd.run_ssh(cmd)
print("OUT:", out)
