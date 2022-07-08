import cisco_ssh
import re

host = '192.168.47.101'
username = 'cisco'
password = 'cisco'
secret = 'cisco'

shell = cisco_ssh.ssh_connect(host, username, password)
cisco_ssh.send(shell, 'terminal length 0')
cisco_ssh.send(shell, 'enable')
cisco_ssh.send(shell, secret)
interface = cisco_ssh.send(shell, 'show interface lo3')

m = re.search(r'Internet address is (.+)', interface)
print(m.group(1))
