import paramiko
import time
import subprocess

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('127.0.0.1', port=2222, username='kortex', password='1')

# Launch kortex-music in floating window
ssh.exec_command('WAYLAND_DISPLAY=wayland-1 XDG_RUNTIME_DIR=/run/user/1000 kitty --class kortex-music --title "KORTEX OS :: MUSIC PLAYER" -e /usr/local/bin/kortex-music >/tmp/kitty_music.log 2>&1 &')
time.sleep(2.5)

# Verify process
stdin, stdout, stderr = ssh.exec_command('ps aux | grep -E "(kortex-music|mpv)"')
proc_out = stdout.read().decode()
print('VM PROCESSES:\n', proc_out)

# Capture screenshot
subprocess.run([
    r'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe',
    'controlvm', 'KortexOS', 'screenshotpng',
    r'c:\Users\Lenovo\KortexOS\docs\screenshots\music_live.png'
])
print('[+] Saved docs/screenshots/music_live.png')
