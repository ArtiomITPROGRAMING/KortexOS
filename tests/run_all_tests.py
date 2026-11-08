import sys
import json
import time
import subprocess
import paramiko

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

def run_ssh(client, cmd):
    stdin, stdout, stderr = client.exec_command(cmd, timeout=20)
    out = stdout.read().decode(errors="replace")
    err = stderr.read().decode(errors="replace")
    rc = stdout.channel.recv_exit_status()
    return out.strip(), err.strip(), rc

def main():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect("127.0.0.1", port=2222, username="kortex", password="1", timeout=10)
    except Exception as e:
        print(f"[-] FAILED to connect SSH: {e}")
        sys.exit(1)

    results = []

    def log_test(name, passed, details=""):
        status = "PASS" if passed else "FAIL"
        print(f"[{status}] {name}")
        if details:
            print(f"       {details}")
        results.append((name, passed, details))

    print("==================================================")
    print("  KORTEX-OS UNIFIED DESIGN & PERSISTENCE TESTS    ")
    print("==================================================")

    # TEST 1: Hyprland Startup & Debug Overlay Cleanliness
    out, _, rc = run_ssh(client, "test -f ~/.config/hypr/hyprland.lua && echo 'LUA_FOUND' || echo 'CLEAN'")
    passed = (rc == 0 and "CLEAN" in out)
    log_test("Check obsolete hyprland.lua removal", passed, f"Result: {out}")

    out, _, rc = run_ssh(client, "grep -A 4 'debug {' ~/.config/hypr/hyprland.conf | grep 'overlay = false'")
    passed = (rc == 0 and "overlay = false" in out)
    log_test("Verify Hyprland debug overlay disabled", passed, f"Config: {out}")

    # TEST 2: MacBook Touchpad Gestures
    out, _, rc = run_ssh(client, "grep -E 'workspace_swipe = true' ~/.config/hypr/theme.conf")
    passed = (rc == 0 and "true" in out)
    log_test("MacBook UX: 3-Finger workspace swipe gestures", passed, f"Theme config: {out}")

    # TEST 3: Spotlight (Super + Space) Keybind
    out, _, rc = run_ssh(client, "grep -E 'kortex-spotlight' ~/.config/hypr/binds.conf")
    passed = (rc == 0 and "SPACE" in out)
    log_test("MacBook UX: Super+Space Spotlight binding", passed, f"Bind: {out}")

    # TEST 4: Layout Switcher Functionality
    out, _, rc = run_ssh(client, "kortex-layout tiling && kortex-layout status")
    passed = (rc == 0 and "tiling" in out)
    log_test("Layout Engine: Switch to Tiling Mode", passed, f"Output: {out}")

    out, _, rc = run_ssh(client, "kortex-layout floating && kortex-layout status")
    passed = (rc == 0 and "floating" in out)
    log_test("Layout Engine: Switch to Floating Mode", passed, f"Output: {out}")

    out, _, rc = run_ssh(client, "kortex-layout grid && kortex-layout status")
    passed = (rc == 0 and "grid" in out)
    log_test("Layout Engine: Switch to Cyber-Deck Grid Mode", passed, f"Output: {out}")

    # TEST 5: Kortex Theme Apply (Multi-Layer & Dual Gradient)
    out, _, rc = run_ssh(client, "kortex-theme-apply --theme cyan && grep -E '\\$col_active' ~/.config/hypr/theme.conf")
    passed = (rc == 0 and "00f0ff" in out)
    log_test("Theme Studio Pro: Dual gradient & layer colors apply", passed, f"Hyprland active border: {out}")

    # TEST 6: Wallpaper Engine (Desktop & Kitty Per-App)
    out, _, rc = run_ssh(client, "kortex-wallpaper desktop grid && kortex-wallpaper status")
    passed = (rc == 0 and "cyber_grid.png" in out)
    log_test("Wallpaper Engine: Desktop wallpaper preset apply", passed, "Grid wallpaper applied")

    out, _, rc = run_ssh(client, "kortex-wallpaper terminal /usr/share/kortex/wallpapers/cyber_grid.png 0.45 && grep 'background_tint 0.45' ~/.config/kitty/kitty.conf")
    passed = (rc == 0 and "0.45" in out)
    log_test("Wallpaper Engine: Kitty per-app background & dimming", passed, f"Kitty config: {out}")

    # TEST 7: OOBE Wizard & First-Run Detection
    out, _, rc = run_ssh(client, "test -x /usr/local/bin/kortex-oobe && echo 'OOBE_READY'")
    passed = (rc == 0 and "OOBE_READY" in out)
    log_test("OOBE Wizard: Executable presence in /usr/local/bin", passed, "kortex-oobe executable")

    out, _, rc = run_ssh(client, "grep 'kortex-oobe' ~/.config/hypr/hyprland.conf")
    passed = (rc == 0 and "kortex-oobe" in out)
    log_test("OOBE Wizard: First-run autostart trigger in hyprland.conf", passed, f"Autostart: {out}")

    # TEST 8: Installer Settings Persistence Hook
    out, _, rc = run_ssh(client, "grep -E 'master-state.json' /usr/local/bin/kortex-install")
    passed = (rc == 0 and "master-state.json" in out)
    log_test("Installer Persistence: Automated settings transfer to disk", passed, "Installer persistence hook present")

    # TEST 9: Master State JSON Integrity
    out, _, rc = run_ssh(client, "cat ~/.config/kortex/master-state.json")
    try:
        mst = json.loads(out)
        passed = (mst.get("theme", {}).get("name") == "cyan" and "palette" in mst.get("theme", {}))
    except Exception:
        passed = False
    log_test("Master State JSON: Schema and persistence validity", passed, "Valid JSON with all sections")

    # TEST 10: Interactive System Tour & Guide (kortex-tour)
    out, _, rc = run_ssh(client, "test -x /usr/local/bin/kortex-tour && echo 'TOUR_READY'")
    passed = (rc == 0 and "TOUR_READY" in out)
    log_test("System Tour: Executable presence in /usr/local/bin", passed, "kortex-tour executable")

    out, _, rc = run_ssh(client, "grep -E 'custom/guide' ~/.config/waybar/config")
    passed = (rc == 0 and "custom/guide" in out)
    log_test("System Tour: Waybar [ ? GUIDE ] button integration", passed, f"Waybar config: {out}")

    out, _, rc = run_ssh(client, "grep -E 'kortex-guide' ~/.config/hypr/binds.conf")
    passed = (rc == 0 and "F1" in out)
    log_test("System Tour: Super+F1 hotkey binding", passed, f"Bind: {out}")

    # TEST 11: VirtualBox Live Screen Capture
    screenshot_file = r"c:\Users\Lenovo\KortexOS\vbox_unified_engine_test.png"
    vbox_res = subprocess.run([
        r"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe",
        "controlvm", "KortexOS", "screenshotpng", screenshot_file
    ], capture_output=True, text=True)
    passed = (vbox_res.returncode == 0)
    log_test("Live Display: Capture active screen frame", passed, f"Saved: {screenshot_file}")

    client.close()

    print("==================================================")
    total = len(results)
    passed_count = sum(1 for _, p, _ in results if p)
    print(f"SUMMARY: {passed_count}/{total} TESTS PASSED")
    print("==================================================")
    if passed_count != total:
        sys.exit(1)

if __name__ == "__main__":
    main()
