import subprocess

def update():
     print('Starting Update')
     subprocess.call("sudo apt-get update", shell=True)
     print('Update Complete')
def upgrade():
     print('Starting Upgrade')
     subprocess.call("sudo apt-get upgrade -y", shell=True)
     print('Upgrade Complete')

update()
upgrade()
