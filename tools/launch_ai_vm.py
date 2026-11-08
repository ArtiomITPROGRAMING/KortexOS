import vm_cmd
import time

cmd = """
export XDG_RUNTIME_DIR=/run/user/1000
export WAYLAND_DISPLAY=wayland-1
export HYPRLAND_INSTANCE_SIGNATURE=acc1aa0bfd4bd575dcb0f76c35ccf12b660a1ab9_1793892415_999265722

kitty --class kortex-ai -e /usr/local/bin/kortex-ai &
sleep 2
"""
out, err, rc = vm_cmd.run_ssh(cmd)
print("OUT:", out)
print("ERR:", err)
