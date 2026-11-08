import paramiko
import os

def sync_vm():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("127.0.0.1", port=2222, username="kortex", password="1", timeout=10)
    sftp = ssh.open_sftp()

    base_local = "c:/Users/Lenovo/KortexOS/profile/airootfs"

    # Files to copy to /tmp and then sudo mv
    binaries = [
        "kortex-layout", "kortex-profile", "kortex-help-hud", "kortex-plugin-status",
        "kortex-settings", "kortex-setting", "kortex-menu", "kortex-grid-align", "kortex-grid-init",
        "kortex-theme-apply", "kortex-theme", "kortex-wallpaper", "kortex-spotlight", "kortex-oobe", "kortex-install",
        "kortex-tour", "kortex-guide", "kortex-music", "kortex-store", "kortex-open", "start-hyprland", "Hyprland"
    ]
    for b in binaries:
        lp = os.path.join(base_local, "usr/local/bin", b)
        if os.path.exists(lp):
            sftp.put(lp, f"/tmp/{b}")
            print(f"Uploaded {b}")

    # Configs
    configs = [
        ("kortex/config.json", "/home/kortex/.config/kortex/config.json"),
        ("kortex/master-state.json", "/home/kortex/.config/kortex/master-state.json"),
        ("hypr/hyprland.conf", "/home/kortex/.config/hypr/hyprland.conf"),
        ("hypr/binds.conf", "/home/kortex/.config/hypr/binds.conf"),
        ("hypr/theme.conf", "/home/kortex/.config/hypr/theme.conf"),
        ("waybar/config", "/home/kortex/.config/waybar/config"),
        ("waybar/style.css", "/home/kortex/.config/waybar/style.css")
    ]
    for rel, dest in configs:
        lp = os.path.join(base_local, "etc/skel/.config", rel)
        if os.path.exists(lp):
            sftp.put(lp, f"/tmp/{os.path.basename(rel)}")
            print(f"Uploaded config {rel}")

    # Wallpapers & Music & Apps catalog
    wall_dir = os.path.join(base_local, "usr/share/kortex/wallpapers")
    if os.path.exists(wall_dir):
        for wf in os.listdir(wall_dir):
            wlp = os.path.join(wall_dir, wf)
            sftp.put(wlp, f"/tmp/{wf}")
            print(f"Uploaded wallpaper {wf}")

    music_dir = os.path.join(base_local, "usr/share/kortex/music")
    if os.path.exists(music_dir):
        for mf in os.listdir(music_dir):
            mlp = os.path.join(music_dir, mf)
            sftp.put(mlp, f"/tmp/{mf}")
            print(f"Uploaded music {mf}")

    apps_json = os.path.join(base_local, "usr/share/kortex/apps.json")
    if os.path.exists(apps_json):
        sftp.put(apps_json, "/tmp/apps.json")
        print("Uploaded apps.json")

    sftp.close()

    # Move into place with sudo
    cmd = """
    echo 1 | sudo -S mv /tmp/kortex-* /tmp/start-hyprland /tmp/Hyprland /usr/local/bin/
    echo 1 | sudo -S chmod +x /usr/local/bin/kortex-* /usr/local/bin/start-hyprland /usr/local/bin/Hyprland
    echo 1 | sudo -S mkdir -p /usr/share/kortex/wallpapers /usr/share/kortex/music
    echo 1 | sudo -S mv /tmp/*.png /usr/share/kortex/wallpapers/ 2>/dev/null || true
    echo 1 | sudo -S mv /tmp/*.wav /tmp/*.mp3 /usr/share/kortex/music/ 2>/dev/null || true
    echo 1 | sudo -S mv /tmp/apps.json /usr/share/kortex/apps.json 2>/dev/null || true
    mkdir -p ~/.config/kortex/plugins ~/.config/hypr ~/.config/waybar
    cp /tmp/config.json ~/.config/kortex/config.json
    cp /tmp/master-state.json ~/.config/kortex/master-state.json
    cp /tmp/hyprland.conf ~/.config/hypr/hyprland.conf
    cp /tmp/binds.conf ~/.config/hypr/binds.conf
    cp /tmp/theme.conf ~/.config/hypr/theme.conf
    cp /tmp/config ~/.config/waybar/config
    cp /tmp/style.css ~/.config/waybar/style.css
    rm -f ~/.config/hypr/hyprland.lua /home/kortex/.config/hypr/hyprland.lua /etc/skel/.config/hypr/hyprland.lua 2>/dev/null || true
    echo 1 | sudo -S cp -rf ~/.config/* /etc/skel/.config/
    echo "[+] ALL SUBSYSTEMS INSTALLED ON VM"
    """
    stdin, stdout, stderr = ssh.exec_command(cmd)
    print(stdout.read().decode())
    print(stderr.read().decode())
    ssh.close()

if __name__ == "__main__":
    sync_vm()
