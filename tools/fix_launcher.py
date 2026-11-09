import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('127.0.0.1', port=2222, username='kortex', password='1')

launcher = """#!/usr/bin/env bash
PORT=8765
if ! pgrep -f "http.server 8765" >/dev/null 2>&1; then
    nohup python3 -m http.server 8765 --directory /usr/share/kortex-gram/web --bind 127.0.0.1 >/dev/null 2>&1 &
    sleep 0.5
fi
export MOZ_ENABLE_WAYLAND=1
exec firefox --new-window "http://127.0.0.1:8765" "$@"
"""

sftp = ssh.open_sftp()
with sftp.file('/tmp/kortex-gram', 'w') as f:
    f.write(launcher)
sftp.close()

stdin, stdout, stderr = ssh.exec_command("echo 1 | sudo -S cp /tmp/kortex-gram /usr/local/bin/kortex-gram && echo 1 | sudo -S chmod +x /usr/local/bin/kortex-gram")
stdout.read()

ssh.close()
print("CLEAN LAUNCHER INSTALLED!")
