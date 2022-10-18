from multiprocessing import AuthenticationError
import paramiko, os
from getpass import getpass

# Creating password prompt
thePass = getpass(prompt = "Please enter your SSH Password: ")

#Host information
host = "10.0.0.36"
port = 22
username = "root"
password = thePass

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password)

except paramiko.AuthenticationException:
    print("Authentication Failed")


sftp = ssh.open_sftp()
path = '/home/'
sftp.put('Week06\\homework\\fs.py', '/home/fs.py')
ssh.exec_command('cd /home/')
ssh.exec_command('python /home/fs.py')
sftp.get('/home/timeline.body', 'C:\\Users\\abija\\Documents\\VisualStudio\\SYS-320-Automation\\Week06\\homework\\timeline.body')

ssh.close()