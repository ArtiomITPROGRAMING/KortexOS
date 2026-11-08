import subprocess
import os
import glob

sig = os.path.basename(glob.glob("/run/user/1000/hypr/*")[0])
env = {
    "XDG_RUNTIME_DIR": "/run/user/1000",
    "HYPRLAND_INSTANCE_SIGNATURE": sig,
    "PATH": "/usr/local/bin:/usr/bin"
}

cmd = ["runuser", "-u", "kortex", "--", "hyprctl", "dispatch", "hl.dsp.window.resize({ x = 500, y = 300 })"]
res = subprocess.run(cmd, env=env, capture_output=True, text=True)
print("Returncode:", res.returncode)
print("Stdout:", res.stdout)
print("Stderr:", res.stderr)
