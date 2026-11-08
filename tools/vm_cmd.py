import sys
import paramiko

def run_ssh(cmd, user="kortex", pwd="1"):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect("127.0.0.1", port=2222, username=user, password=pwd, timeout=10)
    stdin, stdout, stderr = client.exec_command(cmd)
    out = stdout.read().decode()
    err = stderr.read().decode()
    rc = stdout.channel.recv_exit_status()
    client.close()
    return out, err, rc

if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    cmd = sys.argv[1] if len(sys.argv) > 1 else "uname -a"
    out, err, rc = run_ssh(cmd)
    if out:
        print(out, end="")
    if err:
        print(err, end="", file=sys.stderr)
    sys.exit(rc)
