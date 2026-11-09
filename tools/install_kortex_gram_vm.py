import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('127.0.0.1', port=2222, username='kortex', password='1')

launcher = """#!/usr/bin/env bash
PORT=8765
if ! pgrep -f "http.server 8765" >/dev/null 2>&1; then
    python3 -m http.server 8765 --directory /usr/share/kortex-gram/web --bind 127.0.0.1 >/dev/null 2>&1 &
    sleep 0.5
fi
exec firefox --new-window "http://127.0.0.1:8765" "$@"
"""

desktop = """[Desktop Entry]
Name=KortexGram
Comment=Secure Real-Time E2EE Messenger
Exec=kortex-gram
Icon=telegram
Terminal=false
Type=Application
Categories=Network;InstantMessaging;
"""

stdin, stdout, stderr = ssh.exec_command("echo 1 | sudo -S tee /usr/local/bin/kortex-gram >/dev/null")
stdin.write(launcher)
stdin.channel.shutdown_write()
stdout.read()

stdin, stdout, stderr = ssh.exec_command("echo 1 | sudo -S chmod +x /usr/local/bin/kortex-gram")
stdout.read()

stdin, stdout, stderr = ssh.exec_command("echo 1 | sudo -S tee /usr/share/applications/kortex-gram.desktop >/dev/null")
stdin.write(desktop)
stdin.channel.shutdown_write()
stdout.read()

ssh.close()
print("KORTEXGRAM INSTALLED IN VM SUCCESSFULLY!")
