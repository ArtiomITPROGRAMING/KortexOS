import subprocess
import json
import os
import glob
import time

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

# Get clients
out = subprocess.run(["runuser", "-u", "kortex", "--", "hyprctl", "-j", "clients"], env=env, capture_output=True, text=True)
clients = json.loads(out.stdout)
print("Found clients:", len(clients))

# Get monitor dimensions
mon_out = subprocess.run(["runuser", "-u", "kortex", "--", "hyprctl", "-j", "monitors"], env=env, capture_output=True, text=True)
monitors = json.loads(mon_out.stdout)
mw = monitors[0]["width"]
mh = monitors[0]["height"]
print(f"Monitor: {mw}x{mh}")

# Target layout percentages
# 1. kortex-pulse: move 0.5% 4%, size 19% 95%
# 2. kortex-term:  move 20% 4%,  size 57% 62%
# 3. kortex-net:   move 77.5% 4%, size 22% 62%
# 4. kortex-files: move 20% 67%, size 33% 32%
# 5. kortex-kb:    move 53.5% 67%, size 46% 32%

layout = {
    "kortex-pulse": (int(mw * 0.005), int(mh * 0.04), int(mw * 0.19), int(mh * 0.95)),
    "kortex-term":  (int(mw * 0.20),  int(mh * 0.04), int(mw * 0.57), int(mh * 0.62)),
    "kortex-net":   (int(mw * 0.775), int(mh * 0.04), int(mw * 0.22), int(mh * 0.62)),
    "kortex-files": (int(mw * 0.20),  int(mh * 0.67), int(mw * 0.33), int(mh * 0.32)),
    "kortex-kb":    (int(mw * 0.535), int(mh * 0.67), int(mw * 0.46), int(mh * 0.32)),
}

for cls, (x, y, w, h) in layout.items():
    print(f"Aligning {cls} to {x},{y} {w}x{h}")
    f_res = run_hl(f"hl.dsp.focus({{ window = 'class:{cls}' }})")
    time.sleep(0.05)
    res_resize = run_hl(f"hl.dsp.window.resize({{ x = {w}, y = {h} }})")
    time.sleep(0.05)
    res_move = run_hl(f"hl.dsp.window.move({{ x = {x}, y = {y} }})")
    time.sleep(0.05)
    print(f"  Focus: {f_res}, Resize: {res_resize}, Move: {res_move}")

# Focus main terminal at the end
run_hl("hl.dsp.focus({ window = 'class:kortex-term' })")
