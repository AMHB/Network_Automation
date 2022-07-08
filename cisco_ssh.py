import paramiko
from time import sleep
import io

def ssh_connect(host, username, password, port=22):
    conn = paramiko.SSHClient()
    conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    conn.connect(host,
                 port=port,
                 username=username,
                 password=password,
                 look_for_keys=False)
    return conn.invoke_shell()

def wait(n=0.5):
    sleep(n)

def flush(shell):
    wait()
    if shell.recv_ready():
        shell.recv(65535)

def send(shell, cmd):
    flush(shell)
    shell.send(cmd + '\n')
    wait()
    output = ''
    while shell.recv_ready():
        output += shell.recv(65535).decode()
        wait()
    return output
