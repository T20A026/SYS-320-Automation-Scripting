from multiprocessing import AuthenticationError
import paramiko, os
from getpass import getpass

# Creating password prompt
thePass = getpass(prompt = "Please enter your SSH Password: ")

#Host information
host = "192.168.6.71"
port = 2222
username = "abijah.buttendorf"
password = thePass

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password)

except paramiko.AuthenticationException:
    print("Authentication Failed")

# Opens SSH Instance
sftp = ssh.open_sftp()
path = '/home/'

# Moves to Home Dir, and runs Kraken,
ssh.exec_command('cd /home/ubuntu/')
sftp.put('C:\\Users\\abijah.buttendorf\\Documents\\abuttendorf\\Week09\\class\\kraken', 'kraken')
stdin, stdout, stderr = ssh.exec_command('/home/ubuntu/kraken --folder /usr/bin --folder  --folder /usr/sbin/   --folder /usr/local/bin  --folder /sbin  --folder /usr/local/sbin  --folder /bin')

# Formats and grabs Kraken output, placing it in the "output.txt"
output = stdout.readlines()
for line in output:
    with open('output.txt', 'a') as f:
        f.write(line)

# Collecting all directories containing bin
sftp.put('Week06\\homework\\binFinder.py', '/home/binFinder.py')
ssh.exec_command('cd /home/')
ssh.exec_command('python /home/binFinder.py')
sftp.get('/home/bins.body', 'C:\\Users\\abija\\Documents\\VisualStudio\\SYS-320-Automation\\Week06\\homework\\bins.body')

# Running lsof with sudo privlages, and looking for network rep,lated processes
stdin, stdout, stderr = ssh.exec_command('sudo -S lsof -i -n')
stdin.write(thePass + "\n")
output = stdout.readlines()
for lines in output:
    print(lines)


ssh.close()