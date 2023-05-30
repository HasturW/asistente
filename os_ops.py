import subprocess

def sshup():
    subprocess.run(['systemctl','start', 'ssh'])

def sshdown():
    subprocess.run(['systemctl','stop', 'ssh'])

def ftpup():
    subprocess.run(['systemctl','start', 'vsftpd'])

def ftpdown():
    subprocess.run(['systemctl','stop', 'vsftpd'])

def apacheup():
    subprocess.run(['systemctl','start', 'apache2'])

def apachedown():
    subprocess.run(['systemctl','stop', 'apache2'])