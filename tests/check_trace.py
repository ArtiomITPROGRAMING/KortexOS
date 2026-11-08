import pty
import os
import subprocess

master, slave = pty.openpty()
proc = subprocess.Popen(['/usr/local/bin/kortex-ai'], stdin=slave, stdout=slave, stderr=slave, close_fds=True)
os.close(slave)
proc.wait()
data = os.read(master, 8192)
print("OUT:\n", data.decode("utf-8", errors="replace"))
os.close(master)
