import paramiko
import time
import subprocess

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('127.0.0.1', port=2222, username='kortex', password='1')

ssh.exec_command('WAYLAND_DISPLAY=wayland-1 XDG_RUNTIME_DIR=/run/user/1000 kitty --class kortex-tour --title "KORTEX OS :: SYSTEM GUIDE" -e /usr/local/bin/kortex-tour >/tmp/kitty_tour.log 2>&1 &')
time.sleep(2)

stdin, stdout, stderr = ssh.exec_command('cat /tmp/kitty_tour.log; ps aux | grep tour')
print('VM LOG:', stdout.read().decode())

subprocess.run([
    r'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe',
    'controlvm', 'KortexOS', 'screenshotpng',
    r'c:\Users\Lenovo\KortexOS\docs\screenshots\tour_live.png'
])
print('[+] Updated docs/screenshots/tour_live.png')
