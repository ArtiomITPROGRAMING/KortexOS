import subprocess
import os
import glob

sig = os.path.basename(glob.glob("/run/user/1000/hypr/*")[0])
env = {
    "XDG_RUNTIME_DIR": "/run/user/1000",
    "HYPRLAND_INSTANCE_SIGNATURE": sig,
    "PATH": "/usr/local/bin:/usr/bin"
}

def run_hl(code):
    cmd = ["runuser", "-u", "kortex", "--", "hyprctl", "dispatch", code]
    r = subprocess.run(cmd, env=env, capture_output=True, text=True)
    return r.stdout.strip()

tests = [
    'hl.dsp.focus({ window = "address:0x5603e46c0650" })',
    'hl.dsp.focus({ window = "kortex-term" })',
    'hl.dsp.focus({ window = "class:kortex-term" })',
    'hl.dsp.focus({ class = "kortex-term" })',
    'hl.dsp.focuswindow("kortex-term")',
    'hl.dsp.focuswindow("class:kortex-term")',
    'hl.dsp.focus({ address = "0x5603e46c0650" })',
    'hl.dsp.focus({ address = "5603e46c0650" })',
]

for t in tests:
    res = run_hl(t)
    print(f"{t} -> {res}")
