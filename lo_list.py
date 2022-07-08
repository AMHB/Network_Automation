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

interfaces = cisco_ssh.send(shell, 'show ip interface brief')

lo_interfaces = re.findall(r'Loopback\d+', interfaces)
for lo in lo_interfaces:
    tmp = cisco_ssh.send(shell, f'show int {lo}')
    print(tmp)
