import subprocess

add_app_list = ['netatalk']

def install():
	print('Starting Installs')
	for add_app in add_app_list:
		print('Installing {}'.format(add_app))
		subprocess.call('sudo apt-get install {} -y'.format(add_app), shell=True)
	
	print('Installs Complete')


install()
