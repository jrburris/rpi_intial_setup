# from subprocess import STDOUT, check_call
import os
import subprocess
import shutil
from subprocess import STDOUT


remove_file_list = ['libreoffice*', 'wolfram-engine', 'sonic-pi', 'scratch',
                    'python-minecraftpi', 'minecraft-pi', 'scratch2', 'geany',
                    'geany-common', 'greenfoot', 'nodered', 'bluej',
                    'claws-mail', 'claws-mail-i18n', 'nuscratch',
                    'python3-thonny']

# Update and Upgrade
print('Peforming Update')
proc = subprocess.Popen('sudo apt-get update -y', shell=True)
print('Peforming Upgrade')
proc = subprocess.Popen('sudo apt-get upgrade -y', shell=True)

print('Unistalling unwanted files')

for remove_file in remove_file_list:
    print('     Removing {}'.format(remove_file))
    proc = subprocess.Popen('apt-get remove --purge -y {}'.format(remove_file),
                            shell=True)


print('Cleaning up deleted files')
proc = subprocess.Popen('sudo apt-get clean',
                        shell=True)

proc = subprocess.Popen('sudo apt-get autoremove --purge',
                        shell=True)


proc = subprocess.Popen('sudo apt-get install netatalk -y',
                        shell=True)

print('Removing games')
dest = '~/python_games'
shutil.rmtree(dest, ignore_errors=True)

print('Done!')
