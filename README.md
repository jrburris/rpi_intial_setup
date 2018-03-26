# rpi_intial_setup

sudo apt-get install python-apt




python setup.py

## If picon

sudo apt-get install python-smbus python3-smbus python-dev python3-dev
sudo nano /boot/config.txt
## and add the following 2 lines to the end of the file:
dtparam=i2c1=on
dtparam=i2c_arm=on
