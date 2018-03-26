import subprocess
import shutil


remove_file_list = ['libreoffice*', 'wolfram-engine', 'sonic-pi', 'scratch',
                    'python-minecraftpi', 'minecraft-pi', 'scratch2', 'geany',
                    'geany-common', 'greenfoot', 'nodered', 'bluej',
                    'claws-mail', 'claws-mail-i18n', 'nuscratch',
                    'python3-thonny']

add_app_list = ['netatalk']


def update():
    print('Starting Update')
    subprocess.call("sudo apt-get update", shell=True)
    print('Update Complete')


def upgrade():
    print('Starting Upgrade')
    subprocess.call("sudo apt-get upgrade -y", shell=True)
    print('Upgrade Complete')


def remove():
    print('Starting Removal')
    for remove_file in remove_file_list:
        print('Removing {}'.format(remove_file))
        subprocess.call("sudo apt-get remove --purge -y {}".
                        format(remove_file), shell=True)

    print('Running Clean')
    subprocess.call("sudo apt-get clean", shell=True)

    print('Running Autoremove')
    subprocess.call("sudo apt autoremove --purge -y", shell=True)

    print('Removing Games')
    dest = '~/python_games'
    shutil.rmtree(dest, ignore_errors=True)

    print('Removal Complete')


def install():
    print('Starting Installs')
    for add_app in add_app_list:
        print('Installing {}'.format(add_app))
        subprocess.call('sudo apt-get install {} -y'.
                        format(add_app), shell=True)

    print('Installs Complete')


update()
upgrade()
remove()
install()
