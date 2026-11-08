import sys
sys.stdout.reconfigure(encoding='utf-8')
import vm_cmd

cmd = """
export XDG_RUNTIME_DIR=/run/user/1000
export WAYLAND_DISPLAY=wayland-1
kitty --class kortex-settings -e /usr/local/bin/kortex-settings >/tmp/kitty_settings.log 2>&1 &
sleep 1
cat /tmp/kitty_settings.log
"""
out, err, rc = vm_cmd.run_ssh(cmd)
print("OUT:", out)
print("ERR:", err)
