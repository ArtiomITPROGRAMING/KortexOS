import vm_cmd

cmd = """
python3 -c "
import pty, os, subprocess
master, slave = pty.openpty()
proc = subprocess.Popen(['/usr/local/bin/kortex-ai'], stdin=slave, stdout=slave, stderr=slave, close_fds=True)
os.close(slave)
import time
time.sleep(1)
proc.poll()
print('Return code:', proc.returncode)
try:
    data = os.read(master, 4096)
    print("Output:\\n" + data.decode("utf-8", errors="replace"))
except Exception as e:
    print("Read err:", e)
os.close(master)
"
"""
out, err, rc = vm_cmd.run_ssh(cmd)
print("OUT:", out)
print("ERR:", err)
