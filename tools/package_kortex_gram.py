import os
import shutil
import tarfile

tmp_dir = os.path.join(os.environ["TEMP"], "kortex_gram_pkg")
if os.path.exists(tmp_dir):
    shutil.rmtree(tmp_dir)

web_dest = os.path.join(tmp_dir, "usr", "share", "kortex-gram", "web")
bin_dest = os.path.join(tmp_dir, "usr", "local", "bin")
app_dest = os.path.join(tmp_dir, "usr", "share", "applications")

os.makedirs(web_dest, exist_ok=True)
os.makedirs(bin_dest, exist_ok=True)
os.makedirs(app_dest, exist_ok=True)

# 1. Copy web assets
src_web = os.path.join("kortex_gram", "build", "web")
for item in os.listdir(src_web):
    s = os.path.join(src_web, item)
    d = os.path.join(web_dest, item)
    if os.path.isdir(s):
        shutil.copytree(s, d)
    else:
        shutil.copy2(s, d)

# 2. Write launcher
launcher_content = """#!/usr/bin/env bash
PORT=8765
if ! pgrep -f "http.server 8765" >/dev/null 2>&1; then
    nohup python3 -m http.server 8765 --directory /usr/share/kortex-gram/web --bind 127.0.0.1 >/dev/null 2>&1 &
    sleep 0.4
fi
export MOZ_ENABLE_WAYLAND=1
if command -v firefox >/dev/null 2>&1; then
    exec firefox --new-window "http://127.0.0.1:8765" --class "kortex-gram" "$@"
elif command -v chromium >/dev/null 2>&1; then
    exec chromium --app="http://127.0.0.1:8765" --class="kortex-gram" "$@"
else
    xdg-open "http://127.0.0.1:8765"
fi
"""
launcher_path = os.path.join(bin_dest, "kortex-gram")
with open(launcher_path, "w", newline="\n", encoding="utf-8") as f:
    f.write(launcher_content)

# 3. Write desktop entry
desktop_content = """[Desktop Entry]
Name=KortexGram
Comment=Secure Real-Time E2EE Messenger
Exec=kortex-gram
Icon=telegram
Terminal=false
Type=Application
Categories=Network;InstantMessaging;
"""
desktop_path = os.path.join(app_dest, "kortex-gram.desktop")
with open(desktop_path, "w", newline="\n", encoding="utf-8") as f:
    f.write(desktop_content)

# 4. Create tar.gz
out_tar = os.path.join("kortex_gram", "kortex-gram-v1.0.0-linux.tar.gz")
with tarfile.open(out_tar, "w:gz") as tar:
    for root, dirs, files in os.walk(tmp_dir):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, tmp_dir)
            tar_info = tar.gettarinfo(full_path, arcname=rel_path)
            if "bin" in rel_path:
                tar_info.mode = 0o755
            else:
                tar_info.mode = 0o644
            with open(full_path, "rb") as f_obj:
                tar.addfile(tar_info, f_obj)

print("Created bundle:", out_tar, os.path.getsize(out_tar), "bytes")
