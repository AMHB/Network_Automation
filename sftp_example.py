import paramiko
from time import sleep
import io

paramiko.util.log_to_file('paramiko.log')

conn = paramiko.SSHClient()
conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
conn.connect('192.168.47.12',
             port=22,
             username='peyman',
             key_filename='/Users/peyman/.ssh/peyman_auto',
             look_for_keys=False)

sftp = conn.open_sftp()

sftp.get('/etc/passwd', 'passwd')
sftp.put('foo.txt', '/tmp/foo.txt')

sftp.close()
conn.close()
