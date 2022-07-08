import paramiko
from time import sleep
import io

paramiko.util.log_to_file('paramiko.log')

private_key = '''
-----BEGIN OPENSSH PRIVATE KEY-----
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
-----END OPENSSH PRIVATE KEY-----'''

conn = paramiko.SSHClient()
conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
conn.connect('192.168.47.12',
             port=22,
             username='peyman',
             # password='ost',
             # key_filename='/Users/peyman/.ssh/peyman_auto',
             # pkey=paramiko.RSAKey.from_private_key_file('/Users/peyman/.ssh/peyman_auto'),
             pkey=paramiko.RSAKey.from_private_key(io.StringIO(private_key)),
             look_for_keys=False)

shell = conn.invoke_shell()
sleep(1)
banner = shell.recv(65535).decode()

shell.send('grep processor /proc/cpuinfo\n'.encode())
sleep(1)
out = shell.recv(65535).decode()
print(out)

conn.close()
